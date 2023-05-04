#!/usr/bin/env python3
"""Fabric script that distributes an archive to your web servers."""

import os
from fabric.api import env, put, run
from datetime import datetime

env.hosts = ['54.165.197.124', '54.234.35.46']
env.user = 'makterince'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Distributes an archive to your web servers."""
    if not os.path.exists(archive_path):
        return False

    # Upload the archive to the /tmp/ directory of the web server
    archive_name = os.path.basename(archive_path)
    put(archive_path, "/tmp/{}".format(archive_name))

    # Uncompress the archive to the folder
    # /data/web_static/releases/<archive filename without extension>
    release_dir = "/data/web_static/releases/{}".format(
                  archive_name.split('.')[0])
    run("sudo mkdir -p {}".format(release_dir))
    run("sudo tar -xzf /tmp/{} -C {} --strip-components=1".format(
        archive_name, release_dir))
    # Delete the archive from the web server
    run("sudo rm /tmp/{}".format(archive_name))

    # Delete the symbolic link /data/web_static/current from the web server
    run("sudo rm -rf /data/web_static/current")

    # Create a new symbolic link /data/web_static/current on the web server
    # linked to the new version of your code
    run("sudo ln -s {} /data/web_static/current".format(release_dir))

    return True
