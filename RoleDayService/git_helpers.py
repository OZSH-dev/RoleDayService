import subprocess


def get_git_revision_num():
    return subprocess.check_output(['git', 'rev-list', 'HEAD', '--count'])


def get_git_revision_short_hash():
    return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'])