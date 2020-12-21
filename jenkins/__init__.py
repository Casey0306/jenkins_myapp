from flask import Flask
from jenkins.config import Config
from celery import Celery

app = Flask(__name__)
varenv = Config()
app_celery = Celery('tasks', broker=varenv.AMQP_BROKER_URL,
                    backend=varenv.AMQP_BACKEND_URL)

from jenkins import routes
