# Creando redes

- Crear red de imagen

    [Dockerfile](./crear_red/Dockerfile) editado

```shell
# editar contenido Dockerfile
FROM ubuntu

RUN apt-get update && apt-get install net-tools iputils-ping -y

# generar imagen usando Dockerfile
docker image build -t ubuntu-tools .
# salida
Sending build context to Docker daemon  2.048kB
Step 1/2 : FROM ubuntu
 ---> 72300a873c2c
Step 2/2 : RUN apt-get update && apt-get install net-tools iputils-ping -y
 ---> Running in a24f7101eaef
Get:1 http://security.ubuntu.com/ubuntu bionic-security InRelease [88.7 kB]
Get:2 http://archive.ubuntu.com/ubuntu bionic InRelease [242 kB]
...
Fetched 17.6 MB in 2min 6s (139 kB/s)
Reading package lists...
Reading package lists...
Building dependency tree...
Reading state information...
The following additional packages will be installed:
  libcap2 libcap2-bin libidn11 libpam-cap
The following NEW packages will be installed:
  iputils-ping libcap2 libcap2-bin libidn11 libpam-cap net-tools
0 upgraded, 6 newly installed, 0 to remove and 0 not upgraded.
Need to get 336 kB of archives.
After this operation, 1339 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu bionic/main amd64 libcap2 amd64 1:2.25-1.2 [13.0 kB]
...
debconf: delaying package configuration, since apt-utils is not installed
Fetched 336 kB in 3s (97.5 kB/s)
Selecting previously unselected package libcap2:amd64.
(Reading database ... 4046 files and directories currently installed.)
Preparing to unpack .../0-libcap2_1%3a2.25-1.2_amd64.deb ...
Unpacking libcap2:amd64 (1:2.25-1.2) ...
Selecting previously unselected package libidn11:amd64.
Preparing to unpack .../1-libidn11_1.33-2.1ubuntu1.2_amd64.deb ...
Unpacking libidn11:amd64 (1.33-2.1ubuntu1.2) ...
Selecting previously unselected package iputils-ping.
Preparing to unpack .../2-iputils-ping_3%3a20161105-1ubuntu3_amd64.deb ...
Unpacking iputils-ping (3:20161105-1ubuntu3) ...
Selecting previously unselected package libcap2-bin.
Preparing to unpack .../3-libcap2-bin_1%3a2.25-1.2_amd64.deb ...
Unpacking libcap2-bin (1:2.25-1.2) ...
Selecting previously unselected package libpam-cap:amd64.
Preparing to unpack .../4-libpam-cap_1%3a2.25-1.2_amd64.deb ...
Unpacking libpam-cap:amd64 (1:2.25-1.2) ...
Selecting previously unselected package net-tools.
Preparing to unpack .../5-net-tools_1.60+git20161116.90da8a0-1ubuntu1_amd64.deb ...
Unpacking net-tools (1.60+git20161116.90da8a0-1ubuntu1) ...
Setting up libcap2:amd64 (1:2.25-1.2) ...
Setting up net-tools (1.60+git20161116.90da8a0-1ubuntu1) ...
Setting up libidn11:amd64 (1.33-2.1ubuntu1.2) ...
Setting up iputils-ping (3:20161105-1ubuntu3) ...
Setting up libpam-cap:amd64 (1:2.25-1.2) ...
debconf: unable to initialize frontend: Dialog
debconf: (TERM is not set, so the dialog frontend is not usable.)
debconf: falling back to frontend: Readline
debconf: unable to initialize frontend: Readline
Setting up libcap2-bin (1:2.25-1.2) ...
Processing triggers for libc-bin (2.27-3ubuntu1) ...
Removing intermediate container a24f7101eaef
 ---> 6c0352412a2f
Successfully built 6c0352412a2f
Successfully tagged ubuntu-tools:latest

# crear nueva red a usar al generar contenedor de la imagen
# ver ayuda
docker network create --help

Usage:	docker network create [OPTIONS] NETWORK

Create a network

Options:
      --attachable           Enable manual container attachment
      --aux-address map      Auxiliary IPv4 or IPv6 addresses used by Network driver (default map[])
      --config-from string   The network from which copying the configuration
      --config-only          Create a configuration only network
  -d, --driver string        Driver to manage the Network (default "bridge")
      --gateway strings      IPv4 or IPv6 Gateway for the master subnet
      --ingress              Create swarm routing-mesh network
      --internal             Restrict external access to the network
      --ip-range strings     Allocate container ip from a sub-range
      --ipam-driver string   IP Address Management Driver (default "default")
      --ipam-opt map         Set IPAM driver specific options (default map[])
      --ipv6                 Enable IPv6 networking
      --label list           Set metadata on a network
  -o, --opt map              Set driver specific options (default map[])
      --scope string         Control the networks scope
      --subnet strings       Subnet in CIDR format that represents a network segment

# sentencia de comando para crear red con flag -d (driver de red)
docker network create -d bridge br0
8e9c2463ce18fa0e9e653e46ed728f031205d94973d8a428953cd1c606099abe
# inspeccionar nueva red
docker network inspect br0
[
    {
        "Name": "br0",
        "Id": "8e9c2463ce18fa0e9e653e46ed728f031205d94973d8a428953cd1c606099abe",
        "Created": "2020-03-09T20:38:31.624165412-06:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": {},
            "Config": [
                {
                    "Subnet": "172.22.0.0/16",
                    "Gateway": "172.22.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {},
        "Options": {},
        "Labels": {}
    }
]
```

