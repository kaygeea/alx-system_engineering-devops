# Install "flask"(v2.1.0) and pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
