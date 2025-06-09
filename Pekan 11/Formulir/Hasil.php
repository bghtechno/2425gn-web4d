<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nama = $_POST["nama"];
    $email = $_POST["email"];
    $umur = $_POST["umur"];

    echo "<h2>Data yang Anda Kirim:</h2>";
    echo "Nama: " . htmlspecialchars($nama) . "<br>";
    echo "Email: " . htmlspecialchars($email) . "<br>";
    echo "Umur: " . htmlspecialchars($umur) . " tahun<br>";
} else {
    echo "Akses tidak sah.";
}
?>