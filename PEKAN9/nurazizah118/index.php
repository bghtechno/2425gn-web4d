<?php
session_start();

// Inisialisasi array mahasiswa kalau belum ada
if (!isset($_SESSION['mahasiswa'])) {
    $_SESSION['mahasiswa'] = [
        ["nama" => "Nur Azizah", "nim" => "230631100118", "jurusan" => "Pendidikan Informatika"],
    ];
}

// Proses tambah mahasiswa
if (isset($_POST['tambah'])) {
    $nama = htmlspecialchars($_POST['nama']);
    $nim = htmlspecialchars($_POST['nim']);
    $jurusan = htmlspecialchars($_POST['jurusan']);
    $_SESSION['mahasiswa'][] = ["nama" => $nama, "nim" => $nim, "jurusan" => $jurusan];
}

// Proses hapus mahasiswa
if (isset($_GET['hapus'])) {
    $index = $_GET['hapus'];
    unset($_SESSION['mahasiswa'][$index]);
    $_SESSION['mahasiswa'] = array_values($_SESSION['mahasiswa']); // reset index array
}
?>

<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Data Mahasiswa</title>
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(to right, #ffecd2, #fcb69f);
            min-height: 100vh;
            margin: 0;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        h1 {
            color: #ff6f91;
            font-size: 36px;
            margin-bottom: 10px;
        }
        h2 {
            color: #ff6f91;
            margin-bottom: 20px;
            font-size: 32px;
        }
        table {
            width: 70%;
            border-collapse: collapse;
            background: white;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            border-radius: 12px;
            overflow: hidden;
            margin-bottom: 20px;
        }
        th, td {
            padding: 15px;
            text-align: center;
        }
        th {
            background-color: #ffb6b9;
            color: white;
            font-size: 18px;
        }
        td {
            background-color: #ffe0e9;
            font-size: 16px;
        }
        tr:nth-child(even) td {
            background-color: #ffd3da;
        }
        p.keterangan {
            font-size: 18px;
            color: #555;
            margin-top: 10px;
            text-align: center;
        }
        form {
            background: #fff;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            margin-bottom: 30px;
            width: 50%;
        }
        input[type="text"], select {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 8px;
        }
        button {
            background-color: #ff6f91;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #ff4e71;
        }
        .hapus-btn {
            background-color: #ff4e71;
            border: none;
            padding: 5px 10px;
            color: white;
            border-radius: 6px;
            cursor: pointer;
        }
        .hapus-btn:hover {
            background-color: #e53958;
        }
    </style>
</head>
<body>

<h1>🌟 Selamat Datang di Data Mahasiswa 🌟</h1>

<h2>🌸 Tambah Mahasiswa Baru 🌸</h2>

<form method="post" action="">
    <input type="text" name="nama" placeholder="Masukkan Nama" required>
    <input type="text" name="nim" placeholder="Masukkan NIM" required>
    <input type="text" name="jurusan" placeholder="Masukkan Jurusan" required>
    <button type="submit" name="tambah">Tambah</button>
</form>

<h2>🌸 Daftar Mahasiswa 🌸</h2>

<table>
    <tr>
        <th>No</th>
        <th>Nama</th>
        <th>NIM</th>
        <th>Jurusan</th>
        <th>Aksi</th>
    </tr>
    <?php foreach ($_SESSION['mahasiswa'] as $index => $mhs): ?>
    <tr>
        <td><?= $index + 1 ?></td>
        <td><?= ucfirst($mhs["nama"]) ?></td>
        <td><?= $mhs["nim"] ?></td>
        <td><?= $mhs["jurusan"] ?></td>
        <td>
            <a href="?hapus=<?= $index ?>" onclick="return confirm('Yakin ingin menghapus?');">
                <button class="hapus-btn">Hapus</button>
            </a>
        </td>
    </tr>
    <?php endforeach; ?>
</table>

<p class="keterangan">✏️ Tugas ini dibuat untuk penugasan mata kuliah <strong>Pemrograman Web</strong>.</p>

</body>
</html>
