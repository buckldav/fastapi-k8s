# FastAPI + MongoDB + Kubernetes

Boilerplate for FastAPI + MongoDB deployed to a kubernetes cluster.

## FastAPI Dev

`build.sh` and `manifests/fastapi-deployment.yaml` both have `dbuckleysm/myfastapi:v2` as the tag for the FastAPI docker image. This is the image for the FastAPI app in its current state. If you want to make changes to the app and build a new image, replace `dbuckleysm` with your Docker Hub (or other container registry) username in those two files.

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

## Deploy to Kubernetes Cluster

Run a cluster somewhere and [connect to it](https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster/) (with `KUBECONFIG` env var or something). Local cluster options for beginners:

- Docker Desktop has a built in [Kubernetes integration that you can enable](https://docs.docker.com/desktop/kubernetes/). If enabled, your `kubectl` will automatically be connected locally.
- Run [minikube](https://minikube.sigs.k8s.io/docs/start/) locally.

```bash
sh kubectl-start.sh
sh kubectl-stop.sh
```
