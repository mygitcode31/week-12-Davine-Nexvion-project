# Nexvion Infrastructure as Code

## Purpose
This Terraform configuration manages the existing AWS security group used by the Nexvion application and Jenkins deployment environment.

## Infrastructure
- AWS region: ap-south-1
- VPC: vpc-056dff5fe7e42d54d
- Security group: launch-wizard-10
- Security group ID: sg-0859a36e8e8563bd9

## Network rules

| Protocol | Port | Source/Destination |
|---|---:|---|
| TCP | 22 | 0.0.0.0/0 |
| TCP | 80 | 0.0.0.0/0 |
| TCP | 8080 | 0.0.0.0/0 |
| TCP | 8081 | 0.0.0.0/0 |
| All | All | 0.0.0.0/0 (egress) |

These rules reflect the existing lab environment. Public SSH and Jenkins access should be restricted before production use.

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

## Existing resource import
The existing security group was imported into Terraform state:

    terraform import aws_security_group.nexvion sg-0859a36e8e8563bd9

## State management and safety
Terraform state is stored locally and excluded from Git. Never commit state files because they may contain sensitive infrastructure information.

For production, use an encrypted remote state backend with locking.

Always review Terraform plans before applying changes. Do not apply unexpected infrastructure replacements or modifications.
