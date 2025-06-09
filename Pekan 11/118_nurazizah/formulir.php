<?php
// Koneksi database
$host = "localhost";
$user = "root";
$pass = "";
$db   = "pendaftaran_db";

$conn = new mysqli($host, $user, $pass, $db);
if ($conn->connect_error) {
    die("Koneksi gagal: " . $conn->connect_error);
}

// Proses saat form disubmit
$pesan = "";
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nama    = trim($_POST['nama']);
    $email   = trim($_POST['email']);
    $jurusan = $_POST['jurusan'];

    if (empty($nama) || empty($email) || empty($jurusan)) {
        $pesan = "❌ Semua field wajib diisi.";
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $pesan = "❌ Format email tidak valid.";
    } else {
        $stmt = $conn->prepare("INSERT INTO peserta (nama, email, jurusan) VALUES (?, ?, ?)");
        $stmt->bind_param("sss", $nama, $email, $jurusan);
        if ($stmt->execute()) {
            header("Location: peserta.php?success=1");
            exit();
        } else {
            $pesan = "❌ Gagal menyimpan data: " . $conn->error;
        }
        $stmt->close();
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Formulir Pendaftaran</title>
    <style>
        body { font-family: Arial; background: #f0f2f5; }
        .container {
            max-width: 500px; margin: 50px auto; padding: 30px;
            background: #fff; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        input, select, button {
            width: 100%; padding: 10px; margin-top: 10px; border-radius: 5px; border: 1px solid #ccc;
        }
        button {
            background-color: #3498db; color: white; border: none;
        }
        button:hover {
            background-color: #2980b9;
        }
        .message {
            background-color: #f8d7da; color: #721c24; padding: 10px; margin-bottom: 10px; border-radius: 5px;
        }
        .link-peserta {
            text-align: center; margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Formulir Pendaftaran</h2>
        <?php if (!empty($pesan)) echo "<div class='message'>$pesan</div>"; ?>

        <form method="POST">
            <label>Nama</label>
            <input type="text" name="nama" required>

            <label>Email</label>
            <input type="email" name="email" required>

            <label>Jurusan</label>
            <select name="jurusan" required>
                <option value="">-- Pilih Jurusan --</option>
                <option value="Informatika">Informatika</option>
                <option value="TKJ">TKJ</option>
                <option value="RPL">RPL</option>
            </select>

            <button type="submit">Daftar</button>
        </form>

        <div class="link-peserta">
            <a href="peserta.php">Lihat Data Peserta</a>
        </div>
    </div>
</body>
</html>
