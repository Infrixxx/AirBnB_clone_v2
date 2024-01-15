# fabfile.py
from invoke import task
import os.path
from datetime import datetime

@task
def hello(c):
    """Create a tar gzipped archive of the directory web_static."""
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if os.path.isdir("versions") is False:
        if c.local("mkdir -p versions").failed is True:
            return None
    if c.local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
