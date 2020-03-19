# Docker swarm deploy servicio

- Inicio desplegar servicios

```shell
# teniendo sesion activa por ssh, acceder al nodo manager
docker-machine ssh manager1
docker@manager1:~$

# hacer deploy de contenedor que ejecute servicio, ej. Redis con 1 replica

# crear capa servicio
docker service create --replicas 1 --name redis redis:4

xxouscqvq3cbjcrf7d1at7qi0
overall progress: 1 out of 1 tasks 
1/1: running   [==================================================>] 
verify: Service converged 

# ver servicios creados
docker service ls

ID                  NAME                MODE                REPLICAS            IMAGE   
xxouscqvq3cb        redis               replicated          1/1                 redis:4

# inspeccionar servicio en detalle
docker service inspect --pretty redis 

ID:		xxouscqvq3cbjcrf7d1at7qi0
Name:		redis
Service Mode:	Replicated
 Replicas:	1
Placement:
UpdateConfig:
 Parallelism:	1
 On failure:	pause
 Monitoring Period: 5s
 Max failure ratio: 0
 Update order:      stop-first
RollbackConfig:
 Parallelism:	1
 On failure:	pause
 Monitoring Period: 5s
 Max failure ratio: 0
 Rollback order:    stop-first
ContainerSpec:
 Image:		redis:4@sha256:9532d7739157a6f110315b8bc9ff5c81b8f3d44e5155b2ed167bd6a775ba279f
 Init:		false
Resources:
Endpoint Mode:	vip


# eliminar servicio
docker service rm redis

# ver ayuda comandos
docker service --help
Usage:	docker service COMMAND

Manage services

Commands:
  create      Create a new service
  inspect     Display detailed information on one or more services
  logs        Fetch the logs of a service or task
  ls          List services
  ps          List the tasks of one or more services
  rm          Remove one or more services
  rollback    Revert changes to a service configuration
  scale       Scale one or multiple replicated services
  update      Update a service
```