#!/bin/bash
datasette publish cloudrun price.db \
  --service burma-price \
  --metadata metadata.yml \
  --static static:static/ \
  --template-dir=templates/ \
  --extra-options="--setting sql_time_limit_ms 3000"