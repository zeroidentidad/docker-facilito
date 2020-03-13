# Redes

- Definir opciones de red

    Por defecto se crea tipo bridge

    [docker-compose.yml](./redes/docker-compose.yml) editado
    
    [.env](./redes/.env) editado

```shell
# lista redes contenedores
docker network ls
612c099252ff        myapp_default               bridge              local
a35faff8cdf8        none                        null                local
ba300b1ddc6e        variables_entorno_default   bridge              local

# inspeccionar red contenedores servicios previos
docker inspect variables_entorno_default
# salida
[
    {
        "Name": "variables_entorno_default",
        "Id": "ba300b1ddc6e5f0e0741a3b7a2fb2b532fddafd59056acf8e8ca07ed02f25ed5",
        "Created": "2020-03-13T11:58:39.381361002-06:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "172.27.0.0/16",
                    "Gateway": "172.27.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": true,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {
            "633fe15a1a0e2bcb117d67bc614ae04258ae10ec37e1723ec4844fab0a804614": {
                "Name": "mysql",
                "EndpointID": "35c365b11653af1df8bc6cea20c25342b8b747610b342e727237f8426b6098f0",
                "MacAddress": "02:42:ac:1b:00:03",
                "IPv4Address": "172.27.0.3/16",
                "IPv6Address": ""
            },
            "981a72b510d78434f2fef301363d7f9f9828f19a87673227d9956b3e47d35902": {
                "Name": "nginx",
                "EndpointID": "f0e4cf6cf023f3e45c412bf12d995470941fe9c8d4db5f1061d81f0b9fe65228",
                "MacAddress": "02:42:ac:1b:00:02",
                "IPv4Address": "172.27.0.2/16",
                "IPv6Address": ""
            }
        },
        "Options": {},
        "Labels": {
            "com.docker.compose.network": "default",
            "com.docker.compose.project": "variables_entorno",
            "com.docker.compose.version": "1.24.1"
        }
    }
]

# agregar opciones de red en archivo .yml
version: "3.7"

services: 
    nginx:
        image: nginx
        container_name: nginx
        ports: 
            - "80:80"

    mysql:
        image: mysql
        container_name: mysql
        ports: 
            - "3306:3306"
        environment:
            MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}

networks: # <-
    lorem:
        driver: bridge

# probar tratar crear servicios con nueva red definida
cd redes
docker-compose up -d

# salida
WARNING: Some networks were defined but are not used by any service: lorem
Creating network "redes_default" with the default driver
Creating nginx ... done
Creating mysql ... done

# modificar docker-compose.yml para que cada contenedor se agregue a la red
version: "3.7"

services: 
    nginx:
        image: nginx
        container_name: nginx
        ports: 
            - "80:80"

    mysql:
        image: mysql
        container_name: mysql
        ports: 
            - "3306:3306"
        networks: # <-
            - lorem
        environment:
            MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}

networks: 
    lorem:
        driver: bridge

# ejecutar atualizacion modificacion opcion redes servicio mysql
docker-compose up -d

# salida
Creating network "redes_lorem" with driver "bridge"
nginx is up-to-date
Recreating mysql ... done

# inspeccionar red
docker inspect redes_lorem
[
    {
        "Name": "redes_lorem",
        "Id": "9ce54b785e15852a372dba4f5f4ccf59c29f8b7bf952a62ac1c318720d83716e",
        "Created": "2020-03-13T12:18:58.070360395-06:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "172.29.0.0/16",
                    "Gateway": "172.29.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": true,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {
            "4d4b261802b9b880a9b73e96b80a477ada8b94151dc15348f324049bb97e20ec": {
                "Name": "mysql", # <-
                "EndpointID": "4dc6366695b4c13c699363608cb45ee5e2962d3df0ec5547868f97741d788cca",
                "MacAddress": "02:42:ac:1d:00:02",
                "IPv4Address": "172.29.0.2/16",
                "IPv6Address": ""
            }
        },
        "Options": {},
        "Labels": {
            "com.docker.compose.network": "lorem",
            "com.docker.compose.project": "redes",
            "com.docker.compose.version": "1.24.1"
        }
    }
]
```
- Agregar servicios contenedores a una red previa existente

```shell
# lista redes redes previas
docker network ls
NETWORK ID          NAME                      DRIVER              SCOPE
8e9c2463ce18        br0                       bridge              local
a695e3f56cce        br02                      bridge              local
f0b980920805        bridge                    bridge              local
57891919696c        host                      host                local
a35faff8cdf8        none                      null                local
5564e7d69290        redes_default             bridge              local
9ce54b785e15        redes_lorem               bridge              local

# editar docker-compose.yml con las opciones validas, ejemplo con br0
version: "3.7"

services: 
    nginx:
        image: nginx
        container_name: nginx
        ports: 
            - "80:80"

    mysql:
        image: mysql
        container_name: mysql
        ports: 
            - "3306:3306"
        networks: 
            - br0 # <-
        environment:
            MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}

networks: 
    br0:
        external: true # <-

# ejecutar actualizacion
docker-compose up -d

Recreating mysql ... 
Recreating mysql ... done

# inspeccionar red br0 de ejemplo previa
docker inspect br0
[
    {
        "Name": "br0",
        "Id": "8e9c2463ce18fa0e9e653e46ed728f031205d94973d8a428953cd1c606099abe",
        "Created": "2020-03-09T20:38:31.624165412-06:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": {},
            "Config": [
                {
                    "Subnet": "172.22.0.0/16",
                    "Gateway": "172.22.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {
            "ce5958233c855c33fa84bf378bcc755695c52353d751d75e2a06909b8625e07c": {
                "Name": "mysql", # <-
                "EndpointID": "caa9d2d5e21944beffdd3b90eeccdcc9e505a57bd8cc37709d0267352f87690c",
                "MacAddress": "02:42:ac:16:00:02",
                "IPv4Address": "172.22.0.2/16",
                "IPv6Address": ""
            }
        },
        "Options": {},
        "Labels": {}
    }
]
```