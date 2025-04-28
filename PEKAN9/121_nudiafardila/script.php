<?php
// Data dinamis berupa array
$mahasiswa = [
    ["nama" => "Nudia", "nim" => "121", "jurusan" => "Informatika"],
    ["nama" => "Budi", "nim" => "67890", "jurusan" => "Sistem Informasi"],
    ["nama" => "Citra", "nim" => "11223", "jurusan" => "Teknik Komputer"]
];
?>

<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Daftar Mahasiswa</title>
    <style>
        table {
            width: 50%;
            border-collapse: collapse;
            margin: 20px auto;
        }
        th, td {
            border: 1px solid #333;
            padding: 8px 12px;
            text-align: center;
        }
        th {
            background-color: #4CAF50;
            color: white;
        }
    </style>
</head>
<body>

<h2 style="text-align:center;">Daftar Mahasiswa</h2>

<table>
    <thead>
        <tr>
            <th>Nama</th>
            <th>NIM</th>
            <th>Jurusan</th>
        </tr>
    </thead>
    <tbody>
        <?php foreach($mahasiswa as $mhs): ?>
        <tr>
            <td><?php echo htmlspecialchars($mhs['nama']); ?></td>
            <td><?php echo htmlspecialchars($mhs['nim']); ?></td>
            <td><?php echo htmlspecialchars($mhs['jurusan']); ?></td>
        </tr>
        <?php endforeach; ?>
    </tbody>
</table>

</body>
</html>
