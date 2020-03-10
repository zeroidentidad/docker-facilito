# Acceder a maquina virtual

#### Enlace de ayuda: https://docs.docker.com/machine/drivers/virtualbox/

- Acceder a la docker machine de virtualbox

```shell
# listar docker machine disponibles
docker-machine ls
NAME           ACTIVE   DRIVER       STATE     URL                         SWARM   DOCKER     ERRORS
maquina-test   *        virtualbox   Running   tcp://192.168.99.101:2376           v19.03.5

# ver ayuda
docker-machine --help
Options:
...
  
Commands:
  active		Print which machine is active
  config		Print the connection config for machine
  create		Create a machine
  env			Display the commands to set up the environment for the Docker client
  inspect		Inspect information about a machine
  ip			Get the IP address of a machine
  kill			Kill a machine
  ls			List machines
  provision		Re-provision existing machines
  regenerate-certs	Regenerate TLS Certificates for a machine
  restart		Restart a machine
  rm			Remove a machine
  ssh			Log into or run a command on a machine with SSH.
  scp			Copy files between machines
  mount			Mount or unmount a directory from a machine with SSHFS.
  start			Start a machine
  status		Get the status of a machine
  stop			Stop a machine
  upgrade		Upgrade a machine to the latest version of Docker
  url			Get the URL of a machine
  version		Show the Docker Machine version or a machine docker version
  help			Shows a list of commands or help for one command
  
Run 'docker-machine COMMAND --help' for more information on a command.


# ver info de entorno para el cliente de conexion
docker-machine env maquina-test
# salida
export DOCKER_TLS_VERIFY="1"
export DOCKER_HOST="tcp://192.168.99.101:2376"
export DOCKER_CERT_PATH="/home/chucho/.docker/machine/machines/maquina-test"
export DOCKER_MACHINE_NAME="maquina-test"
# Run this command to configure your shell: 
# eval $(docker-machine env maquina-test)

# por medio de eval $(docker-machine env maquina-test)
# se marca * de que el cliente de docker apunta la maquina virtual
```

- Conexion cliente enlazado

```shell
# conexion cliente docker a maquina
eval $(docker-machine env maquina-test)
# descarcar imagen de webserver nginx de ejemplo
docker image pull nginx
# salida
Using default tag: latest
latest: Pulling from library/nginx
68ced04f60ab: Pull complete 
28252775b295: Pull complete 
a616aa3b0bf2: Pull complete 
Digest: sha256:2539d4344dd18e1df02be842ffc435f8e1f699cfc55516e2cf2cb16b7a9aea0b
Status: Downloaded newer image for nginx:latest
docker.io/library/nginx:latest
# ejecutar contenedor en la maquina
docker container run -d -p 80:80 nginx
0b0148ec3724e7ca50463188d16e098f702bc2a5b8d493fd062424f587c577fb
# obtener ip de la maquina virtual
docker-machine ip maquina-test
192.168.99.101
# probar con cURL peticion get, o desde el navegador, ej curl
curl 192.168.99.101:80
#salida
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

...
</body>
</html>

# ver los contenedores en la conexion cliente activa
docker container ls -a
CONTAINER ID    IMAGE    COMMAND                  CREATED          STATUS           PORTS
0b0148ec3724    nginx    "nginx -g 'daemon of…"   4 minutes ago    Up 4 minutes     0.0.0.0:80->80/tcp 

# salir
miusuario@mihost:~$ exit
```

- Conexion por SSH

```shell
# uso secuencia de comandos: docker-machine ssh nombre-maquina
docker-machine ssh maquina-test
# prueba sesion conexion ssh
   ( '>')
  /) TC (\   Core is distributed with ABSOLUTELY NO WARRANTY.
 (/-_--_-\)           www.tinycorelinux.net

docker@maquina-test:~$
# listar contenedores activos en maquina virtual
docker@maquina-test:~$ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED           STATUS          PORTS
0b0148ec3724   nginx     "nginx -g 'daemon of…"   13 minutes ago    Up 13 minutes   0.0.0.0:80->80/tcp
# salir
docker@maquina-test:~$ exit
logout
exit status 127
```

- Eliminar Docker machine creada previamente

```shell
# uso comando rm nombre-maquina
docker-machine rm maquina-test
# salida
About to remove maquina-test
WARNING: This action will delete both local reference and remote instance.
Are you sure? (y/n): Y
Successfully removed maquina-test
```