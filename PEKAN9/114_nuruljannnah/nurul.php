<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>pemrograman web 4d_nurul114</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color:rgb(255, 0, 242);
            padding: 40px;
            text-align: center;
        }
        .card {
            background: white;
            padding: 30px;
            border-radius: 10px;
            display: inline-block;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            color:rgb(255, 0, 174);
        }
        p {
            font-size: 18px;
            color: #333;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>Selamat Datang🤗</h1>
        <?php
            $nama = "Nurul Jannah";
            $nim = "230631100114";
            $tanggal = date("d-m-Y");

            echo "<p>Nama: <strong>$nama</strong></p>";
            echo "<p>NIM: <strong>$nim</strong></p>";
            echo "<p>Tanggal hari ini: <strong>$tanggal</strong></p>";
        ?>
        <p>Ini adalah tugas mata kuliah <strong>Pemrograman Web</strong> tentang menampilkan data dinamis dengan PHP</p>
    </div>
</body>
</html>
