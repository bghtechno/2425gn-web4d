<?php
// Data statis
$nama = "laila";
$kelas = "X RPL ";
$mataPelajaran = "Pemrograman Web";

// Data dinamis (menggunakan array)
$mataPelajaranList = array("Matematika", "Fisika", "Pemrograman Web", "Bahasa Inggris");
?>

<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP Sederhana</title>
</head>
<body>

    <h1>Selamat datang, <?php echo $nama; ?>!</h1>
    <p>Kamu berada di kelas: <?php echo $kelas; ?>.</p>
    <p>Mata Pelajaran yang sedang dipelajari: <?php echo $mataPelajaran; ?>.</p>

    <h2>Daftar Mata Pelajaran</h2>
    <ul>
        <?php
        // Menampilkan daftar mata pelajaran menggunakan perulangan
        foreach ($mataPelajaranList as $mataPelajaran) {
            echo "<li>" . $mataPelajaran . "</li>";
        }
        ?>
    </ul>

</body>
</html>
