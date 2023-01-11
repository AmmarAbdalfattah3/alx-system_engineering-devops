#a manifest that executes a command

exec { 'puppet-lint':
  command => '/usr/bin/apt-get -y install puppet-lint -v 2.5.0',
}
