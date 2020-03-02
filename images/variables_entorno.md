# Variables de entorno

- Pasar variable local a contenedor

```shell
# ejemplo uso flag -e en contenedor con autodestruccion (--rm)
docker container run -it --rm -e USER=$USER ubuntu
# ver valor de la variable cmd echo
root@6fbd329cab5f:/ echo $USER
chucho
```

- Establecer variable en Dockerfile

[Dockerfile](./env/Dockerfile)

```shell
# modificacion Dockerfile para establecer variable de entorno
FROM ubuntu

ENV USER Zero

RUN mkdir app
RUN cd /app && touch data.txt

COPY ./src/ /app/src/
 
ADD pictures.tar.xz /com/src

# guardar cambios valor ENV en archivos a agregar/copiar y generar imagen
cd env
docker image build -t ubuntu-file:v5 .
# salida
Sending build context to Docker daemon  717.8kB
Step 1/6 : FROM ubuntu
 ---> 72300a873c2c
Step 2/6 : ENV USER Zero
 ---> Running in dbc082d17817
Removing intermediate container dbc082d17817
 ---> 121233ceca01
Step 3/6 : RUN mkdir app
 ---> Running in 6d38ce89f9a5
Removing intermediate container 6d38ce89f9a5
 ---> a681638d0001
Step 4/6 : RUN cd /app && touch data.txt
 ---> Running in 28ce59bc98b4
Removing intermediate container 28ce59bc98b4
 ---> 3c04b5f74a8b
Step 5/6 : COPY ./src/ /app/src/
 ---> ac040747916e
Step 6/6 : ADD pictures.tar.xz /com/src
 ---> e5c2aebf6978
Successfully built e5c2aebf6978
Successfully tagged ubuntu-file:v5
```

- Verificar uso nuevo Dockerfile e imagen de salida

```shell
# listar imagenes existentes y ver si esta la nueva version
docker image ls
# salida
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
ubuntu-file         v5                  e5c2aebf6978        51 seconds ago      64.9MB
# probar creando contenedor con nueva imagen, uso flag --rm para autodestruccion al salir
docker container run --rm -it ubuntu-file:v5
# ver resultado variable ENV establecida
root@77172a23cb96:/ echo $USER
Zero
```

- Cambiar valor ENV despues de usar Dockerfile al crear nuevo contenedor

```shell
# variables establecidas a imagen pueden ser reemplazadas al crear contenedor
docker container run --rm -it -e USER="Madafaka" ubuntu-file:v5
# ver resultado variable ENV establecida
root@950f9b62d4cb:/ echo $USER
Madafaka
```