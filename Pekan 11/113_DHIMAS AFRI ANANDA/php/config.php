petualangan-web/
├── index.php
├── login.php
├── register.php
├── dashboard.php
├── game.php
├── profile.php
├── includes/
│   ├── config.php
│   ├── header.php
│   ├── footer.php
│   ├── functions.php
├── assets/
│   ├── css/
│   │   ├── style.css
│   ├── js/
│   │   ├── script.js
│   ├── images/
├── uploads/

config
<?php
// Koneksi database
$host = 'localhost';
$dbname = 'game_petualangan';
$username = 'root';
$password = '';

try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Koneksi gagal: " . $e->getMessage());
}

// Buat tabel jika belum ada
$sql = "
    CREATE TABLE IF NOT EXISTS pengguna (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL UNIQUE,
        email VARCHAR(100) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL,
        avatar VARCHAR(255) DEFAULT 'default.png',
        level INT DEFAULT 1,
        pengalaman INT DEFAULT 0,
        dibuat_pada TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS pencapaian (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        judul VARCHAR(100) NOT NULL,
        deskripsi TEXT,
        dicapai_pada TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES pengguna(id)
    );
";
$pdo->exec($sql);

session_start();
?>

header
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Petualangan Seru - <?php echo $judulHalaman ?? 'Beranda'; ?></title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
    <header class="header-game">
        <div class="container">
            <h1><a href="index.php">Petualangan Seru</a></h1>
            <nav>
                <ul>
                    <?php if (isset($_SESSION['user_id'])): ?>
                        <li><a href="dashboard.php">Dashboard</a></li>
                        <li><a href="game.php">Main Game</a></li>
                        <li><a href="profile.php">Profil</a></li>
                        <li><a href="logout.php">Keluar</a></li>
                    <?php else: ?>
                        <li><a href="index.php">Beranda</a></li>
                        <li><a href="login.php">Masuk</a></li>
                        <li><a href="register.php">Daftar</a></li>
                    <?php endif; ?>
                </ul>
            </nav>
        </div>
    </header>
    <main class="container">

footer
    </main>
    <footer class="footer-game">
        <div class="container">
            <p>&copy; <?php echo date('Y'); ?> Petualangan Seru. Semua hak dilindungi.</p>
            <div class="tautan-sosial">
                <a href="#" class="ikon-sosial">🎮</a>
                <a href="#" class="ikon-sosial">🏆</a>
                <a href="#" class="ikon-sosial">📜</a>
            </div>
        </div>
    </footer>
    <script src="assets/js/script.js"></script>
</body>
</html>

index
<?php 
$judulHalaman = "Beranda";
include 'includes/header.php'; 
?>

<section class="hero">
    <div class="konten-hero">
        <h2>Mulai Petualangan Epik Anda!</h2>
        <p>Bergabunglah dengan ribuan pemain dalam game petualangan berbasis teks yang seru ini.</p>
        <div class="tombol-aksi">
            <a href="register.php" class="btn btn-primer">Mulai Petualangan</a>
            <a href="login.php" class="btn btn-sekunder">Lanjutkan Perjalanan</a>
        </div>
    </div>
</section>

<section class="fitur">
    <div class="kartu-fitur">
        <div class="ikon-fitur">⚔️</div>
        <h3>Lawan Monster</h3>
        <p>Hadapi makhluk menakutkan dan tingkatkan level karakter Anda.</p>
    </div>
    <div class="kartu-fitur">
        <div class="ikon-fitur">🧩</div>
        <h3>Pecahkan Teka-teki</h3>
        <p>Asah otak Anda dengan teka-teki dan tebakan yang rumit.</p>
    </div>
    <div class="kartu-fitur">
        <div class="ikon-fitur">🏆</div>
        <h3>Dapatkan Pencapaian</h3>
        <p>Kumpulkan prestasi dan buktikan kehebatan Anda.</p>
    </div>
</section>

<?php include 'includes/footer.php'; ?>

login
<?php
$judulHalaman = "Masuk";
include 'includes/header.php';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $username = $_POST['username'];
    $password = $_POST['password'];
    
    $stmt = $pdo->prepare("SELECT * FROM pengguna WHERE username = ?");
    $stmt->execute([$username]);
    $user = $stmt->fetch();
    
    if ($user && password_verify($password, $user['password'])) {
        $_SESSION['user_id'] = $user['id'];
        $_SESSION['username'] = $user['username'];
        header("Location: dashboard.php");
        exit();
    } else {
        $error = "Username atau password salah!";
    }
}
?>

