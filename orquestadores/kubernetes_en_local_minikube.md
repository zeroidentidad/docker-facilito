# Kubernetes en local minikube

- Instalación minikube y kubectl

    Enlaces de documentación instalación minikube:
    - https://kubernetes.io/docs/tasks/tools/install-minikube/
    - https://minikube.sigs.k8s.io/docs/start/

    Enlace de documentación instalaciones kubectl CLI:
    - https://kubernetes.io/docs/tasks/tools/install-kubectl/

- Usando minikube

```shell
# iniciar minikube 
minikube start

🎉  minikube 1.8.2 is available! Download it: https://github.com/kubernetes/minikube/releases/tag/v1.8.2
💡  To disable this notice, run: 'minikube config set WantUpdateNotification false'

🙄  minikube v1.6.2 on Ubuntu 18.04
✨  Selecting 'virtualbox' driver from user configuration (alternates: [none])
💡  Tip: Use 'minikube start -p <name>' to create a new cluster, or 'minikube delete' to delete this one.
🔄  Starting existing virtualbox VM for "minikube" ...
⌛  Waiting for the host to be provisioned ...
🐳  Preparing Kubernetes v1.17.0 on Docker '19.03.5' ...
🚀  Launching Kubernetes ... 
🏄  Done! kubectl is now configured to use "minikube"

# una vez finalice inicio minikube, verificar el estado del clúster
minikube status

# usar kubectl, ver ayuda
kubectl run --help

Create and run a particular image, possibly replicated.

 Creates a deployment or job to manage the created container(s).

Examples:
  # Start a single instance of nginx.
  kubectl run nginx --image=nginx
  
  # Start a single instance of hazelcast and let the container expose port 5701 .
  kubectl run hazelcast --image=hazelcast --port=5701
  
  # Start a single instance of hazelcast and set environment variables "DNS_DOMAIN=cluster" and "POD_NAMESPACE=default" in the container.
  kubectl run hazelcast --image=hazelcast --env="DNS_DOMAIN=cluster" --env="POD_NAMESPACE=default"
  
  # Start a single instance of hazelcast and set labels "app=hazelcast" and "env=prod" in the container.
  kubectl run hazelcast --image=hazelcast --labels="app=hazelcast,env=prod"
  
  # Start a replicated instance of nginx.
  kubectl run nginx --image=nginx --replicas=5
  
  # Dry run. Print the corresponding API objects without creating them.
  kubectl run nginx --image=nginx --dry-run
  ...

# ejemplo crear servicio de kubernetes 
kubectl run nginx --image=nginx

# ver pods en ejecución, ver todo: kubectl get all
kubectl get pods

NAME                     READY   STATUS    RESTARTS   AGE
nginx-7c5f787696-vjgkx   1/1     Running   0          56s

# ver deployments en ejecución
kubectl get deployments

NAME    READY   UP-TO-DATE   AVAILABLE   AGE
nginx    1/1     1            1           56s
```