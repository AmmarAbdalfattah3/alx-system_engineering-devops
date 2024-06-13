exec { 'update_nginx_limits':
  command     => 'sed -i "s/15/15000/" /etc/default/nginx && systemctl restart nginx',
  path        => ['/bin', '/usr/bin'],
  refreshonly => true,
  logoutput   => true,
  unless      => 'grep -q "15" /etc/default/nginx',
}
