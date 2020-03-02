# Argumentos

- Establecer argumento en Dockerfile

[Dockerfile](./arg/Dockerfile)

```shell
# modificacion Dockerfile para agregar argumento, sintaxis interpolacion
ARG DISTRO="ubuntu:18.04"

FROM ${DISTRO}

ENV USER Zero

RUN mkdir app
RUN cd /app && touch data.txt

COPY ./src/ /app/src/
 
ADD pictures.tar.xz /com/src

# guardar cambios valor ARG en archivos a agregar/copiar y generar imagen
cd arg
docker image build -t ubuntu-file:v6 .
# salida
Sending build context to Docker daemon  717.8kB
Step 1/7 : ARG DISTRO="ubuntu:18.04"
Step 2/7 : FROM ${DISTRO}
18.04: Pulling from library/ubuntu
Digest: sha256:04d48df82c938587820d7b6006f5071dbbffceb7ca01d2814f81857c631d44df
Status: Downloaded newer image for ubuntu:18.04
 ---> 72300a873c2c
Step 3/7 : ENV USER Zero
 ---> Using cache
 ---> 121233ceca01
Step 4/7 : RUN mkdir app
 ---> Using cache
 ---> a681638d0001
Step 5/7 : RUN cd /app && touch data.txt
 ---> Using cache
 ---> 3c04b5f74a8b
Step 6/7 : COPY ./src/ /app/src/
 ---> Using cache
 ---> ac040747916e
Step 7/7 : ADD pictures.tar.xz /com/src
 ---> Using cache
 ---> e5c2aebf6978
Successfully built e5c2aebf6978
Successfully tagged ubuntu-file:v6
```

- Verificar uso nuevo Dockerfile e imagen de salida

```shell
# listar imagenes existentes y ver si esta la nueva version
docker image ls
# salida
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
ubuntu-file         v6                  e5c2aebf6978        About an hour ago   64.9MB
# probar creando contenedor con nueva imagen, uso flag --rm para autodestruccion al salir
docker container run --rm -it ubuntu-file:v6
# ver resultado variable ENV establecida
root@77172a23cb96:/ echo $USER
Zero
```

- Cambiar valor ARG en el build al usar Dockerfile para generar imagen

```shell
# argumentos establecidos a Dockerfile pueden ser reemplazados al crear imagen
docker image build -t ubuntu-file:v7 --build-arg DISTRO=ubuntu:19.04 .
# salida
Sending build context to Docker daemon  717.8kB
Step 1/7 : ARG DISTRO="ubuntu:18.04"
Step 2/7 : FROM ${DISTRO}
19.04: Pulling from library/ubuntu
4dc9c2fff018: Pull complete 
0a4ccbb24215: Pull complete 
c0f243bc6706: Pull complete 
5ff1eaecba77: Pull complete 
Digest: sha256:2adeae829bf27a3399a0e7db8ae38d5adb89bcaf1bbef378240bc0e6724e8344
Status: Downloaded newer image for ubuntu:19.04
 ---> c88ac1f841b7
Step 3/7 : ENV USER Zero
 ---> Running in 9ec2e361077d
Removing intermediate container 9ec2e361077d
 ---> 68a078ad3307
Step 4/7 : RUN mkdir app
 ---> Running in e38e40625f3a
Removing intermediate container e38e40625f3a
 ---> 45a90284b01d
Step 5/7 : RUN cd /app && touch data.txt
 ---> Running in e1debe455561
Removing intermediate container e1debe455561
 ---> ca1c4a1873ad
Step 6/7 : COPY ./src/ /app/src/
 ---> 12a1a9f6c657
Step 7/7 : ADD pictures.tar.xz /com/src
 ---> a7b053afd9f6
Successfully built a7b053afd9f6
Successfully tagged ubuntu-file:v7

# listar imagenes existentes y ver si esta la nueva version
docker image ls
# salida
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
ubuntu-file         v7                  a7b053afd9f6        About a minute ago   70.7MB
```