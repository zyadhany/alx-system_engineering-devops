# install programe

exec { 'install_flask':
  command => '/usr/bin/apt-get -y install puppet-lint -v 2.5.0',
}
