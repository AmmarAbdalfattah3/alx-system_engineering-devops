#a manifest file to create a file named school in /tmp path
file { '/tmp/school':
	mode => '0744'
	owner => 'www-data'
	group => 'www-data'
	content => 'I love Puppet'

}
