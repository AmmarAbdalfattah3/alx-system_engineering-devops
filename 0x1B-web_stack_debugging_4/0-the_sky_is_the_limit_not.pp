exec { 'update_nginx_limits':
  command     => 'sed -i "s/4/15000/" /etc/default/nginx && systemctl restart nginx',
  path        => ['/bin', '/usr/bin'],
  refreshonly => true,
  logoutput   => true,
  unless      => 'grep -q "4" /etc/default/nginx',
}
