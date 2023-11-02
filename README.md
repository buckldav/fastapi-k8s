# FastAPI + MongoDB + Kubernetes

Boilerplate for FastAPI + MongoDB deployed to a kubernetes cluster.

## FastAPI Dev

`build.sh` and `manifests/fastapi-deployment.yaml` both have `dbuckleysm/myfastapi:v2` as the tag for the FastAPI docker image. Replace `dbuckleysm` with your Docker Hub (or other container registry) username.

```bash
cd myfastapi
# reqs (install in venv)
pip install -r requirements.txt
# local dev (run mongodb somewhere)
# replace with your mongo connection uri
export DB_CONNECTION_URI="mongodb://admin:password@localhost:27017"
# localhost:8000 (default)
uvicorn main:app --reload
# build and tag docker image
sh build.sh
```

## Kubernetes

Run a cluster somewhere and connect to it (with `KUBECONFIG` env var or something). Options for beginners:

- Docker Desktop has a built in [Kubernetes integration that you can enable](https://docs.docker.com/desktop/kubernetes/).
- Run [minikube](https://minikube.sigs.k8s.io/docs/start/) locally.

```bash
sh kubectl-start.sh
sh kubectl-stop.sh
```
