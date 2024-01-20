#!/usr/bin/pup
#killing a process named killmenow
exec {'killmenow':
command => 'pkill killmenow'
}
