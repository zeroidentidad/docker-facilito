# Compartiendo archivos con contenedores

- Crear contenedores y definir volumen en uso

```shell
# creacion primer contenedor modo interactivo accediendo automaticamente
docker container run -it -v vprueba:/app ubuntu
# creacion segundo contenedor en otra pestaña/ventana de terminal
docker container run -it -v vprueba:/src ubuntu
# accediendo en ambas rutas /app y /src se obtiene la misma salida del volumen
a  b  c
# creando/eliminando nuevo archivo en un contenedor se ve reflejado en el otro
root@0625356f4b30:/src# touch d

root@d11e8dfc9b9c:/app# ls
a  b  c  d
```

- Compartir directorio/archivos desde carpeta personal del sistema

```shell
# ir a ruta deseada, ejemplo: /home/tuusuario/ y crear carpeta a compartir
mkdir compartido_docker
# crear archivos de ejemplo para ver los cambios sincronizados
cd compartido_docker && touch index.html
# crear contenedor vinculando la carpeta creada previamente
docker container run -it -v /home/tuusuario/compartido_docker:/app ubuntu
# acceder a ruta app y ver los archivos compartidos
cd /app && ls
# saida
root@b82a2d65569c:/ cd /app && ls
index.html
# crear archivo desde el contenedor y revisar en ruta /home/tuusuario/compartido_docker
root@b82a2d65569c:/ touch abc.txt
#salida fuera del contenedor
cd /home/tuusuario/compartido_docker && ls
abc.txt  index.html
```

- Compartir archivo especifico desde carpeta personal del sistema

```shell
# modificar index.html creado previamente
nano index.html
# con el contenido
<h1> Hola desde docker-sistema </h1>
# descargar imagen de nginx para ejemplo hub.docker.com/_/nginx
docker image pull nginx
# crear contenedor definiendo archivo compartido y puertos expuestos contenedor-sistema 
docker container run -d -v /home/tuusuario/compartido_docker/index.html:/usr/share/nginx/html/index.html -p 80:80 nginx
# hacer peticion GET con curl
curl localhost
#salida
<h1> Hola desde docker-sistema </h1>
```



### Nota: para indentificar a contenedores con nombre personalizado indicar --name

docker run *--name* 