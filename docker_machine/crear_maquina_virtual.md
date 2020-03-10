# Crear maquina virtual

#### Enlace de ayuda: https://docs.docker.com/machine/get-started/

- Crear docker machine usando driver virtualbox

    Enlace doc driver: https://docs.docker.com/machine/drivers/virtualbox/

```shell
# listar si hay maquinas creadas
docker-machine ls
# sentencia de comandos de ejemplo docker machine de prueba
docker-machine create --driver virtualbox maquina-test
# salida log
Creating CA: /home/miusuario/.docker/machine/certs/ca.pem
Creating client certificate: /home/miusuario/.docker/machine/certs/cert.pem
Running pre-create checks...
(maquina-test) Image cache directory does not exist, creating it at /home/miusuario/.docker/machine/cache...
(maquina-test) No default Boot2Docker ISO found locally, downloading the latest release...
(maquina-test) Latest release for github.com/boot2docker/boot2docker is v19.03.5
(maquina-test) Downloading /home/miusuario/.docker/machine/cache/boot2docker.iso from https://github.com/boot2docker/boot2docker/releases/download/v19.03.5/boot2docker.iso...
(maquina-test) 0%....10%....20%....30%....40%....50%....60%....70%....80%....90%....100%
Creating machine...
(maquina-test) Copying /home/miusuario/.docker/machine/cache/boot2docker.iso to /home/miusuario/.docker/machine/machines/maquina-test/boot2docker.iso...
(maquina-test) Creating VirtualBox VM...
(maquina-test) Creating SSH key...
(maquina-test) Starting the VM...
(maquina-test) Check network to re-create if needed...
(maquina-test) Waiting for an IP...
Waiting for machine to be running, this may take a few minutes...
Detecting operating system of created instance...
Waiting for SSH to be available...
Detecting the provisioner...
Provisioning with boot2docker...
Copying certs to the local machine directory...
Copying certs to the remote machine...
Setting Docker configuration on the remote daemon...
Checking connection to Docker...
Docker is up and running!
To see how to connect your Docker Client to the Docker Engine running on this virtual machine, run: docker-machine env maquina-test

# ver datos de conexion
docker-machine env maquina-test
# salida
export DOCKER_TLS_VERIFY="1"
export DOCKER_HOST="tcp://192.168.99.101:2376"
export DOCKER_CERT_PATH="/home/miusuario/.docker/machine/machines/maquina-test"
export DOCKER_MACHINE_NAME="maquina-test"
# Run this command to configure your shell: 
# eval $(docker-machine env maquina-test)

# en terminal de la nueva maquina para iniciar
eval $(docker-machine env maquina-test)

# listar maquinas docker
docker-machine ls
NAME           ACTIVE   DRIVER       STATE     URL                         SWARM   DOCKER     ERRORS
maquina-test   *        virtualbox   Running   tcp://192.168.99.101:2376           v19.03.5 
```