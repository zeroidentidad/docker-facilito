# Inspeccionando redes

- Ver redes disponibles a usar

```shell
# usar comando network para info de ayuda
docker network
# salida
Usage:  docker network COMMAND

Manage networks

Commands:
  connect     Connect a container to a network
  create      Create a network
  disconnect  Disconnect a container from a network
  inspect     Display detailed information on one or more networks
  ls          List networks
  prune       Remove all unused networks
  rm          Remove one or more networks

# listar redes disponibles
docker network ls
#salida
NETWORK ID          NAME                      DRIVER              SCOPE
e8a56097f041        bridge                    bridge              local
2c325b6f3a3c        go-react-todo_default     bridge              local
57891919696c        host                      host                local
c0b942849c43        miniapi-node-rn_default   bridge              local
a35faff8cdf8        none                      null                local

# inspeccionar tipo de red
docker network inspect bridge
#salida
[
    {
        "Name": "bridge",
        "Id": "e8a56097f041f0fe69320f9d119be8a17c3aad81e8c2d20f4df35783e081b5d9",
        "Created": "2020-03-08T20:14:08.096383017-06:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "172.17.0.0/16",
                    "Gateway": "172.17.0.1"
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
        "Options": {
            "com.docker.network.bridge.default_bridge": "true",
            "com.docker.network.bridge.enable_icc": "true",
            "com.docker.network.bridge.enable_ip_masquerade": "true",
            "com.docker.network.bridge.host_binding_ipv4": "0.0.0.0",
            "com.docker.network.bridge.name": "docker0",
            "com.docker.network.driver.mtu": "1500"
        },
        "Labels": {}
    }
]
# parte de interes props "IPAM"

# probar agregando un contenedor por defecto 
# (docker container run -dit --network bridge ubuntu)
docker container run -dit ubuntu
2bba6a2c370dcfa7be6c8e7a2ad37238b40b66eef5ae556dc84d999f72e33df9
# inspeccionar red nuevamente
docker network inspect bridge
#salida en ejecucion nuevo contenedor
[
    {
        "Name": "bridge",
        "Id": "e8a56097f041f0fe69320f9d119be8a17c3aad81e8c2d20f4df35783e081b5d9",
        "Created": "2020-03-08T20:14:08.096383017-06:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "172.17.0.0/16",
                    "Gateway": "172.17.0.1"
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
        "Containers": { #new info
            "2bba6a2c370dcfa7be6c8e7a2ad37238b40b66eef5ae556dc84d999f72e33df9": {
                "Name": "trusting_brahmagupta",
                "EndpointID": "f5b7efc97266d5a8da175117cdffbba8466b8166d5a0db60ce2080a77c2787b1",
                "MacAddress": "02:42:ac:11:00:02",
                "IPv4Address": "172.17.0.2/16",
                "IPv6Address": ""
            }
        },
        "Options": {
            "com.docker.network.bridge.default_bridge": "true",
            "com.docker.network.bridge.enable_icc": "true",
            "com.docker.network.bridge.enable_ip_masquerade": "true",
            "com.docker.network.bridge.host_binding_ipv4": "0.0.0.0",
            "com.docker.network.bridge.name": "docker0",
            "com.docker.network.driver.mtu": "1500"
        },
        "Labels": {}
    }
]

# otra forma
docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS
2bba6a2c370d        ubuntu              "/bin/bash"         3 minutes ago       Up 3 minutes

docker container inspect 2bba6a2c370d
# salida
[
    {
        "Id": "2bba6a2c370dcfa7be6c8e7a2ad37238b40b66eef5ae556dc84d999f72e33df9",
        "Created": "2020-03-09T18:52:28.237349195Z",
        "Path": "/bin/bash",
        "Args": [],
        "State": {
            ...
        },
        ...
        "HostConfig": {
            ...
        },
        "GraphDriver": {
            ...
        },
        "Mounts": [],
        "Config": {
            ...
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "9065ed75f1b874b3db78e09cc92ca9dd1a2e3f908f432ef0640cf9474117125f",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {},
            "SandboxKey": "/var/run/docker/netns/9065ed75f1b8",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "f5b7efc97266d5a8da175117cdffbba8466b8166d5a0db60ce2080a77c2787b1",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.2",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "02:42:ac:11:00:02",
            "Networks": {
                "bridge": { # interest info
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "e8a56097f041f0fe69320f9d119be8a17c3aad81e8c2d20f4df35783e081b5d9",
                    "EndpointID": "f5b7efc97266d5a8da175117cdffbba8466b8166d5a0db60ce2080a77c2787b1",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.2",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:11:00:02",
                    "DriverOpts": null
                }
            }
        }
    }
]
```

