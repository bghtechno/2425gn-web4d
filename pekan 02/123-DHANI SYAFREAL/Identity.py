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

# 2 Casting dan Type Data
print("----------INTEGER----------")
data_int = 10
# menyatakan bilangan bulat
data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)  # akan false bila int bernilai nol(0)
print("Data =", data_int, ",type =", type(data_int))
print("Data =", data_float, ",type =", type(data_float))
print("Data =", data_str, ",type =", type(data_str))
print("Data =", data_bool, ",type =", type(data_bool), ("\n"))

# 2.1 Casting dan Type Data
print("----------FLOAT----------")
data_float = 10.8
# menyatakan bilangan yang mempunyai koma
data_int = int(data_float)  # akan dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float)  # akan false bila float bernilai nol(0)
print("Data =", data_float, ",type =", type(data_float))
print("Data =", data_int, ",type =", type(data_int))
print("Data =", data_str, ",type =", type(data_str))
print("Data =", data_bool, ",type =", type(data_bool), ("\n"))

# 2.2 Casting dan Type Data
print("----------STRING----------")
data_str = 10
# menyatakan karakter/kalimat bisa berupa huruf, angka dll (diapit tanda " atau ')
data_int = int(data_str)  # akan dibulatkan ke bawah
data_float = float(data_str)  # akan false bila float bernilai nol(0)
data_bool = bool(data_str)
print("Data =", data_str, ",type =", type(data_str))
print("Data =", data_int, ",type =", type(data_int))
print("Data =", data_float, ",type =", type(data_float))
print("Data =", data_bool, ",type =", type(data_bool), ("\n"))

# 2.3 Casting dan Type Data
print("----------BOOLEAN----------")
data_bool = True
# menyatakan benar True yang bernilai 1, atau salah False yang bernilai 0
data_int = int(data_bool)  # akan dibulatkan ke bawah
data_float = float(data_bool)
data_str = bool(
    data_bool
)  # akan false bila bool bernilai nol(0) dan true bila bool bernilai selain nol
print("Data =", data_bool, ",type =", type(data_bool))
print("Data =", data_int, ",type =", type(data_int))
print("Data =", data_float, ",type =", type(data_float))
print("Data =", data_str, ",type =", type(data_str), ("\n"))

# 2.4 Type Data
print("----------List----------")
data_list = ["x", 1, "y", 11]
# menggunakan brackets[],
# data untaian yang menyimpan berbagai tipe data dan isinya bisa berubah-ubah
print(f"data = {data_list} -> type = {type(data_list)}\n")

# 2.5 Type Data
print("----------Tuple----------")
data_tuple = ("x", 1, "y", 11)
# menggunakan parentheses(),
# data untaian yang menyimpan berbagai tipe data dan isinya tidak bisa diubah
print(f"data = {data_tuple} -> type = {type(data_tuple)}\n")

# 2.6 Type Data
print("----------Complex----------")
data_complex = 100j
# menyatakan pasangan angka real dan imajiner
print(f"data = {data_complex} -> type = {type(data_complex)}\n")

# 2.7 Type Data
print("----------Range----------")
data_range = range(1, 11, 111)
# hanya berisi bilangan bulat(integer(int))
print(f"data = {data_range} -> type = {type(data_range)}\n")

# 2.8 Type Data
print("----------Dictionary----------")
data_dictionary = {"name": "Bill", "age": 20}
print(f"data = {data_dictionary} -> type = {type(data_dictionary)}\n")

# 2.9 Type Data
print("----------Set----------")
data_set = {11, "z", 1.1, "a", 1.11}
print(f"data = {data_set} -> type = {type(data_set)}\n")

# 2.1.0 Type Data
print("----------Frozenset----------")
data_frozenset = frozenset({11, "z", 1.1, "a", 1.11})
print(f"data = {data_frozenset} -> type = {type(data_frozenset)}\n")

# 2.1.1 Type Data
print("----------Bytes----------")
data_bytes = b"Hello World"
print(f"data = {data_bytes} -> type = {type(data_bytes)}\n")

# 2.1.2 Type Data
print("----------Bytearray----------")
data_bytearray = bytearray(5)
print(f"data = {data_bytearray} -> type = {type(data_bytearray)}\n")

# 2.1.3 Type Data
print("----------Memoryview----------")
data_memoryview = memoryview(bytes(5))
print(f"data = {data_memoryview} -> type = {type(data_memoryview)}\n")

# Numbers, string, boolean
a = 10
print(a, "bertipe", type(a))
b = 1.7
print(b, "bertipe", type(b))
c = 1 + 2j
print(c, " Bertipe bilangan kompleks? ", isinstance(1 + 2j, complex))

#
x = [0] * 10005
# inisialisasi array 0 sebanyak 10005; x[0]=0
x[1] = 1
# x[1]=1

for j in range(2, 10001):
    x[j] = x[j - 1] + x[j - 2]  # Fibonacci
print(x[10000])

#
b = 0.1234567890123456789
print(b)

a = 1234567890123456789
print(a)

c = 1 + 5j
print(c)

s = """Ini adalah string
yang memiliki baris pertama
dan selanjutnya baris kedua"""

# List
x = [5, 10, 15, 20, 25, 30, 35, 40]
print(x[5])
print(x[-1])
print(x[3:5])
print(x[:5])
print(x[-3:])
print(x[1:7:2])

x = [1, 2, 3]
x[2] = 4
print(x)

x = [1, 2, 3]
x[2] = 4
x.append(5)
print(x)

binatang = ["kucing", "rusa", "badak", "gajah"]
del binatang[2]
print(binatang)

list1 = ["Dhani", 123, "Syafreal", 231, 321]

# print(list1)

# print(list1[2])

jumlList1 = len(list1)
# print(jumlList1)

for i in list1:
    print(i)

x = [1, 2, 3]
x[2] = 4
x.append(5)
print(x)

iterasi = 0
for i in range(len(list1)):
    print("Nomor", iterasi, "ke-", i)
    iterasi += 1

genap = []
ganjil = []

num = 20
for i in range(num + 1):
    if i % 2 == 0:
        genap.append(i)
    elif i % 2 == 1:
        ganjil.append(i)

print(genap)
print(ganjil)

# Slicing
s = "Hello World!"
print(s[4])  # ambil karakter kelima dari string s
print(s[6:11])  # ambil karakter ketujuh hingga sebelas dari string s
s[5] = (
    "d"  # ubah karakter keenam dari string s menjadi "d", seharusnya gagal karena immutable
)
s = "Halo Dunia!"  # ubah isi string s menjadi "Halo Dunia!", seharusnya berhasil karena mutable
print(s)

# Tuple (tuple tidak dapat melakukan perubahan)
t = (5, "program", 1 + 3j)
print(t[1])
print(t[0:3])
# print(t[0]=10)

# Set (Unordered)
a = {1, 2, 2, 3, 3, 3}
print(a)
# Karena set bersifat unordered,
# maka kita tidak bisa mengambil sebagian data /
# elemen datanya menggunakan proses slicing
a = {1, 2, 3}
print(a[1])

# Dictionary
d = {1: "value", "key": 2}
print(type(d))

d = {1: "value", "key": 2}
print(type(d))
print("d[1] = ", d[1])
print("d['key'] = ", d["key"])

# Stack
"""
stack() inisialisasi stack yang kosong
push(data) penambahan data baru pada stack di posisi top
pop() menghapus data pada stak di posisi top
peek() informasi data uang terletak pada posisi top
isEmpty() untuk memeriksa apakah stack dalam keadaan kosong
size() informasi jumlah data yang terdapat pada stack
"""


def stack():
    s = []
    return s


def push(s, data):
    s.append(data)


def pop(s):
    data = s.pop()
    return data


def peek(s):
    # return (s[Len(s)-1])
    return s[-1]


def isEmpty(s):
    return s == []


def size(s):
    return len(s)


data = stack()
print(data)

# coba bikin code untuk membalik kata (reversing word)

a = "dhani"
hasil = ""
for i in range(len(a) - 1, -1, -1, -1, -1):
    print(a)
    hasil = hasil + a[i]

print(hasil)

# aku = stack("dhani")

# “if it walks like a duck and it quacks like a duck,
# then it must be a duck”
# (Jika sesuatu berjalan seperti bebek dan bersuara seperti bebek,
# maka kemungkinan besar ia adalah bebek).
10  #
print("----------INTRODUCTION----------")
nama = "Dhani Syafreal"
kelas = "XI-TKJ 1"
absen = 31

a = nama
b = kelas
c = absen

print("Profil:", a, b, c)

# %s string, %d integer, %f desimal
# %.<digit>f - Bilangan desimal dengan sejumlah digit angka dibelakang koma.
# %x/%X - Bilangan bulat dalam representasi Hexa (huruf kecil/huruf besar)
nama = "Dhani"
tglahir = "5 Okt"
tahun = 2004.7324582
print("Nama saya %s, lahir %s %s" % (nama, tglahir, int(tahun)))

c, a = 10, 11
print("10: %X and 11: %x" % (a, c))

# Input ()
value = input("ketik angka: ")
print(value)

# 16 input user
print("----------Input----------")
a = input("jumlah: ")
if int(a) < 50:
    print("Sampah")
elif int(a) < 100:
    print("Monoton")
else:
    print("Fantastis")

