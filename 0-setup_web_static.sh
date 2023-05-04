#!/usr/bin/env bash
# Install Nginx if it is not already installed
if ! command -v nginx &> /dev/null
then
	sudo apt-get update
	sudo apt-get install -y nginx
fi

# Create necessary folders if they don't exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html

# Create a fake HTML file to test Nginx configuration
echo "<html><head><title>Test Page</title></head><body><p>This is a test page.</p></body></html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link
sudo rm -f /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Set ownership of /data/ folder to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
CONFIG_STRING="\\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n"
sudo sed -i "/^\s*server\s*{/{:a;N;/^\s*}/!ba;s/\n$/\$CONFIG_STRING\n/}" /etc/nginx/sites-available/default

# Restart Nginx to apply changes
sudo service nginx restart
