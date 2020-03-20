# Docker api
 
 - Ejemplo interacción Docker API

    - Enlace doc base: https://docs.docker.com/engine/api/sdk/

    - Doc api actual: https://docs.docker.com/engine/api/v1.40/

    - Imagen para ejemplo: https://hub.docker.com/_/python

    [app.py](./docker_api/app.py) editado


```shell
# crear directorio para codigo ejemplo (docker_api)
cd docker_api

# descargar imagen lenguaje desarrollo
docker image pull python:3.6

3.6: Pulling from library/python
50e431f79093: Pull complete 
dd8c6d374ea5: Pull complete 
c85513200d84: Pull complete 
55769680e827: Pull complete 
f5e195d50b88: Pull complete 
bcd75869ea17: Pull complete 
f02a073bb16c: Pull complete 
d317a9591eb3: Pull complete 
579334b3a1fd: Pull complete 
Digest: sha256:0b6aeeb47c4a5e0051bb41c7a7f300b69e68af873081f8f2f7fbcd8d5c47e264
Status: Downloaded newer image for python:3.6
docker.io/library/python:3.6

# crear script py de ejemplo
touch app.py

# ejecutar contenedor de imagen descargada y mapear socket comunicacion api
docker run -dit -v $PWD:/home/app -v /var/run/docker.sock:/var/run/docker.sock python:3.6
6fa8652345dcc0fa102968767320e1086118cc1c66f80eb4cfce0000ea54dd2b

# ver contenedores en ejecucion
docker ps
CONTAINER ID     IMAGE        COMMAND       CREATED              STATUS
6fa8652345dc     python:3.6   "python3"     About a minute ago   Up About a minute

# ingresar a ejecutar comandos en contenedor
docker exec -it 6fa8652345dc bash
root@6fa8652345dc:/ cd /home/app && ls
app.py

# instalar SDK para python con pip
pip install docker

Collecting docker
  Downloading docker-4.2.0-py2.py3-none-any.whl (143 kB)
     |████████████████████████████████| 143 kB 222 kB/s 
Collecting six>=1.4.0
  Downloading six-1.14.0-py2.py3-none-any.whl (10 kB)
Collecting requests!=2.18.0,>=2.14.2
  Downloading requests-2.23.0-py2.py3-none-any.whl (58 kB)
     |████████████████████████████████| 58 kB 180 kB/s 
Collecting websocket-client>=0.32.0
  Downloading websocket_client-0.57.0-py2.py3-none-any.whl (200 kB)
     |████████████████████████████████| 200 kB 255 kB/s 
Collecting idna<3,>=2.5
  Downloading idna-2.9-py2.py3-none-any.whl (58 kB)
     |████████████████████████████████| 58 kB 171 kB/s 
Collecting certifi>=2017.4.17
  Downloading certifi-2019.11.28-py2.py3-none-any.whl (156 kB)
     |████████████████████████████████| 156 kB 253 kB/s 
Collecting urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1
  Downloading urllib3-1.25.8-py2.py3-none-any.whl (125 kB)
     |████████████████████████████████| 125 kB 153 kB/s 
Collecting chardet<4,>=3.0.2
  Downloading chardet-3.0.4-py2.py3-none-any.whl (133 kB)
     |████████████████████████████████| 133 kB 106 kB/s 
Installing collected packages: six, idna, certifi, urllib3, chardet, requests, websocket-client, docker
Successfully installed certifi-2019.11.28 chardet-3.0.4 docker-4.2.0 idna-2.9 requests-2.23.0 six-1.14.0 urllib3-1.25.8 websocket-client-0.57.0
root@6fa8652345dc:/home/app#

# editar script creado previamente
code app.py

# codigo de ejemplo
import docker

client = docker.DockerClient('unix://var/run/docker.sock')

for container in client.containers.list():
    print(container.name)

# ejecutar codigo en contenedor
root@6fa8652345dc:/home/app# python app.py

nice_jepsen

# comprobar salida host
chucho@enigma:~$ docker ps
CONTAINER ID   IMAGE        COMMAND     CREATED          STATUS           NAMES
6fa8652345dc   python:3.6   "python3"   18 minutes ago   Up 18 minutes    nice_jepsen

# modificacion obtener tags imagenes host en script
import docker

client = docker.DockerClient('unix://var/run/docker.sock')

for container in client.containers.list():
    print(container.name)

for image in client.images.list():
    print(image.tag)

# salida python app.py
root@6fa8652345dc:/home/app# python app.py
nice_jepsen
<bound method Image.tag of <Image: 'zeroidentidad/goregresionpredict:latest'>>
<bound method Image.tag of <Image: 'zeroidentidad/goregresiontrain:multiple'>>
<bound method Image.tag of <Image: 'zeroidentidad/goregresiontrain:lineal'>>
<bound method Image.tag of <Image: 'node:latest'>>
<bound method Image.tag of <Image: 'mysql:latest'>>
<bound method Image.tag of <Image: 'nginx:latest'>>
<bound method Image.tag of <Image: 'python:3.6'>>

# modificacion crear contenedor en host con el script
import docker

client = docker.DockerClient('unix://var/run/docker.sock')

container = client.containers.run("nginx", detach=True, ports={'80/tcp': 80})

for container in client.containers.list():
    print(container.name)

# salida python app.py
root@6fa8652345dc:/home/app# python app.py
relaxed_brahmagupta
nice_jepsen

# comprobar salida host
chucho@enigma:~$ docker ps

CONTAINER ID   IMAGE        COMMAND                  CREATED           STATUS          PORTS                NAMES
c5b8e117fac0   nginx        "nginx -g 'daemon of…"   37 seconds ago    Up 33 seconds   0.0.0.0:80->80/tcp   relaxed_brahmagupta
6fa8652345dc   python:3.6   "python3"                40 minutes ago    Up 40 minutes                        nice_jepsen
```