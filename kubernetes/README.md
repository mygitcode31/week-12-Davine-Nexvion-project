# Nexvion Kubernetes Deployment

## Overview
Nexvion is deployed as a static e-commerce frontend on a single-node K3s cluster.

## Architecture
- Kubernetes distribution: K3s
- Container runtime: containerd
- Namespace: nexvion
- Container image: nexvion-web:v1
- Replicas: 2
- Configuration: ConfigMap
- Service: ClusterIP
- Ingress controller: Traefik
- Public HTTP port: 80

## Kubernetes Resources
The nexvion.yaml manifest defines:
- Namespace
- Nginx ConfigMap
- Deployment with two replicas
- ClusterIP Service
- Traefik Ingress

## Deployment
Apply the manifest:

    sudo k3s kubectl apply -f kubernetes/nexvion.yaml

Check deployment:

    sudo k3s kubectl get all -n nexvion

## Verification
The homepage, products page and payment page returned HTTP 200 through the Kubernetes Ingress.

## Limitations
The application is a static frontend. It does not provide a production backend, database or real payment processing.
