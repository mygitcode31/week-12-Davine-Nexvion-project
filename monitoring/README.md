# Monitoring and Centralized Logging

## Overview
Nexvion infrastructure monitoring and centralized logging run in the Kubernetes monitoring namespace.

## Metrics Stack

- Prometheus: metrics collection and storage.
- Node Exporter: EC2 CPU and memory metrics.
- Kube State Metrics: Kubernetes resource and pod-state metrics.
- Grafana: metrics exploration and visualization.

## Logging Stack

- Grafana Alloy: collects Kubernetes pod logs through the Kubernetes API.
- Loki: centralized log storage and querying.
- Grafana: log exploration using the Loki datasource.

Loki uses single-binary Monolithic deployment with filesystem storage and a 2Gi persistent volume. Multi-tenancy is enabled with tenant ID `local`.

Alloy runs as one Deployment and discovers Kubernetes pods. It adds namespace, pod, container and node labels before forwarding logs to Loki.

## Helm Configuration

- prometheus-values.yaml
- grafana-values.yaml
- loki-values.yaml
- alloy-values.yaml

Chart versions:
- Prometheus: 29.47.2
- Grafana: 14.4.1
- Loki: 21.3.1
- Alloy: 1.16.0

Grafana credentials are stored in Kubernetes Secret `grafana-admin`. No credentials are committed to Git.

## Verified Metrics

### EC2 CPU utilization
`100 * (1 - avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])))`

### EC2 memory utilization
`100 * (1 - node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)`

### Nexvion pod CPU
`sum by (pod) (rate(container_cpu_usage_seconds_total{namespace="nexvion",container!="",image!=""}[5m]))`

### Nexvion pod readiness
`kube_pod_status_ready{namespace="nexvion",condition="true"}`

Both Nexvion replicas returned readiness value 1.

## Verified Logging

Grafana Loki datasource successfully connected.

LogQL query tested in Grafana Explore:

`{namespace="nexvion"}`

Nexvion Kubernetes logs were visible in Grafana Explore.

## Access

Grafana is exposed internally through a ClusterIP service.

EC2 port-forward:

`kubectl --kubeconfig ~/.kube/config port-forward -n monitoring svc/grafana 3000:80 --address 127.0.0.1`

Windows Git Bash SSH tunnel:

`ssh -i "$HOME/Downloads/myautomation.pem" -N -L 3000:127.0.0.1:3000 ubuntu@13.232.186.176`

Open `http://localhost:3000`.

Prometheus service:
`http://prometheus-server.monitoring.svc.cluster.local`

Loki gateway:
`http://loki-gateway.monitoring.svc.cluster.local`

## Incident Analyzer

`scripts/incident_analyzer.py` is a Python rule-based incident triage utility.

It detects:
- HTTP 5xx errors
- Connection refused/reset
- Readiness/liveness probe failures
- CrashLoopBackOff
- OOMKilled

Test command:

`python3 scripts/incident_analyzer.py scripts/sample_logs/incidents.log`

The sample test detected five incidents. This is rule-based analysis, not a live LLM integration.

## Limitations

- Single-node Kubernetes lab deployment; not highly available.
- Grafana persistence is disabled.
- Loki uses local filesystem storage and is not production-grade distributed storage.
- Alloy uses Kubernetes API log collection rather than host-level log file mounts.
- No custom Grafana dashboard has been provisioned.
- Incident analyzer uses predefined rules and recommendations.
- This is a learning and demonstration environment, not a production monitoring architecture.
