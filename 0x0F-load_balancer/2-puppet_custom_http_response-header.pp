# Install Nginx web server with Puppet

$config_file = '/etc/nginx/nginx.conf'
$search = 'http {'
$config = "${search}\\n\tadd_header X-Served-By"

exec { 'update packages':
  command => '/usr/bin/apt-get update'
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update packages']
}

exec { 'configure firewall':
  command => '/usr/sbin/ufw allow "Nginx HTTP"'
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  mode    => '0644',
  owner   => 'root',
  group   => 'root'
}

exec { 'add custom header':
  command => "/usr/bin/sed -i 's|${search}|${config} \"${hostname}\";|' ${config_file}",
  unless  => "/usr/bin/grep -q 'X-Served-By' ${config_file}"
}

exec { 'restart Nginx':
  command => '/usr/sbin/service nginx restart'
}
