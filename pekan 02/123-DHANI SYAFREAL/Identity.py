# 1
daftar_peserta = 300

if daftar_peserta > 200:
    print("jumlah overload\n")
else:
    print("jumlah tidak overlord\n")


# 4
def factorial(num):
    store = num
    times = num
    for i in (1, num):
        store = num - i
        times = store * times
        return times


print(factorial(10))


# 5
class parent:
    def __init__(self, name, hobby):
        self.name = name
        self.hobby = hobby

    def myfunc(self):
        print("Hello...\n", "My name is", self.name, "and my hobby is", self.hobby)


id = parent("Vengeance", "Reading")
id.myfunc()


# 8 Menghitung jumlah penduduk di Indonesia
print("----------POPULASI ID----------")
pria = 134229998
wanita = 137119901
a = pria
b = wanita
c = a + b

print("Jumlah Pria ID: ", a)
print("Jumlah Wanita ID: ", b)
print("Total jumlah penduduk ID: ", c)
print("Selisih: ", b - a)

# 9 Menghitung populasi di Dunia
print("----------POPULASI CONTINENTS & WORLD----------")
Asia = 4679661000
Eropa = 1373486000
Afrika = 747747000
Amerika_Selatan = 659744000
Amerika_Utara = 371108000
Australia = 43220000
Antartika = 5000

a = Asia
b = Eropa
c = Afrika
d = Amerika_Selatan
e = Amerika_Utara
f = Australia
g = Antartika

print("Populasi Bumi : ", a + b + c + d + e + f + g)
print("Benua dengan populasi tertinggi hingga kebawah, yaitu: ")
print("1. Asia:", a)
print("2. Eropa:", b)
print("3. Afrika:", c)
print("4. Amerika Selatan:", d)
print("5. Amerika Utara:", e)
print("6. Australia:", f)
print("7. Antartika:", g)


# 14 Parents
print("---------------UNIT TESTING--------------")


class parent:
    def __init__(self, hair, height):  # _INIT_ (INITIALIZATION)
        self.hair = hair
        self.height = height

    def parentmethod():
        print("This is parent method")


print("-----------------------------")


# 14.1 Childs
class child(parent):
    def __init__(self, hair, height):
        parent.__init__(self, hair, height)

    def childmethod(self):
        print("This is a child method")


Anna = child("Brown", "tall")
print(Anna.childmethod())
# 15 Example - plotting histogram using matplotib
print("---------------EXAMPLE--------------")
import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
print(a)
b = np.ones(2)
print(b)
# 15.1 Sort -> Ngesort number dari yang terkecil hingga ke besar
print("---------------SORT--------------")
c = np.array([2, 5, 7, 3, 5, 8, 1, 0, 9, 4])
print("data c sebelum di sort:", c)
print("data c sesudah di sort:", np.sort(c))
print("\n")

# 15.2 Concatenate -> Menggabungkan 2 list jadi satu
print("---------------CONCATENATE--------------")
d = np.array([2, 3, 4, 5])
e = np.array([6, 7, 8, 9])
f = np.concatenate((d, e))
print("array d:", d)
print("array e:", e)
print("Hasil gabungan dari array d dan e:", f)
# 15.3 Shape -> Ada berapa kolom dan ada berapa baris dalam suatu array
print("---------------SHAPE--------------")
array_example = np.array(
    [
        [
            [0, 1, 2, 3, 4, 5, 6],
            [7, 8, 9, 10, 11, 12, 13],
            [0, 1, 2, 3, 4, 5, 6],
            [7, 8, 9, 10, 11, 12, 13],
            [0, 1, 2, 3, 4, 5, 6],
            [7, 8, 9, 10, 11, 12, 13],
        ]
    ]
)
print(array_example.shape)
# 15.4 Size -> Kita ingin tahu jumlah total angka di dalam array
print("---------------SIZE--------------")
print(array_example.size)
# 15.5 Reshape -> Shape baru kepada array tanpa mengganti
"""
print("---------------RE-SHAPE--------------")
array_example_2 = array_example.reshape(1,2)
print(array_example_2)
"""
# 15.6
print("---------------RE-EXAMPLE--------------")
a = np.array([1, 2, 3, 4, 5, 6])
print(a)
b = np.zeros(3)
print(b)
# 15.7 Sort -> Ngesort number dari yang terkecil hingga ke besar
c = np.array([2, 5, 7, 3, 5, 8, 1, 0, 9, 4])
# 15.8 Index ->
d = c[9]
print(d)
# 15.9 Reshaphe
"""
#15.10 Array 1 = array 2 sama jumlah angkanya, susunanya beda
reshape_array_1 = [[1,4],
                    [2,5],
                    [3,6]] # 1 list, 3 baris, 2 kolom (1 x 3 x 2)
reshape_array_2 = reshape_array_1.shape(1,2)
print(reshape_array_2)
"""


