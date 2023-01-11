#a manifest file to install flask package

exec { 'puppet-lint':
  command => '/usr/bin/apt-get -y install puppet-lint -v 2.5.0',
}