- Desconectar o conectar contenedor de alguna red

```shell
# ver ayuda para desconectar
docker network disconnect --help

# listar contenedores para deconectar
docker container ls
CONTAINER ID        IMAGE         COMMAND             CREATED             STATUS
2bba6a2c370d        ubuntu        "/bin/bash"         25 minutes ago      Up 25 minute

# hacer deconexion contenedor activo
docker network disconnect bridge 2bba6a2c370d
# inspeccionar red bridge si ya no esta disponible
docker network inspect bridge
        ...
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {}, #vacio
        "Options": {
        ...

# hacer reconexion contenedor activo
docker network connect bridge 2bba6a2c370d
# inspeccionar red bridge si esta nuevamente disponible
docker network inspect bridge
        ...
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {
            "2bba6a2c370dcfa7be6c8e7a2ad37238b40b66eef5ae556dc84d999f72e33df9": {
                "Name": "trusting_brahmagupta",
                "EndpointID": "23cf3fca2575cfcddf824e41395d7a0e4fbf830855bc149cc91fc25120416402",
                "MacAddress": "02:42:ac:11:00:02",
                "IPv4Address": "172.17.0.2/16",
                "IPv6Address": ""
            }
        },
        "Options": {
        ...       
```

- Agregar contenedor a otro tipo de red

