# update limit for nginx
exec { 'update soft limit for nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# Restart Nginx
exec { 'restart nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
