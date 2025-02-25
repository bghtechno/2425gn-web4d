from flask import Flask, render_template, request, redirect, url_for
import json
import hashlib

app = Flask(__name__)

# Data penyimpanan sementara
database = {
    "users": [],
    "books": [],
    "classes": [],
    "presensi": [],
    "transactions": [],
    "evaluations": []
}

class Pengguna:
    def __init__(self, username, password):
        self.username = username
        self.password = hashlib.sha256(password.encode()).hexdigest()

class Mahasiswa(Pengguna):
    def __init__(self, username, password, nim, nama, jurusan, angkatan):
        super().__init__(username, password)
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan
        self.angkatan = angkatan
        self.nilai = {}
        self.jadwal = []
        self.pinjaman_buku = []
        self.presensi = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        for user in database['users']:
            if user['username'] == username and user['password'] == hashed_password:
                return redirect(url_for('dashboard'))
        return "Login Gagal!"
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', users=database['users'])

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        new_user = {"username": username, "password": hashlib.sha256(password.encode()).hexdigest()}
        database['users'].append(new_user)
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/add_book', methods=['POST'])
def add_book():
    book_title = request.form['book_title']
    database['books'].append(book_title)
    return redirect(url_for('dashboard'))

@app.route('/attendance', methods=['POST'])
def attendance():
    username = request.form['username']
    database['presensi'].append(username)
    return redirect(url_for('dashboard'))

@app.route('/payment', methods=['POST'])
def payment():
    username = request.form['username']
    amount = request.form['amount']
    database['transactions'].append({"username": username, "amount": amount})
    return redirect(url_for('dashboard'))

@app.route('/evaluate', methods=['POST'])
def evaluate():
    username = request.form['username']
    feedback = request.form['feedback']
    database['evaluations'].append({"username": username, "feedback": feedback})
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
