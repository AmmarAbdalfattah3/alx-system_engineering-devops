#!/usr/bin/env bash
file_line { 'identify file':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  replace => 'true',
  line    => '	IdentifyFile ~/.ssh/school'
}

file_line { 'prevent password authentication':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  replace => 'true',
  line    => '	PasswordAuthentication no',
}
