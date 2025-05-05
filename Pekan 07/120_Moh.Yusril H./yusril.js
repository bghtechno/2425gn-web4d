document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("contactForm");

    form.addEventListener("submit", function (e) {
        e.preventDefault();

        const name = document.getElementById("name").value.trim();
        const email = document.getElementById("email").value.trim();
        const message = document.getElementById("message").value.trim();

        if (name === "" || email === "" || message === "") {
            alert("Semua kolom harus diisi!");
            return;
        }

        if (!validateEmail(email)) {
            alert("Email tidak valid!");
            return;
        }

        alert("Pesan berhasil dikirim!");
        form.reset();
    });

    function validateEmail(email) {
        const re = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;
        return re.test(email.toLowerCase());
    }
});
