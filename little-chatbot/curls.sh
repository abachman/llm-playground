#!/bin/sh

curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"prompt": "What is a good style of shoe for prom?"}' \
  127.0.0.1:5000/chat