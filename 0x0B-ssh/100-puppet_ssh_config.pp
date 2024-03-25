#!/usr/bin/env bash

file_line { 'identity file':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  replace => 'true',
  line    => 'IdentityFile ~/.ssh/school',
}

file_line { 'prevent password authentication':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  replace => 'true',
  line    => 'PasswordAuthentication no',
}
