# Installing with Kubernetes

Running CameraHub with Kubernetes is a powerful but complex choice if you want to run CameraHub in the cloud, at scale.

This guide assumes you already have a Kubernetes cluster available.

It is recommended that you install CameraHub into its own namespace, and not into `default`.

## Secrets

Add your own secret environment files (either global or per-environment) with your site-specific config in, using the variables described in
[`README.md`](README.md#configuring-camerahub). You can see the Kubernetes default values for these variables in
[`secret.yaml`](../kubernetes/kustomize/camerahub/secret.yaml).

* `kubernetes/kustomize/camerahub.env`
* `kubernetes/overlays/dev/dev.env`
* `kubernetes/overlays/prod/prod.env`

Variables in `dev.env` or `prod.env` override those in `camerahub.env`, and those in `camerahub.env` override the global defaults.
`.env` files won't get added to the git repo due to the `.gitignore` file. Example environment files are included at:

* `kubernetes/kustomize/camerahub.env.example`
* `kubernetes/overlays/dev/dev.env.example`
* `kubernetes/overlays/prod/prod.env.example`

## Production

The production Kustomize overlay configures CameraHub as a 2-replica deployment of CameraHub, deployed from the `latest` Docker image,
which represents the latest stable tag of CameraHub. It uses a single Postgresql replica to store its data. This is not quite
production-ready, and work is ongoing to engineer this properly. It configures an Ingress resource with an SSL certificate provisioned
by Letsencrypt - for this you will need to install [cert-manager](https://cert-manager.io/docs/installation/kubernetes/) before proceeding.

To install CameraHub into Kubernetes using Kustomize, run this:

```sh
# Apply production manifests
kubectl apply -k kubernetes/overlays/prod
```

Run the following command to get the IP address that CameraHub is running on:

```sh
kubectl get -o jsonpath="{.spec.clusterIP}" service camerahub
```

Then navigate to it by IP address, like [http://1.2.3.4:8000](http://1.2.3.4:8000). Login with default username `admin` and password `admin`.

## Development

The development Kustomize overlay configures CameraHub as a single replica deployment of CameraHub, deployed from the `testing` Docker image,
which is buit from git `master` on every push. It uses a single Postgresql replica to store its data. It creates a NodePort Service resource
on `localhost` on a high port.

```sh
# Apply development manifests
kubectl apply -k kubernetes/overlays/dev
```

Run the following command to get the IP address and port that CameraHub is running on:

```sh
kubectl get -o jsonpath="http://{.spec.clusterIP}:{.spec.ports[0].port}" service camerahub
```

Then navigate to it, like [http://10.10.10.10:32000](http://10.10.10.10:32000). Login with default username `admin` and password `admin`.
