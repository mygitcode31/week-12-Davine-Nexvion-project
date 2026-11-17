# Nexvion Infrastructure as Code

## Purpose
This Terraform configuration manages the existing AWS security group used by the Nexvion application and Jenkins deployment environment.

## Infrastructure
- AWS region: ap-south-1
- VPC: vpc-056dff5fe7e42d54d
- Security group: launch-wizard-10
- Security group ID: sg-0859a36e8e8563bd9
- Authentication: EC2 instance IAM role

## Current network rules

| Protocol | Port | Source/Destination |
|---|---:|---|
| TCP | 22 (SSH) | 0.0.0.0/0 |
| TCP | 80 (HTTP website) | 0.0.0.0/0 |
| TCP | 8080 (Jenkins) | 0.0.0.0/0 |
| TCP | 8081 (Docker Compose website) | 0.0.0.0/0 |
| All protocols | All ports (egress) | 0.0.0.0/0 |

These rules reflect the existing learning/lab environment and were verified against the live AWS security group.

## Security scan findings

Trivy filesystem scan on 2026-11-17 reported:

| Check | Result |
|---|---|
| Dockerfile HIGH/CRITICAL misconfigurations | 0 |
| Kubernetes manifest HIGH/CRITICAL misconfigurations | 0 |
| Helm templates HIGH/CRITICAL misconfigurations | 0 |
| Terraform misconfigurations | 2 |

Remaining Terraform findings:

- AWS-0104 (CRITICAL): unrestricted outbound traffic.
- AWS-0107 (HIGH): unrestricted inbound traffic.

The inbound finding is associated with public access rules, particularly SSH on port 22. Jenkins on port 8080 is also publicly reachable and should not be exposed without appropriate access controls.

The Trivy scan was filtered to HIGH and CRITICAL severity. A result of `-` in other scanner columns means that category was not scanned for that target; it does not mean the target passed that scan.

## Production security recommendations

Before production deployment:

1. Restrict SSH (port 22) to a trusted administrator IP/CIDR or use AWS Systems Manager Session Manager.
2. Restrict Jenkins (port 8080) to a VPN, trusted network, or private access path. Use authentication and TLS.
3. Keep port 80 public only if the website is intended to be publicly accessible; preferably serve it through HTTPS on port 443.
4. Restrict port 8081 to trusted users or remove the public rule if direct Compose access is not required.
5. Replace unrestricted egress with only the outbound destinations and ports required by the workload. Plan this carefully for package repositories, container registries, monitoring, and AWS services.
6. Review IPv4 and IPv6 rules, security group references, and network paths before deployment.

No live AWS security group rules were changed as part of this security review. The existing EC2 access path was intentionally preserved.

## Authentication
Terraform uses the EC2 instance IAM role. AWS access keys are not stored in this repository.

## Files
- main.tf: AWS provider and security group resource.
- variables.tf: Configurable infrastructure values.
- .terraform.lock.hcl: Provider dependency lock file.
- .gitignore: Excludes Terraform state and provider files.

## Setup and validation

Run from the terraform directory:

    terraform init
    terraform fmt
    terraform validate
    terraform plan

Review every plan carefully. Do not apply unexpected infrastructure replacements or modifications.

## Existing resource import

The existing security group was imported into Terraform state:

    terraform import aws_security_group.nexvion sg-0859a36e8e8563bd9

## State management and safety

Terraform state is stored locally and excluded from Git. Never commit state files because they may contain sensitive infrastructure information.

For production, use an encrypted remote state backend with locking.

Always review Terraform plans before applying changes. Confirm that SSH access and an alternative recovery method are available before changing security group rules.
