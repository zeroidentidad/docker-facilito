# Modo interactivo

## Ejercicio con imagen de Ubuntu

- https://hub.docker.com/_/ubuntu

- Descargar imagen:

```shell
# ultima version de mayor compatbilidad
docker image pull ubuntu
# version especifica indicar tag
docker image pull ubuntu:rolling
```

- Crear contenedor:

```shell
docker image ls
# ultima version de mayor compatbilidad
docker container run ubuntu:latest
# version especifica indicar tag
docker container run ubuntu:rolling
```

- Uso modo interactivo contenedor:

```shell
# ver ayuda
docker container run --help
# indicar version tag y agregar combinación flags -i (stdin) -t (tty)
docker container run -it ubuntu:latest
# al salir contenedor se apaga para usar en segundo plano agregar flag -d
docker container run -itd ubuntu:latest
# ejemplo con nginx
docker container run -d nginx
```