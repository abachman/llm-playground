#!/bin/sh

curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Please introduce yourself as FashionBot and ask a question that invites discussion about contemporary fashion or art."}' \
  127.0.0.1:5000/chat
