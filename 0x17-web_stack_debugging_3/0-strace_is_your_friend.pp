# Corrects misspelt extension used in the WordPress file - `wp-settings.php`; `phpp` extension to `php`.

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
