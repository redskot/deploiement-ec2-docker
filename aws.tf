terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.89.0"
    }
  }
}

provider "aws" {
  region = "us-east-1" # Déplace la région ici
}

data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"] # Canonical
}

# 🔑 Génération de la clé SSH
resource "tls_private_key" "ssh_key" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "local_file" "private_key_pem" {
  content  = tls_private_key.ssh_key.private_key_pem
  filename = "${path.module}/my_terraform_key"
  file_permission = "0400" # 🔥 Ajoute les bonnes permissions
}

resource "aws_key_pair" "generated_key" {
  key_name   = "my_terraform_key"
  public_key = tls_private_key.ssh_key.public_key_openssh
}

# 🚀 Création de l'instance avec la clé générée
resource "aws_instance" "web" {
  ami             = data.aws_ami.ubuntu.id
  instance_type   = "t3.micro"
  key_name        = aws_key_pair.generated_key.key_name
  security_groups = [data.aws_security_group.default_sg.name]

  tags = {
    Name = "HelloWorld"
  }
}


# 🔍 Récupération du SG existant
data "aws_security_group" "default_sg" {
  filter {
    name   = "group-name"
    values = ["default_sg"]
  }
}


/* ### 🔐 Sécurité : Autoriser SSH
resource "aws_security_group" "default_sg" {
  name        = "default_sg"
  description = "Autoriser SSH, HTTP et Flask (5000)"

  # 🚀 SSH (Port 22)
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # Accès total (tu peux restreindre)
  }

  # 🌍 HTTP (Port 80)
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # 🚀 Flask ou toute app sur port 5000
  ingress {
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # 🔄 Tout trafic sortant est autorisé
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
 */

output "instance_public_ip" {
  description = "Adresse IP publique de l'instance"
  value       = aws_instance.web.public_ip
}

output "private_key_path" {
  description = "Chemin du fichier de clé privée"
  value       = local_file.private_key_pem.filename
}

