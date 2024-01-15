from fabric.api import env, put, run, task

env.hosts = ["54.236.43.143", "54.160.124.186"]


@task
def do_deploy():
    """Distribute an archive to the web servers."""
    archive_path = env.archive_path
    if not archive_path:
        print("Error: Archive path not provided.")
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
        print("Deployment successful!")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