# 22
import numpy as np

num1 = np.array([00, 123, 456, 789, 101])
num2 = np.array([00, 988, 765, 432, 1010])
num1 + num2
print("result :", num1 + num2)
print("result :", num1 - num2)
print("result :", num1 * num2)
print("result :", num1 / num2)
print("result :", num1**num2)
print("result :", num1 // num2)
print("result :", num1 % num2)
print("result :", num1 is num2)
print("result :", num1 is not num2)
print("result :", num1 < num2)
print("result :", num1 > num2)
print("result :", num1 <= num2)
print("result :", num1 >= num2)
print("result :", num1 == num2)
print("result :", num1 != num2)

# 23
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2.0, 0.01)
s1 = 1 + np.sin(2 * np.pi * t)  # sinus
s2 = 0.5 + 0.5 * t  # garis lurus
fig, ax = plt.subplots()
ax.plot(t, s1, "r-", t, s2, "b:")
ax.set(xlabel="waktu t(s)", ylabel="tegangan (mV)", title="plot dua fungsi")
ax.grid()
ax.legend(["s1 = 1 + sin(2*pi*t)", "s2 = 0.5 + 0.5 * t"])
fig.savefig("test.png")
plt.show()


# 24
def modulus(num1, num2):
    result = num1 % num2
    return result


print("Hasil dari 10 % 3 adalah", modulus(10, 3))


# 25
class Monarch:
    def __init__(self, class_name, job):
        self.class_name = class_name
        self.job = job


class Shadow_Monarch(Monarch):
    pass


SungJinWoo = Monarch("Sung Jin Woo", "Monarch")
Shadow = Shadow_Monarch("Shadow", "Monarch")

print(SungJinWoo.class_name)
print(Shadow.class_name)


# 25.1
class human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(f"My name is {self.name} and my age {self.age} years")


class male(human):
    pass


class female(human):
    pass


print1 = human("Heracles", 20)
print1.intro()

print2 = male("Zeus", 70)
print2.intro()

print2 = female("Kratos", 40)
print2.intro()

# 26

# import unittest as ut

# def do_stuff(num):
#     return num + 5

# class TestMain(ut.TestCase):
#     def test_do_stuff(self):
#         test_param = 10
#         result = do_stuff(test_param)
#         self.assertEqual(result, 15)

# ut.main()

# 26.1
import unittest


# symbols = [('M', 1000), ('C M', 900), ('D', 500), ('C D', 400), ('C', 100), ('X C', 90), ('L', 50), ('X L', 40), ('X', 10), ('I X', 9), ('V', 5), ('I V', 4), ('I', 1)]

# def romannumeral(number):
#     while number > 0:
#         for symbol, value in symbols:
#             if number - value >= 0:
#                 print symbol,
#                 number = number - value
#                 continue

# number_in = raw_input("Enter a number: ")
# romannumeral(int(number_in))


symbols = [
    ("M", 1000),
    ("CM", 900),
    ("D", 500),
    ("CD", 400),
    ("C", 100),
    ("XC", 90),
    ("L", 50),
    ("XL", 40),
    ("X", 10),
    ("IX", 9),
    ("V", 5),
    ("IV", 4),
    ("I", 1),
]


def romannumeral(number):
    outstring = ""
    while number > 0:
        for symbol, value in symbols:
            if number - value >= 0:
                outstring += symbol
                number = number - value
                continue
    return outstring


class Test(unittest.TestCase):
    def test_9(self):
        self.assertEqual(romannumeral(9), "IX")

    def test_29(self):
        self.assertEqual(romannumeral(29), "XXIX")

    def test_707(self):
        self.assertEqual(romannumeral(707), "DCCVII")

    def test_1800(self):
        self.assertEqual(romannumeral(1800), "MDCCC")


# if __name__ == '__main__':
#     number_in = raw_input("Enter a number: ")
#     romannumeral(int(number_in))


# 27
class Family:
    being = "The Gods"
    being1 = "Goddessess"

    def __init__(self, name, somebody, age):
        self.name = name
        self.somebody = somebody
        self.age = age
        being = "The Gods"
        being1 = "Goddessess"


