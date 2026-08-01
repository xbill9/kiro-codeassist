#!/bin/bash
# Exports active AWS credentials to .aws_creds for use by Makefile and other tools.

set -euo pipefail

CREDS=$(aws configure export-credentials 2>/dev/null) || {
    echo "Error: Failed to export AWS credentials. Run 'aws sso login' or 'aws configure'." >&2
    exit 1
}

{
    echo "AWS_ACCESS_KEY_ID=$(echo "$CREDS" | jq -r .AccessKeyId)"
    echo "AWS_SECRET_ACCESS_KEY=$(echo "$CREDS" | jq -r .SecretAccessKey)"
    TOKEN=$(echo "$CREDS" | jq -r '.SessionToken // empty')
    [[ -n "$TOKEN" ]] && echo "AWS_SESSION_TOKEN=$TOKEN"
} > .aws_creds

echo "Saved credentials to .aws_creds"
