<?php
$host = "localhost";
$user = "root";
$pass = "";
$db   = "pendaftaran_db";
$conn = new mysqli($host, $user, $pass, $db);
if ($conn->connect_error) die("Koneksi gagal: " . $conn->connect_error);

$id = $_GET['id'] ?? 0;

// Ambil data lama
$data = $conn->query("SELECT * FROM peserta WHERE id=$id")->fetch_assoc();

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nama = $_POST['nama'];
    $email = $_POST['email'];
    $jurusan = $_POST['jurusan'];

    $sql = "UPDATE peserta SET nama=?, email=?, jurusan=? WHERE id=?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("sssi", $nama, $email, $jurusan, $id);
    $stmt->execute();

    header("Location: peserta.php?success=Data berhasil diupdate!");
    exit();
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Edit Peserta</title>
    <style>
        body { font-family: Arial; background: #f0f2f5; }
        .container {
            max-width: 500px; margin: 50px auto; background: #fff;
            padding: 30px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        input, select, button {
            width: 100%; padding: 10px; margin-top: 10px; border-radius: 5px; border: 1px solid #ccc;
        }
        button {
            background-color: #2ecc71; color: white; border: none;
        }
        a { display: block; margin-top: 20px; text-align: center; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Edit Data Peserta</h2>
        <form method="POST">
            <label>Nama</label>
            <input type="text" name="nama" value="<?= $data['nama'] ?>" required>

            <label>Email</label>
            <input type="email" name="email" value="<?= $data['email'] ?>" required>

            <label>Jurusan</label>
            <select name="jurusan" required>
                <option value="Informatika" <?= $data['jurusan']=='Informatika'?'selected':'' ?>>Informatika</option>
                <option value="TKJ" <?= $data['jurusan']=='TKJ'?'selected':'' ?>>TKJ</option>
                <option value="RPL" <?= $data['jurusan']=='RPL'?'selected':'' ?>>RPL</option>
            </select>

            <button type="submit">Simpan Perubahan</button>
        </form>

        <a href="peserta.php">← Kembali ke Data Peserta</a>
    </div>
</body>
</html>
