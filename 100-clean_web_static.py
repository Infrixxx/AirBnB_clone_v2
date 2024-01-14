#!/usr/bin/python3
"""
Deletes out-of-date archives
fab -f 100-clean_web_static.py do_clean:number=2
    -i ~/.ssh/school -u ubuntu > /dev/null 2>&1
"""

import os
from fabric.api import *

env.hosts = ['54.236.43.143', '54.160.124.186']

def do_clean(number=0):
    """Delete out-of-date archives.
    Args:
        number (int): The number of archives to keep.
    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
    number = int(number)

    # Delete local archives
    local_archives = sorted(os.listdir("versions"))
    [local("rm ./versions/{}".format(a)) for a in local_archives[:-number]]

    # Delete remote archives on both web servers
    with cd("/data/web_static/releases"):
        remote_archives = run("ls -tr").split()
        remote_archives = [a for a in remote_archives if "web_static_" in a]
        [run("rm -rf ./{}".format(a)) for a in remote_archives[:-number]]

# Run the script with the given number of archives to keep
do_clean(2)
