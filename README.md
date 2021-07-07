# An example Docker / Kubernetes app for Mindforge training!


## Launching the Kubernetes manifests:
kubectl apply -k kube

## Updating the app:

#### Keep-it-simple-mode:
NEW_TAG="$(date +%s)"

docker build -t mindforge-test:${NEW_TAG} .

kubectl set image deployment/mindforge mindforge=mindforge-test:${NEW_TAG}

#### TODO:

- Add kubernetes resources

- Add an easier way to develop

- Go to production!
