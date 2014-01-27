from fabric.api import env, task, run, cd

# default config for development environment
env.use_ssh_config = False
env.hosts = ['vagrant@127.0.0.1:2222']  # does not work with "localhost"
env.key_filename = '~/.vagrant.d/insecure_private_key'
env.output_prefix = False
env.disable_known_hosts = True

# --- actions for vagrant dev box


@task
def setup_dev_env():
    """
    Resets the virtualenv library and the database, loads some
    fixture data to speed up development environment setup
    """
    with cd("gedgo_env"):
        run("sh setup_dev_env.sh; ", shell=True)


@task
def server():
    """
    Runs a local development server
    """
    with cd("gedgo_env"):
        run("foreman start", shell=True)


@task
def test():
    """
    Run the unit tests
    """
    with cd("gedgo_env"):
        run("virtualenv/bin/flake8 gedgo")
        run("virtualenv/bin/python manage.py test gedgo")
