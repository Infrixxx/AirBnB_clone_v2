<<<<<<< HEAD
#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.
import os.path
from fabric.api import env, put, run

env.hosts = ["54.236.43.143", "54.160.124.186"]


def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if not os.path.isfile(archive_path):
        return False

    file = os.path.basename(archive_path)
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed:
        return False

    if run("rm -rf /data/web_static/releases/{}".format(name)).failed:
        return False

    if run("mkdir -p /data/web_static/releases/{}".format(name)).failed:
        return False

    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(file, name)).failed:
        return False

    if run("rm /tmp/{}".format(file)).failed:
        return False

    if run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(name, name)).failed:
        return False

    if run("rm -rf /data/web_static/releases/{}/web_static".format(name)).failed:
        return False

    if run("rm -rf /data/web_static/current").failed:
        return False

    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(name)).failed:
        return False

    return True
=======
#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.
import os.path
from fabric.api import *

env.hosts = ["54.236.43.143", "54.160.124.186"]


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False
>>>>>>> 2815c180d8bdec225fe1c368a02e28663a24f66b
