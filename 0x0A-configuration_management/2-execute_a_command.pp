#a manifest that executes a command

exec {'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
