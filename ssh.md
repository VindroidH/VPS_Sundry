# ssh

``` shell
ssh -i id_rsa {user}@{ip_address}
```

## upload file
``` shell
scp {file} {user}@{ip_address}:{path}
```

## edit server ssh config
``` shell
vi /etc/ssh/sshd_config
# AuthorizedKeysFile .ssh/authorized_keys
->
AuthorizedKeysFile .ssh/authorized_keys

# disable password login
PasswordAuthentication no

service ssh restart
```
