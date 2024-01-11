<?php
// Execute your Python script
$output = shell_exec("ascii_art.py");  // Adjust the Python script name
echo $output;
?>