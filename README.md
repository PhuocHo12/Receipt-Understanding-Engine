# Receipt Understanding Engine

A lightweight AI engine for extracting structured information from receipt images using a modular processing pipeline.

This project demonstrates how receipt images captured from edge devices can be processed through an AI pipeline to produce structured JSON outputs. The system is designed to run as a standalone service or be integrated as a component in larger AI systems.

---

## Overview

Many real-world applications require automated understanding of receipts or bills for tasks such as:

* expense management
* accounting automation
* financial record keeping
* retail analytics

`receipt-understanding-engine` provides a simple reference implementation of how such a system can be built using modern AI techniques and asynchronous processing pipelines.

The engine simulates a typical document AI workflow:

Receipt Image → Text Extraction → Data Parsing → Structured Output

---

## Features

* Receipt image processing pipeline
* Modular extraction and parsing architecture
* Asynchronous processing with Redis
* MQTT communication for device integration
* Structured JSON receipt output
* Easily extendable AI components

---

## System Pipeline

The engine processes receipts through the following stages:

1. **Device Upload**

A device captures a receipt image and sends it through MQTT.

2. **Task Queue**

The receipt processing task is pushed into a Redis queue.

3. **AI Worker**

A worker retrieves the task and runs the receipt understanding pipeline.

4. **Data Extraction**

The engine extracts relevant information from the receipt.

5. **Structured Output**

The result is returned as structured JSON.

```
Device
  │
  │ MQTT
  ▼
Gateway
  │
  ▼
Redis Queue
  │
  ▼
Receipt Worker
  │
  ▼
Receipt Engine Pipeline
  │
  ▼
Structured JSON Output
```

---

## Project Structure

```
receipt-understanding-engine
│
├── src
│   ├── engine
│   │   ├── pipeline.py
│   │   ├── extractor.py
│   │   └── parser.py
│   │
│   ├── messaging
│   │   ├── mqtt_client.py
│   │   └── redis_queue.py
│   │
│   ├── schemas
│   │   └── receipt_schema.py
│   │
│   └── utils
│
├── workers
│   └── worker.py
│
├── device_simulator
│   └── send_receipt.py
│
├── examples
│   └── receipts
│
└── scripts
```

---

## Example Output

Example structured receipt:

```json
{
  "store": "Circle K",
  "date": "2025-03-01",
  "items": [
    { "name": "Coffee", "price": 2.5 },
    { "name": "Bread", "price": 1.2 }
  ],
  "total": 3.7
}
```

---

## Quick Start

### Install dependencies

```
pip install -r requirements.txt
```

### Start Redis

```
docker run -p 6379:6379 redis
```

### Run worker

```
python scripts/run_worker.py
```

### Send test receipt

```
python device_simulator/send_receipt.py
```

---

## Extending the Engine

The engine is designed to be modular. You can easily extend it with:

* OCR models
* Vision-Language Models (VLM)
* LLM-based parsing
* database storage
* REST APIs

The core pipeline can be replaced or upgraded without affecting the surrounding system.

---

## Use Cases

* expense tracking systems
* receipt digitization platforms
* accounting automation tools
* retail data extraction
* document AI research

---

## License

MIT License
