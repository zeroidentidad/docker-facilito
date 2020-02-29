
# Ejercicio inicial - pull image

- https://hub.docker.com/  -> busqueda: https://hub.docker.com/search?q=fernando93d&type=image

## En terminal:

```shell
docker image pull fernando93d/hello
```

Despues listar si aparece en las imagenes decargadas:

```shell
docker image ls
```

### *Generación contenedor de la imagen hello*

Estructura de ayuda:

```shell
docker container run --help
```

Ejemplo usando la imagen descargada:

```shell
docker container run fernando93d/hello
```
