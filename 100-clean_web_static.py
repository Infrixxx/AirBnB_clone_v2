#!/usr/bin/python3
"""
Deletes out-of-date archives on local and remote servers.

Usage:
  fab -f 100-clean_web_static.py do_clean:number=2 -i <ssh-key> -u <username>

Example:
  fab -f 100-clean_web_static.py do_clean:number=2 -i ~/.ssh/school -u ubuntu
"""

import os
from fabric.api import *
import logging

# Set logging level for debugging
logging.basicConfig(level=logging.DEBUG)

env.hosts = ['54.236.43.143', '54.160.124.186']  # Replace with your server IPs

@task
def do_clean(number=0):
    """Deletes out-of-date archives, keeping the specified number of most recent versions.

    Args:
        number (int): The number of archives to keep (default: 0, keeps only the most recent).
    """

    logging.info("Starting archive cleanup...")

    number = 1 if int(number) == 0 else int(number)  # Ensure at least one archive is kept

    # Clean local archives
    with lcd("versions"):
        archives = sorted(os.listdir("."))
        for _ in range(number):
            archives.pop()  # Remove the most recent archives
        for archive in archives:
            local("rm ./{}".format(archive))
            logging.info("Deleted local archive: {}".format(archive))

    # Clean remote archives
    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]  # Filter relevant archives
        for _ in range(number):
            archives.pop()
        for archive in archives:
            run("rm -rf ./{}".format(archive))
            logging.info("Deleted remote archive: {}".format(archive))

    logging.info("Archive cleanup completed.")
