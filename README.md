# dapr_minikube

## install required modules

```
# start minikube
minikube start

# install dapr using helm
helm repo add dapr https://dapr.github.io/helm-charts/
helm upgrade --install dapr dapr/dapr --version=1.9 --namespace dapr-system --create-namespace

# push image on minikube
eval $(minikube docker-env)
minikube image build -f Dockerfile

# apply dapr deployment file
kubectl apply -f deployments/dapr

# deploy the app
kubectl apply -f deployments/app-deployment.yaml
```