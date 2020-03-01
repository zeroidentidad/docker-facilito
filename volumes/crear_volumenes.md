# Compartir archivos con contenedores

- Ver comandos creacion volumen

```shell
# ver ayuda
docker volume --help
# por default el driver disponible es para volumen local
```

- Creacion volumen

```shell
# ver ayuda
docker volume create --help
# volumen de prueba
docker volume create vprueba
# inspeccionar volumen creado
docker volume inspect vprueba
# salida
[
    {
        "CreatedAt": "2020-03-01T09:14:14-06:00",
        "Driver": "local",
        "Labels": {},
        "Mountpoint": "/var/lib/docker/volumes/vprueba/_data",
        "Name": "vprueba",
        "Options": {},
        "Scope": "local"
    }
]
# acceder a listar recursos
sudo ls /var/lib/docker/volumes
```

- Montar volumen a ruta dentro de contenedor previamente creado

```shell
# uso flag -v
docker container run -dit -v vprueba:/app ubuntu
# ejecutar comandos usando ID de salida
docker exec -it 72eece304d28096202bf17b30456eb74f4ddfb44cdf26de754b1d3e94b25a6f2 bash
# ver carpeta en contenedor vinculada al volumen creado
root@72eece304d28:/ ls
app  bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
# probar creando archivos dentro de /app
root@72eece304d28:/ cd app && touch a && touch b && touch c && ls
```

- Eliminar contenedor y ver que pasa en el volumen

```shell
# salir
root@72eece304d28:/app exit
# listar contenedores en ejecucion docker container ls == docker ps
docker ps
# eliminacion forzada contenedor actual en ejecucion, flag -f
docker container rm -f 72eece304d28
# nuevamente inspeccionar volumen creado previamente
docker volume inspect vprueba
# ver que hay en data
sudo ls /var/lib/docker/volumes/vprueba/_data
# salida archivos creados desde el contenedor
a  b  c
```

- Montar volumen previo en otra ruta y contenedor nuevo

```shell
# usar imagen descargada previamente y acceder interactivamente
docker container run -it -v vprueba:/src ubuntu
# revisar directorios
root@51c0efe2a923:/ ls
# salida
bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  src  srv  sys  tmp  usr  var
# revisar en src y ver si hay archivos creados previamente del contenedor eliminado
root@51c0efe2a923:/ cd /src && ls
# salida
a  b  c
```