# 17 Type data
print("----------Input Data----------")
data_int = int(input("masukkan data :"))  # data yang dimaksukkan pasti str(string)
print("data =", data_int, ",type :", type(data_int))
data_float = float(input("masukkan data :"))
print("data :", data_float, ",type :", type(data_float))
data_str = str(input("masukkan data :"))
print("data :", data_str, ",type :", type(data_str))
# 17.1
data_bool = bool(int(input("masukkan data :")))
print("data :", data_bool, ",type :", type(data_bool))

# 18 #Class/Kelas bisa kita sebut juga Blueprint/Cetakan
name = input("my name: ")

hobby = input("my hobby: ")

yob = input("year of birth: ")
yob = int(yob)

age = 2021 - yob

thx = "Thank you"
# 18.1 #Object/Instance
print(
    "\n" "My name is",
    name,
    "and my hobby is",
    hobby,
    ",",
    "I was born in",
    yob,
    "and my age is",
    age,
)
print(thx)

# Command line argument
import sys

print("Ada", len(sys.argv), "argumen")
print("List argumen:", str(sys.argv))
print("index 1", sys.argv[0])

# 13 RANDOM
print("----------INPUT RANDOM----------")
data = input("Input angka: ")
if int(data) < 10:
    print("U  G L Y   B A S T A R D !!!")
elif int(data) < 100:
    print("S H U T   U P !!!")
elif int(data) < 1000:
    print("S I T I   M A R K O N A !!!")
else:
    print("W H A T   T H E   F U C K !!!")

# Transformasi int, char, str
# Upper() & lower()
x = "aku adalah anak sehat"
print(len(x))
x = x.upper()
print(x)
x = x.lower()
print(x)

# Awalan dan Akhiran
# strip()=kanan-kiri
# rstrip()=kanan
# lstrip()=kiri
kata = "CodeCodeDicodingCodeCode"
print(kata.strip("Code"))

# startswith() & endswith()
print("Dicoding Indonesia".startswith("Dicoding"))
print("Dicoding Indonesia".endswith("Indonesia"))

# Memisah dan menggabung string
# Join()
print(" ".join(["Dicoding", "Indonesia", "!"]))
print("123".join(["Dicoding", "Indonesia", "!"]))

# Split()
print("Dicoding Indonesia !".split())
print("Dicoding123Indonesia123!".split("123"))
print(
    """Halo,
aku ikan,
aku suka sekali menyelam
aku tinggal di perairan.
Badanku licin dan renangku cepat.
Senang berkenalan denganmu.""".split(
        "\n"
    )
)

# Mengganti elemen string
# replace()
string = "Ayo belajar Coding di Dicoding"
print(string.replace("Coding", "Pemrograman"))

string = "Ayo belajar Coding di Dicoding karena Coding adalah bahasa masa depan"
print(string.replace("Coding", "Pemrograman", 1))

# Pengecekan String
# isupper(), islower(), isalpha(), isalnum(),
# isdecimal(), isspace(), istitle()
kata = "DICODING"
kata.isupper()
kata = "Dicoding"
kata.isupper()

kata = "dicoding"
kata.islower()
kata = "Dicoding"
kata.islower()

print("Dicoding".upper().lower())  # Chain of Method
print("Dicoding".lower().upper())
print("DICODING".upper().lower().islower())
print("DICODING".upper().lower().isupper())

print("dicoding".isalpha())

print("dicoding123".isalnum())

"12345".isdecimal()

"    ".isspace()

"Dicoding Indonesia".istitle()

# Contoh Implementasi dari method "Pengecekan string"
while True:
    print("Masukkan nama Anda:")
    name = input()
    if name.isalpha():
        print("Halo", name)
        break
    print("Masukkan nama Anda dengan benar.")

# Formatting pada string, zfill()
# Penerapan zfill pada angka
# Contoh 1: Penggunaan zfill 5 pada angka satuan
angka = 5
print(str(angka).zfill(5))
# Contoh 2: Penggunaan zfill 5 pada angka ratusan
angka = 300
print(str(angka).zfill(5))
# Contoh 3: Penggunaan zfill 5 pada angka desimal negatif (memiliki koma)
angka = -0.45
print(str(angka).zfill(5))
# Contoh 4: Penggunaan zfill 7 pada angka desimal negatif (memiliki koma)
angka = -0.45
print(str(angka).zfill(7))

# Penerapan zfill pada string
# Contoh 1
kata = "aku"
print(kata.zfill(5))
# Contoh 2
kata = "kamu"
print(kata.zfill(5))
# Contoh 3
kata = "dirinya"
print(kata.zfill(5))

# Text potition, rjust(), ijust(), center()
"Dicoding".rjust(20)

"Dicoding".ljust(20)
"Dicoding".ljust(20, "!")

"Dicoding".center(20)

# String Literals
# st1 = 'Jum'at' #incorrect
st1 = "Jum'at"  # kurang efektif
print(st1)

st1 = "Jum'at"  #
# \' Single quote
# \" Double quote
# \t Tab
# \n Newline (line break)
# \\ Backslash
print("Halo!\nKapan terakhir kali kita bertemu?\nKita bertemu hari Jum'at yang lalu.")
multi_line = """Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum’at yang lalu."""
print(multi_line)

# Raw Strings
print(r"Dicoding\tIndonesia")  # Karena menggunakan raw str
# maka kalimat secara mentah tercetak

# Cara biasa
a = 2
a = a * 3
print(a)
# Cara efisien
a = 2
a *= 3
print(a)

a = "Hai " * 2
print(a)
a = ("Hai ") * 2  # tuple
print(a)
a = ["Hai "] * 2  # list
print(a)
# a = {"Hai "} * 2#dictionary =error
# print(a)

# 3 Assignment Operators
print("----------Assignment Operators----------")


def operasi():
    x = 5
    if x == 5:
        x += 5
        print(f"x = 5:\n x += 5\n  = {x}\n"),
        x = 5
        x -= 5
        print(f"x = 5:\n x -= 5\n  = {x}\n"),
        x = 5
        x *= 5
        print(f"x = 5:\n x *= 5\n  = {x}\n"),
        x = 5
        x /= 5
        print(f"x = 5:\n x /= 5\n  = {x}\n"),
        x = 5
        x %= 5
        print(f"x = 5:\n x %= 5\n  = {x}\n"),
        x = 5
        x //= 5
        print(f"x = 5:\n x //= 5\n  = {x}\n"),
        x = 5
        x **= 5
        print(f"x = 5:\n x **= 5\n  = {x}\n"),
        x = 5
        x &= 5
        print(f"x = 5:\n x &= 5\n  = {x}\n"),
        x = 5
        x |= 5
        print(f"x = 5:\n x |= 5\n  = {x}\n"),
        x = 5
        x ^= 5
        print(f"x = 5:\n x ^= 5\n  = {x}\n"),
        x = 5
        x <<= 5
        print(f"x = 5:\n x <<= 5\n  = {x}\n"),
        x = 5
        x >>= 5
        print(f"x = 5:\n x >>= 5\n  = {x}\n"),
        return True


print(operasi())

# 11 operasi aritmatika
print("----------OPERASI ARITMATIKA----------")
a = 11
b = 4
# operasi penambahan +
hasil = a + b
print(a, "+", b, "=", hasil)
# operasi pengurangan -
hasil = a - b
print(a, "-", b, "=", hasil)
# operasi perkalian *
hasil = a * b
print(a, "*", b, "=", hasil)
# operasi pembagian /
hasil = a / b
print(a, "/", b, "=", hasil)
# operasi eksponen (pangkat) **
hasil = a**b  # pemangkatan contoh(2 pangkat 3)
# tips: untuk akar dua, gunakan pangkat 0.5.
print(a, "**", b, "=", hasil)
# operasi floor division //
hasil = a // b  # membulatkan kebawah dari hasil pembagian(/)
print(a, "//", b, "=", hasil)
# operasi modulus %
hasil = a % b  # sisa pembagian
print(a, "%", b, "=", hasil)

# 11.1 calculate
print("----------CALCULATE----------")


class calculate:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def plus(self):
        print(
            f"result of {self.num1}",
            "+",
            self.num2,
            " +",
            self.num3,
            " : ",
            self.num1 + self.num2 + self.num3,
        )

    def minus(self):
        print(
            f"result of {self.num1}",
            "-",
            self.num2,
            " -",
            self.num3,
            " : ",
            self.num1 - self.num2 - self.num3,
        )

    def times(self):
        print(
            f"result of {self.num1}",
            "*",
            self.num2,
            " *",
            self.num3,
            " : ",
            self.num1 * self.num2 * self.num3,
        )

    def divide(self):
        print(
            f"result of {self.num1}",
            "/",
            self.num2,
            " /",
            self.num3,
            " : ",
            self.num1 / self.num2 / self.num3,
        )


calculate = calculate(5, 10, 4)
calculate.plus()
calculate.minus()
calculate.times()
calculate.divide()

# 12 prioritas operasi, operational precedence
print("----------PRIORITAS OPERASI----------")

# 1. ()
# 2. eksponen **
# 3. perkalian dan teman2nya *,**,/,//,%
# 4. penambahan dan pengurangan +,-

a = 2
b = 3
c = 4
hasil = a * b**c / b // a % b + c - b
print(a, "*", b, "**", c, "/", b, "//", a, "%", b, "+", c, "-", b, "=", hasil)
hasil = (a * b) ** c
print("(", a, "*", b, ")**", c, "=", hasil)
hasil = a - b + c * (b / a)
print(a, "-", b, "+", c, "*(", b, "/", a, ")=", hasil)

# 28
# Operasi logika atau boolean
# Tabel kebenaran
# NOT, OR, AND, XOR

