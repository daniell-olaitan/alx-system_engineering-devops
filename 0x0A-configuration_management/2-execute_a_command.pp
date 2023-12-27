# executes a command using puppet

exec { 'kiil_a_process':
  command => '/usr/bin/pkill killmenow',
}
