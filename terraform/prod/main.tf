data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"] #canonical

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }
}

module "ec2_instance" {
  source = "terraform-aws-modules/ec2-instance/aws"

  name                                = "cimov-spot-instance"
  create_spot_instance                = true
  spot_instance_interruption_behavior = "stop"
  spot_type                           = "persistent"

  ami                         = data.aws_ami.ubuntu.id
  associate_public_ip_address = true
  iam_role_name               = var.iam_role
  key_name                    = var.key_name
  instance_type               = var.instance_type
  subnet_id                   = var.subnet_id
  vpc_security_group_ids      = var.security_groups

  tags = {
    Terraform   = "true"
    Environment = "prod"
    Owner       = "engels.souza"
  }
}