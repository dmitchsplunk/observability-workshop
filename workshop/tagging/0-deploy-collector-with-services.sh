#!/bin/bash

IMPL=${1:-py}

if [ ! -f /home/splunk/.helmok ]; then
  cd /home/splunk/workshop/tagging/ || exit
  ./1-deploy-otel-collector.sh
  ./2-deploy-creditcheckservice.sh "${IMPL}"
  ./3-deploy-creditprocessorservice.sh
  ./4-deploy-load-generator.sh

  echo "$INSTANCE" > /home/splunk/.helmok
fi
