document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("dataForm");
    const tableBody = document.querySelector("#dataTable tbody");

    form.addEventListener("submit", function(event) {
        event.preventDefault();
        resetErrorMessages();
        
        const nama = document.getElementById("nama").value.trim();
        const alamat = document.getElementById("alamat").value.trim();
        const kota = document.getElementById("kota").value;
        let isValid = true;

        // Validasi Nama
        if (nama === "") {
            showError("namaError", "Nama wajib diisi!");
            isValid = false;
        }

        // Validasi Alamat
        if (alamat === "") {
            showError("alamatError", "Alamat wajib diisi!");
            isValid = false;
        }

        // Validasi Kota
        if (kota === "") {
            showError("kotaError", "Kota wajib dipilih!");
            isValid = false;
        }

        if (isValid) {
            addDataToTable(nama, alamat, kota);
            form.reset();
        }
    });

    // Fungsi untuk menampilkan pesan error
    function showError(elementId, message) {
        const errorElement = document.getElementById(elementId);
        errorElement.textContent = message;
    }

    // Fungsi untuk reset pesan error
    function resetErrorMessages() {
        const errorElements = document.querySelectorAll('.error');
        errorElements.forEach(element => {
            element.textContent = '';
        });
    }

    // Fungsi untuk menambahkan data ke tabel
    function addDataToTable(nama, alamat, kota) {
        const newRow = tableBody.insertRow();
        newRow.insertCell(0).textContent = nama;
        newRow.insertCell(1).textContent = alamat;
        newRow.insertCell(2).textContent = kota;
    }
});