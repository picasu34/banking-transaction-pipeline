# Banking Transaction Pipeline

Enterprise serverless banking transaction processing system built on AWS.

## Architecture

API Gateway
    ↓
Validation Lambda
    ↓
SQS FIFO
    ↓
Processor Lambda
    ↓
DynamoDB

Additional Services:
- SNS
- EventBridge
- Step Functions
- CloudWatch
- S3
- Glue
- Athena
- Secrets Manager

## AWS Services Used

- API Gateway
- Lambda
- SQS
- SNS
- DynamoDB
- EventBridge
- Step Functions
- CloudWatch
- Secrets Manager
- S3
- Glue
- Athena

## Features

- Transaction Validation
- Fraud Detection
- Dead Letter Queue
- CloudWatch Monitoring
- Email Notifications
- Audit Events
- Data Archival
- Analytics

## Sample Transaction

{
  "transaction_id": "TXN100001",
  "customer_id": "C2001",
  "amount": "75000",
  "currency": "INR"
}

## Deployment

sam build
sam deploy --guided