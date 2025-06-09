<?php
// Function untuk hash password
function hashPassword($password) {
    return password_hash($password, PASSWORD_DEFAULT);
}

// Cek apakah form disubmit
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Superglobal
    $nama = $_POST["nama"];
    $umur = (int)$_POST["umur"]; // Casting
    $email = $_POST["email"];
    $password = $_POST["password"];
    $jurusan = $_POST["jurusan"];

    // Operator dan if...else...
    if ($umur < 17) {
        echo "<p style='color:red;'>Maaf, umur Anda belum mencukupi untuk mendaftar.</p>";
        exit;
    } elseif ($umur >= 17 && $umur <= 25) {
        $status = "Remaja Dewasa";
    } else {
        $status = "Dewasa";
    }

    // Switch untuk kategori jurusan
    switch ($jurusan) {
        case "tkj":
            $jurusan_text = "Teknik Komputer dan Jaringan";
            break;
        case "rpl":
            $jurusan_text = "Rekayasa Perangkat Lunak";
            break;
        case "mm":
            $jurusan_text = "Multimedia";
            break;
        default:
            $jurusan_text = "Lainnya";
    }

    // Buat array data
    $data = [
        "nama" => $nama,
        "umur" => $umur,
        "email" => $email,
        "password" => hashPassword($password),
        "jurusan" => $jurusan_text,
        "status_umur" => $status,
        "tanggal_daftar" => date("Y-m-d H:i:s")
    ];

    // Encode ke JSON
    $json_data = json_encode($data, JSON_PRETTY_PRINT);

    // Simpan ke file
    file_put_contents("pendaftaran.json", $json_data);

    // Baca ulang dari file dan tampilkan
    $isi = file_get_contents("pendaftaran.json");
    $hasil = json_decode($isi, true);

    // Tampilkan hasil
    echo "<h3>Data Pendaftaran:</h3>";
    foreach ($hasil as $key => $value) {
        echo "<p><strong>" . ucfirst(str_replace('_', ' ', $key)) . "</strong>: $value</p>";
    }
}
?>

<!-- Form HTML -->
<form method="POST">
    <label>Nama:</label><br>
    <input type="text" name="nama" required><br>

    <label>Umur:</label><br>
    <input type="number" name="umur" required><br>

    <label>Email:</label><br>
    <input type="email" name="email" required><br>

    <label>Password:</label><br>
    <input type="password" name="password" required><br>

    <label>Jurusan:</label><br>
    <select name="jurusan" required>
        <option value="tkj">TKJ</option>
        <option value="rpl">RPL</option>
        <option value="mm">MM</option>
    </select><br><br>

    <button type="submit">Daftar</button>
</form>
