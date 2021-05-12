Installing with Kubernetes
##########################

Running CameraHub with Kubernetes is a powerful but complex choice if you want to run CameraHub in the cloud, at scale.

This guide assumes you already have a Kubernetes cluster available, and a `Helm 3 <https://helm.sh/>`_ client.

It is recommended that you install CameraHub into its own namespace, and not into ``default``.

There is a Helm chart which can install CameraHub with a reasonable set of defaults:

.. code-block:: bash

    helm repo add camerahub https://camerahub.github.io/charts

For full details, check out the `chart repo <https://github.com/camerahub/charts>`_.
