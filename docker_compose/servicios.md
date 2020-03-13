# Servicios

- Definir archivo opciones contenedores de servicio

    [docker-compose.yml](./servicios/docker-compose.yml) editado

    Versiones de archivo: https://docs.docker.com/compose/compose-file/

```shell
# editar contenido de docker-compose.yml en arbol de identaciones
version: "3.7"

services: 
    nginx:
        image: nginx
        ports: 
            - "80:80"

# a nivel del archivo en la terminal levantar el servicio usando el archivo
cd servicios
docker-compose up

# salida
Creating network "servicios_default" with the default driver
Creating servicios_nginx_1 ... done
Attaching to servicios_nginx_1
# log al acceder desde el navegador
nginx_1  | 172.23.0.1 - - [13/Mar/2020:10:55:07 +0000] "GET / HTTP/1.1" 200 612 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36" "-"
nginx_1  | 2020/03/13 10:55:08 [error] 6#6: *1 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 172.23.0.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost", referrer: "http://localhost/"
nginx_1  | 172.23.0.1 - - [13/Mar/2020:10:55:08 +0000] "GET /favicon.ico HTTP/1.1" 404 555 "http://localhost/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36" "-"

# salida con Ctrl+C, ver ayuda
^CGracefully stopping... (press Ctrl+C again to force)
Stopping servicios_nginx_1 ... done

docker-compose --help

...
  build              Build or rebuild services
  bundle             Generate a Docker bundle from the Compose file
  config             Validate and view the Compose file
  create             Create services
  down               Stop and remove containers, networks, images, and volumes
  events             Receive real time events from containers
  exec               Execute a command in a running container
  help               Get help on a command
  images             List images
  kill               Kill containers
  logs               View output from containers
  pause              Pause services
  port               Print the public port for a port binding
  ps                 List containers
  ...
  start              Start services
  stop               Stop services
  top                Display the running processes
  unpause            Unpause services
  up                 Create and start containers
  version            Show the Docker-Compose version information

# ver ayuda, comando up
docker-compose up --help

...
-d, --detach               Detached mode: Run containers in the background,
                               print new container names. Incompatible with
                               --abort-on-container-exit.
    --no-color                 Produce monochrome output.
    --quiet-pull               Pull without printing progress information
    --no-deps                  Don't start linked services.
    --force-recreate           Recreate containers even if their configuration
                               and image haven't changed.
    ...
                               in the Compose file.
    --exit-code-from SERVICE   Return the exit code of the selected service
                               container. Implies --abort-on-container-exit.
    --scale SERVICE=NUM        Scale SERVICE to NUM instances. Overrides the
                               `scale` setting in the Compose file if present.
```

- Eliminar contenedores de servicio y configuraciones

```shell
# uso comando down
cd servicios
docker-compose down

# salida
Stopping servicios_nginx_1 ... done
Removing servicios_nginx_1 ... done
Removing network servicios_default
```

- Personalizar nombre servicio contenedor

```shell
# editar docker-compose.yml
version: "3.7"

services: 
    nginx:
        image: nginx
        container_name: nginx # <-
        ports: 
            - "80:80"
```            

- Agregar servicio en contenedor

```shell
# editar docker-compose.yml
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

# probar creando con opciones antes de cambios
cd servicios
docker-compose up

Creating network "servicios_default" with the default driver
Creating nginx ... done
Attaching to nginx
^CGracefully stopping... (press Ctrl+C again to force)
Stopping nginx ... done

# probar compose con los ultimos cambios del docker-compose.yml
cd servicios
docker-compose up -d

Starting nginx ... done
Creating mysql ... done

# ver contendores de servicios en ejecucion
docker-compose ps
Name              Command             State          Ports       
-----------------------------------------------------------------
mysql   docker-entrypoint.sh mysqld   Exit 1                     
nginx   nginx -g daemon off;          Up       0.0.0.0:80->80/tcp

# ver registro logs del servicio que no se activo
docker-compose logs mysql

#salida
Attaching to mysql
mysql | 2020-03-13 16:06:58+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.0.19-1debian10 started.
mysql | 2020-03-13 16:07:01+00:00 [Note] [Entrypoint]: Switching to dedicated user 'mysql'
mysql | 2020-03-13 16:07:01+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.0.19-1debian10 started.
mysql | 2020-03-13 16:07:01+00:00 [ERROR] [Entrypoint]: Database is uninitialized and password option is not specified
mysql | You need to specify one of MYSQL_ROOT_PASSWORD, MYSQL_ALLOW_EMPTY_PASSWORD and MYSQL_RANDOM_ROOT_PASSWORD

# para arreglar, eliminar contenedores definidos en el .yml
docker-compose down
Stopping nginx ... done
Removing mysql ... done
Removing nginx ... done
Removing network servicios_default

# agregar opciones de entorno requeridas del servicio mysql
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
        environment: 
            MYSQL_ROOT_PASSWORD: root # <-

# probar nuevamente servicios queden en ejecución
docker-compose up -d
Creating network "servicios_default" with the default driver
Creating mysql ... done
Creating nginx ... done

# ver si todos los servicios definidos estan en ejecución
Name              Command             State          Ports       
-----------------------------------------------------------------
mysql   docker-entrypoint.sh mysqld   Up      3306/tcp, 33060/tcp
nginx   nginx -g daemon off;          Up      0.0.0.0:80->80/tcp

# exponer puerto servicio mysql y actualizar contendores
...
    mysql:
        image: mysql
        container_name: mysql
        ports: 
            - "3306:3306" # <-
        environment:
            MYSQL_ROOT_PASSWORD: root
# actualizar
docker-compose up -d
Recreating mysql ... 
Recreating mysql ... done

# ver cambios en ejecucion
docker-compose ps
Name              Command             State                 Ports              
-------------------------------------------------------------------------------
mysql   docker-entrypoint.sh mysqld   Up      0.0.0.0:3306->3306/tcp, 33060/tcp
nginx   nginx -g daemon off;          Up      0.0.0.0:80->80/tcp
```  