import os
import shutil
from jenkins import varenv
from jenkins.docker_api import DockerApi
from jenkins.git_api import GitApi
from jenkins import app_celery


@app_celery.task
def build_image_docker(imagetag):
    try:
        apigit = GitApi(git_clone_url=varenv.URL_GIT_CLONE,
                        workdir=varenv.WORKDIR_APP)
        apidocker = DockerApi(docker_url=varenv.DOCKER_SOCKET_TCP_CONNECT,
                              workdir=varenv.WORKDIR_APP)
        session = apidocker.connect()
        if apidocker.check_image_tag_use(session=session,
                                         tag_name=imagetag):
            folder_name = 'openstack' + imagetag
            apigit.clone_from_git(folder=folder_name)
            apidocker.image_build(session=session,
                                  image_tag=imagetag, folder=folder_name)
            path = os.path.join(varenv.WORKDIR_APP, folder_name)
            shutil.rmtree(path, ignore_errors=False)
        else:
            print('Image_tag is already used')
    except Exception as e:
        print(e)
