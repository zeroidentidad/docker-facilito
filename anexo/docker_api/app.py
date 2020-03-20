import docker

client = docker.DockerClient('unix://var/run/docker.sock')

container = client.containers.run("nginx", detach=True, ports={'80/tcp': 80})

for container in client.containers.list():
    print(container.name)

for image in client.images.list():
    print(image.tag)    