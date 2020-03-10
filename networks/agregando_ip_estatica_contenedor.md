# Agregando Ip estática a contenedor

- Crear red con un rango de IP

```shell
# ver ayuda y agregar red con rango de ejemplo
# flag --subnet para un segmento de red y --gateway
docker network create --subnet 10.1.0.0/24 --gateway 10.1.0.1 br02
a695e3f56ccea89425bcef9b803be7298a58f94ac9ad29bc5d361aeebbcc8969

# listar redes para ver creada previamente
docker network ls
NETWORK ID          NAME                      DRIVER              SCOPE
8e9c2463ce18        br0                       bridge              local
a695e3f56cce        br02                      bridge              local

# inspeccionar red generada
docker network inspect br02
[
    {
        "Name": "br02",
        "Id": "a695e3f56ccea89425bcef9b803be7298a58f94ac9ad29bc5d361aeebbcc8969",
        "Created": "2020-03-09T21:49:03.831258621-06:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": {},
            "Config": [
                {
                    "Subnet": "10.1.0.0/24", #info interes
                    "Gateway": "10.1.0.1"
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

- Generar contenedor con IP estatica

```shell
# ejecutar nuevo contenedor usando red creada previamente
# uso flag --ip
docker container run -it --ip 10.1.0.11 --network br02 ubuntu-tools
# ver info de red
root@f93bf0ccdc60:/ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.1.0.11  netmask 255.255.255.0  broadcast 10.1.0.255
        ether 02:42:0a:01:00:0b  txqueuelen 0  (Ethernet)
        RX packets 104  bytes 11268 (11.2 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

# inspeccionar red creada previamente
docker network inspect br02
[
    {
        "Name": "br02",
        "Id": "a695e3f56ccea89425bcef9b803be7298a58f94ac9ad29bc5d361aeebbcc8969",
        "Created": "2020-03-09T21:49:03.831258621-06:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": {},
            "Config": [
                {
                    "Subnet": "10.1.0.0/24",
                    "Gateway": "10.1.0.1"
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
        "Containers": {
            "f93bf0ccdc609c610690fcddbf1f50652ca5d37996516366b1de627630ddfa2a": {
                "Name": "modest_wescoff",
                "EndpointID": "3f323f99b2defd9e5904fe76538fef3d2ebb2a5e3b22f5f28c9db23a7d334b1d",
                "MacAddress": "02:42:0a:01:00:0b",
                "IPv4Address": "10.1.0.11/24", # ip manual
                "IPv6Address": ""
            }
        },
        "Options": {},
        "Labels": {}
    }
]
```