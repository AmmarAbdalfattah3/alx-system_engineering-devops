#a manifest file to install flask package

exec {'puppet-lint':
  command => '/usr/bin/pip3 install flask==2.1.0',
}
