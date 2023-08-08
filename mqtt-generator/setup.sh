#!/bin/bash

export mqtt_endpoint=$(aws iot describe-endpoint --endpoint-type iot:Data-ATS| jq -r ".endpointAddress")
export mqtt_client_id="sensor-01"
export mqtt_topic="my-topic/thing"