# 12 = 1100, 6 = 0110
# bilangan 1 yang angkanya bertepatan dengan 1 menjadi 1,
# maka hasilnya 0100 (4)
a = 12 & 6
print(a)

# 12 = 1100, 3 = 0011
# bilangan 1 yang angkanya bertepatan dengan 1/0 menjadi 1,
# maka hasilnya 1111 (15)
a = 12 | 3
print(a)

# 12 = 1100, 6 = 0110
# bilangan yang angkanya bertepatan sama menjadi 0,
# maka hasilnya 1010
a = 12 ^ 6
print(a)

print("=====NOT=====")
x = True
y = not x  # Negasi x (not(~))
print(y)
print("----------")
x = False
y = not x  # Negasi x
print(y)

# Jika ada satu 'True', maka bernilai True (or(|))
print("=====OR=====")
x = True
y = True
z = x or y
print(x, "OR", y, "=", z)
x = True
y = False
z = x or y
print(x, "OR", y, "=", z)
x = False
y = True
z = x or y
print(x, "OR", y, "=", z)
x = False
y = False
z = x or y
print(x, "OR", y, "=", z)

# Jika ada satu 'False', maka bernilai False (and(&))
print("=====AND=====")
x = True
y = True
z = x and y
print(x, "AND", y, "=", z)
x = True
y = False
z = x and y
print(x, "AND", y, "=", z)
x = False
y = True
z = x and y
print(x, "AND", y, "=", z)
x = False
y = False
z = x and y
print(x, "AND", y, "=", z)

# jika nilai sama maka false dan sebaliknya (xor(^))
print("=====XOR=====")
x = True
y = True
z = x ^ y
print(x, "XOR", y, "=", z)
x = True
y = False
z = x ^ y
print(x, "XOR", y, "=", z)
x = False
y = True
z = x ^ y
print(x, "XOR", y, "=", z)
x = False
y = False
z = x ^ y
print(x, "XOR", y, "=", z)

# 19 Temprature Celcius
Celcius = float(input("Input the Celcius number:"))
print("Temprature:", Celcius, "°C")
# 19.1 Celcius ke Reamur -> R=(4/5)C
Reamur = (4 / 5) * Celcius
print("Temprature:", Reamur, "°R")
# 19.2 Celcius ke Fahrenheit -> F=(9/5)C + 32
Fahrenheit = ((9 / 5) * Celcius) + 32
print("Temprature:", Fahrenheit, "°F")
# 19.3 Celcius ke Kelvin -> K=(5/5)C + 273
Kelvin = ((5 / 5) * Celcius) + 273
print("Temprature:", Kelvin, "°K")
print("\n")
# 19.4 Temprature Reamur
Reamur = float(input("Input the Reamur number:"))
print("Temprature:", Reamur, "°R")
# 19.5 Reamur ke Celcius -> C=(5/4)R
Celcius = (5 / 4) * Reamur
print("Temprature:", Celcius, "°C")
# 19.6 Reamur ke Fahrenheit -> F=(9/4)R + 32
Fahrenheit = ((9 / 4) * Reamur) + 32
print("Temprature:", Fahrenheit, "°F")
# 19.7 Reamur ke Kelvin -> K=(5/4)R + 273
Kelvin = ((5 / 4) * Reamur) + 273
print("Temprature:", Kelvin, "°K")
print("\n")
# 19.8 Temprature Fahrenheit
Fahrenheit = float(input("Input the Fahrenheit number:"))
print("Temprature:", Fahrenheit, "°F")
# 19.9 Fahrenheit ke Celcius -> C=(5/9)F-32
Celcius = (5 / 9) * (Fahrenheit - 32)
print("Temprature:", Celcius, "°C")
# 19.1.0 Fahrenheit ke Reamur -> R=(4/9)F-32
Reamur = (4 / 9) * (Fahrenheit - 32)
print("Temprature:", Reamur, "°R")
# 19.1.1 Fahrenheit ke Kelvin -> K=((5/9)F-32) + 273
Kelvin = (5 / 9) * (Fahrenheit - 32) + 273
print("Temprature:", Kelvin, "°K")
print("\n")
# 19.1.2 Temprature Kelvin
Kelvin = float(input("Input the Kelvin number:"))
print("Temprature:", Kelvin, "°K")
# 19.1.3 Kelvin ke Celcius -> C=(5/5)K-372
Celcius = (5 / 5) * (Kelvin - 273)
print("Temprature:", Celcius, "°C")
# 19.1.4 Kelvin ke Reamur -> R=(4/5)K-273
Reamur = (4 / 5) * (Kelvin - 273)
print("Temprature:", Reamur, "°R")
# 19.1.5 Kelvin ke Fahrenheit -> K=((5/5)K-273) + 32
Fahrenheit = (9 / 5) * (Kelvin - 273) + 32
print("Temprature:", Fahrenheit, "°F")

# 20 str(string)
name = "Vengeance De Valens"
fake_number = "123456789"  # bukan int
print(name[0])  # mendapatkan value/nilai menggunakan index
print(name[0:9])  # bisa tanpa 0
print(name[10:19])  # bisa tanpa 19
print(name[0:19])  # bisa tanpa index 19 alias 0 saja atau tanpa index hanya colon(:)
print(fake_number[:])  # intinya hanya bisa digunakan pada str(string)
print(fake_number + ",", (name[0:9]))

# 21 Operasi Komparasi
x = 5
y = 10
# dibawah ini variabelnya (x,y) bisa diubah menjadi literal (angka)
# < (lebih kecil)
hasil = x < y
print(x, "<", y, "=", hasil)
# > (lebih besar)
hasil = x > y
print(x, ">", y, "=", hasil)
# <= (lebih kecil atau sama dengan)
hasil = x <= y
print(x, "<=", y, "=", hasil)
# >= (lebih besar atau sama dengan)
hasil = x >= y
print(x, ">=", y, "=", hasil)
# == (sama dengan atau kesetaraan)
hasil = x == y
print(x, "==", y, "=", hasil)
# != (tidak sama dengan)
hasil = x != y
print(x, "!=", y, "=", hasil)
# Note (<,>,<=,>=,==,!=) dapat bekerja pada syntax literal
# Note (is, is not) tidak efisien bila input nilai literal
# is (adalah) sebagai komparasi object identity
x = 5
y = 10
print("Data x:", x, "id:", hex(id(x)))
print("Data y:", y, "id:", hex(id(y)))
print(x is y)
# is not (bukan adalah)
print(x is not y)

# print(int('90+10')) #error
# eval()
print(eval("90+10"))  # success

# Operasi pada list, set & string
# Len()
contoh_list = [1, 3, 3, 5, 5, 5, 7, 7, 9]
print(contoh_list)
print(len(contoh_list))

contoh_set = set([1, 3, 3, 5, 5, 5, 7, 7, 9])
print(contoh_set)
print(len(contoh_set))

contoh_string = "Belajar Python"
print(contoh_string)
print(len(contoh_string))

# min() dan max()
angka = [13, 7, 24, 5, 96, 84, 71, 11, 38]
print(min(angka))
print(max(angka))

# count()
genap = [2, 4, 4, 6, 6, 6, 8, 10, 10]
print(genap.count(6))
string = "Belajar Python di Dicoding sangat menyenangkan"
substring = "a"
print(string.count(substring))

# Penggabungan dan replikasi
angka = [2, 4, 6, 8]
huruf = ["P", "Y", "T", "H", "O", "N"]
gabung = angka + huruf
print(gabung)

learn = ["P", "Y", "T", "H", "O", "N"]
replikasi = learn * 2
print(replikasi)

# Fungsi pengali juga dapat
# Anda manfaatkan untuk inisialisasi List.
tujuh = [7] * 7
print(len(tujuh))
print(tujuh)


# Operator in & not in
kalimat = "Belajar Python di Dicoding sangat menyenangkan"
print("Dicoding" in kalimat)
print("tidak" in kalimat)
print("Dicoding" not in kalimat)
print("tidak" not in kalimat)

# Memberikan value to multiple variable (list & tuple)
# tidak efisien
data = ["shirt", "white", "L"]
apparel = data[0]
color = data[1]
size = data[2]
# efisien (nb: jumlah variable & item harus sama)
data = ["shirt", "white", "L"]  # From List
apparel, color, size = data
data = ("shirt", "white", "L")  # From Tuple
apparel, color, size = data

# Penggunaan assignment pada multi variabel ini dapat
# Anda gunakan untuk menukar nilai dua atau lebih variabel
apparel, color = "shirt", "white"
apparel, color = color, apparel
print(apparel)
print(color)

# Sort()  #Mengurutkan int or str
# Metode sort tidak dapat mengurutkan list yang
# memiliki angka dan string sekaligus di dalamnya.
siswa = ["Mahendra Wisnu W", "Dhani Syafreal"]  # str
print("sebelum", siswa)
terurut = sorted(siswa)
print("sesudah", terurut)

angka = [100, 1000, 500, 200, 5]  # int
angka.sort()
print(angka)

kendaraan = ["motor", "mobil", "helikopter", "pesawat"]
kendaraan.sort()
print(kendaraan)

kendaraan = ["motor", "mobil", "helikopter", "pesawat"]
kendaraan.sort(reverse=True)  # reverse=True, untuk memperbalik urutan
print(kendaraan)

