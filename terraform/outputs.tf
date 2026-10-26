output "app_url" {
  description = "Open this in your browser once the service is running"
  value       = "http://${aws_lb.app.dns_name}"
}

output "github_actions_role_arn" {
  description = "Save this as the AWS_ROLE_ARN variable in your GitHub repo"
  value       = aws_iam_role.github_deploy.arn
}

output "ecr_repository_url" {
  description = "Where the Docker image is stored"
  value       = aws_ecr_repository.app.repository_url
}

output "ecs_cluster_name" {
  description = "Name of the ECS cluster"
  value       = aws_ecs_cluster.main.name
}

output "ecs_service_name" {
  description = "Name of the ECS service"
  value       = aws_ecs_service.app.name
}
