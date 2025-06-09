<?php
$host = "localhost";
$user = "root";
$pass = "";
$db   = "pendaftaran_db";

$conn = new mysqli($host, $user, $pass, $db);
if ($conn->connect_error) die("Koneksi gagal: " . $conn->connect_error);

$id = $_GET['id'] ?? 0;
$conn->query("DELETE FROM peserta WHERE id=$id");

header("Location: peserta.php?success=Data berhasil dihapus!");
exit();
