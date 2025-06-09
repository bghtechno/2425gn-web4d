<?php
$host = "localhost";
$user = "root";
$pass = "";
$db   = "pendaftaran_db";
$conn = new mysqli($host, $user, $pass, $db);
if ($conn->connect_error) die("Koneksi gagal: " . $conn->connect_error);

// Cari data jika ada input search
$cari = isset($_GET['cari']) ? trim($_GET['cari']) : '';
$sql = "SELECT * FROM peserta WHERE nama LIKE '%$cari%' ORDER BY id DESC";
$result = $conn->query($sql);

// Tampilkan pesan jika ada
$pesan = "";
if (isset($_GET['success'])) {
    $pesan = "✅ " . htmlspecialchars($_GET['success']);
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Data Peserta</title>
    <style>
        body { font-family: Arial; background: #eef1f4; }
        .container {
            max-width: 900px; margin: 50px auto; background: #fff;
            padding: 30px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { border: 1px solid #ddd; padding: 12px; text-align: center; }
        th { background-color: #3498db; color: white; }
        .message {
            background-color: #d4edda; color: #155724; padding: 10px;
            margin-bottom: 15px; border-radius: 5px;
        }
        .search-bar {
            display: flex; justify-content: space-between; align-items: center;
        }
        input[type="text"] {
            padding: 8px; width: 70%; border-radius: 5px; border: 1px solid #ccc;
        }
        .link-form {
            margin-top: 20px; display: block; text-align: center;
        }
        a.button {
            padding: 5px 10px; text-decoration: none;
            color: white; border-radius: 5px;
        }
        .edit-btn { background-color: #f39c12; }
        .delete-btn { background-color: #e74c3c; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Data Peserta</h2>

        <?php if (!empty($pesan)) echo "<div class='message'>$pesan</div>"; ?>

        <form class="search-bar" method="GET">
            <input type="text" name="cari" placeholder="Cari nama..." value="<?= htmlspecialchars($cari) ?>">
            <button type="submit">Cari</button>
        </form>

        <table>
            <thead>
                <tr>
                    <th>No</th>
                    <th>Nama</th>
                    <th>Email</th>
                    <th>Jurusan</th>
                    <th>Aksi</th>
                </tr>
            </thead>
            <tbody>
                <?php
                if ($result->num_rows > 0) {
                    $no = 1;
                    while ($row = $result->fetch_assoc()) {
                        echo "<tr>
                            <td>$no</td>
                            <td>{$row['nama']}</td>
                            <td>{$row['email']}</td>
                            <td>{$row['jurusan']}</td>
                            <td>
                                <a class='button edit-btn' href='edit.php?id={$row['id']}'>Edit</a>
                                <a class='button delete-btn' href='hapus.php?id={$row['id']}' onclick=\"return confirm('Yakin mau hapus?')\">Hapus</a>
                            </td>
                        </tr>";
                        $no++;
                    }
                } else {
                    echo "<tr><td colspan='5'>Belum ada data peserta.</td></tr>";
                }
                ?>
            </tbody>
        </table>

        <a class="link-form" href="formulir.php">← Kembali ke Formulir</a>
    </div>
</body>
</html>
