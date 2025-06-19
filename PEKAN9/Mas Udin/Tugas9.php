
<?php

$mahasiswa = [
    ["nama" => "Arinal", "nim" => "12385768", "jurusan" => "PBSI"],
    ["nama" => "Adam", "nim" => "12345698", "jurusan" => "Informatika"],
    ["nama" => "Dhimas", "nim" => "12357866", "jurusan" => "PGSD"]
];
?>

<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Daftar Mahasiswa</title>
    <style>
        table {
            border-collapse: collapse;
            width: 50%;
            margin: 20px auto;
        }
        th, td {
            border: 1px solid #999;
            padding: 10px;
            text-align: center;
        }
        th {
            background-color: #eee;
        }
    </style>
</head>
<body>

    <h2 style="text-align: center;">Daftar Mahasiswa</h2>

    <table>
        <tr>
            <th>Nama</th>
            <th>NIM</th>
            <th>Jurusan</th>
        </tr>
        <?php foreach ($mahasiswa as $mhs): ?>
            <tr>
                <td><?= htmlspecialchars($mhs["nama"]) ?></td>
                <td><?= htmlspecialchars($mhs["nim"]) ?></td>
                <td><?= htmlspecialchars($mhs["jurusan"]) ?></td>
            </tr>
        <?php endforeach; ?>
    </table>

</body>
</html>
