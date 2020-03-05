# Trabajando con usuarios

- Modificación Dockerfile para agregar usuario

    [Dockerfile](./adduser/Dockerfile)

```shell
# modificacion Dockerfile para ejemplo con RUN adduser - USER
ARG DISTRO="ubuntu:18.04"

FROM ${DISTRO}

RUN useradd -ms /bin/bash zero_user

RUN mkdir app
RUN cd /app && touch data.txt

COPY ./src/ /app/src/

USER zero_user

RUN cd /home/zero_user && touch data.txt

# guardando y a nivel de archivos ejemplo probar creando nueva imagen
cd adduser
docker image build -t ubuntu-file:v9 .
# salida
Sending build context to Docker daemon  1.431MB
Step 1/8 : ARG DISTRO="ubuntu:18.04"
Step 2/8 : FROM ${DISTRO}
 ---> 72300a873c2c
Step 3/8 : RUN useradd -ms /bin/bash zero_user
 ---> Running in 29e9704c0a6d
Removing intermediate container 29e9704c0a6d
 ---> 1ee0f5ba8d06
Step 4/8 : RUN mkdir app
 ---> Running in f591a7702252
Removing intermediate container f591a7702252
 ---> a8822b42c60c
Step 5/8 : RUN cd /app && touch data.txt
 ---> Running in b112e2d3635f
Removing intermediate container b112e2d3635f
 ---> f431473465de
Step 6/8 : COPY ./src/ /app/src/
 ---> 7c60c5fcbeca
Step 7/8 : USER zero_user
 ---> Running in 01f1003a8a81
Removing intermediate container 01f1003a8a81
 ---> 852a8c304b07
Step 8/8 : RUN cd /home/zero_user && touch data.txt
 ---> Running in ce76078b3b3e
Removing intermediate container ce76078b3b3e
 ---> 503a6fe85213
Successfully built 503a6fe85213
Successfully tagged ubuntu-file:v9
```

- Verificar uso nuevo Dockerfile con adduser e imagen de salida

```shell
# listar imagenes existentes y ver si esta la nueva version
docker image ls
# salida
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
ubuntu-file         v9                  503a6fe85213        56 seconds ago      65.3MB

# probar creando contenedor con nueva imagen, uso flag --rm para autodestruccion al salir
docker container run --rm -it ubuntu-file:v9
# ver resultado acceso con usuario agregado
zero_user@fd8112cfff86:/$ cd /home/zero_user/ && ls
data.txt
```

- Definir utilizar usuario root en contendor existende de imagen previa

```shell
# crear contenedor de prueba, opcional -d para salir sin detener
docker container run -it ubuntu-file:v9
zero_user@a15f6fb2ed89:/$
# en otra terminal, usar ejecucion comando para cambiar a usuario root, directiva exec
docker container exec -u 0 -it a15f6fb2ed89 bash
root@a15f6fb2ed89:/
# probar viendo los archivos para root
root@a15f6fb2ed89:/ cd app/src && ls
pictures2.tar.xz  soloyo.txt
```