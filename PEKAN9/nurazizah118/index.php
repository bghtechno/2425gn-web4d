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
    </style>
</head>
<body>

<h2>🌸 Daftar Mahasiswa 🌸</h2>

<?php
$mahasiswa = [
    ["nama" => "Nur Azizah", "nim" => "230631100118", "jurusan" => "Pendidikan Informatika"],
];
?>

<table>
    <tr>
        <th>No</th>
        <th>Nama</th>
        <th>NIM</th>
        <th>Jurusan</th>
    </tr>
    <?php foreach ($mahasiswa as $index => $mhs): ?>
    <tr>
        <td><?= $index + 1 ?></td>
        <td><?= ucfirst($mhs["nama"]) ?></td>
        <td><?= $mhs["nim"] ?></td>
        <td><?= $mhs["jurusan"] ?></td>
    </tr>
    <?php endforeach; ?>
</table>

</body>
</html>
