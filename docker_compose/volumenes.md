# Volumenes

- Definir volumenes contenedores de servicios

    [docker-compose.yml](./volumenes/docker-compose.yml) editado
    
    [.env](./volumenes/.env) editado

    [index.html](./volumenes/index.html) editado

```shell
# editar a nivel services y networks opciones volumes y seccion servicio
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
            - br0
        environment:
            MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
        volumes: #<-
            - mysql:/var/lib/mysql

networks: 
    br0:
        external: true

volumes: 
    mysql: #<-

# ejecutar cambios
docker-compose up -d
Creating network "volumenes_default" with the default driver
Creating volume "volumenes_mysql" with default driver
Creating nginx ... done
Creating mysql ... done

#listar volumenes existentes
DRIVER              VOLUME NAME
local               7d4a58f06ecfc507371f3e95cb1dd959398834ecbd77be305b61697317a6b999
local               319b6af381fd7720f51ec1a8dad8d1a25a50a09c6b8b865bf76ebdff9ac04093
local               954259ac4575a0f9b83648e99dbfd8e771189e5839a1c2462b094224e124b74b
local               c3340e05ae9d915d09a86fda0d693b4d5777ca20b4461f3fc1f44e9a7bef0019
local               d0db5248d10a9f5a1c39c1f0f5f846709276a1451199d1be5419b0ff85c04a41
local               f17fc0cadd995c5d5acbe465241b6ea0eada1a9a5e3eabd6581e3b4a9983b74c
local               volumenes_mysql
```

- Definir volumen compartiendo archivo(s)

```shell
# crear archivo index.html de ejemplo
cd volumenes
touch index.html

# modificar docker-compose.yml para agregar volumen compartido
# ejemplo modificacion seccion servicio nginx, usando ruta actual
version: "3.7"

services: 
    nginx:
        image: nginx
        container_name: nginx
        ports: 
            - "80:80"
        volumes: # <-
            - ./index.html:/usr/share/nginx/html/index.html

    mysql:
        image: mysql
        container_name: mysql
        ports: 
            - "3306:3306"
        networks: 
            - br0
        environment:
            MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
        volumes:
            - mysql:/var/lib/mysql

networks: 
    br0:
        external: true

volumes: 
    mysql: 

# ejecutar cambios
docker-compose up -d

Recreating nginx ... 
Recreating nginx ... done

# revisar en el browser
```
![localhost](./img/volumenes.png)