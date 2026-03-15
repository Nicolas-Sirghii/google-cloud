# Use official Caddy image
FROM caddy:latest

# Copy your Caddyfile
COPY Caddyfile /etc/caddy/Caddyfile

# Copy your website files to Caddy's root
COPY index.html /usr/share/caddy/index.html
