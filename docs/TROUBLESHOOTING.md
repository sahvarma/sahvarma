# AmeriLife Troubleshooting Guide

## Common Issues

### 1. ModuleNotFoundError: No module named 'pandas'

**Cause:** Dependencies not installed

**Solution:**
```bash
pip install -r requirements.txt
```

### 2. Failed to read CSV

**Cause:** CSV file path incorrect or file missing

**Solution:**
- Verify file exists: `ls data/stgContractDetails.csv`
- Check file permissions: `chmod 644 data/stgContractDetails.csv`
- Specify correct path: `python scripts/rest_api_bulk.py --csv-path /path/to/file.csv`

### 3. Authorization Failed

**Cause:** Invalid or expired bearer token

**Solution:**
- Verify token in `.env` file
- Check token expiration
- Obtain new token if expired

### 4. Connection Timeout

**Cause:** Network issue or API endpoint unavailable

**Solution:**
- Check network connectivity: `ping api.designer-na.cloud.varicent.com`
- Increase timeout: `python scripts/rest_api_bulk.py --timeout 120`
- Check API status

### 5. 413 Payload Too Large

**Cause:** Batch size exceeds server limit

**Solution:**
- Script automatically handles this
- If persists, reduce batch size: `python scripts/rest_api_bulk.py --batch-size 1000`

### 6. 400 Bad Request

**Cause:** Invalid data in CSV

**Solution:**
- Validate CSV format
- Check data types match schema
- Review CSV for special characters

### 7. Permission Denied

**Cause:** Insufficient file permissions

**Solution:**
```bash
chmod 755 scripts/
chmod 755 data/
```

## Debug Mode

Enable verbose logging:

```bash
logging_level=DEBUG python scripts/rest_api_bulk.py --verbose
```

## Getting Help

1. Check this guide first
2. Review error messages carefully
3. Check API logs
4. Create GitHub issue with:
   - Error message
   - Python version
   - OS information
   - Steps to reproduce
