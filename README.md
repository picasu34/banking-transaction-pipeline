# Banking Transaction Pipeline

Enterprise-grade serverless banking transaction processing platform built using AWS serverless services.

## Project Overview

This project processes banking transactions in real time using an event-driven architecture.

Features include:

- Transaction validation
- Fraud detection
- Asynchronous processing
- Workflow orchestration
- Email notifications
- Analytics reporting
- Data archival
- CI/CD automation

---

## Architecture

Client
  ↓
API Gateway
  ↓
Validation Lambda
  ↓
SQS FIFO Queue
  ↓
Processor Lambda
  ↓
DynamoDB

Additional Integrations:

SNS → Email Notifications

EventBridge → Audit Events

Step Functions → Workflow Orchestration

S3 → Transaction Archive

Glue → Metadata Catalog

Athena → Analytics Queries

CloudWatch → Monitoring

GitHub Actions → CI/CD

---

## AWS Services Used

| Service | Purpose |
|----------|----------|
| API Gateway | REST API |
| Lambda | Serverless compute |
| SQS FIFO | Reliable messaging |
| SNS | Notifications |
| DynamoDB | Transaction storage |
| Step Functions | Workflow orchestration |
| EventBridge | Audit events |
| S3 | Data archival |
| Glue | Data catalog |
| Athena | Analytics |
| CloudWatch | Monitoring |
| Secrets Manager | Secret storage |

---

## Sample Transaction

```json
{
  "transaction_id": "TXN100001",
  "customer_id": "C2001",
  "customer_name": "Kumar Nitin",
  "account_number": "123456789",
  "transaction_type": "DEBIT",
  "amount": "75000",
  "currency": "INR",
  "merchant": "Amazon",
  "channel": "UPI"
}