# Variables de entorno

- Definir variables entorno con archivo externo .env

    [docker-compose.yml](./servicios/docker-compose.yml) editado
    [.env](./servicios/.env) editado

```shell
# modificar docker-compose.yml para leer .env con sistanxis de interpolación
version: "3.7"

services: 
    nginx:
        image: nginx
        container_name: nginx
        ports: 
            - "80:80"

    mysql:
        image: mysql
        container_name: mysql
        ports: 
            - "3306:3306"
        environment:
            MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}

# agregar nombre=valor a variables en .env
MYSQL_ROOT_PASSWORD=root

# actualizar con modifcaciones del .yml
cd variables_entorno
docker-compose up -d

Creating nginx ... done
Creating mysql ... done
```