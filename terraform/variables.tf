variable "aws_region" {
  description = "AWS deployment region"
  type        = string
  default     = "ap-south-1"
}

variable "vpc_id" {
  description = "Existing AWS VPC ID"
  type        = string
  default     = "vpc-056dff5fe7e42d54d"
}

variable "security_group_name" {
  description = "Name of the existing Nexvion security group"
  type        = string
  default     = "launch-wizard-10"
}

variable "security_group_description" {
  description = "Description of the existing security group"
  type        = string
  default     = "launch-wizard-10 created 2026-11-15T12:56:53.339Z"
}
