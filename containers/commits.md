# Commits

## Tomar un contenedor con sus recursos y transformalo a imagen

- Ejemplo con contenedor de imagen base

```shell
# generar contenedor de prueba de una imagen oficial de ejemplo
docker container run -dit ubuntu
3e6940d3242dd687b32c484435d963f740f62a153a27e0550ee2c2a40b4172f8
# listar imagen creada
docker container ls
CONTAINER ID        IMAGE               COMMAND             CREATED              STATUS
3e6940d3242d        ubuntu              "/bin/bash"         About a minute ago   Up About a minute
# ejecutar comandos para hacer cambios en el contenedor
docker container exec -it 3e6940d3242d bash
root@3e6940d3242d:/ touch data.txt
root@3e6940d3242d:/ ls
bin  boot  data.txt  dev  etc  home
root@3e6940d3242d:/ exit

# usar el comando commit, ver ayuda
docker container commit --help
# generar imagen 
docker container commit 3e6940d3242d ubuntu-data
sha256:227cf61c3ba2b4168008e0efffadd61958cb398b6126ef63e0153c0b4e5178a8
# listar imagenes
docker image ls
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
ubuntu-data         latest              227cf61c3ba2        50 seconds ago      64.2MB
ubuntu-tools        latest              6c0352412a2f        15 hours ago        94.5MB

# probar ejecutar nuevo contenedor con imagen del commit creada previamente
root@a99cd579cafb:/ ls
bin  boot  data.txt  dev  etc  home  lib
```