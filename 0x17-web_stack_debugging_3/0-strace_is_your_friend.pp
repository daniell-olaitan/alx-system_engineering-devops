# fixes wordpress typo

exec {'fix-apache-word-press':
  command => '/usr/bin/sed -i "s/phpp/php/g" /var/www/html/wp-settings.php';
}
