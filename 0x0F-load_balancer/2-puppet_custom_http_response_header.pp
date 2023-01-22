#creates custom header called X-Served-By usign puppet
exec { 'automate with puppet':
  command  => 'apt-get -y update;
  sudo apt-get -y install nginx;
  sed -i "/root /var/www/html;/a add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default;
  service nginx restart',
  provider => shell,
}
