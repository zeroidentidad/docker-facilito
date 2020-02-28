
# Comandos basicos

- Listar contenedores activos

```shell
docker container ls

# ver ayuda
docker container ls --help
```

    - Mostrar todos:

```shell
docker container ls -a
```

- Eliminar contenedores

```shell
# ver ayuda
docker container rm --help

# usar en el comando el ID o nombre del contenedor
docker container rm 837af9cd50ce
docker container rm mystifying_wing
```

- Crear y luego iniciar contenedores

```shell
# ejemplo usando imagen descargada previamente
docker container create fernando93d/hello

#iniciar contenedor en status Created usando su ID o nombre
docker container start d8fbea903afc
docker container start focused_neumann

# solo ejecuta script y sale
```

- Detener contenedores en ejecucion:

```shell
# usando su ID o nombre
docker container stop d8fbea903afc
```
... continua en [Modo interactivo](./modo_interactivo.md)