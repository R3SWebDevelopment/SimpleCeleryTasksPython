from flask import Flask, request
from celery.result import AsyncResult
from tasks import random_secret_word

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    args = request.args
    task_id = args.get('task_id', default=None)
    if task_id is None:
        task = random_secret_word.delay()
        html_response = f"<html><body><a href='/?task_id={task.id}'>Fetch Result</a></body></html>"
    else:
        res = AsyncResult(task_id)
        html_response = f"<html><body><p>Your Random Word is</p><p>{res.get()}</p></body></html>"
    return html_response
