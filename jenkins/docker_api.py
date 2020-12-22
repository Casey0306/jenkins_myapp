import os
import docker


class DockerApi:

    def __init__(self, docker_url, workdir):
        self.docker_url = docker_url
        self.workdir = workdir

    def connect(self):
        client = docker.DockerClient(base_url=self.docker_url)
        return client

    def image_build(self, session, image_tag, folder):
        path = os.path.join(self.workdir, folder)
        image, log = session.images.build(path=path, tag=image_tag)
        for line in log:
            print(line)

    def check_image_tag_use(self, session, tagname):
        list_image_tag = []
        list_images = session.images.list()
        if list_images:
            for image in list_images:
                if image.tags:
                    for image_tag in image.tags:
                        list_image_tag.append(image_tag)
            if list_image_tag:
                if tagname in list_image_tag:
                    return None
        return not None

    def check_image_created(self, session, image_created):
        list_image_tag = []
        list_image_short_id = []
        for image in session.images.list():
            list_image_tag.append(image.tags[0])
            list_image_short_id.append(image.short_id)
        if image_created.tags[0] in list_image_tag and image_created.short_id in list_image_short_id:
            return not None
        return None
