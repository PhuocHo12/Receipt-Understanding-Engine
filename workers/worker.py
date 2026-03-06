from src.messaging.redis_queue import RedisQueue
from src.engine.pipeline import ReceiptEngine


def run_worker():

    queue = RedisQueue()
    engine = ReceiptEngine()

    print("Worker started...")

    while True:

        task = queue.pop()

        if not task:
            continue

        image_path = task["image_path"]

        result = engine.process(image_path)

        print("Processed receipt:")
        print(result)


if __name__ == "__main__":
    run_worker()