kubectl apply -f manifests/db-pv.yaml 
kubectl apply -f manifests/db-pvc.yaml
kubectl apply -f manifests/fastapi-deployment.yaml
kubectl apply -f manifests/fastapi-service.yaml