# Metode sort menggunakan urutan ASCII, sehingga nilai huruf kapital
# (uppercase) akan lebih dahulu dibandingkan huruf kecil (lowercase)
kendaraan = ["motor", "mobil", "helikopter", "Pesawat"]
kendaraan.sort()
print(kendaraan)
# Mengatasinya dapat menggunakan (key=str.lower)
# hal ini akan menganggap semua objek menggunakan huruf kecil
kendaraan = ["Motor", "Mobil", "helikopter", "pesawat"]
kendaraan.sort(key=str.lower)
print(kendaraan)

# (8421=1111)
# 2 adalah desimal dijadikan biner = __10
# geser ke kiri 2x menjadi __10 -> 10__ -> (8)
# ___ = _ _ _ _ (1 oktet berisi 4 angka biner(1/0))
a = 2 << 2
print(a)
# 9 dijadikan biner = 1001 (8+1)
# geser ke kanan 1x menjadi _100 (4)
a = 9 >> 1
print(a)

# Operator perbandingan (lt, gt, le, ge, eq, ne)
from operator import *

hijau = 5
kuning = 10
print("Kelereng Hijau = {}".format(hijau))
print("Kelereng Kuning = {}".format(kuning))
for func in (lt, le, eq, ne, ge, gt):
    print("{}(hijau, kuning): {}".format(func.__name__, func(hijau, kuning)))

# 6 Control flow
print("\n")
print("----------SEQUENTIIAL----------")
nilai1 = 234
nilai2 = 123
nilai3 = 543

print("Data: ", nilai3 + nilai2)

# 7 Control flow
print("----------DECISION----------")
data = [
    32,
    1,
    23,
    2,
    1,
    5,
    14,
    68,
    5,
    45,
    42,
    5,
    7,
    8,
    9,
    15,
    3,
    42,
    3,
    42,
    3,
    4,
    23,
    4,
    23,
    4,
    1,
    56,
    756,
    75,
    67,
    58,
    5,
    4,
    6,
    45,
    47,
    6,
    4,
    63,
    3,
    25,
    8,
    0,
    1,
    223,
    63,
    2,
    34,
    7,
    8,
]
if len(data) > 50:
    print("Oke data mencukupi: " + str(len(data)))
else:
    print("Eits datanya kurang")

# dinamisme Python
if False:
    (
        9 + "satu"
    )  # Baris ini tidak dioperasikan, sehingga tidak muncul notifikasi TypeError
else:
    9 + 1

# range()
# Fungsi range() memberikan deret bilangan dengan pola tertentu
# Fungsi range() dapat memiliki 1-3 parameter (n, p, q)
for i in range(5):  # 5=n
    print(i)

for i in range(1, 11):  # 1=n, 11=p
    print(i)

print([_ for _ in range(0, 20, 5)])  # 0=n, 20=p, 5=q

# Percabangan
# if, Python menganggap setiap nilai non-zero dan non-null
# sebagai True dan nilai zero/null sebagai False.
kelerengku = 10
if kelerengku:
    print("Cetak ini jika benar")
    print(kelerengku)

# else
tinggi_badan = int(input("Masukkan tinggi badan Anda : "))
if tinggi_badan >= 160:
    print("Silakan, Anda boleh masuk")
else:
    print("Maaf, Anda belum boleh masuk")

bilangan = 4
if bilangan % 2 == 0:
    print("Bilangan {} adalah genap".format(bilangan))
else:
    print("Bilangan {} adalah ganjil".format(bilangan))


# elif
nilai = int(input("Masukkan nilai tugas Anda : "))
if nilai > 80:
    print("Selamat! Anda mendapat nilai A")
    print("Pertahankan!")
elif nilai > 70:
    print("Hore! Anda mendapat nilai B")
    print("Tingkatkan!")
elif nilai > 60:
    print("Hmm.. Anda mendapat nilai C")
    print("Ayo semangat!")
else:
    print("Waduh, Anda mendapat nilai D")
    print("Yuk belajar lebih giat lagi!")


bilangan = -3
if bilangan > 0:
    print("Bilangan {} adalah positif".format(bilangan))
elif bilangan < 0:
    print("Bilangan {} adalah negatif".format(bilangan))
else:
    print("Bilangan {} adalah nol".format(bilangan))
# modify
bilangan = int(input("input angka : "))
if bilangan % 2 == 0:
    print("Bilangan {} adalah genap".format(bilangan))
else:
    print("Bilangan {} adalah ganjil".format(bilangan))


hasil = None
pesan = hasil or "Tidak ada data"
print(pesan)

# Perulangan
# for
for huruf in "Dicoding":  # Contoh pertama
    print("Huruf: {}".format(huruf))

flowers = ["mawar", "melati", "anggrek"]
for flower in flowers:  # Contoh kedua
    print("Flower: {}".format(flower))

# perulangan berdasarkan indeks atau range dengan memanfaatkan fungsi len():
flowers = ["mawar", "melati", "anggrek"]
for index in range(len(flowers)):
    print("Flowers: {}".format(flowers[index]))

# While, Python tidak memiliki do.. while statement
# reminder - True di Python termasuk semua nilai non-zero

count = 0
while count < 7:
    print("Hitungannya adalah: {}".format(count))
    count = count + 1

# infinit / infinite loop
var = 1
while var == 1:  # This constructs an infinite loop
    num = input("Masukkan angka: ")
    print("Anda memasukkan angka: {}".format(num))


while True:  # This constructs an infinite loop
    num = input("Masukkan angka: ")
    print("Anda memasukkan angka: {}".format(num))

# Perulangan(Loop) bertingkat
# Tambahkan parameter end pada print
# untuk mengatur karakter yang mengakhiri pencetakan string/teks Anda.
# Secara default, karakter end ini adalah newline ('\n').
for i in range(0, 6):
    for j in range(0, 6 - i):
        print("*", end="")
    print()

# Kontrol perulangan
# Break
for huruf in "Dico ding":
    if huruf == " ":
        break
    print("Huruf saat ini: {}".format(huruf))

#
for i in range(0, 10):
    for j in range(0, 10):
        if j > i:
            print()
            break
        else:
            print("*", end="")

# continue, mengabaikan pernyataan (statement)
# yang berada antara continue hingga akhir blok perulangan.
for huruf in "Dico ding":
    if huruf == " ":
        continue
    print("Huruf saat ini: {}".format(huruf))

# 1 loop dan 1 if (tanpa else)
jumlah_baris = 10
baris = 0
bintang = 0
while baris < jumlah_baris:
    if (bintang) >= (baris + 1):
        print()
        baris = baris + 1
        bintang = 0
        continue  # Saat masuk ke if, maka bagian print * diluar if tidak akan dijalankan, langsung ulang ke while
    print("*", end="")
    bintang = bintang + 1

# else setelah for
for item in items:
    if cari(item):
        # ditemukan!
        proses_item()
        break
else:
    # Item tidak ditemukan
    not_found_in_container()

# struktur pseudocode yang diikuti dalam membuat else pada perulangan
# if any(something_about(thing) for each thing in container):
#    do_something(that_thing)
# else:
#    no_such_thing()

# Contoh penggunaan dari for-else
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "equals", x, "*", n / x)
            break

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "equals", x, "*", n / x)
            break
    else:
        # loop fell through without finding a factor
        print(n, " adalah bilangan prima")

# Else setelah While
n = 10
while n > 0:
    n = n - 1
    if n == 7:
        break
    print(n)
else:
    print("Loop selesai")

# loop akan di break saat nilai n == 7
n = 10
while n > 0:
    n = n - 1
    print(n)
else:
    print("Loop selesai")

# Pass
def sebuahfungsi():
    pass


# Jika Anda mendeklarasi sebuah fungsi tanpa kode apapun, justru akan terjadi error
# def sebuahfungsi():

# Contoh pass untuk mengantisipasi exception/kegagalan fungsi
var1 = ""
while var1 != "exit":
    var1 = input("Please enter an integer (type exit to exit): ")
    print(int(var1))

# Bandingkan dengan pendekatan berikut (mengenai exception, import/library sys,
# dan try/except akan dibahas pada modul-modul pembelajaran berikutnya
import sys

data = ""
while data != "exit":
    try:
        data = input("Please enter an integer (type exit to exit): ")
        print("got integer: {}".format(int(data)))
    except:
        if data == "exit":
            pass  # exit gracefully without prompt any error
        else:
            print("error: {}".format(sys.exc_info()[0]))

# List Comprehension (membuat list dengan inline loop dan if)
# Cara 1
angka = [1, 2, 3, 4]
pangkat = []
for n in angka:
    pangkat.append(n**2)
print(pangkat)

# Cara 2 List Comprehension
angka = [1, 2, 3, 4]
pangkat = [n**2 for n in angka]
print(pangkat)

# List comprehension adalah salah satu cara untuk menghasilkan list
# baru berdasarkan list atau iterables yang telah ada sebelumnya
# new_list = [expression for_loop_one_or_more conditions]

# Contoh3 menemukan item yang ada di kedua list
list1 = ["d", "i", "c", "o"]
list2 = ["d", "i", "n", "g"]
duplikat = []
for a in list1:
    for b in list2:
        if a == b:
            duplikat.append(a)

print(duplikat)  # Output ['d','i']
# bandingkan
# Contoh4 Implementasi dengan list comprehension
list1 = ["d", "i", "c", "o"]
list2 = ["d", "i", "n", "g"]
duplikat = [a for a in list1 for b in list2 if a == b]
print(duplikat)  # Output: ['d','i']

# Contoh 5 kecilkan semua huruf
list_a = ["Hello", "World", "In", "Python"]
small_list_a = [_.lower() for _ in list_a]
print(small_list_a)

