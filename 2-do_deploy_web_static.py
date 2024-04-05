#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.
from fabric.api import env, put, run
from os.path import exists
from os import makedirs
env.hosts = ['52.86.107.84', '34.237.91.238']


def do_deploy(archive_path):
    """Distributes an archive to a web server.
    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if not exists(archive_path):
        return False

    try:
        filename = archive_path.split("/")[-1]
        no_ext = filename.split(".")[0]
        remote_path = "/tmp/" + filename
        put(archive_path, remote_path)
        run("mkdir -p /data/web_static/releases/{}/".format(no_ext))
        run("tar -xzf {} -C /data/web_static/releases/{}/"
            .format(remote_path, no_ext))
        run("rm {}".format(remote_path))
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(no_ext, no_ext))
        run("rm -rf /data/web_static/releases/{}/web_static".format(no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(no_ext))
        return True
    except Exception:
        return False

