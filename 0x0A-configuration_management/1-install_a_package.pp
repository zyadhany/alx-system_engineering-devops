# install flask

exec { 'install_flask':
  command => '/usr/bin/pip3 -y install Flask -v 2.1.0',
}