# Anda tidak perlu bingung saat melihat kode di Internet yang
# menuliskan seperti contoh di atas, karena garis bawah (underscore)
# termasuk penamaan variabel yang valid. Secara umum "_"
# biasa digunakan sebagai throwaway variable (variabel tidak penting).
list_a = range(1, 10, 2)
x = [[a**2, a**3] for a in list_a]
print(x)

# Class
# Definisi dari kelas menggunakan sintaksis class
# seperti halnya definisi fungsi yang menggunakan sintaksis def
class NamaKelas:
    pass  # gantikan dengan pernyataan-pernyataan,
    # misal: atribut atau metode


# Class support dua macam operasi
# 1. Mengacu pada atribut.
# 2. Pembuatan instance atau dalam bahasa Inggris disebut instantiation.
class Kalkulator:
    """contoh kelas kalkulator sederhana"""

    i = 12345  # def attr i

    def f(self):  # def func i
        return "hello world"


Kalkulator.i = (
    1024  # maka nilai atribut i dalam Kalkulator berubah dari 12345 menjadi 1024
)


# Objek (object: an instance of a class)
k = (
    Kalkulator()
)  # membuat instance dari kelas jadi objek, kemudian disimpan pada variabel k

print(k.f())  # akan mencetak hello world ke layar


# Class’ Constructor
# fungsi khusus atau metode sebagai constructor ini bernama __init__ atau
# biasa diucapkan sebagai "double underscore init". Pada saat dilakukan
# instantiation dari class, metode __init__ ini secara otomatis akan dipanggil
# terlebih dahulu.

# definisi class Kalkulator di atas jika diubah dengan menggunakan constructor.
class Kalkulator:
    """contoh kelas kalkulator sederhana"""

    def __init__(self):
        self.i = 12345

    def f(self):
        return "hello world"


class KeranjangBelanja:
    """contoh tidak baik dilakukan dengan definisi variabel terbagi"""

    isi = (
        []
    )  # menggunakan list di sini akan terbagi untuk semua instance. JANGAN DILAKUKAN


# dengan dilengkapi constructor pun proses instantiation tidak berubah dari sebelumnya.
k = (
    Kalkulator()
)  # membuat instance dari kelas jadi objek, kemudian disimpan pada variabel k

# constructor memiliki parameter i yang bersifat opsional, apabila dalam proses instantiation
# tidak dikirimkan parameter, secara otomatis i akan diisi nilai bawaan 12345.
class Kalkulator:
    """contoh kelas kalkulator sederhana"""

    def __init__(self, i=12345):
        self.i = (
            i  # i adalah variabel pada constructor, self.i adalah variabel dari class
        )

    def f(self):
        return "hello world"


k = Kalkulator(i=1024)  # melakukan instantiation sekaligus mengisi atribut i jadi 1024
print(k.i)  # mencetak atribut i dari objek k dengan keluaran nilai 1024

# Metode (Method)
# - Metode dari objek (object method)
# - Metode dari class (class method)
# - Metode secara static (static method)

# untuk sebuah metode, sebetulnya dikirimkan objek (hasil instance dari class)
# sebagai argumen pertamanya, dalam hal ini bernama self.
k.f()
# ekuivalen dengan
Kalkulator.f(k)

# fungsi decorator adalah sebuah fungsi yang mengembalikan fungsi lain,
# biasanya digunakan sebagai fungsi transformasi dengan "pembungkus" sintaksis @wrapper.

# Class method adalah sebuah fungsi yang mengubah metode menjadi metode dari class (class method).
# Metode dari class (class method) menerima masukan class secara implisit sebagai
# argumen pertama yang secara konvensi diberikan nama cls.
class Kalkulator:
    """contoh kelas kalkulator sederhana"""

    def f(self):
        return "hello world"

    @classmethod
    def tambah_angka(cls, angka1, angka2):
        return "{} + {} = {}".format(angka1, angka2, angka1 + angka2)


# pemanggilan dari class
Kalkulator.tambah_angka(1, 2)  # tanpa perlu memberikan masukan untuk argumen cls

# pemanggilan metode dari objek
k = Kalkulator()
print(k.tambah_angka(1, 2))

# Staticmethod adalah sebuah fungsi yang mengubah metode menjadi metode statis (static method).
# Metode statis (static method) tidak menerima masukan argumen pertama secara implisit.

# metode statis
class Kalkulator:
    """contoh kelas kalkulator sederhana"""

    def f(self):
        return "hello world"

    @staticmethod
    def kali_angka(angka1, angka2):
        return "{} x {} = {}".format(angka1, angka2, angka1 * angka2)


# Pemanggilan dari class
a = Kalkulator.kali_angka(2, 3)
print(a)

# Pemanggilan dari objek
k = Kalkulator()
a = k.kali_angka(2, 3)
print(a)


# Mekanisme Pewarisan (Inheritance)
# Paradigma Pemrograman Berorientasi Objek memiliki konsep pewarisan atau
# dalam bahasa Inggris disebut inheritance
class Kalkulator:
    """contoh kelas kalkulator sederhana. anggap kelas ini tidak boleh diubah!"""

    def __init__(self, nilai=0):
        self.nilai = nilai

    def tambah_angka(self, angka1, angka2):
        self.nilai = angka1 + angka2
        if self.nilai > 9:  # kalkulator sederhana hanya memroses sampai 9
            print("kalkulator sederhana melebihi batas angka: {}".format(self.nilai))
        return self.nilai


# membuat class KalkulatorKali yang mewarisi class Kalkulator
class KalkulatorKali(Kalkulator):
    """contoh mewarisi kelas kalkulator sederhana"""

    def kali_angka(self, angka1, angka2):
        self.nilai = angka1 * angka2
        return self.nilai


# pemanggilan class KalkulatorKali
kk = KalkulatorKali()
a = kk.kali_angka(2, 3)  # sesuai dengan definisi class memiliki fitur kali_angka
print(a)

b = kk.tambah_angka(5, 6)  # memiliki fitur tambah_angka karena mewarisi dari Kalkulator
print(b)

# Menimpa (Override) Metode dengan Nama yang Sama Dengan Kelas Dasar

# menimpa metode tambah_angka untuk menghilangkan batasan yang dimiliki.
class KalkulatorKali(Kalkulator):
    """contoh mewarisi kelas kalkulator sederhana"""

    def kali_angka(self, angka1, angka2):
        self.nilai = angka1 * angka2
        return self.nilai

    def tambah_angka(self, angka1, angka2):
        self.nilai = angka1 + angka2
        return self.nilai


kk = KalkulatorKali()

b = kk.tambah_angka(5, 6)  # fitur tambah_angka yang dipanggil milik KalkulatorKali
print(b)


# Pemanggilan Metode Kelas Dasar dari Kelas Turunan dengan Sintaksis Super
# Ubah sebagian fitur
class KalkulatorTambah(Kalkulator):
    """contoh mewarisi kelas kalkulator sederhana"""

    def tambah_angka(self, angka1, angka2):
        if (
            angka1 + angka2 <= 9
        ):  # fitur ini sudah oke di kelas dasar, gunakan yang ada saja
            super().tambah_angka(
                angka1, angka2
            )  # panggil fungsi dari Kalkulator lalu isi nilai
        else:  # ini adalah fitur baru yang ingin diperbaiki dari keterbatasan kelas dasar
            self.nilai = angka1 + angka2
        return self.nilai


# Variabel Privat di Python
# di Python ada konvensi dimana penggunaan nama yang diawali dengan garis bawah (underscore),
# baik itu fungsi, metode, maupun anggota data, akan dianggap sebagai non-publik.


# Pernak-Pernik Terkait Struktur Data
# cukup mendefinisikan saja sebuah class kosong, selanjutnya penamaan item data dapat
# secara langsung didefinisikan dan diisikan saat sudah instantiation.
class Pegawai:
    pass  # definisi class kosong


don = Pegawai()  # membuat Pegawai baru menjadi objek bernama don

# tambahkan item data pada objek sebagai record
don.nama = "Don Doo"
don.bagian = "IT"
don.gaji = 999

# Menampilkan Hello World
print("Hello World")

# perhitungan 2 angka
print("="*10, "Perhitungan 2 angka", "="*10)
angka1 = int(input("Masukkan angka pertama \t\t: "))
angka2 = int(input("Masukkan angka kedua \t\t: "))
operat = input("Masukkan lambang operator \t: ")

if operat == "+":
    hasil = angka1 + angka2
    print("{} + {} = {}".format(angka1, angka2, hasil))
elif operat == "-":
    hasil = angka1 - angka2
    print("{} - {} = {}".format(angka1, angka2, hasil))
elif operat == "*":
    hasil = angka1 * angka2
    print("{} * {} = {}".format(angka1, angka2, hasil))
elif operat == "/":
    hasil = angka1 / angka2
    print("{} / {} = {}".format(angka1, angka2, hasil))
else:
    print("\nMohon isi dengan benar!")

# Akar kuadrat
num = int(input("Masukkan angka : √"))
numm = num
# fungsi
numm **= 0.5
print("Akar kuadrat √%0.0f adalah %0.1f" % (num, numm))

# Luas segitiga
print("Luas Δ")
alas = int(input("Masukkan alas segitiga \t\t: "))
tinggi = int(input("Masukkan tinggi segitiga \t: "))
# rumus l = 1/2*a*t dan K = sisi
luas = 0.5 * (alas * tinggi)
print("Luas Δ dengan alas {} dan tinggi {} adalah {}".format(alas, tinggi, luas))

