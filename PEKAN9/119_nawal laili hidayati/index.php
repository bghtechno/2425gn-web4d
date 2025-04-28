<?php
// Variabel biasa
$judul = "Halo, Selamat Datang!";
$nama = "Nawal Laili Hidayati"; // Nama kamu!

// Menampilkan teks
echo "<h1>$judul</h1>";
echo "<p>Selamat datang, $nama!</p>";

// Data array sederhana
$buah = ["Apel", "Jeruk", "Mangga", "Pisang"];

echo "<h2>Daftar Buah:</h2>";
echo "<ul>";

// Menampilkan data array
foreach ($buah as $item) {
    echo "<li>$item</li>";
}

echo "</ul>";
?>
