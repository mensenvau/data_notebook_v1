FROM jupyterhub/jupyterhub:latest

# Install PySpark & Other Data Science Libraries
RUN pip install --no-cache-dir \
    ipykernel \
    pyspark \
    pandas \
    numpy \
    matplotlib

# Ensure Jupyter recognizes the installed Python environment
RUN python3 -m ipykernel install --name "python3" --user

# Install JupyterHub authentication plugin
RUN pip install --no-cache-dir dockerspawner jupyterhub-nativeauthenticator

# Ensure system files exist
RUN touch /etc/passwd /etc/shadow

# Manually create the admin user
RUN useradd -m -s /bin/bash admin && echo "admin:adminpassword" | chpasswd && usermod -aG sudo admin

# Ensure home directory exists and set proper permissions
RUN mkdir -p /home/admin/notebooks && \
    chown -R admin:admin /home/admin && \
    chmod -R 777 /home/admin

# Copy JupyterHub configuration
COPY jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py

# ✅ Copy the SQL magic script for each user's IPython startup
RUN mkdir -p /etc/skel/.ipython/profile_default/startup
COPY ipython_config.py /etc/skel/.ipython/profile_default/startup/ipython_config.py

# Install Spark dependencies
RUN apt-get update && apt-get install -y openjdk-8-jdk-headless wget && \
    wget -qO- https://archive.apache.org

# Set working directory
WORKDIR /srv/jupyterhub

# Expose the JupyterHub port
EXPOSE 8000

# Start JupyterHub
CMD ["jupyterhub", "-f", "/srv/jupyterhub/jupyterhub_config.py"]