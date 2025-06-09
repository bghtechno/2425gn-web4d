<?php
$submitted = $_SERVER["REQUEST_METHOD"] == "POST";
$name = $email = "";

if ($submitted) {
  $name = htmlspecialchars($_POST["name"]);
  $email = htmlspecialchars($_POST["email"]);
}
?>

<!DOCTYPE html>
<html>
<body>

<h2>Formulir Pendaftaran</h2>

<form method="POST">
  Name: <input type="text" name="name"><br><br>
  E-mail: <input type="text" name="email"><br><br>
  <input type="submit">
</form>

<?php if ($submitted): ?>
  <h3>Data yang Anda Kirim:</h3>
  Name: <?php echo $name; ?><br>
  Email: <?php echo $email; ?>
<?php endif; ?>

</body>
</html>

