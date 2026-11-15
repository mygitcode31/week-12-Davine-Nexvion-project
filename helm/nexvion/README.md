# Nexvion Helm Chart

## Overview
This Helm chart packages the Nexvion Kubernetes deployment.

## Chart Information
- Chart name: nexvion
- Chart version: 1.0.0
- Application version: v1

## Configurable Values
The values.yaml file controls:
- Replica count
- Container image and tag
- Image pull policy
- Service type and port
- Ingress class and host
- CPU and memory requests and limits

## Validation

    helm lint helm/nexvion

    helm template nexvion helm/nexvion --namespace nexvion

## Installation

    helm upgrade --install nexvion helm/nexvion \
      --namespace nexvion \
      --kubeconfig ~/.kube/config \
      --wait

## Verification

    helm status nexvion -n nexvion --kubeconfig ~/.kube/config

## Deployment Result
Successfully installed as Helm release nexvion, revision 1, with two running application replicas.

## Limitation
The chart uses a locally imported container image with imagePullPolicy Never. The image must exist in the K3s containerd image store on the target node.
