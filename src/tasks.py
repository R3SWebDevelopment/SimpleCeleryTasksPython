from celery import Celery
from urllib.request import Request, urlopen
import random
import os

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")


@celery.task(name="random_secret_word")
def random_secret_word(*args, **kwargs):
    url = "https://svnweb.freebsd.org/csrg/share/dict/words?revision=61569&view=co"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    web_byte = urlopen(req).read()

    webpage = web_byte.decode('utf-8')
    first500 = webpage[:500].split("\n")
    random.shuffle(first500)

    picked_word = first500[0]

    return picked_word
