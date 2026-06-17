# AmeriLife API Documentation

## Overview

This document provides detailed information about the Varicent API integration used by AmeriLife.

## Endpoint

```
POST https://api.designer-na.cloud.varicent.com/api/v1/customtables/stgContractDetailsAPI/inputforms/0/data/rows
```

## Authentication

- **Type**: Bearer Token
- **Header**: `Authorization: Bearer <token>`
- **Model**: AmeriLifeDev

## Request Format

### Single Record
```json
{
  "rows": [
    [
      "000001",
      "INB.AML123456",
      "CON-1234567",
      "12345678",
      "CARRIER1",
      "AFF100",
      "Contract_1",
      "2021-01-15",
      "2022-01-15",
      "ACTIVE",
      "2021-02-01",
      "RENEWAL",
      "2021-02-01",
      "TEST01",
      "Test contract",
      "1234567890-9876543210",
      "2026-06-17 14:00:00.000",
      "NPN1234567890",
      "PAYEE123456",
      "MKR12345",
      "PROF123456"
    ]
  ],
  "inputFormId": 1
}
```

### Batch Records
```json
{
  "rows": [
    [row1_data],
    [row2_data],
    [row3_data]
  ],
  "inputFormId": 1
}
```

## Response Codes

| Code | Description |
|------|-------------|
| 200 | Success |
| 400 | Bad Request |
| 401 | Unauthorized |
| 413 | Payload Too Large |
| 500 | Server Error |

## Error Handling

AmeriLife automatically handles the following:
- **413 Errors**: Batch size is split and retried
- **Network Errors**: Detailed logging and graceful termination
- **Timeout Errors**: Configurable with sensible defaults

## Rate Limiting

No explicit rate limiting documented. Monitor response times for optimal batch size.

## Best Practices

1. Use batch sizes between 500-2000 records
2. Implement proper error logging
3. Monitor API response times
4. Use dry-run mode for testing
5. Validate CSV data before submission
