# create to shh config

file { 'configpass':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  content   => "# SSH client configuration
                Host *
                    IdentityFile ~/.ssh/school
                    PasswordAuthentication no",
}
