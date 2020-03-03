# Dockerignore

### Excluir archivos a copiar

- Uso Dockerfile de ejemplo

    [Dockerfile](./dockerignore/Dockerfile)

- Ejemplo [.dockerignore](./dockerignore/.dockerignore) al mismo nivel del archivo Dockerfile

```shell
# modificacion Dockerfile para ejemplo con Dockerignore
ARG DISTRO="ubuntu:18.04"

FROM ${DISTRO}

RUN mkdir app
RUN cd /app && touch data.txt

COPY ./src/ /app/src/

# contenido exclusiones .dockerignore
./src/*.html
./src/hola.txt
./src/subcarpeta

# crear .dockerignore ejemplo para excluir algunos archivos de COPY
cd dockerignore
docker image build -t ubuntu-file:v8 .
# salida
Sending build context to Docker daemon  1.431MB
Step 1/5 : ARG DISTRO="ubuntu:18.04"
Step 2/5 : FROM ${DISTRO}
 ---> 72300a873c2c
Step 3/5 : RUN mkdir app
 ---> Using cache
 ---> e6755560ff34
Step 4/5 : RUN cd /app && touch data.txt
 ---> Using cache
 ---> ff1c74b8cdce
Step 5/5 : COPY ./src/ /app/src/
 ---> a924445c8ab0
Successfully built a924445c8ab0
Successfully tagged ubuntu-file:v8
```

- Verificar uso nuevo Dockerfile con .dockerignore e imagen de salida

```shell
# listar imagenes existentes y ver si esta la nueva version
docker image ls
# salida
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
ubuntu-file         v8                  a924445c8ab0        35 seconds ago      64.9MB

# probar creando contenedor con nueva imagen, uso flag --rm para autodestruccion al salir
docker container run --rm -it ubuntu-file:v8
# ver resultado archivos copiados y que fueron ignorados
root@f813eb993818:/ cd app/src && ls
pictures2.tar.xz  soloyo.txt
```