#Tugas 1
print("Tugas 1")
angka = int(input("masukkan angka : "))
if angka >= 1:
    print("positif")
elif angka == 0:
    print("nol")
else:
    print("negatif")
    
#Tugas 2
print("Tugas nomor 2")
i = 2
while i <= 20:
    print(i)
    i += 2
#Tugas 3
print("Tugas nomor 3")
def factorial(n):
    if  n == 0 or n == 1:
       return 1
    else:
           return n*factorial (n-1)
print(factorial(10))
 

#Tugas 4
print("Tugas nomor 4")
password = ("papam ganteng")
nama = input("masukkan nama :")
passw = input("masukkan password :")

if password == ("papam ganteng"):
    print("halo,",nama)
else:
    print("password salah!")

#Tugas 5
print("Tugas nomor 5")
nis = ("25720")
print("             Menu")
print("Setting      Itulah      Credit")
pick = input("Mau kemana?")
if pick == ("Setting"):
    print("Setting")
if pick == ("itulah"):
    print("Itulah")
if pick == ("Credit"):
    print("made by papam")
login = input("masukkan nis :")
if nis == ("25720"):
    print("Login berhasil")



