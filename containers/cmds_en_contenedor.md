# Comandos dentro de un contenedor

- Acceder a ejecutar comandos en contenedor activo

```shell
# ver ayuda
docker container --help
# entonces usar comando attach indicando ID o nombre contenedor
docker container attach fb452880cd88
# al indicar exit, el contenedor se apaga, volver iniciar
docker container start fb452880cd88
```

- Salir de ejecutar comandos dejando contenedor activo

```shell
# ver ayuda
docker container exec --help
# entonces usar indicando ID o nombre contenedor mas comando/flag deseado
docker container exec fb452880cd88 ls
docker container exec fb452880cd88 ls -al
docker container exec fb452880cd88 ls | grep a
# para forma dentro del contenedor sin apagarlo con flags -i -t
docker container exec -it fb452880cd88 bash
# al indicar exit, se mantiene activo
```

- Ver procesos ejecutandose en contenedor activo
```shell
docker container top fb452880cd88
# referente a otras terminales de entrada exec
```