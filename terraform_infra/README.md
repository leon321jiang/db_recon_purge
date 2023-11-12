# Terraform Infrastructure for [Your Project Name]

This Terraform project sets up the necessary infrastructure on AWS. It defines resources for [brief description of resources, e.g., "computing instances, databases, networking components"].

## Prerequisites

Before running this Terraform project, you should have the following:

- Terraform v[specific version, e.g., 0.12+]
- AWS CLI configured with Administrator access
- [Any other prerequisites]

## Configuration

The `test_infra.tf` file contains the Terraform configurations. You should review and update the configurations to match your AWS environment and infrastructure requirements.

## Resources

This Terraform configuration will create the following resources for testing purposes:

- 1 RDS instance - mySQL (Postgres and Oracle code are NOT working for now)  
- 2 DynamoDB tables
    - onboarded_db_list: store a list of db and  
    - records_deleted: a copy of all db deleted from the onboarded_db_list 

## Usage

To use this Terraform project, run the following commands:

1. Initialize the Terraform environment:

    ```
    terraform init
    ```

2. Validate the Terraform files:

    ```
    terraform validate
    ```

3. Plan the Terraform deployment:

    ```
    terraform plan
    ```

4. Apply the Terraform configuration to create the infrastructure:

    ```
    terraform apply
    ```

5. To destroy the infrastructure managed by Terraform:

    ```
    terraform destroy
    ```

## Variables

You should define the following variables in your `terraform.tfvars` file:

- `aws_region`: The AWS region to deploy resources
- [Other variables required by `test_infra.tf`]

## Outputs

The following outputs will be provided by the Terraform configuration:

....

## Notes