class Father(Family):
    def __init__(self, name, somebody, age, job):
        super().__init__(name, somebody, age)
        self.job = job

    def myFather(self):
        print("----------Profil The Father----------\n")
        print(
            f"My {self.somebody}`s name is",
            self.name,
            "he is",
            self.age,
            "years old",
            "and works as a",
            self.job,
            "\n",
        )


class Mother(Family):
    def __init__(self, name, somebody, age, job):
        super().__init__(name, somebody, age)
        self.job = job

    def myMother(self):
        print("----------Profil The Mother----------\n")
        print(
            f"My {self.somebody}`s name is",
            self.name,
            "she is",
            self.age,
            "years old",
            "and works as a",
            self.job,
            "\n",
        )


class Brother(Family):
    def __init__(self, name, somebody, age, job):
        super().__init__(name, somebody, age)
        self.job = job

    def myBrother(self):
        print("----------Profil The Brother----------\n")
        print(
            f"My {self.somebody}`s name is",
            self.name,
            "he is",
            self.age,
            "years old",
            "and works as a",
            self.job,
            "\n",
        )


class Sister(Family):
    def __init__(self, name, somebody, age, job):
        super().__init__(name, somebody, age)
        self.job = job

    def mySister(self):
        print("----------Profil The Sister----------\n")
        print(
            f"My {self.somebody}`s name is",
            self.name,
            "she is",
            self.age,
            "years old",
            "and works as a",
            self.job,
            "\n",
        )


father = Father("Zeus", "Father", 45, "God of sky and thunder")
mother = Mother("Hera", "Mother", 40, "Goddess of marriage")
brother = Brother(
    "Hephaestus",
    "Brother",
    20,
    "god of technology,"
    " blacksmiths, craftsmen, sculptors, metals, metallurgy,"
    " fire and volcanoes",
)
sister = Sister("Angelos", "Sister", 18, "Goddess chthonic")

father.myFather(), print(Family.being, "\n")
mother.myMother(), print(Family.being1, "\n")
brother.myBrother(), print(Family.being, "\n")
sister.mySister(), print(Family.being1, "\n")


# 29
import numpy as np

# data ke1 == list, data ke2 == baris,data ke3 == kolom
arr = np.zeros([1, 23, 22])
arr1 = np.ones([1, 23, 22])
result = arr != arr1
# print(arr)
print(f"==========================================================================")
print(f"                              Matrix")
# print(arr1)
print(f"==========================================================================")
print(f"zeros != ones =: ")
print(result)

# 30
# Combinated area rentang than number
inputNum = float(input("input the number \nless than 3 \nor \nmore than 10\n:"))
# ++++++++++3----------
numArea1 = inputNum < 3
print(f"The number less than 3\n: {numArea1}")
# ----------10++++++++++
numArea2 = inputNum > 10
print(f"The number more than 10\n: {numArea2}")
# +++++3----------10+++++
numCorrect = numArea1 or numArea2
print(f"Number the ur input is: {numCorrect}")

print("======================")
# Combinated area rentang than number
inputNum = float(input("input the number \nmore than 3 \nand \nless than 10\n: "))
# ----------3++++++++++
numArea1 = inputNum > 3
print(f"The number more than 3\n: {numArea1}")
# ++++++++++10----------
numArea2 = inputNum < 10
print(f"The number less than 10\n: {numArea2}")
# -----3++++++++++10-----
numCorrect = numArea1 and numArea2
print(f"Number the ur input is: {numCorrect}")


# 31
def get(x=[], index=0):
    return x[index]


num = [1, 2, 3, 4, 5, 6]
print(get(num, 5))

# 32
# For loop
data = input("Masukkan data anything: ")

for d in data:
    print(d)

print(f"=================")

number = input("masukkan angka:")

if int(number) < 10:
    print("Yeahhh its good bro!")

elif int(number) < 100:
    print("Emm its oke")

else:
    print("Dont touch the keyboard dude!!")


# 33
class Olympus:
    race = "God"

    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position
        race = "God"

    def execution(self):
        print(
            f"Namanya adalah {self.name}",
            "yang berumur",
            self.age,
            "tahun",
            "dan menempati posisi sebagai",
            self.position,
        )


e1 = Olympus("Zeus", 45, "Raja ara Dewa")
e2 = Olympus("Hera", 40, "Dewi Pernikahan")
e3 = Olympus("Heracles", 20, "Pahlawan terbesar Yunani")

e1.execution()
e2.execution()
e3.execution()

# 34 Pythonic Indonesia Belajar
mylist = [1, 2, 3]
for i in range(len(mylist)):
    print(f"{mylist[i]}")
print("\n")
for a in mylist:
    print(f"{a}")


def four():
    print("empat-four")


def five():
    print("lima-five")


