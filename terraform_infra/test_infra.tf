provider "aws" {
  region = "us-west-2"
}

resource "aws_dynamodb_table" "records_deleted" {
  name         = "records_deleted"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "db_name"

  attribute {
    name = "db_name"
    type = "S"
  }
}

resource "aws_dynamodb_table" "onboarded_db_list" {
  name           = "onboarded_db_list"
  billing_mode   = "PROVISIONED"
  read_capacity  = 5
  write_capacity = 5
  hash_key       = "db_name"

  attribute {
    name = "db_name"
    type = "S"
  }

  tags = {
    Name = "onboarded_db_list"
  }
}

# mySQL instance
resource "aws_db_instance" "my_db_instance" {
  allocated_storage       = 20
  storage_type            = "gp2"
  engine                  = "MySQL"
  engine_version          = "8.0.35"
  instance_class          = "db.t2.micro"
  db_name                 = "testrdsmysql"
  username                = var.db_username
  password                = var.db_password
  parameter_group_name    = "default.mysql8.0"
  skip_final_snapshot     = true
  publicly_accessible     = true
  backup_retention_period = 0
  identifier              = var.db_instance_identifier
}

/*
TODO: the following two don't work right now, need to be fixed
# PostgreSQL RDS instance 
resource "aws_db_instance" "postgres_instance" {
  allocated_storage    = 20
  engine               = "aurora-postgresql"
  instance_class       = "db.t3.medium" # This is the smallest instance type for RDS
  db_name                 = "testrdspostgres"
  username             = var.db_username
  password             = var.db_password
  parameter_group_name = "default.postgres13"
  skip_final_snapshot  = true
}

# Oracle RDS instance
resource "aws_db_instance" "oracle_instance" {
  allocated_storage    = 20
  storage_type         = "gp2"
  engine               = "oracle-se1" # Specify the desired Oracle edition
  engine_version       = "19.0.0.0.ru-2020-04.rur-2020-04.r1" # Specify the desired engine version
  instance_class       = "db.t3.micro" # This is the smallest instance type for RDS
  db_name              = "testrdsoracle"
  username             = var.db_username
  password             = var.db_password
  parameter_group_name = "default.oracle-ee-19"
  skip_final_snapshot  = true
}
*/