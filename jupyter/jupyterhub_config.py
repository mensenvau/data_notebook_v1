import os
from nativeauthenticator import NativeAuthenticator  # type: ignore

os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-11-openjdk-amd64"
os.environ["PATH"] = os.environ["JAVA_HOME"] + "/bin:" + os.environ["PATH"]

c = get_config()  # type: ignore

c.JupyterHub.authenticator_class = "nativeauthenticator.NativeAuthenticator"

# Define admin users
c.Authenticator.admin_users = {"admin"}
c.Authenticator.allowed_users = {"admin"}

# Use SimpleLocalProcessSpawner
c.JupyterHub.spawner_class = "jupyterhub.spawner.LocalProcessSpawner"

# Increase timeout for slow starts
c.Spawner.start_timeout = 120  # Increase timeout to 2 minutes
c.Spawner.http_timeout = 60  # Allow more time for the server to respond

# Ensure users start in JupyterLab instead of classic notebook
c.Spawner.default_url = "/lab"
c.Spawner.cmd = ["jupyter-labhub", "--allow-root"]

# Set home directory
c.Spawner.notebook_dir = "/home/{username}/notebooks"

# Remove pre_spawn_hook (causes issues inside Docker)
