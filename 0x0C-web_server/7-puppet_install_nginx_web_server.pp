# Install and configures Nginx using Puppet

$link = 'https://www.youtube.com/watch?v=QH2-TGUlwu4'
$conf = "server_name\ _;\n\trewrite ^/redirect_me/?$ ${link} permanent;"
$config = '/etc/nginx/sites-available/default'

exec { 'update packages':
  command => '/usr/bin/apt-get update'
}

package { 'nginx':
  ensure => installed
}

exec { 'configure firewall':
  command => '/usr/sbin/ufw allow "Nginx HTTP"'
}

file { 'root file':
  ensure => file,
  source => 'Hello World!',
  path   => '/var/www/html/index.html',
  owner  => 'root',
  group  => 'root',
  mode   => '0644'
}

exec { 'configure redirect':
  command => "/usr/bin/sed -i \"s|^server_name\ _;|${conf}|\" ${config}"
}

exec { 'restart server':
  command => '/usr/sbin/service nginx restart'
}
