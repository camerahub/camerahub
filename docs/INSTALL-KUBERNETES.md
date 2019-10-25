# Installing with Kubernetes

_Note: these instructions are a work in progress_

Running PhotoDB with Kubernetes is a powerful but complex choice if you want to run PhotoDB in the cloud, at scale.

This guide assumes you already have a Kubernetes cluster available.

It is recommended that you install PhotoDB into its own namespace, and not into `default`.

This project contains a directory of Kubernetes manifests which set up a 2-replica deployment of PhotoDB which uses a single Postgresql
replica to store its data. This is not quite production-ready, and work is ongoing to engineer this properly.

To install PhotoDB into Kubernetes, run this

```sh
cd kubernetes
kubectl apply -f .
```

Run the following command to get the IP address that PhotoDB is running on:

```sh
kubectl get -o jsonpath="{.spec.clusterIP}" service photodb
```

Then navigate to it by IP address, like [http://1.2.3.4:8000](http://1.2.3.4:8000). Login with default username `admin` and password `admin`.