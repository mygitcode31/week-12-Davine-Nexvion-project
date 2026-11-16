# Prometheus and Grafana Monitoring

## Overview
Prometheus and Grafana monitor the Nexvion Kubernetes deployment and EC2 infrastructure.

## Components
- Prometheus: metrics collection and storage.
- Node Exporter: EC2 CPU and memory metrics.
- Kube State Metrics: Kubernetes pod and resource-state metrics.
- Grafana: metrics exploration and visualization.

## Deployment
Both Prometheus and Grafana are deployed using Helm in the monitoring namespace.

Configuration files:
- prometheus-values.yaml
- grafana-values.yaml

Grafana credentials are stored in the Kubernetes Secret grafana-admin. No credentials are committed to Git.

## Verified metrics
The following queries were successfully tested in Grafana Explore.

### EC2 CPU utilization
`100 * (1 - avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])))`

### EC2 memory utilization
`100 * (1 - node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)`

### Nexvion pod CPU
`sum by (pod) (rate(container_cpu_usage_seconds_total{namespace="nexvion",container!="",image!=""}[5m]))`

### Nexvion pod readiness
`kube_pod_status_ready{namespace="nexvion",condition="true"}`

Both Nexvion replicas returned readiness value 1.

## Access
Grafana is exposed internally using a ClusterIP service.

EC2 port-forward command:
`sudo k3s kubectl port-forward -n monitoring svc/grafana 3000:80 --address 127.0.0.1`

Local SSH tunnel:
`ssh -i "$HOME/Downloads/myautomation.pem" -N -L 3000:127.0.0.1:3000 ubuntu@13.232.186.176`

Open http://localhost:3000.

Prometheus internal service:
`http://prometheus-server.monitoring.svc.cluster.local`

## Limitations
- This is a single-node Kubernetes lab deployment.
- Grafana persistence is disabled to conserve resources.
- Metrics were verified in Grafana Explore; a custom dashboard has not been provisioned.
- This is not a production high-availability monitoring architecture.
