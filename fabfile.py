# fabfile.py
from fabric import task

@task
def hello(c):
    print("Hello, Fabric!")
