<?php
// Data produk (simulasi dari database)
$products = [
    ['nama' => 'Laptop ASUS ROG', 'harga' => 15000000, 'stok' => 5],
    ['nama' => 'Keyboard Mechanical', 'harga' => 750000, 'stok' => 10],
    ['nama' => 'Mouse Logitech', 'harga' => 250000, 'stok' => 20]
];
?>

<!DOCTYPE html>
<html>
<head>
    <title>Daftar Produk</title>
</head>
<body>

    <h2>Daftar Produk</h2>

    <table border="1" cellpadding="10" cellspacing="0">
        <tr>
            <th>No</th>
            <th>Nama Produk</th>
            <th>Harga (Rp)</th>
            <th>Stok</th>
        </tr>

        <?php
        $no = 1;
        foreach ($products as $produk) {
            echo "<tr>";
            echo "<td>" . $no++ . "</td>";
            echo "<td>" . htmlspecialchars($produk['nama']) . "</td>";
            echo "<td>" . number_format($produk['harga'], 0, ',', '.') . "</td>";
            echo "<td>" . $produk['stok'] . "</td>";
            echo "</tr>";
        }
        ?>
    </table>

</body>
</html>