- Agregar contenedor a red de imagen previa

```shell
# crear contenedores nombrados de prueba para usar red creada previamente
docker container run -dit --network br0 --name chost1 ubuntu-tools
35a0180c4e62a261a4e166d2d1aa08d2a38af6d8a98591db5d017641c16a99c6

docker container run -dit --network br0 --name chost2 ubuntu-tools
59be481166019b9e50ef54704686a1809aa1135753dfc60cfcc14e5d8db37cfa

# listar contenedores en ejecucion
docker ps
CONTAINER ID     IMAGE            COMMAND         CREATED              STATUS               NAMES
59be48116601     ubuntu-tools     "/bin/bash"     About a minute ago   Up About a minute    chost2
35a0180c4e62     ubuntu-tools     "/bin/bash"     2 minutes ago        Up 2 minutes         chost1

# probar comunicacion red contenedores accediendo a ejecucion de comandos
# terminal 1
docker container exec -it chost1 bash
root@35a0180c4e62:/ ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.22.0.2  netmask 255.255.0.0  broadcast 172.22.255.255
        ether 02:42:ac:16:00:02  txqueuelen 0  (Ethernet)

# terminal 2
docker container exec -it chost2 bash
root@59be48116601:/ ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.22.0.3  netmask 255.255.0.0  broadcast 172.22.255.255
        ether 02:42:ac:16:00:03  txqueuelen 0  (Ethernet)

# ping entre ip de contenedores
# terminal 1 ping a chost2
root@35a0180c4e62:/ ping 172.22.0.3
PING 172.22.0.3 (172.22.0.3) 56(84) bytes of data.
64 bytes from 172.22.0.3: icmp_seq=1 ttl=64 time=0.213 ms
64 bytes from 172.22.0.3: icmp_seq=2 ttl=64 time=0.161 ms
64 bytes from 172.22.0.3: icmp_seq=3 ttl=64 time=0.161 ms
64 bytes from 172.22.0.3: icmp_seq=4 ttl=64 time=0.163 ms
64 bytes from 172.22.0.3: icmp_seq=5 ttl=64 time=0.160 ms
^C
--- 172.22.0.3 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4100ms
rtt min/avg/max/mdev = 0.160/0.171/0.213/0.025 ms

# terminal 2 ping a chost1
root@59be48116601:/ ping 172.22.0.2
PING 172.22.0.2 (172.22.0.2) 56(84) bytes of data.
64 bytes from 172.22.0.2: icmp_seq=1 ttl=64 time=0.317 ms
64 bytes from 172.22.0.2: icmp_seq=2 ttl=64 time=0.162 ms
64 bytes from 172.22.0.2: icmp_seq=3 ttl=64 time=0.161 ms
64 bytes from 172.22.0.2: icmp_seq=4 ttl=64 time=0.161 ms
64 bytes from 172.22.0.2: icmp_seq=5 ttl=64 time=0.161 ms
64 bytes from 172.22.0.2: icmp_seq=6 ttl=64 time=0.161 ms
64 bytes from 172.22.0.2: icmp_seq=7 ttl=64 time=0.161 ms
^C
--- 172.22.0.2 ping statistics ---
7 packets transmitted, 7 received, 0% packet loss, time 6131ms
rtt min/avg/max/mdev = 0.161/0.183/0.317/0.055 ms

# terminal 1 ping a chost2 - igual usando nombre del contenedor
root@35a0180c4e62:/ ping chost2
PING chost2 (172.22.0.3) 56(84) bytes of data.
64 bytes from chost2.br0 (172.22.0.3): icmp_seq=1 ttl=64 time=0.178 ms
64 bytes from chost2.br0 (172.22.0.3): icmp_seq=2 ttl=64 time=0.162 ms
64 bytes from chost2.br0 (172.22.0.3): icmp_seq=3 ttl=64 time=0.163 ms
^C
--- chost2 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2025ms
rtt min/avg/max/mdev = 0.162/0.167/0.178/0.016 ms
```
