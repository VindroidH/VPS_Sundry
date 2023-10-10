/etc/caddy/Caddyfile

sudo apt install -y debian-keyring debian-archive-keyring apt-transport-https
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | sudo tee /etc/apt/sources.list.d/caddy-stable.list
sudo apt update
sudo apt install caddy

caddy adapt
caddy fmt
caddy stop
caddy run


```
1.example.org, 2.example.org
{
root * /var/www/{host}
file_server
# vmess
reverse_proxy /help localhost:23456
# vless + http/2
reverse_proxy /download localhost:23457 {
    transport http {
      versions h2c
    }
}
# vless + ws + cdn
reverse_proxy /download2 localhost:23458
}
```