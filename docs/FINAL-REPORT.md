# Final Project Report: Nexvion DevOps Platform

## 1. Project Overview
Nexvion is a frontend-only e-commerce demonstration used to implement a DevOps and cloud-native delivery workflow on AWS EC2.

## 2. Objectives
- Automate source validation, image building and deployment.
- Containerize and harden the frontend.
- Deploy the application on Kubernetes using Helm.
- Implement infrastructure and configuration validation.
- Monitor infrastructure and application workloads.
- Centralize Kubernetes logs and demonstrate incident triage.

## 3. Technology Stack
- OS: Ubuntu Linux
- Source control: Git and GitHub
- CI/CD: Jenkins and GitHub Webhook
- Containers: Docker and Docker Compose
- Security: Trivy and Gitleaks
- IaC: Terraform
- Configuration management: Ansible
- Orchestration: K3s Kubernetes
- Deployment packaging: Helm
- Metrics: Prometheus, Node Exporter, Kube State Metrics
- Visualization: Grafana
- Logging: Grafana Alloy and Loki
- Incident triage: Python

## 4. Implementation Summary

### CI/CD and Containers
Jenkins pipeline validates source code, builds the Docker image, scans it with Trivy, deploys using Docker Compose and verifies application pages.

The hardened Nginx image runs as a non-root user with a read-only filesystem and restricted Linux capabilities. The tested v5 image had zero HIGH and CRITICAL Trivy findings.

### Infrastructure and Configuration
Terraform was used to import and validate the existing AWS security group configuration. Ansible playbook validation completed successfully using a local inventory.

### Kubernetes
The frontend was deployed to a single-node K3s cluster through Helm with two replicas, health probes, resource settings and container security controls.

### Monitoring and Logging
Prometheus collects EC2 and Kubernetes metrics. Grafana provides metrics exploration. Grafana Alloy collects Kubernetes pod logs and forwards them to Loki. The Loki datasource and Nexvion log query were verified in Grafana Explore.

### Incident Analyzer
A Python rule-based utility identifies HTTP 5xx errors, connection failures, probe failures, CrashLoopBackOff and OOMKilled patterns. Sample testing detected five incidents. It is not a live LLM integration.

## 5. Security and Validation
- Trivy image scan: zero HIGH and CRITICAL findings for v5.
- Docker container: non-root execution and restricted capabilities.
- Kubernetes: non-root security context, read-only root filesystem, seccomp and dropped capabilities.
- Jenkins pipeline: successful build, scan, deployment and endpoint verification.
- Ansible: local playbook validation successful.
- Terraform: formatting, validation and plan checks completed.

The existing AWS security group has broad ingress and egress exposure identified during Terraform security analysis. It remains unchanged in this lab to avoid disrupting access.

## 6. Application and Service Access
- Nexvion frontend: http://13.232.186.176/
- Jenkins: http://13.232.186.176:8080/
- Grafana: access through the documented SSH tunnel and local port-forward in monitoring/README.md.

## 7. Limitations
- The application is a static frontend demo; there is no production backend, database or real payment processing.
- Terraform validates an imported security group and does not provision the complete environment.
- Ansible validation uses a local inventory.
- Kubernetes is a single-node lab cluster.
- Grafana persistence is disabled.
- Loki uses local filesystem storage.
- The Python incident analyzer is rule-based, not live AI inference.
- The environment is not designed for production high availability.

## 8. Evidence Checklist
Capture and include:
- Jenkins successful pipeline.
- Trivy v5 image scan results.
- Terraform validation and plan.
- Successful Ansible playbook run.
- Kubernetes pods and Helm release.
- Prometheus metrics in Grafana.
- Loki datasource connection and Nexvion logs in Grafana Explore.
- Python incident analyzer output.
- Personal GitHub repository and project documentation.

## 9. Conclusion
The project demonstrates an end-to-end learning workflow covering CI/CD, container security, infrastructure validation, Kubernetes deployment, monitoring, centralized logging and basic incident triage. It provides practical experience with commonly used DevOps and cloud-native tools while documenting the limitations of the lab environment.
