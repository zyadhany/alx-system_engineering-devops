# create to shh config

file { 'config':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
  line   => '    PasswordAuthentication no',
}
