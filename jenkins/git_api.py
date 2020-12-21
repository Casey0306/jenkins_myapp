import os
import git


class GitApi:

    def __init__(self, git_clone_url, workdir):
        self.git_clone_url = git_clone_url
        self.workdir = workdir

    def clone_from_git(self, folder):
        path = os.path.join(self.workdir, folder)
        git.Repo.clone_from(self.git_clone_url, path, branch='master')
