# Configure the SSH server to authenticates only through SSH keys

$config = 'PasswordAuthentication no'
$attr = 'PasswordAuthentication'
$id = 'IdentityFile ~/.ssh/school'
exec { 'Turn off passwd auth':
  command => "/usr/bin/sed -i '/${attr}/c ${config}' /etc/ssh/ssh_config",
}

exec { 'Declare identity file':
  command => "/usr/bin/sed -i '/IdentityFile/c ${id} /etc/ssh/ssh_config",
}
