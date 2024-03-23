#a manifest file to install flask package

package {'puppet-lint':
  ensure  => '2.1.0',
  provider => 'gem',
}
