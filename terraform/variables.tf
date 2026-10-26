variable "aws_region" {
  description = "AWS region to deploy into"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Name used for the repo, cluster and other resources"
  type        = string
  default     = "ecs-fargate-app"
}

variable "github_repo" {
  description = "GitHub repo allowed to deploy, in the form owner/name"
  type        = string
  default     = "minenhledlamini116/aws-ecs-fargate-app"
}

variable "vpc_cidr" {
  description = "IP range for the VPC"
  type        = string
  default     = "10.1.0.0/16"
}

variable "public_subnet_cidrs" {
  description = "IP ranges for the two public subnets"
  type        = list(string)
  default     = ["10.1.1.0/24", "10.1.2.0/24"]
}

variable "container_port" {
  description = "Port the app listens on inside the container"
  type        = number
  default     = 8080
}

variable "desired_count" {
  description = "How many copies of the container to run"
  type        = number
  default     = 2
}
