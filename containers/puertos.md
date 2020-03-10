# Puertos

- Imagen y contenedor de prueba inical

```shell
# descarga imagen nginx para ejemplo hub.docker.com/_/nginx
docker image pull nginx
# ejecutar contenedor de prueba con imagen nginx
docker container run -d nginx
449b68085f6c96c9a3f9a55ea5e9f3a495e311f486e323fdcd6092311a902f56
# listar contenedor creado
docker container ls
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS
449b68085f6c        nginx               "nginx -g 'daemon of…"   2 minutes ago       Up 2 minutes        80/tcp
f93bf0ccdc60        ubuntu-tools        "/bin/bash"              37 minutes ago      Up 35 minutes             

# probar mostrar info del index
curl localhost
# servicio de nginx se expone dentro pero no fuera del contenedor
curl: (7) Failed to connect to localhost port 80: Conexión rehusada
```

- Exponer puerto de contenedor a host local

```shell
# detener contenedores de pruebas anteriores
docker stop $(docker ps -q)
# ejecutar nuevo contenedor de prueba con imagen nginx
# uso flag -p (publicar puerto host local), no -P (mayus, aleatoriamente)
# -p sistema:contenedor
docker container run -d -p 8080:80 nginx
66dd98b03d3fd28b443d1ec611d981fd18606f60c01045fc52fdd2b7406be7f7

# probar mostrar info del index
curl localhost:8080
# servicio de nginx ahora se expone fuera del contenedor
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
```

- Ver puertos expueto de contenedor

```shell
# listar contenedores creados en ejecucion
docker container ls
CONTAINER ID        IMAGE     COMMAND                  CREATED          STATUS         PORTS 
66dd98b03d3f        nginx     "nginx -g 'daemon of…"   8 minutes ago    Up 8 minutes   0.0.0.0:8080->80/tcp
# uso comando port
docker container port 66dd98b03d3f
# salida
80/tcp -> 0.0.0.0:8080
```

- Asignar puerto aleatoriemante de contenedor a host local
```shell
# ejecutar nuevo contenedor de prueba con imagen nginx
# uso flag -P (mayus, aleatoriamente)
docker container run -d -P nginx
105a2e895101ab51ccad7f6c3849d0a670b491ac90eb0567b01a55fc769cbb71
# listar contenedores creados en ejecucion
docker container ls
CONTAINER ID     IMAGE      COMMAND                  CREATED          STATUS         PORTS
105a2e895101     nginx      "nginx -g 'daemon of…"   18 seconds ago   Up 14 seconds  0.0.0.0:32768->80/tcp
66dd98b03d3f     nginx      "nginx -g 'daemon of…"   17 minutes ago   Up 17 minutes  0.0.0.0:8080->80/tcp

# probar mostrar info del index
curl localhost:32768
# servicio de nginx ahora se expone fuera del contenedor con el puerto aleatorio
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
```

- Nota multiples servicios a exponer puertos

```shell
# concatenar flags -p valor sistema:contenedor
docker container run -d -p 8080:80 -p 3001:3000 -p 2222:2222 nginx
```