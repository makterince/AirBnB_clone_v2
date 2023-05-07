#!/usr/bin/python3
""" This script generates a .tgz archive from web_satic folder """
from fabric.api import local, env
from datetime import datetime

env.hosts = ['54.165.197.124']
env.user = 'ubuntu'
env.key_filename = '/ssh/id_rsa.pub'


def do_pack():
    """Create a tgz archive from the contents of web_static folder"""
    try:
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(current_time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except (subprocess.CalledProcessError, OSError, Exception) as e:
        return None
