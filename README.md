# docker-s3-volume-backup [WIP]

## Purpose

This project allows backup on docker volumes to Amazon S3.

## Usage

```
docker run -e AWS_ACCESS_KEY_ID="key" \
  -e AWS_SECRET_ACCESS_KEY="secret" \
  -e S3_BUCKET_NAME="bucket" \
  -v "/var/run/docker.sock:/var/run/docker.sock" \
  -v "/:/data"
```
