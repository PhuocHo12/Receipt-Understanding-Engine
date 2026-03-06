import json
import redis


class RedisQueue:

    def __init__(self, host="localhost", port=6379, queue_name="receipt_tasks"):
        self.redis = redis.Redis(host=host, port=port, decode_responses=True)
        self.queue_name = queue_name

    def push(self, task: dict):
        self.redis.lpush(self.queue_name, json.dumps(task))

    def pop(self):

        task = self.redis.brpop(self.queue_name)

        if task:
            return json.loads(task[1])

        return None