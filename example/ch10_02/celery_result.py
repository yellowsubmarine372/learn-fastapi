from celery.result import AsyncResult
from common.messaging import celery

if __name__ == "__main__":
    async_result = AsyncResult("fca90a97-851f-40a7-9a49-c88905d731c4", app=celery)
    result = async_result.result

    print(result)