<?php
session_start();

if (!isset($_SESSION['mahasiswa'])) {
    $_SESSION['mahasiswa'] = [
        ["nama" => "Nur Azizah", "nim" => "230631100118", "jurusan" => "Pendidikan Informatika"],
    ];
}

if (isset($_POST['tambah'])) {
    $nama = htmlspecialchars($_POST['nama']);
    $nim = htmlspecialchars($_POST['nim']);
    $jurusan = htmlspecialchars($_POST['jurusan']);
    $_SESSION['mahasiswa'][] = ["nama" => $nama, "nim" => $nim, "jurusan" => $jurusan];
    header("Location: ".$_SERVER['PHP_SELF']);
    exit;
}

if (isset($_GET['hapus'])) {
    $index = $_GET['hapus'];
    unset($_SESSION['mahasiswa'][$index]);
    $_SESSION['mahasiswa'] = array_values($_SESSION['mahasiswa']);
    header("Location: ".$_SERVER['PHP_SELF']);
    exit;
}
?>

<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Data Mahasiswa Estetik</title>
    <style>
        body {
            font-family: 'Comic Sans MS', cursive, sans-serif;
            background: linear-gradient(135deg, #ffe1f0, #ffdede);
            min-height: 100vh;
            margin: 0;
            padding: 30px;
            display: flex;
            flex-direction: column;
            align-items: center;
            overflow-x: hidden;
        }
        h1, h2 {
            color: #ff69b4;
            margin: 10px 0;
            text-shadow: 1px 1px white;
        }
        table {
            width: 80%;
            border-collapse: collapse;
            background: #fff0f5;
            box-shadow: 0 6px 12px rgba(0,0,0,0.1);
            border-radius: 12px;
            overflow: hidden;
            animation: fadeIn 1s ease;
        }
        th, td {
            padding: 15px;
            text-align: center;
        }
        th {
            background-color: #ffb6c1;
            color: white;
        }
        td {
            background-color: #fff5f8;
        }
        tr.removed {
            animation: fadeOut 0.5s forwards;
        }
        @keyframes fadeOut {
            to { opacity: 0; transform: translateX(-100px); }
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        button {
            padding: 10px 18px;
            border: none;
            border-radius: 10px;
            background-color: #ff69b4;
            color: white;
            cursor: pointer;
            transition: 0.3s;
        }
        button:hover {
            background-color: #ff1493;
        }
        .hapus-btn {
            background-color: #ff4e6a;
        }
        .hapus-btn:hover {
            background-color: #d6304f;
        }
        .keterangan {
            margin-top: 20px;
            font-size: 18px;
            color: #555;
            text-align: center;
        }

        /* MODAL */
        .modal {
            display: none;
            position: fixed;
            z-index: 1;
            left: 0; top: 0;
            width: 100%; height: 100%;
            background-color: rgba(0,0,0,0.4);
        }
        .modal-content {
            background-color: #fff;
            margin: 10% auto;
            padding: 20px;
            border-radius: 12px;
            width: 300px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        }
        input[type="text"] {
            width: 100%;
            padding: 10px;
            margin: 8px 0;
            border: 1px solid #ddd;
            border-radius: 8px;
        }
        .close {
            color: #aaa;
            float: right;
            font-size: 22px;
            cursor: pointer;
        }
        .close:hover {
            color: #ff69b4;
        }
    </style>
</head>
<body>

<h1>✨ Selamat Datang! ✨</h1>
<h2>🌸 Daftar Mahasiswa 🌸</h2>

<!-- Tombol tambah -->
<button onclick="document.getElementById('modalForm').style.display='block'">+ Tambah Mahasiswa</button>

<!-- Tabel Mahasiswa -->
<table>
    <tr>
        <th>No</th>
        <th>Nama</th>
        <th>NIM</th>
        <th>Jurusan</th>
        <th>Aksi</th>
    </tr>
    <?php foreach ($_SESSION['mahasiswa'] as $index => $mhs): ?>
    <tr id="row<?= $index ?>">
        <td><?= $index + 1 ?></td>
        <td><?= ucfirst($mhs['nama']) ?></td>
        <td><?= $mhs['nim'] ?></td>
        <td><?= $mhs['jurusan'] ?></td>
        <td>
            <button class="hapus-btn" onclick="hapusMahasiswa(<?= $index ?>)">Hapus</button>
        </td>
    </tr>
    <?php endforeach; ?>
</table>

<p class="keterangan">📚 Tugas ini dibuat untuk penugasan mata kuliah <strong>Pemrograman Web</strong>.</p>

<!-- Modal Form -->
<div id="modalForm" class="modal">
    <div class="modal-content">
        <span class="close" onclick="document.getElementById('modalForm').style.display='none'">&times;</span>
        <form method="post" action="">
            <input type="text" name="nama" placeholder="Nama" required>
            <input type="text" name="nim" placeholder="NIM" required>
            <input type="text" name="jurusan" placeholder="Jurusan" required>
            <button type="submit" name="tambah">Simpan</button>
        </form>
    </div>
</div>

<!-- Script untuk hapus -->
<script>
function hapusMahasiswa(index) {
    if (confirm("Yakin mau hapus? 🥺")) {
        const row = document.getElementById("row" + index);
        row.classList.add("removed");
        setTimeout(() => {
            window.location.href = "?hapus=" + index;
        }, 400);
    }
}
</script>

</body>
</html>
