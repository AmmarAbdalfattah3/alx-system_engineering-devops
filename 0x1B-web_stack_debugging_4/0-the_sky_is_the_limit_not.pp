exec { 'update_nginx_limits':
  command     => 'sed -i "s/auto/15000/" /etc/default/nginx && systemctl restart nginx',
  path        => ['/bin', '/usr/bin'],
  refreshonly => true,
  logoutput   => true,
  unless      => 'grep -q "auto" /etc/default/nginx',
}
