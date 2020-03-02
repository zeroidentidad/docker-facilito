# Dockerfile

## Imagen como una clase donde un contenedor es una instancia de la misma

### Ejemplo practico

- Generar archivo [Dockerfile](./Dockerfile)

```shell
# crear Dockerfile a editar
nano Dockerfile
# contenido de ejemplo, sobre estructura directivas
FROM ubuntu

RUN mkdir app
RUN cd /app && touch data.txt
# ubicarse donde fue creado archivo y construir imagen usando el Dockerfile
# uso flag -t para nombre (tag image) y con . detectar Dockerfile en la ruta actual
docker image build -t ubuntu-file2 .
# salida
Sending build context to Docker daemon  68.61kB
Step 1/3 : FROM ubuntu
 ---> 72300a873c2c
Step 2/3 : RUN mkdir app
 ---> Running in d8788cec57b7
Removing intermediate container d8788cec57b7
 ---> e6755560ff34
Step 3/3 : RUN cd /app && touch data.txt
 ---> Running in a7e9c74ded95
Removing intermediate container a7e9c74ded95
 ---> ff1c74b8cdce
Successfully built ff1c74b8cdce
Successfully tagged ubuntu-file2:latest
```

- Verificar resultado uso Dockerfile

```shell
# listar imagenes existentes y ver si esta la personalizada
docker image ls
# salida
REPOSITORY          TAG                 IMAGE ID            CREATED              SIZE
ubuntu-file2        latest              ff1c74b8cdce        About a minute ago   64.2MB
# probar creando contenedor con la nueva imagen
docker container run -it ubuntu-file2
# ver resultado operaciones creacion
ls
cd app && ls
```