# Logs

- Mostrar log ejecución contenedor

```shell
# ver ayuda, uso comando logs
docker container logs --help
# ejecutar contendor de prueba
docker container run fernando93d/hello
# listar info contenedores creados
docker container ls -a
CONTAINER ID        IMAGE                        COMMAND                  CREATED
69616d34fa55        fernando93d/hello            "python ./app.py"        4 minutes ago  
# uso logs en contenedor simple inicial
docker container logs 69616d34fa55
# salida, registro de ejecucion
    __  __      __         __  ___                __    
   / / / /___  / /___ _   /  |/  /_  ______  ____/ /___ 
  / /_/ / __ \/ / __ `/  / /|_/ / / / / __ \/ __  / __ \
 / __  / /_/ / / /_/ /  / /  / / /_/ / / / / /_/ / /_/ /
/_/ /_/\____/_/\__,_/  /_/  /_/\__,_/_/ /_/\__,_/\____/ 
                                                        
```

- Mostrar log ejecución contenedor de BD

    Imagen de referencia: https://hub.docker.com/_/mysql

```shell
# descargar imagen de mysql para prueba
docker image pull mysql
# ejecutar contendor de prueba
docker container run -d mysql
c8cd7fad6a62feb79dedc2afda7838c58fa471521e678c9d5322f988b1278cc1
# listar info contenedores creados
docker container ls -a
CONTAINER ID        IMAGE                        COMMAND                  CREATED
c8cd7fad6a62        mysql                        "docker-entrypoint.s…"   39 seconds ago
# no quedo en ejecucion en segundo plano con -d
# uso logs en contenedor para ver que paso
docker container logs c8cd7fad6a62
# salida, registro de ejecucion errores
2020-03-10 15:32:40+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.0.19-1debian10 started.
2020-03-10 15:32:41+00:00 [Note] [Entrypoint]: Switching to dedicated user 'mysql'
2020-03-10 15:32:41+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.0.19-1debian10 started.
2020-03-10 15:32:41+00:00 [ERROR] [Entrypoint]: Database is uninitialized and password option is not specified
You need to specify one of MYSQL_ROOT_PASSWORD, MYSQL_ALLOW_EMPTY_PASSWORD and MYSQL_RANDOM_ROOT_PASSWORD                                                     
```