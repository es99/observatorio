terraform {
  backend "s3" {
    bucket = "iac-webapps-infopublic"
    key    = "servidor2-ohio"
    region = "sa-east-1"
  }
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  required_version = "~> 1.5"
}

provider "aws" {
  region = "us-east-2"
}