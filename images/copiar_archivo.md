# Copiar archivo(s) a imagen creada

- Generar archivo [Dockerfile](./copy/Dockerfile) ubicacion de copia

```shell
# modificacion Dockerfile en ubicacion de la copia
FROM ubuntu

RUN mkdir app
RUN cd /app && touch data.txt

COPY ./src/hola.txt /app/src/com/hola.txt
# guardar cambios en raiz archivos a copiar y generar imagen
cd copy
docker image build -t ubuntu-file:v2 .
# salida
Sending build context to Docker daemon  3.072kB
Step 1/4 : FROM ubuntu
 ---> 72300a873c2c
Step 2/4 : RUN mkdir app
 ---> Using cache
 ---> e6755560ff34
Step 3/4 : RUN cd /app && touch data.txt
 ---> Using cache
 ---> ff1c74b8cdce
Step 4/4 : COPY ./src/hola.txt /app/src/com/hola.txt
 ---> 8f79ad4d8c95
Successfully built 8f79ad4d8c95
Successfully tagged ubuntu-file:v2
```

- Verificar uso nuevo Dockerfile e imagen de salida

```shell
# listar imagenes existentes y ver si esta la nueva version
docker image ls
# salida
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
ubuntu-file         v2                  8f79ad4d8c95        2 minutes ago       64.2MB
# probar creando contenedor con nueva imagen, uso flag --rm para autodestruccion al salir
docker container run --rm -it ubuntu-file:v2
# ver resultado operaciones creacion
ls
cd app && ls
# salida
data.txt  src
```

## Copiar carpeta con archivo(s)/carpeta(s) a imagen creada

[Dockerfile](./copy2/Dockerfile)

```shell
# modificacion Dockerfile en ubicacion de la copia
FROM ubuntu

RUN mkdir app
RUN cd /app && touch data.txt

COPY ./src/ /app/src/

# guardar cambios en raiz archivos a copiar y generar imagen
cd copy2
docker image build -t ubuntu-file:v3 .
# salida
Sending build context to Docker daemon  4.608kB
Step 1/4 : FROM ubuntu
 ---> 72300a873c2c
Step 2/4 : RUN mkdir app
 ---> Using cache
 ---> e6755560ff34
Step 3/4 : RUN cd /app && touch data.txt
 ---> Using cache
 ---> ff1c74b8cdce
Step 4/4 : COPY ./src/ /app/src/
 ---> aebc50757e13
Successfully built aebc50757e13
Successfully tagged ubuntu-file:v3
```

- Verificar uso nuevo Dockerfile e imagen de salida

```shell
# listar imagenes existentes y ver si esta la nueva version
docker image ls
# salida
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
ubuntu-file         v3                  aebc50757e13        9 seconds ago       64.2MB
# probar creando contenedor con nueva imagen, uso flag --rm para autodestruccion al salir
docker container run --rm -it ubuntu-file:v3
# ver resultado operaciones creacion
cd app && ls
cd app/src && ls
# salida
data.txt  src
hola.txt  index.html
```

## Agregar archivo(s)/carpeta(s) con alguna operacion a imagen creada

[Dockerfile](./add/Dockerfile)

```shell
# modificacion Dockerfile en ubicacion de la copia
FROM ubuntu

RUN mkdir app
RUN cd /app && touch data.txt

COPY ./src/ /app/src/

ADD pictures.tar.xz /com/src

# guardar cambios en raiz archivos a agregar, copiar y generar imagen
cd add
docker image build -t ubuntu-file:v4 .
# salida
Sending build context to Docker daemon  717.8kB
Step 1/5 : FROM ubuntu
 ---> 72300a873c2c
Step 2/5 : RUN mkdir app
 ---> Using cache
 ---> e6755560ff34
Step 3/5 : RUN cd /app && touch data.txt
 ---> Using cache
 ---> ff1c74b8cdce
Step 4/5 : COPY ./src/ /app/src/
 ---> Using cache
 ---> aebc50757e13
Step 5/5 : ADD pictures.tar.xz /com/src
 ---> acda63e2fd27
Successfully built acda63e2fd27
Successfully tagged ubuntu-file:v4
```

- Verificar uso nuevo Dockerfile e imagen de salida

```shell
# listar imagenes existentes y ver si esta la nueva version
docker image ls
# salida
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
ubuntu-file         v4                  acda63e2fd27        About a minute ago   64.9MB
# probar creando contenedor con nueva imagen, uso flag --rm para autodestruccion al salir
docker container run --rm -it ubuntu-file:v4
# ver resultado operaciones creacion
cd com && ls
cd src && ls
# salida
src
159865.jpg  162157.png
```