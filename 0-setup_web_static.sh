#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.

# Update package lists and install Nginx
apt-get update
apt-get install -y nginx

# Create necessary directories with appropriate permissions
mkdir -p /data/web_static/{releases/test,shared}
chown -R www-data:www-data /data/web_static

# Add a test index.html file
echo "Holberton School" > /data/web_static/releases/test/index.html

# Create a symbolic link to the current release
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Configure Nginx
cat << EOF > /etc/nginx/sites-available/default
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $hostname;

    # Directly serve static content from the 'current' directory
    root /data/web_static/current;
    index index.html index.htm;

    location /redirect_me {
        return 301 http://github.com/besthor;
    }

    error_page 404 /404.html;
    location /404 {
        internal;
    }
}
EOF

# Restart Nginx with error checking
service nginx restart || systemctl status nginx.service
