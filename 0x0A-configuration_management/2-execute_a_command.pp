# pkill

exec { 'kill_killmenow_process':
  command => 'pkill -f "killmenow"',
  provider => 'shell',
}
