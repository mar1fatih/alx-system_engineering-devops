# fixing the failed requests problem

exec { 'fixing failed requests':
  command => 'sed -i "s/15/10000/g" /etc/default/nginx && sudo service nginx restart',
  path    => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin'],
}