```shell
# detener los contenedores en ejecucion
docker stop $(docker ps -q)
# salida listado contenedores detenidos
2bba6a2c370d
2cca7a2c380f
# eliminar todos los contenedores en caso necesario
docker container prune

# crear contenedor de prueba en red none
docker run -dit --network none ubuntu
bd983fff11842f70bd58d6f7540f1f2dadaea44c629a53b11dbe00333ad6c374
# crear contenedor de prueba en red host
docker run -dit --network host ubuntu
2895d18f93bb5e14ef3f0231ea5cb03b64d484bec5859983d657ceebf8e5924b

# inspeccionar red none de los contenedores
docker network inspect none
[
    {
        "Name": "none",
        "Id": "a35faff8cdf87b6ee9b698ea972f33fe685e55ee86461c89f8894d5a29530c03",
        "Created": "2019-10-28T10:30:21.768635701-06:00",
        "Scope": "local",
        "Driver": "null",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": []
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {
            "bd983fff11842f70bd58d6f7540f1f2dadaea44c629a53b11dbe00333ad6c374": {
                "Name": "modest_nightingale",
                "EndpointID": "3b52dc279fa23137cbbe9ea549d984753cfead03484e696f22f286d0233ddb6d",
                "MacAddress": "",
                "IPv4Address": "",
                "IPv6Address": ""
            }
        },
        "Options": {},
        "Labels": {}
    }
]
# inspeccionar red host de los contenedores
docker network inspect host
[
    {
        "Name": "host",
        "Id": "57891919696c8f62e118abd3d1650f1eebbefd65f5b6cd660aad5dd95212ce89",
        "Created": "2019-10-28T10:30:21.904418256-06:00",
        "Scope": "local",
        "Driver": "host",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": []
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {
            "2895d18f93bb5e14ef3f0231ea5cb03b64d484bec5859983d657ceebf8e5924b": {
                "Name": "angry_khorana",
                "EndpointID": "3dea4d58beffa6dfbe1bc0022b2d5a903f0d9a2b7c8cfe7c361a2342b744ee88",
                "MacAddress": "",
                "IPv4Address": "",
                "IPv6Address": ""
            }
        },
        "Options": {},
        "Labels": {}
    }
]

# probar tratando de acceder a internet desde el contenedor en la red none
docker container exec -it modest_nightingale bash
root@bd983fff1184:/ apt-get update
# salida
Err:1 http://archive.ubuntu.com/ubuntu bionic InRelease
  Temporary failure resolving 'archive.ubuntu.com'
Err:2 http://security.ubuntu.com/ubuntu bionic-security InRelease
  Temporary failure resolving 'security.ubuntu.com'
Err:3 http://archive.ubuntu.com/ubuntu bionic-updates InRelease
  Temporary failure resolving 'archive.ubuntu.com'
Err:4 http://archive.ubuntu.com/ubuntu bionic-backports InRelease
  Temporary failure resolving 'archive.ubuntu.com'
Reading package lists... Done
W: Failed to fetch http://archive.ubuntu.com/ubuntu/dists/bionic/InRelease  Temporary failure resolving 'archive.ubuntu.com'
W: Failed to fetch http://archive.ubuntu.com/ubuntu/dists/bionic-updates/InRelease  Temporary failure resolving 'archive.ubuntu.com'
W: Failed to fetch http://archive.ubuntu.com/ubuntu/dists/bionic-backports/InRelease  Temporary failure resolving 'archive.ubuntu.com'
W: Failed to fetch http://security.ubuntu.com/ubuntu/dists/bionic-security/InRelease  Temporary failure resolving 'security.ubuntu.com'
W: Some index files failed to download. They have been ignored, or old ones used instead.

# probar tratando de acceder a internet desde el contenedor en la red host
docker container exec -it angry_khorana bash
root@mihost:/ apt-get update
# salida
Get:1 http://archive.ubuntu.com/ubuntu bionic InRelease [242 kB]
Get:2 http://security.ubuntu.com/ubuntu bionic-security InRelease [88.7 kB]
Get:3 http://archive.ubuntu.com/ubuntu bionic-updates InRelease [88.7 kB]
Get:4 http://security.ubuntu.com/ubuntu bionic-security/universe amd64 Packages [824 kB]
Get:5 http://archive.ubuntu.com/ubuntu bionic-backports InRelease [74.6 kB]                 
Get:6 http://archive.ubuntu.com/ubuntu bionic/main amd64 Packages [1344 kB]
...                                                               
Fetched 17.6 MB in 1min 28s (201 kB/s)                                                                                                               
Reading package lists... Done
# instalar net tools para ver config de red
apt-get install net-tools
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following NEW packages will be installed:
  net-tools
0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
Need to get 194 kB of archives.
After this operation, 803 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu bionic/main amd64 net-tools amd64 1.60+git20161116.90da8a0-1ubuntu1 [194 kB]
Fetched 194 kB in 2s (126 kB/s)     
debconf: delaying package configuration, since apt-utils is not installed
Selecting previously unselected package net-tools.
(Reading database ... 4046 files and directories currently installed.)
Preparing to unpack .../net-tools_1.60+git20161116.90da8a0-1ubuntu1_amd64.deb ...
Unpacking net-tools (1.60+git20161116.90da8a0-1ubuntu1) ...
Setting up net-tools (1.60+git20161116.90da8a0-1ubuntu1) ...
# usar ifconfig para ver detalle de la red host
ifconfig
# salida
docker0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        inet 172.17.0.1  netmask 255.255.0.0  broadcast 172.17.255.255
        inet6 fe80::42:2bff:fe41:ea6a  prefixlen 64  scopeid 0x20<link>
        ether 02:42:2b:41:ea:6a  txqueuelen 0  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 4483  bytes 211843 (211.8 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 283763  bytes 159165894 (159.1 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 283763  bytes 159165894 (159.1 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

# info equivalente en el sistema host
miusuario@mihost:~$ ifconfig
#salida
docker0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        inet 172.17.0.1  netmask 255.255.0.0  broadcast 172.17.255.255
        inet6 fe80::42:2bff:fe41:ea6a  prefixlen 64  scopeid 0x20<link>
        ether 02:42:2b:41:ea:6a  txqueuelen 0  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 4483  bytes 211843 (211.8 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Bucle local)
        RX packets 285435  bytes 159473924 (159.4 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 285435  bytes 159473924 (159.4 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```