<section class="form-container">
    <h2>Masuk ke Akun Anda</h2>
    <?php if (isset($error)): ?>
        <div class="pesan-error"><?php echo $error; ?></div>
    <?php endif; ?>
    <form method="POST">
        <div class="form-group">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>
        </div>
        <div class="form-group">
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>
        </div>
        <button type="submit" class="btn btn-primer">Masuk</button>
    </form>
    <p>Belum punya akun? <a href="register.php">Daftar di sini</a></p>
</section>

<?php include 'includes/footer.php'; ?>

game
<?php
$judulHalaman = "Main Game";
include 'includes/header.php';

if (!isset($_SESSION['user_id'])) {
    header("Location: login.php");
    exit();
}

// Dapatkan data pengguna
$stmt = $pdo->prepare("SELECT * FROM pengguna WHERE id = ?");
$stmt->execute([$_SESSION['user_id']]);
$user = $stmt->fetch();

// Proses aksi game
if (isset($_POST['aksi'])) {
    $aksi = $_POST['aksi'];
    
    switch ($aksi) {
        case 'jelajah':
            $hasil = "Anda menemukan hutan misterius!";
            $pengalaman = rand(5, 15);
            break;
        case 'bertarung':
            $hasil = "Anda mengalahkan monster dan mendapatkan hadiah!";
            $pengalaman = rand(10, 20);
            break;
        case 'istirahat':
            $hasil = "Anda beristirahat dan memulihkan tenaga.";
            $pengalaman = 0;
            break;
        default:
            $hasil = "Aksi tidak dikenal.";
            $pengalaman = 0;
    }
    
    // Update pengalaman pengguna
    $pengalamanBaru = $user['pengalaman'] + $pengalaman;
    $levelBaru = $user['level'];
    
    // Cek level up (setiap 100 XP)
    if ($pengalamanBaru >= 100) {
        $levelBaru = floor($pengalamanBaru / 100) + 1;
        $pesanLevel = "Selamat! Anda naik ke level $levelBaru!";
    }
    
    $stmt = $pdo->prepare("UPDATE pengguna SET pengalaman = ?, level = ? WHERE id = ?");
    $stmt->execute([$pengalamanBaru, $levelBaru, $_SESSION['user_id']]);
    
    // Refresh data pengguna
    $stmt = $pdo->prepare("SELECT * FROM pengguna WHERE id = ?");
    $stmt->execute([$_SESSION['user_id']]);
    $user = $stmt->fetch();
}
?>

<section class="game-container">
    <h2>Petualangan Anda</h2>
    
    <div class="profil-pemain">
        <div class="avatar">
            <img src="assets/images/avatars/<?php echo $user['avatar']; ?>" alt="Avatar" width="100">
        </div>
        <div class="info-pemain">
            <h3><?php echo $user['username']; ?></h3>
            <p>Level: <?php echo $user['level']; ?></p>
            <div class="bar-pengalaman">
                <div class="pengalaman-terisi" style="width: <?php echo ($user['pengalaman'] % 100); ?>%"></div>
            </div>
            <p>XP: <?php echo $user['pengalaman']; ?></p>
        </div>
    </div>
    
    <?php if (isset($hasil)): ?>
        <div class="hasil-aksi">
            <p><?php echo $hasil; ?></p>
            <?php if ($pengalaman > 0): ?>
                <p>+<?php echo $pengalaman; ?> XP</p>
            <?php endif; ?>
            <?php if (isset($pesanLevel)): ?>
                <p class="level-up"><?php echo $pesanLevel; ?></p>
            <?php endif; ?>
        </div>
    <?php endif; ?>
    
    <form method="POST" class="aksi-game">
        <button type="submit" name="aksi" value="jelajah" class="btn btn-primer">Jelajahi</button>
        <button type="submit" name="aksi" value="bertarung" class="btn btn-primer">Bertarung</button>
        <button type="submit" name="aksi" value="istirahat" class="btn btn-sekunder">Istirahat</button>
    </form>
    
    <div class="log-petualangan">
        <h3>Log Petualangan</h3>
        <p>Selamat datang di dunia petualangan! Pilih aksi untuk memulai.</p>
    </div>
