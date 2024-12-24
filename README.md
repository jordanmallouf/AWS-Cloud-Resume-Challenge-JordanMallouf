# AWS Cloud Resume Challenge
Welcome to my Cloud Resume Challenge project! This repository brings together frontend, backend, and infrastructure to create a fully functional serverless application hosted on AWS. This challenge is more than just a resume—it's a demonstration of cloud computing and automation skills.

# What this Project Includes
## Frontend
The website is visually appealing and functional, hosted globally on AWS.

__Files__:
* _index.html_: The main webpage structure.
* _script.js_: The logic powering the visitor counter.
* _styles.css_: Custom styling for a cleaner look.

__Hosting__: Delivered via S3 and ClouFront for fast, secure access.

## Backend
Serverless backend logic to keep track of website visitors.

__Features__:
* Updates a DynamoDB table, VisitorCounter, to count user website visits.
* Accessible through an HTTP API Gateway endpoint.

__Key Components__:
* _VisitorCounterFunction.py_: The lambda function logic.
* _TestLambdaFunction.py_: Unit tests to ensure backend reliability.
* _lambda.zip_: Packaged for deployment.

## Infrastructure
Infrastructure as Code (IaC) ensures everything is reproducible and scalable.

__Tools Used__: AWS Serverless Application Model (SAM).

__File__:
* _template.yml_: Defines all AWS resources in one place.

## CI/CD Pipelines
Automated deployments make sure the latest changes are live without maual effort.

__Frontend__: Syncs files to S3 and invalidates CloudFront cache, ensuring that the latest content is served.

__Backend__: Deploys Lambda function and updates infrastructure with AWS SAM.

# How It's Organized



│   ├── lambda.zip

├── infrastructure/

│   ├── template.yml
