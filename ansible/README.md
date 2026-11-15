# Nexvion Ansible Configuration Management

## Purpose
Automate basic configuration checks and deployment verification for the Nexvion EC2 host.

## Architecture
- Control node: Nexvion EC2 instance
- Managed host: Local EC2 instance using Ansible local connection
- Application: Nexvion static website
- Container runtime: Docker Engine
- Deployment: Docker Compose

## Files
- ansible.cfg: Ansible configuration.
- inventory.ini: Defines the local managed host.
- site.yml: Configuration and verification playbook.

## Tasks automated
1. Gather host facts.
2. Ensure Docker Engine, Docker CLI, containerd, and Docker Compose packages are installed.
3. Ensure Docker service is enabled and running.
4. Validate Docker Compose configuration.
5. Verify homepage returns HTTP 200.
6. Verify products page returns HTTP 200.
7. Verify payment page returns HTTP 200.

## Execute

Run from the ansible directory:

    ansible-playbook site.yml

Check syntax:

    ansible-playbook site.yml --syntax-check

## Validation result
The playbook executed successfully:
- Tasks OK: 8
- Changed: 0
- Failed: 0
- Unreachable: 0

The existing Nexvion container was not rebuilt or restarted.

## Scope and limitations
This implementation manages the local EC2 host. Remote multi-server configuration can be added through an extended inventory when additional managed hosts are available.