</section>

<?php include 'includes/footer.php'; ?>

profil
<?php
$judulHalaman = "Profil";
include 'includes/header.php';

if (!isset($_SESSION['user_id'])) {
    header("Location: login.php");
    exit();
}

// Dapatkan data pengguna
$stmt = $pdo->prepare("SELECT * FROM pengguna WHERE id = ?");
$stmt->execute([$_SESSION['user_id']]);
$user = $stmt->fetch();

// Proses update profil
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $email = $_POST['email'];
    
    // Handle upload avatar
    if (isset($_FILES['avatar']) && $_FILES['avatar']['error'] == 0) {
        $ekstensi = pathinfo($_FILES['avatar']['name'], PATHINFO_EXTENSION);
        $namaFile = uniqid() . '.' . $ekstensi;
        $tujuan = 'assets/images/avatars/' . $namaFile;
        
        if (move_uploaded_file($_FILES['avatar']['tmp_name'], $tujuan)) {
            // Hapus avatar lama jika bukan default
            if ($user['avatar'] != 'default.png') {
                unlink('assets/images/avatars/' . $user['avatar']);
            }
            $avatar = $namaFile;
        } else {
            $error = "Gagal mengupload avatar.";
        }
    } else {
        $avatar = $user['avatar'];
    }
    
    if (!isset($error)) {
        $stmt = $pdo->prepare("UPDATE pengguna SET email = ?, avatar = ? WHERE id = ?");
        if ($stmt->execute([$email, $avatar, $_SESSION['user_id']])) {
            $sukses = "Profil berhasil diperbarui!";
            // Refresh data pengguna
            $stmt = $pdo->prepare("SELECT * FROM pengguna WHERE id = ?");
            $stmt->execute([$_SESSION['user_id']]);
            $user = $stmt->fetch();
        } else {
            $error = "Gagal memperbarui profil.";
        }
    }
}
?>

<section class="profil-container">
    <h2>Profil Anda</h2>
    
    <?php if (isset($error)): ?>
        <div class="pesan-error"><?php echo $error; ?></div>
    <?php endif; ?>
    
    <?php if (isset($sukses)): ?>
        <div class="pesan-sukses"><?php echo $sukses; ?></div>
    <?php endif; ?>
    
    <form method="POST" enctype="multipart/form-data">
        <div class="form-group">
            <label for="username">Username:</label>
            <input type="text" id="username" value="<?php echo $user['username']; ?>" disabled>
            <small>Username tidak dapat diubah</small>
        </div>
        
        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" value="<?php echo $user['email']; ?>" required>
        </div>
        
        <div class="form-group">
            <label for="level">Level:</label>
            <input type="text" id="level" value="<?php echo $user['level']; ?>" disabled>
        </div>
        
        <div class="form-group">
            <label for="pengalaman">Pengalaman:</label>
            <input type="text" id="pengalaman" value="<?php echo $user['pengalaman']; ?>" disabled>
        </div>
        
        <div class="form-group">
            <label for="avatar">Avatar:</label>
            <div class="avatar-preview">
                <img src="assets/images/avatars/<?php echo $user['avatar']; ?>" alt="Avatar" width="100">
            </div>
            <input type="file" id="avatar" name="avatar" accept="image/*">
        </div>
        
        <button type="submit" class="btn btn-primer">Perbarui Profil</button>
    </form>
</section>

<?php include 'includes/footer.php'; ?>
