# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0.

import time
import json
import os
import random


from awscrt import mqtt
from awsiot import mqtt_connection_builder

import numpy as np

def generate_sine():
    """Generates sine wave in 1 dimensional array"""

    cycles = 50
    resolution = 5000

    length = np.pi * 2 * cycles

    return np.sin(np.arange(0, length, length/resolution))


if __name__ == '__main__':

    # Create a MQTT connection from the command line data
    mqtt_connection = mqtt_connection_builder.mtls_from_path(
        endpoint=os.environ["mqtt_endpoint"],
        port=8883,
        cert_filepath="device_cert.pem",
        pri_key_filepath="device_cert.key",
        client_id=os.environ["mqtt_client_id"],
        clean_session=False,
        keep_alive_secs=30,)

    connect_future = mqtt_connection.connect()
    connect_future.result()
    print("Connected!")

    message_count = 1000
    message_topic = os.environ["mqtt_topic"]


    if message_count == 0:
        print("Sending messages until program killed")
    else:
        print(f"Sending {message_count} message(s)")


    messages = generate_sine()

    count = 0
    while count <= len(messages):
        message = {
            "sender": os.environ["mqtt_client_id"],
            "value": messages[count]
        }
        
        message_json = json.dumps(message)
        print(f"Publishing message to topic '{message_topic}': {message}")
        mqtt_connection.publish(
            topic=message_topic,
            payload=message_json,
            qos=mqtt.QoS.AT_LEAST_ONCE)
        time.sleep(1)
        count+= 1

    # Disconnect
    print("Disconnecting...")
    disconnect_future = mqtt_connection.disconnect()
    disconnect_future.result()
    print("Disconnected!")
