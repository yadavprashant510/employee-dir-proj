resource "aws_ecs_cluster" "main" {
  name = "employee-cluster"
}

data "aws_ecr_repository" "app" {
  name = "employee-app"
}

resource "aws_ecs_task_definition" "app" {

  family                   = "employee-app"
  network_mode             = "bridge"

  requires_compatibilities = ["EC2"]

  container_definitions = templatefile(
    "${path.module}/task-definition.json.tpl",
    {
      image = "${data.aws_ecr_repository.app.repository_url}:latest"
    }
  )
}

resource "aws_ecs_service" "app" {

  name            = "employee-service"

  cluster         = aws_ecs_cluster.main.id

  task_definition = aws_ecs_task_definition.app.arn

  desired_count   = 2
}