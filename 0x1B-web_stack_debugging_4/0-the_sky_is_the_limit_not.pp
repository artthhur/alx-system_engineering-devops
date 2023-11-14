# Puppet manifest to increase ULIMIT for Nginx in /etc/default/nginx and restart Nginx

# Increases the ULIMIT of the default file
exec { 'fix_for_nginx':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin:/bin',
} ->

# Restarts Nginx
exec { 'nginx_restart':
  command => '/etc/init.d/nginx restart',  # Use the correct restart command
  path    => '/etc/init.d',
}
