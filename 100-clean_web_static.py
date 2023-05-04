#!/usr/bin/python3
"""
    Fabric script that deletes out-of-date archives
"""

from fabric.api import *

env.hosts = ['54.165.197.124', '54.234.35.46']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'

def do_clean(number=0):
    """
    Deletes unnecessary archives in the versions folder and releases folder
    """
    number = int(number)
    if number < 1:
        number = 1
        
    with cd('/data/web_static/releases'):
        # Sort releases by creation time and get list of all releases
        releases = sorted(run('ls -tr').split())
        
        # Get list of releases to delete
        to_delete = releases[:-number]
        
        # Delete old releases
        for release in to_delete:
            if release != 'test':
                run('rm -rf {}'.format(release))
        
    with cd('/data/web_static/releases'):
        # Sort releases by creation time and get list of all releases
        releases = sorted(run('ls -tr ../versions').split())

        # Get list of releases to delete
        to_delete = releases[:-number]
        
        # Delete old releases
        for release in to_delete:
            run('rm -rf ../versions/{}'.format(release))
            
if __name__ == "__main__":
    do_clean()