case = "six"
switch = {
    "four": four,
    "five": five,
}
switch[case]()


a = -1
b = "negatif" if a < 0 else "positif"
print(f"{a} bernilai {b}")

for a in range(22):
    print("Hello World")

mylist = [1, 2, 3]
dest = 1
if dest in mylist:
    print("ditemukan")
else:
    print("tidak ditemukan")


def myfunction():
    name = "dani"
    nis = "007"
    return name, nis


a, b = myfunction()
print(f"name : {a}")
print(f"nis : {b}")


name = ["dani", "hendra"]
nis = ["007", "006"]
siswa = list(zip(nis, name))
print(f"siswa : {siswa}")


siswa = [("007", "dani"), ("006", "hendra")]
nis, name = zip(*siswa)
print(f"nis : {nis}")
print(f"name : {name}")


mylist = [1, 1, 2, 1, 3, 3]
value = 1
amount = mylist.count(value)  # 0
# for item in mylist:
#     if item == value:
#         amount += 1
print(f"Ditemukan angka {value}", f"berjumlah {amount}, " f"di dalam {mylist}")


name = "Vengeance"
age = 17
print("Nama saya {0}, Usia saya {1}".format(name, age))
student = {
    "nis": "007",
    "name": "Scanvenger",
    "age": 18,
}
print("Nama saya {name}, Usia saya {age}".format(**student))


data1 = {"nis": "007", "name": "Vengeance"}
data2 = {"umur": 17, "nilai rata2": 90.0}
siswa = {**data1, **data2}
print(f"siswa: {siswa}")


kecepatan = [10, 20, 30]
bataskecepatan = 30
# lajunorm = True
for laju in kecepatan:
    if laju > bataskecepatan:
        lajunorm = False
        print("Jangan kebut-kebut oeyyyy!!!")
        break
# if lajunorm:
else:
    print("alon-alon asal kelakon...")


gaji = 100_000_000
print(f"gaji : {gaji}")


# 'aieo'
# '4130'
source = "aieo"
dest = "4130"
str_in = "kota sidoarjo"
str_out = ""
transtation_tabel = str.maketrans(source, dest)
str_out = str_in.translate(transtation_tabel)
# translasi = {
#     'a': '4',
#     'i': '1',
#     'e': '3',
#     'o': '0'
# }
# for x in str_in:
#     val = translasi.get(x)
#     str_out += val if val else x
print(f"convertion value: {str_out}")


def custom_key(name):
    return name.split()[-1]


student = ["Dhani Syafreal", "Mahendra Wisnu", "Dsreal Python"]
print(f"sebelum terurut: {student}")
# for i in range(len(student)-1):
#     for j in range(i+1, len(student)):
#         if student[i].split()[-1] > student[j].split()[-1]:
#             student[i], student[j] = student[j], student[i]
ordinal = sorted(student, key=custom_key)
## ordinal = sorted(student, key=lambda x: x.split()[-1])
print(f"sesudah terurut: {ordinal}")


def cetaknama(fname, lname):
    print(f"{fname} {lname}")


cetaknama("Dhani", "Syafreal")
cetaknama(fname="Dhani", lname="Syafreal")
cetaknama(lname="Syafreal", fname="Dhani")


def jumlahkan(p_satu, p_dua):
    return p_satu + p_dua


mylist = [10, 20]
# list_value = jumlahkan(mylist[0], mylist[1])
list_value = jumlahkan(*mylist)
print(f"list_value: {list_value}")

mydict = {"p_satu": 100, "p_dua": 200}
# dict_value = jumlahkan(mydict['p_satu'], mydict['p_dua'])
dict_value = jumlahkan(**mydict)
print(f"dict_value: {dict_value}")

x = " Bahasa Pemrograman Python: Guido Van RoSSum "
print(f"x: {x}")
y = x.strip().upper().replace(":", ";")
# .lower berfungsi untuk mengecilkan seluruh alfabet yg di tunjuk
print(f"y: {y}")


def salam(name, message=""):
    print(f"Hai {name}! {message}")


salam("Dhani", "Good Luck!!")
salam("Bejo")


set1 = {1, 2, 3}
set2 = {2, 3, 4}
union_set = set1.union(set2)
print(union_set)


import pandas as pd

dict = {
    "subdistrict": ["Tanggulangin", "Tulangan", "Buduran"],
    "Population": [201115, 102339, 99710],
    "Male": [
        45097,
        51423,
        49710,
    ],
    "Female": [44707, 50916, 49000],
}

df = pd.DataFrame(dict)

print(df)
print(df.dtypes)

