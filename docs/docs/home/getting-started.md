# Getting Started

## Install and Configure AWS CDK

Lambda Forge is built on top of AWS Cloud Development Kit (CDK) and it's essential for defining cloud infrastructure in code and provisioning it through AWS CloudFormation. Execute the following commands to install the AWS CDK globally and set up your AWS credentials:

```
npm install -g aws-cdk
aws configure
cdk bootstrap
```

During the configuration, you will be prompted to enter your AWS Access Key ID, Secret Access Key, default region name, and output format.

## Create a GitHub Personal Access Token

Lambda Forge uses CodePipeline to interact with your GitHub repository. To enable this, generate a GitHub personal access token by following these steps:

1. Navigate to "Developer Settings" in your GitHub account.
2. Select "Personal access tokens," then "Tokens (classic)."
3. Click "Generate new token," ensuring the "repo" scope is selected for full control of private repositories.
4. Complete the token generation process.

You can find more informations about creating a GitHub Token [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

Your token will follow this format: `ghp_********************************`

### Store the Token on AWS Secrets Manager

Save this token in AWS Secrets Manager as `plain text` using the exact name **github-token**. This specific naming is vital as it corresponds to the default identifier that the CDK looks for within your AWS account.

## Create a new S3 Bucket

Create a new S3 bucket dedicated to storing documentation artifacts that are going to be automatically generated by the pipeline.

## Create a New Directory

```
mkdir lambda_forge_demo
cd lambda_forge_demo
```

## Create a New Virtual Environment

```
python3 -m venv venv
source venv/bin/activate
```

## Install lambda-forge

```
pip install lambda-forge
```

### Forge CLI

The Forge Command Line Interface (CLI) is a powerful, versatile tool designed to streamline the development, deployment, and management of applications. It enables developers to automate repetitive tasks, manage project configurations, and interact directly with the services and infrastructure without leaving the terminal. This CLI tool simplifies complex processes through straightforward commands, significantly reducing development time and effort.

### Verify Installation

Having successfully installed Lambda Forge, you are now ready to explore the capabilities of the Forge CLI. Begin by entering the following command to access the comprehensive list of available options and commands:

```
forge --help
```

Here's a concise list of the commands supported by Forge:

```
Commands:
  authorizer  Generates an authorizer for AWS Lambda functions.
  deploy      Deploys a stack to AWS
  diagram     Create a diagram of the project in png format
  doc         Creates a new doc template for the project.
  function    Creates a Lambda function with a predefined structure and...
  layer       Creates and installs a new Lambda layer.
  live        Starts a live development environment for the specified...
  output      List the outputs of the stacks on AWS CloudFormation
  project     Initializes a new AWS Lambda project with a specified...
  service     Scaffolds the structure for a specified AWS service...
  test        Run the tests or coverage of the project
```

For a comprehensive list of configurations that each Forge command supports, you can refer to the command line help by running:

`forge $COMMAND --help`.

Later in this tutorial, we'll delve into the specifics of each command. But for now, let's kickstart by establishing the foundation of our project.

## Create a New Project

Start a new project named `lambda-forge-demo`.

```
forge project --name lambda-forge-demo --repo-owner "$GITHUB-OWNER" --repo-name "$GITHUB-REPO" --bucket "$S3-BUCKET" --account "$AWS-ACCOUNT"
```

Make sure to replace `$GITHUB-OWNER` and `$GITHUB-REPO` with the actual GitHub owner and the name of an empty repository and the `$S3-BUCKET` with the name of a S3 bucket and the `$AWS-ACCOUNT` with your AWS Account ID.

Alternatively, you can also run `forge project` to create the project in interactive mode.

### Project Structure

Upon creatig your project, some directories and files are automatically generated for you. This initial structure is designed to streamline the setup process and provide a solid foundation for further development.

In the upcoming sections of this tutorial, we'll explore each of these components in detail. For now, familiarize yourself with the foundational structure that should resemble the following:

```
.
├── docs
│   ├── __init__.py
│   └── config.py
│
├── infra
│   ├── __init__.py
│   ├── services
│   │   ├── __init__.py
│   │   ├── aws_lambda.py
│   │   └── api_gateway.py
│   ├── stacks
│   │   ├── __init__.py
│   │   ├── dev_stack.py
│   │   ├── lambda_stack.py
│   │   ├── prod_stack.py
│   │   └── staging_stack.py
│   └── stages
│       ├── __init__.py
│       └── deploy.py
│
├── .coveragerc
├── .gitignore
├── app.py
├── cdk.json
├── pytest.ini
├── README.md
└── requirements.txt
```

The `cdk.json` file, located at the root of your directory, serves as the central configuration hub for Lambda Forge projects. When you run the `forge project` command, Forge automatically applies the informed settings into the cdk.json file.

```json title="cdk.json" linenums="41"
    "region": "$AWS-REGION",
    "account": "$AWS-ACCOUNT",
    "name": "Lambda-Forge-Demo",
    "repo": {
      "owner": "$GITHUB-OWNER",
      "name": "$GITHUB-REPO"
    },
    "bucket": "$S3-BUCKET",
```