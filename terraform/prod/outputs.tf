output "ami" {
  value = module.ec2_instance.ami
}

output "instance_id" {
  value = module.ec2_instance.id
}

output "az" {
  value = module.ec2_instance.availability_zone
}

output "public_dns" {
  value = module.ec2_instance.public_dns
}

output "public_ip" {
  value = module.ec2_instance.public_ip
}

output "private_ip" {
  value = module.ec2_instance.private_ip
}