df = df.astype({"Population": "float", "Male": "float", "Female": "float"})
print(df)
print(df.dtypes)

# df.apply(pd.to_numeric, errors='Missing value')
# print(df)


# df = pd.read_excel("../input/datasmart2/Data smk kksi.xlsx", sheet_name="Daftar Peserta Didik")
# pd.set_option('display.max_rows', df.shape[0]+1)
# df


# sns.set()
# sns.relplot(x="Date",
#             y="PPDB",
#             ci="sd",
#             kind="line",
#             data=df
#            );

for i in range(1, 3):
    for j in range(1, 2):
        print()

lis = ["Arinal\n", "Ardi\n", "Dhani\n", "Dhimas\n", "Nawal\n", "Septian\n"]

for i in lis:
    print(i * 5)


"""
strsaya = input("Masukkan nama : ")
strsaya = len(strsaya)
print("Panjang string : {} huruf".format(strsaya))

halo = "Halo, dunia!"
index = halo.count("a")
print("jumlah huruf a : {}".format(index))

kalimat = input("Masukkan kalimat : ")
kalimat = kalimat.upper()
print(kalimat)

kal1 = input("Masukkan kalimat1 : ")
kal2 = input("Masukkan kalimat2 : ")
kal1 = len(kal1)
kal2 = len(kal2)
if kal1 == kal2:
    print("Panjang kalimat sama!")
elif kal1 != kal2:
    print("Panjang kalimat tidak sama!")
else:
    ("Error!")

a = "Python adalah Bahasa pemrograman yang powerfull."
print("Karakter ganjil : ",a[1::2])
"""
# Inisialisasi harga es kopyor dan siomay
harga_es_kopyor = 10000
harga_siomay = 8000

# Menampilkan menu kepada pengguna
print("Selamat datang di Market Place!")
print("Menu:")
print("1. Es Kopyor - Rp. 10,000")
print("2. Siomay - Rp. 8,000")

# Meminta pengguna memasukkan pilihan
pilihan = input("Pilih menu (1/2): ")

# Menggunakan if-else untuk menentukan pilihan pengguna
if pilihan == "1":
    jumlah_es_kopyor = int(input("Berapa es kopyor yang ingin Anda beli: "))
    total_harga = jumlah_es_kopyor * harga_es_kopyor
    print(f"Total harga untuk {jumlah_es_kopyor} es kopyor adalah Rp. {total_harga}")
elif pilihan == "2":
    jumlah_siomay = int(input("Berapa siomay yang ingin Anda beli: "))
    total_harga = jumlah_siomay * harga_siomay
    print(f"Total harga untuk {jumlah_siomay} siomay adalah Rp. {total_harga}")
else:
    print("Pilihan tidak valid. Silakan pilih menu 1 atau 2.")

    print("Terima kasih telah berbelanja di Market Place!")

# Mencetak sederhana dengan berurutan
print("AKU BELAJAR PYTHON")
print("DENGAN PENUH SEMANGAT!")
print("\n")


# Pengambilan Keputusan dengan Percabangan
ipkMhSiswa = 4.00
if ipkMhSiswa == 4.00:
    print("Amat Baik")
elif ipkMhSiswa <= 4.00:
    print("Baik")
elif ipkMhSiswa <= 3.00:
    print("Cukup")
else:
    print("Kurang")
print("\n")


# Struktur Perulangan
for i in range(5):
    spasi = " " * (5 - i)
    bintang = "*" * (2 * i + 1)
    print(spasi, bintang)


# Struktur Fungsi
# Panjang, Tinggi, Lebar Sisi balok
def menghitung_luas_balok(p, l, t):
    luas = p * l * t
    return luas


p = 10
l = 5
t = 4
print("Luas Persegi balok : ", menghitung_luas_balok(p, l, t))
print("\n")


"""
def menghitung_perkalian(angka):
    hasil = angka*angka
    return hasil

angka = 4
print("Hasil perkalian",angka,"adalah",menghitung_perkalian(angka))
"""

"""def hitungTotalUang(hargaPasar, jumlahMagis):
    return hargaPasar * jumlahMagis


hargaPasar = int(input("hargaPasar = "))
jumlahMagis = int(input("jumlahMagis = "))

hasil = hitungTotalUang(hargaPasar, jumlahMagis)
print(f'Rp.{hasil}')

"""


def levelMax(level, kekuatanMonster):
    return level - min(kekuatanMonster)


level = int(input("level = "))
level = level**2
kekuatanMonster = [100, 50, 20, 500, 10]

hasil = levelMax(level, kekuatanMonster)
print(hasil)
