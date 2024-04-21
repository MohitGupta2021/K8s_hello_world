# hello-world-k8s
Kubernetes "Hello World" Application.

Using hello-world YAML file to deploy simple "Hello World" equivalent application
on already setup kubernetes cluster.
use the following commands 
1. minikube start
2.kubectl apply -f helloworld.yaml
3.kubectl expose deployment helloworld --type=NodePort
4 .minikube service helloworld
5.python main.py


Thank You.
