# install programe

exec { 'puppet-lint':
  command => '/usr/bin/pip3 install flask==2.1.0',
}