# Program perhitungan segitiga Δ
line = "="
print("\nProgram perhitungan Δ sama sisi, sama kaki, sembarang")

sisi1 = int(input("\nMasukkan panjang sisi ke A \t: "))
sisi2 = int(input("Masukkan panjang sisi ke B \t: "))
sisi3 = int(input("Masukkan panjang sisi ke C \t: "))

if sisi1 == sisi2 == sisi3:
    print("\nTeridentifikasi sebagai Δ sama sisi")
    # mencari tinggi Δ sama sisi
    sisi11 = sisi1*0.5
    tinggi = (sisi2**2) - (sisi11**2)
    tinggi **= 0.5  # **0.5 == akar kuadrat
    print(line, "\tTinggi \t\t: %0f" % (tinggi))
    # mencari keliling Δ sama sisi rumus k=sisi1+sisi2+sisi3
    keliling = sisi1+sisi2+sisi3
    print(line, "\tKeliling\t: %0.0f" % (keliling))
    # mencari luas Δ sama sisi rumus l=1/2*a*t
    alas = sisi1
    luas = 0.5 * alas * tinggi
    print(line, "\tLuas \t\t: %0f" % (luas))

elif sisi1 != sisi2 == sisi3:
    print("\nTeridentifikasi sebagai Δ sama kaki")
    # mencari tinggi Δ sama kaki
    sisi11 = sisi1*0.5
    tinggi = (sisi2**2) - (sisi11**2)
    tinggi **= 0.5  # **0.5 == akar kuadrat
    print(line, "\tTinggi \t\t: %0f" % (tinggi))
    # mencari keliling Δ sama sisi rumus k=sisi1+sisi2+sisi3
    keliling = sisi1+sisi2*2
    print(line, "\tKeliling\t: %0.0f" % (keliling))
    # mencari luas Δ sama sisi rumus l=1/2*a*t
    alas = sisi1
    luas = 0.5 * alas * tinggi
    print(line, "\tLuas \t\t: %0f" % (luas))

elif sisi1 == sisi3 != sisi2:
    print("\nTeridentifikasi sebagai Δ sama kaki")
    # mencari tinggi Δ sama kaki
    sisi22 = sisi2*0.5
    tinggi = (sisi1**2) - (sisi22**2)
    tinggi **= 0.5  # **0.5 == akar kuadrat
    print(line, "\tTinggi \t\t: %0f" % (tinggi))
    # mencari keliling Δ sama sisi rumus k=sisi1+sisi2+sisi3
    keliling = sisi2+sisi1*2
    print(line, "\tKeliling\t: %0.0f" % (keliling))
    # mencari luas Δ sama sisi rumus l=1/2*a*t
    alas = sisi2
    luas = 0.5 * alas * tinggi
    print(line, "\tLuas \t\t: %0f" % (luas))

elif sisi1 == sisi2 != sisi3:
    print("\nTeridentifikasi sebagai Δ sama kaki")
    # mencari tinggi Δ sama kaki
    sisi33 = sisi3*0.5
    tinggi = (sisi1**2) - (sisi33**2)
    tinggi **= 0.5  # **0.5 == akar kuadrat
    print(line, "\tTinggi \t\t: %0f" % (tinggi))
    # mencari keliling Δ sama sisi rumus k=sisi1+sisi2+sisi3
    keliling = sisi3+sisi1*2
    print(line, "\tKeliling\t: %0.0f" % (keliling))
    # mencari luas Δ sama sisi rumus l=1/2*a*t
    alas = sisi3
    luas = 0.5 * alas * tinggi
    print(line, "\tLuas \t\t: %0f" % (luas))

elif sisi1 != sisi2 != sisi3:
    print("\nTeridentifikasi sebagai Δ sembarang")
    # mencari keliling Δ sembarang rumus k=sisi1+sisi2+sisi3
    keliling = sisi1+sisi2+sisi3
    print(line, "\tKeliling\t: %0.0f" % (keliling))
    # mencari luas Δ sembarang 
    # rumus s=(a+b+c)/2 dan l=(s(s-a)(s-b)(s-c))**0.5
    a = sisi1
    b = sisi2
    c = sisi3
    s = (a+b+c)/2
    luas = (s*(s-a)*(s-b)*(s-c))
    luas **= 0.5
    print(line, "\tLuas \t\t: %0f" % (luas))
    # mencari tinggi Δ sembarang
    #tinggi = input("sisi yang manakah untuk dijadikan alas? A/B/C :")
    #if tinggi == "A":

else:
    print("\nError!... ")
    print("Inputkan nilai dengan benar")

# Program kalkulator sederhana
calc = input("Masukkan simbol operasi yang di inginkan (ex: + - * /) : ")

if calc == "+":
    num1 = int(input("Angka ke 1 : "))
    num2 = int(input("Angka ke 2 : "))
    result = num1 + num2
    print("{} + {} = {}".format(num1, num2, result))
elif calc == "-":
    num1 = int(input("Angka ke 1 : "))
    num2 = int(input("Angka ke 2 : "))
    result = num1 - num2
    print("{} - {} = {}".format(num1, num2, result))
elif calc == "*":
    num1 = int(input("Angka ke 1 : "))
    num2 = int(input("Angka ke 2 : "))
    result = num1 * num2
    print("{} * {} = {}".format(num1, num2, result))
elif calc == "/":
    num1 = int(input("Angka ke 1 : "))
    num2 = int(input("Angka ke 2 : "))
    result = num1 / num2
    print("{} / {} = {}".format(num1, num2, result))

"""
elif sisi1 != sisi2 == sisi3:
    print("\nTeridentifikasi sebagai Δ sama kaki")
    #Struktur Perulangan
    for i in range(6):
        spasi = " "*(6-i)
        bintang = "*" * (2*i+1)
        print(spasi,bintang)
    print(line)
    # mencari tinggi Δ sama kaki
    sisi11 = sisi1*0.5
    tinggi = (sisi2**2) - (sisi11**2)
    tinggi **= 0.5  # **0.5 == akar kuadrat
    print(line, "\tTinggi \t\t: ",tinggi)
    # mencari keliling Δ sama sisi rumus k=sisi1+sisi2+sisi3
    keliling = sisi1+sisi2*2
    print(line, "\tKeliling\t: ",keliling)
    # mencari luas Δ sama sisi rumus l=1/2*a*t
    alas = sisi1
    luas = 0.5 * alas * tinggi
    print(line, "\tLuas \t\t: ",luas)

elif sisi1 == sisi3 != sisi2:
    print("\nTeridentifikasi sebagai Δ sama kaki")
    for i in range(6):
        spasi = " "*(6-i)
        bintang = "*" * (2*i+1)
        print(spasi,bintang)
    print(line)
    # mencari tinggi Δ sama kaki
    sisi22 = sisi2*0.5
    tinggi = (sisi1**2) - (sisi22**2)
    tinggi **= 0.5  # **0.5 == akar kuadrat
    print(line, "\tTinggi \t\t: ",tinggi)
    # mencari keliling Δ sama sisi rumus k=sisi1+sisi2+sisi3
    keliling = sisi2+sisi1*2
    print(line, "\tKeliling\t: ",keliling)
    # mencari luas Δ sama sisi rumus l=1/2*a*t
    alas = sisi2
    luas = 0.5 * alas * tinggi
    print(line, "\tLuas \t\t: ",luas)

elif sisi1 == sisi2 != sisi3:
    print("\nTeridentifikasi sebagai Δ sama kaki")
    #Struktur Perulangan
    for i in range(6):
        spasi = " "*(6-i)
        bintang = "*" * (2*i+1)
        print(spasi,bintang)
    print(line)
    # mencari tinggi Δ sama kaki
    sisi33 = sisi3*0.5
    tinggi = (sisi1**2) - (sisi33**2)
    tinggi **= 0.5  # **0.5 == akar kuadrat
    print(line, "\tTinggi \t\t: ",tinggi)
    # mencari keliling Δ sama sisi rumus k=sisi1+sisi2+sisi3
    keliling = sisi3+sisi1*2
    print(line, "\tKeliling\t: ",keliling)
    # mencari luas Δ sama sisi rumus l=1/2*a*t
    alas = sisi3
    luas = 0.5 * alas * tinggi
    print(line, "\tLuas \t\t: ",luas)

elif sisi1 != sisi2 != sisi3:
    print("\nTeridentifikasi sebagai Δ sembarang")
    #Struktur Perulangan
    for i in range(4):
        spasi = " "*(4-i)
        bintang = "* " * (2*i+1)
        print(spasi,bintang)
    print(line)
    # mencari keliling Δ sembarang rumus k=sisi1+sisi2+sisi3
    keliling = sisi1+sisi2+sisi3
    print(line, "\tKeliling\t: ",keliling)
    # mencari luas Δ sembarang 
    # rumus s=(a+b+c)/2 dan l=(s(s-a)(s-b)(s-c))**0.5
    a = sisi1
    b = sisi2
    c = sisi3
    s = (a+b+c)/2
    luas = (s*(s-a)*(s-b)*(s-c))
    luas **= 0.5
    print(line, "\tLuas \t\t: ",luas)
    # mencari tinggi Δ sembarang
    #tinggi = input("sisi yang manakah untuk dijadikan alas? A/B/C :")
    #if tinggi == "A":
"""

class Node:
    def __init__(self, title, artist):
        """
        Inisialisasi node dengan judul lagu dan artis.
        """
        self.title = title
        self.artist = artist
        self.next = None

