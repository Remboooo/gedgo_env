from fabric.api import env, task, run, cd

# default config for development environment
env.use_ssh_config = False
env.hosts = ['vagrant@127.0.0.1:2222']  # does not work with "localhost"
env.key_filename = '~/.vagrant.d/insecure_private_key'
env.output_prefix = False
env.disable_known_hosts = True

# --- actions for vagrant dev box


@task
def setup_env():
    """
    Resets the virtualenv library and creates a new
    database if it doesn't already exist
    """
    with cd("gedgo_env"):
        run("sh setup_env.sh; ", shell=True)


@task
def server():
    """
    Runs a local development server
    """
    with cd("gedgo_env"):
        run("foreman start", shell=True)
