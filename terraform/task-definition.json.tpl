[
  {
    "name": "employee-app",
    "image": "${image}",
    "essential": true,

    "portMappings": [
      {
        "containerPort": 5000,
        "hostPort": 5000
      }
    ],

    "memory": 512,
    "cpu": 256
  }
]