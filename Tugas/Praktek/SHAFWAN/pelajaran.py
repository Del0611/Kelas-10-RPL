angka_rahasia = 7
tebakan = 0

while tebakan != angka_rahasia:
    tebakan = int(input("Tebak angka (1-10): "))
    
    if tebakan == angka_rahasia:
        print("Benar!")
    else:
        print("Salah, coba lagi"
