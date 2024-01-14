#!/usr/bin/env bash
# Script that sets up web servers for the deployment of web_static

# Update and install Nginx
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

# Create directory structure and HTML file
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set ownership
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
nginx_config_snippet="location /hbnb_static { alias /data/web_static/current/; }"
sudo bash -c "echo '$nginx_config_snippet' >> /etc/nginx/sites-enabled/default"

# Restart Nginx
sudo service nginx restart
