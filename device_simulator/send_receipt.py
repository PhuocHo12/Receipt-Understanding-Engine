import json
import paho.mqtt.publish as publish


def send_receipt():

    payload = {
        "image_path": "examples/receipts/sample.jpg"
    }

    publish.single(
        "receipt/upload",
        json.dumps(payload),
        hostname="localhost",
        port=1883
    )

    print("Receipt sent")


if __name__ == "__main__":
    send_receipt()