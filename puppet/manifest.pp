Exec {
  path => "/usr/local/bin:/usr/bin:/bin",
}
Package {
  require => Exec["epel.repo", "yum update"],
}

exec { "epel.repo":
  command => 'yum -y -q localinstall http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm',
  path    => ['/bin', '/usr/bin'],
  unless  => 'rpm -qa | grep epel',
}
exec { "yum update":
  command => "/usr/bin/yum -y -q update",
  refreshonly => true,
}
package {
  "git": ensure => installed;
  "libxml2": ensure => installed;
  "libxslt": ensure => installed;
  "gcc": ensure => installed;
  "libxslt-devel": ensure => installed;
  "python": ensure => installed;
  "python-devel": ensure => installed;
  "python-setuptools": ensure => installed;
  "mysql": ensure => installed;
  "mysql-server": ensure => installed;
  "mysql-devel": ensure => installed;
  "redis": ensure => installed;
  "rubygems": ensure => installed;
}
exec { "easy_install pip":
  unless => "which pip",
  require => Package['python-setuptools'],
}
exec { "pip install virtualenv":
  unless => "which virtualenv",
  require => Exec["easy_install pip"],
}
service { "mysqld":
  ensure => running,
}
exec { "mysql -e 'CREATE DATABASE IF NOT EXISTS gedgo;'":
  require => Service[mysqld],
}
service { 'redis':
  ensure => 'running',
  enable => 'true',
  require => Package['redis'],
}
service { "iptables":
  ensure => stopped,
}
exec { "gem install foreman":
  unless => "which foreman",
  require => Package['rubygems'],
}
