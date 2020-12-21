import os


class Config:
    URL_GIT_CLONE = os.getenv('URL_GIT_CLONE')
    DOCKER_SOCKET_TCP_CONNECT = os.getenv('DOCKER_SOCKET_TCP_CONNECT')
    WORKDIR_APP = os.getenv('WORKDIR_APP')
    AMQP_BROKER_URL = os.getenv('AMQP_BROKER_URL')
    AMQP_BACKEND_URL = os.getenv('AMQP_BACKEND_URL')
