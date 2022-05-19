#!/bin/bash
datasette publish cloudrun price.db \
  --service burma-price \
  --metadata metadata.yml \
  --extra-options="--setting sql_time_limit_ms 3000"