class Playlist:
    def __init__(self):
        """
        Inisialisasi linked list untuk menyimpan lagu-lagu dalam playlist.
        """
        self.head = None
        self.tail = None
        self.count = 0

    def tambah_lagu(self, title, artist):
        """
        Menambahkan lagu baru ke playlist.
        """
        new_node = Node(title, artist)
        if not self.head:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.count += 1

    def putar_lagu_berikutnya(self):
        """
        Memutar lagu berikutnya dalam playlist.
        """
        if self.head:
            current = self.head
            self.head = self.head.next
            print(f"Memutar: {current.title} - {current.artist}")
        else:
            print("Playlist kosong.")

    def hapus_lagu(self, title):
        """
        Menghapus lagu dari playlist berdasarkan judul.
        """
        current = self.head
        previous = None
        while current:
            if current.title == title:
                if previous:
                    previous.next = current.next
                    if current == self.tail:
                        self.tail = previous
                else:
                    self.head = current.next
                self.count -= 1
                return
            previous = current
            current = current.next
        print(f"Lagu '{title}' tidak ditemukan.")

    def tampilkan_daftar_lagu(self):
        """
        Menampilkan daftar lagu dalam playlist.
        """
        current = self.head
        while current:
            print(f"{current.title} - {current.artist}")
            current = current.next

    def total_jumlah_lagu(self):
        """
        Menghitung total jumlah lagu dalam playlist.
        """
        return self.count

