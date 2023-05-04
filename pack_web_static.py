#!/usr/bin/env python3
archive_path = './versions/web_static_{}.tgz'.format(
    datetime.utcnow().strftime('%Y%m%d%H%M%S'))
if do_pack() is None:
    print("Failed to generate archive!")
else:
    if do_deploy(archive_path):
        print("New version deployed!")
    else:
        print("Deployment failed!")
