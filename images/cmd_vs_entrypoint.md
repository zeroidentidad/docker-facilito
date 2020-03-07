# CMD vs ENTRYPOINT

- Ejemplo uso CMD simple 

    [Dockerfile](./cmd-entrypoint/cmd/Dockerfile) editado

```shell
# contenido Dockerfile de ejemplo
FROM ubuntu

CMD ["echo", "Hola mundo prros"]
# ejemplo creacion imagen
cd cmd-entrypoint/cmd
docker image build -t cmd .
# salida
Sending build context to Docker daemon  2.048kB
Step 1/2 : FROM ubuntu
 ---> 72300a873c2c
Step 2/2 : CMD ["echo", "Hola mundo prros"]
 ---> Running in 2a9fa2597d86
Removing intermediate container 2a9fa2597d86
 ---> ef8eafaa130d
Successfully built ef8eafaa130d
Successfully tagged cmd:latest

# ejemplo ejecución contenedor
docker container run cmd
#salida
Hola mundo prros
```

- Reemplazo CMD al generar contendor

```shell
# contenido de directiva CMD puede reemplazarse al pasar
# argumentos de comandos al ejecutar nuevo contenedor

# ejemplo ejecución contenedor
docker container run cmd echo "Zero :v"
#salida
Zero :v

# revision contenedores, ver reemplazo
docker container ls -a
#salida
CONTAINER ID        IMAGE       COMMAND                  CREATED             STATUS                     
47f6ab9956d4        cmd         "echo 'Zero :v'"         52 seconds ago      Exited (0) 47 seconds ago
e459956550ae        cmd         "echo 'Hola mundo pr…"   25 minutes ago      Exited (0) 24 minutes ago
```

### ENTRYPOINT: 
*funciona de manera similar a CMD con la diferencia que no puede ser reemplazado como CMD al ejecutar contenedor*

- Ejemplo uso ENTRYPOINT simple 

    [Dockerfile](./cmd-entrypoint/entrypoint/Dockerfile) editado

```shell
# contenido Dockerfile de ejemplo
FROM ubuntu

ENTRYPOINT ["echo", "Hola mundo prros"]

# CMD ["echo", "Hola mundo prros"]

# ejemplo creacion imagen
cd cmd-entrypoint/entrypoint
docker image build -t cmd:v2 .
# salida
Sending build context to Docker daemon  2.048kB
Step 1/2 : FROM ubuntu
 ---> 72300a873c2c
Step 2/2 : ENTRYPOINT ["echo", "Hola mundo prros"]
 ---> Running in 8fda08168c0f
Removing intermediate container 8fda08168c0f
 ---> f5dc0f9148be
Successfully built f5dc0f9148be
Successfully tagged cmd:v2

# ejemplo ejecución contenedor
docker container run cmd:v2
#salida
Hola mundo prros
```

- Tratar reemplazo CMD al generar contendor

```shell
# ejemplo ejecución contenedor
docker container run cmd:v2 echo "Zero :v"
#salida
Hola mundo prros Zero :v

# revision contenedores, ver si reemplazo
docker container ls -a
#salida
CONTAINER ID        IMAGE       COMMAND                  CREATED              STATUS
9cba2d8882e6        cmd:v2      "echo 'Hola mundo pr…"   28 seconds ago       Exited (0) 24 seconds ago
310a388318e2        cmd:v2      "echo 'Hola mundo pr…"   About a minute ago   Exited (0) About a minute ago
```

### ENTRYPOINT+CMD:
*ambas directivas en el Dockerfile pueden combinar su funcionamiento*

- Ejemplo uso ENTRYPOINT+CMD simple 

    [Dockerfile](./cmd-entrypoint/entrypoint+cmd/Dockerfile) editado

```shell
# contenido Dockerfile de ejemplo
FROM ubuntu

ENTRYPOINT ["echo"]

CMD ["Hola mundo prros"]

# ejemplo creacion imagen
cd cmd-entrypoint/entrypoint+cmd
docker image build -t cmd:v3 .
# salida
Sending build context to Docker daemon  2.048kB
Step 1/3 : FROM ubuntu
 ---> 72300a873c2c
Step 2/3 : ENTRYPOINT ["echo"]
 ---> Running in 2e7b6341e11e
Removing intermediate container 2e7b6341e11e
 ---> ee025252176c
Step 3/3 : CMD ["Hola mundo prros"]
 ---> Running in d363b5106658
Removing intermediate container d363b5106658
 ---> 133d89781cae
Successfully built 133d89781cae
Successfully tagged cmd:v3

# ejemplo ejecución contenedor
docker container run cmd:v3
#salida
Hola mundo prros
```

- Tratar reemplazo CMD de ENTRYPOINT al generar contendor

```shell
# ya no seria necesario indicar el comando a usar que ya quedo definido
# por defecto desde ENTRYPOINT

# ejemplo ejecución contenedor indicando argumento
docker container run cmd:v3 "Zero :v"
#salida
Zero :v

# revision contenedores, ver si reemplazo
docker container ls -a
#salida
CONTAINER ID        IMAGE       COMMAND                  CREATED              STATUS
21a5401fd608        cmd:v3      "echo 'Zero :v'"         About a minute ago   Exited (0) About a minute ago
9e8bc8520b0d        cmd:v3      "echo 'Hola mundo pr…"   4 minutes ago        Exited (0) 4 minutes ago
```