# Main program
if __name__ == "__main__":
    playlist = Playlist()

    while True:
        print("\nMenu:")
        print("1. Tambah Lagu")
        print("2. Putar Lagu Berikutnya")
        print("3. Hapus Lagu")
        print("4. Tampilkan Daftar Lagu")
        print("5. Total Jumlah Lagu")
        print("6. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1":
            title = input("Masukkan judul lagu: ")
            artist = input("Masukkan nama artis: ")
            playlist.tambah_lagu(title, artist)
        elif pilihan == "2":
            playlist.putar_lagu_berikutnya()
        elif pilihan == "3":
            title = input("Masukkan judul lagu yang ingin dihapus: ")
            playlist.hapus_lagu(title)
        elif pilihan == "4":
            print("Daftar Lagu:")
            playlist.tampilkan_daftar_lagu()
        elif pilihan == "5":
            total = playlist.total_jumlah_lagu()
            print(f"Total jumlah lagu: {total}")
        elif pilihan == "6":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

"""
class Node:
    def __init__(self, task, is_completed=False):
        
        #Inisialisasi node dengan data tugas dan status selesai.
        
        self.task = task
        self.is_completed = is_completed
        self.next = None

class TaskList:
    def __init__(self):
        
        #Inisialisasi linked list untuk menyimpan tugas.
        
        self.head = None
        self.count = 0

    def tambah_tugas(self, task):
        
        #Menambahkan tugas baru ke linked list.
        
        new_node = Node(task)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def tandai_selesai(self, task):
        
        #Menandai tugas sebagai selesai.
        
        current = self.head
        while current:
            if current.task == task:
                current.is_completed = True
                return
            current = current.next
        print(f"Tugas '{task}' tidak ditemukan.")

    def hapus_tugas(self, task):
        
        #Menghapus tugas dari linked list.
        
        current = self.head
        previous = None
        while current:
            if current.task == task:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                self.count -= 1
                return
            previous = current
            current = current.next
        print(f"Tugas '{task}' tidak ditemukan.")

    def tampilkan_belum_selesai(self):
        
        #Menampilkan daftar tugas yang belum selesai.
        
        current = self.head
        while current:
            if not current.is_completed:
                print(f"Tugas: {current.task}")
            current = current.next

    def tampilkan_selesai(self):
        
        #Menampilkan daftar tugas yang sudah selesai.
        
        current = self.head
        while current:
            if current.is_completed:
                print(f"Tugas: {current.task}")
            current = current.next

# Main program
if __name__ == "__main__":
    task_list = TaskList()

    while True:
        print("\nMenu:")
        print("1. Tambah Tugas")
        print("2. Tandai Selesai")
        print("3. Hapus Tugas")
        print("4. Tampilkan Daftar Tugas Belum Selesai")
        print("5. Tampilkan Daftar Tugas Selesai")
        print("6. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1":
            task = input("Masukkan nama tugas: ")
            task_list.tambah_tugas(task)
        elif pilihan == "2":
            task = input("Masukkan nama tugas yang telah selesai: ")
            task_list.tandai_selesai(task)
        elif pilihan == "3":
            task = input("Masukkan nama tugas yang ingin dihapus: ")
            task_list.hapus_tugas(task)
        elif pilihan == "4":
            print("Daftar Tugas Belum Selesai:")
            task_list.tampilkan_belum_selesai()
        elif pilihan == "5":
            print("Daftar Tugas Selesai:")
            task_list.tampilkan_selesai()
        elif pilihan == "6":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


class Node:
    def __init__(self, suhu):
        self.suhu = suhu  # Nilai suhu
        self.next = None  # Pointer ke node berikutnya dalam linked list

class DataSuhu:
    def __init__(self):
        self.head = None  # Node pertama dalam linked list
        self.count = 0  # Jumlah total data suhu dalam daftar

    def __len__(self):
        return self.count  # Mengembalikan jumlah total data suhu

    def tambah_suhu(self, suhu):
        node_baru = Node(suhu)  # Membuat node baru dengan nilai suhu
        node_baru.next = self.head  # Mengatur node baru sebagai node pertama dalam linked list
        self.head = node_baru  # Mengatur node baru sebagai node pertama
        self.count += 1  # Menambah jumlah total data suhu

    def hapus_suhu(self, suhu):
        current = self.head
        previous = None
        while current:
            if current.suhu == suhu:  # Jika suhu cocok
                if previous:
                    previous.next = current.next  # Menghapus node dengan mengubah pointer node sebelumnya
                else:
                    self.head = current.next  # Menghapus node pertama
                self.count -= 1  # Mengurangi jumlah total data suhu
                return
            previous = current
            current = current.next
        print(f"Data suhu '{suhu}' tidak ditemukan.")

    def tampilkan_suhu(self):
        current = self.head
        while current:
            print(f"Suhu: {current.suhu}")  # Menampilkan nilai suhu
            current = current.next  # Pindah ke node berikutnya

    def rata_rata_suhu(self):
        total_suhu = 0
        current = self.head
        while current:
            total_suhu += current.suhu  # Menambahkan nilai suhu
            current = current.next
        if self.count == 0:
            return 0  # Mengembalikan 0 jika tidak ada data suhu
        return total_suhu / self.count  # Mengembalikan rata-rata suhu

# Program Utama
if __name__ == "__main__":
    data_suhu = DataSuhu()  # Membuat objek DataSuhu

    # Loop utama untuk menampilkan menu dan memproses pilihan pengguna
    while True:
        print("\nMenu:")
        print("1. Tambah Data Suhu")
        print("2. Hapus Data Suhu")
        print("3. Tampilkan Seluruh Data Suhu")
        print("4. Hitung Rata-rata Suhu")
        print("5. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")  # Meminta input pilihan dari pengguna

        if pilihan == "1":
            suhu = float(input("Masukkan nilai suhu: "))
            data_suhu.tambah_suhu(suhu)  # Memanggil metode tambah_suhu
        elif pilihan == "2":
            suhu = float(input("Masukkan nilai suhu yang ingin dihapus: "))
            data_suhu.hapus_suhu(suhu)  # Memanggil metode hapus_suhu
        elif pilihan == "3":
            print("Data Suhu:")
            data_suhu.tampilkan_suhu()  # Memanggil metode tampilkan_suhu
        elif pilihan == "4":
            rata_rata = data_suhu.rata_rata_suhu()
            print(f"Rata-rata suhu: {rata_rata}")  # Menampilkan rata-rata suhu
        elif pilihan == "5":
            break  # Keluar dari program
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")  # Pesan jika pilihan tidak valid


class Node:
    def __init__(self, nama, nilai=None):
        self.nama = nama  # Nama mahasiswa
        self.nilai = nilai  # Nilai ujian, nilai default adalah None
        self.next = None  # Pointer ke node berikutnya dalam linked list

class DaftarMahasiswa:
    def __init__(self):
        self.head = None  # Node pertama dalam linked list
        self.count = 0  # Jumlah total mahasiswa dalam daftar

    def __len__(self):
        return self.count  # Mengembalikan jumlah total mahasiswa

    def tambah_mahasiswa(self, nama):
        node_baru = Node(nama)  # Membuat node baru dengan nama mahasiswa
        node_baru.next = self.head  # Mengatur node baru sebagai node pertama dalam linked list
        self.head = node_baru  # Mengatur node baru sebagai node pertama
        self.count += 1  # Menambah jumlah total mahasiswa

    def tambah_nilai(self, nama, nilai):
        current = self.head
        while current:
            if current.nama == nama:  # Jika nama mahasiswa cocok
                current.nilai = nilai  # Menetapkan nilai ujian
                return
            current = current.next
        print(f"Mahasiswa '{nama}' tidak ditemukan.")

    def hapus_mahasiswa(self, nama):
        current = self.head
        previous = None
        while current:
            if current.nama == nama:  # Jika nama mahasiswa cocok
                if previous:
                    previous.next = current.next  # Menghapus node dengan mengubah pointer node sebelumnya
                else:
                    self.head = current.next  # Menghapus node pertama
                self.count -= 1  # Mengurangi jumlah total mahasiswa
                return
            previous = current
            current = current.next
        print(f"Mahasiswa '{nama}' tidak ditemukan.")

    def tampilkan_mahasiswa(self):
        current = self.head
        while current:
            print(f"Nama: {current.nama}, Nilai: {current.nilai}")  # Menampilkan nama dan nilai ujian
            current = current.next  # Pindah ke node berikutnya

    def rata_rata_nilai(self):
        total_nilai = 0
        current = self.head
        while current:
            if current.nilai is not None:
                total_nilai += current.nilai  # Menambahkan nilai ujian yang tidak None
            current = current.next
        if self.count == 0:
            return 0  # Mengembalikan 0 jika tidak ada mahasiswa
        return total_nilai / self.count  # Mengembalikan rata-rata nilai ujian

# Program Utama
if __name__ == "__main__":
    daftar_mahasiswa = DaftarMahasiswa()  # Membuat objek DaftarMahasiswa
    
    # Loop utama untuk menampilkan menu dan memproses pilihan pengguna
    while True:
        print("\nMenu:")
        print("1. Tambah Mahasiswa")
        print("2. Tambah Nilai Ujian")
        print("3. Hapus Data Mahasiswa")
        print("4. Tampilkan Seluruh Daftar Mahasiswa")
        print("5. Hitung Nilai Rata-rata Ujian")
        print("6. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")  # Meminta input pilihan dari pengguna

        if pilihan == "1":
            nama = input("Masukkan nama mahasiswa: ")
            daftar_mahasiswa.tambah_mahasiswa(nama)  # Memanggil metode tambah_mahasiswa
        elif pilihan == "2":
            nama = input("Masukkan nama mahasiswa yang ingin ditambahkan nilai: ")
            nilai = float(input("Masukkan nilai ujian: "))
            daftar_mahasiswa.tambah_nilai(nama, nilai)  # Memanggil metode tambah_nilai
        elif pilihan == "3":
            nama = input("Masukkan nama mahasiswa yang ingin dihapus: ")
            daftar_mahasiswa.hapus_mahasiswa(nama)  # Memanggil metode hapus_mahasiswa
        elif pilihan == "4":
            print("Daftar Mahasiswa:")
            daftar_mahasiswa.tampilkan_mahasiswa()  # Memanggil metode tampilkan_mahasiswa
        elif pilihan == "5":
            rata_rata = daftar_mahasiswa.rata_rata_nilai()
            print(f"Rata-rata nilai ujian: {rata_rata}")  # Menampilkan rata-rata nilai ujian
        elif pilihan == "6":
            break  # Keluar dari program
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")  # Pesan jika pilihan tidak valid


# Definisi kelas Node untuk merepresentasikan node dalam linked list
class Node:
    def __init__(self, data):
        self.data = data  # Data yang disimpan dalam node
        self.next = None   # Pointer yang menunjukkan ke node berikutnya dalam linked list

# Definisi kelas DaftarBuah untuk menyimpan daftar buah dalam linked list
class DaftarBuah:
    def __init__(self):
        self.head = None  # Node pertama dalam linked list
        self.count = 0    # Jumlah total buah dalam daftar

    # Metode khusus untuk mengimplementasikan fungsi len() pada objek DaftarBuah
    def __len__(self):
        return self.count

    # Metode untuk menambahkan buah baru ke dalam linked list
    def tambah_buah(self, nama):
        node_baru = Node(nama)  # Membuat node baru dengan data nama
        node_baru.next = self.head  # Mengatur node baru sebagai node pertama dalam linked list
        self.head = node_baru  # Mengatur node baru sebagai node pertama
        self.count += 1  # Menambah jumlah total buah

    # Metode untuk menghapus buah dari linked list berdasarkan nama
    def hapus_buah(self, nama):
        sekarang = self.head  # Node yang sedang diperiksa
        sebelumnya = None  # Node sebelum node yang sedang diperiksa
        while sekarang:
            if sekarang.data == nama:  # Jika data node sama dengan nama yang dicari
                if sebelumnya:
                    sebelumnya.next = sekarang.next  # Mengubah pointer node sebelumnya untuk mengabaikan node yang dihapus
                else:
                    self.head = sekarang.next  # Mengubah node pertama jika node yang dihapus adalah node pertama
                self.count -= 1  # Mengurangi jumlah total buah
                return
            sebelumnya = sekarang
            sekarang = sekarang.next
        print(f"Buah '{nama}' tidak ditemukan.")  # Pesan jika buah tidak ditemukan

    # Metode untuk menampilkan daftar buah dalam linked list
    def tampilkan_buah(self):
        sekarang = self.head  # Node yang sedang ditampilkan
        while sekarang:
            print(sekarang.data)  # Menampilkan data buah
            sekarang = sekarang.next  # Berpindah ke node berikutnya

# Program Utama
if __name__ == "__main__":
    daftar_buah = DaftarBuah()  # Membuat objek daftar_buah dari kelas DaftarBuah
    
    # Loop utama untuk menampilkan menu dan memproses pilihan pengguna
    while True:
        print("\nMenu:")
        print("1. Tambah Buah")
        print("2. Hapus Buah")
        print("3. Tampilkan Daftar Buah")
        print("4. Total Buah")
        print("5. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")  # Meminta input pilihan dari pengguna

        if pilihan == "1":
            nama = input("Masukkan nama buah: ")
            daftar_buah.tambah_buah(nama)  # Memanggil metode tambah_buah
        elif pilihan == "2":
            nama = input("Masukkan nama buah yang ingin dihapus: ")
            daftar_buah.hapus_buah(nama)  # Memanggil metode hapus_buah
        elif pilihan == "3":
            print("Daftar Buah:")
            daftar_buah.tampilkan_buah()  # Memanggil metode tampilkan_buah
        elif pilihan == "4":
            total = len(daftar_buah)
            print(f"Total jumlah buah: {total}")  # Menampilkan total jumlah buah
        elif pilihan == "5":
            break  # Keluar dari program
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")  # Pesan jika pilihan tidak valid
"""
"""
# Definisi kelas Node untuk merepresentasikan node dalam linked list
class Node:
    def __init__(self, data):
        self.data = data  # Data yang disimpan dalam node
        self.next = None   # Pointer yang menunjukkan ke node berikutnya dalam linked list

# Definisi kelas DaftarKaryawan untuk menyimpan daftar karyawan dalam linked list
class DaftarKaryawan:
    def __init__(self):
        self.head = None  # Node pertama dalam linked list
        self.count = 0    # Jumlah total karyawan dalam daftar

    # Metode khusus untuk mengimplementasikan fungsi len() pada objek DaftarKaryawan
    def __len__(self):
        return self.count

    # Metode untuk menambahkan karyawan baru ke dalam linked list
    def tambah_karyawan(self, nama):
        node_baru = Node(nama)  # Membuat node baru dengan data nama
        node_baru.next = self.head  # Mengatur node baru sebagai node pertama dalam linked list
        self.head = node_baru  # Mengatur node baru sebagai node pertama
        self.count += 1  # Menambah jumlah total karyawan

    # Metode untuk menghapus karyawan dari linked list berdasarkan nama
    def hapus_karyawan(self, nama):
        sekarang = self.head  # Node yang sedang diperiksa
        sebelumnya = None  # Node sebelum node yang sedang diperiksa
        while sekarang:
            if sekarang.data == nama:  # Jika data node sama dengan nama yang dicari
                if sebelumnya:
                    sebelumnya.next = sekarang.next  # Mengubah pointer node sebelumnya untuk mengabaikan node yang dihapus
                else:
                    self.head = sekarang.next  # Mengubah node pertama jika node yang dihapus adalah node pertama
                self.count -= 1  # Mengurangi jumlah total karyawan
                return
            sebelumnya = sekarang
            sekarang = sekarang.next
        print(f"Karyawan '{nama}' tidak ditemukan.")  # Pesan jika karyawan tidak ditemukan

    # Metode untuk menampilkan daftar karyawan dalam linked list
    def tampilkan_karyawan(self):
        sekarang = self.head  # Node yang sedang ditampilkan
        while sekarang:
            print(sekarang.data)  # Menampilkan data karyawan
            sekarang = sekarang.next  # Berpindah ke node berikutnya

# Program Utama
if __name__ == "__main__":
    daftar_karyawan = DaftarKaryawan()  # Membuat objek daftar_karyawan dari kelas DaftarKaryawan
    
    # Loop utama untuk menampilkan menu dan memproses pilihan pengguna
    while True:
        print("\nMenu:")
        print("1. Tambah Karyawan")
        print("2. Hapus Karyawan")
        print("3. Tampilkan Daftar Karyawan")
        print("4. Total Karyawan")
        print("5. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")  # Meminta input pilihan dari pengguna

        if pilihan == "1":
            nama = input("Masukkan nama karyawan: ")
            daftar_karyawan.tambah_karyawan(nama)  # Memanggil metode tambah_karyawan
        elif pilihan == "2":
            nama = input("Masukkan nama karyawan yang ingin dihapus: ")
            daftar_karyawan.hapus_karyawan(nama)  # Memanggil metode hapus_karyawan
        elif pilihan == "3":
            print("Daftar Karyawan:")
            daftar_karyawan.tampilkan_karyawan()  # Memanggil metode tampilkan_karyawan
        elif pilihan == "4":
            total = len(daftar_karyawan)
            print(f"Total jumlah karyawan: {total}")  # Menampilkan total jumlah karyawan
        elif pilihan == "5":
            break  # Keluar dari program
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")  # Pesan jika pilihan tidak valid
"""
