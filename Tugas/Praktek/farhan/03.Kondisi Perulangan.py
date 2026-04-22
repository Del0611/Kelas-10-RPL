#1.for
for i in range(5):
    print("Perulangan ke-", i)
    
i = 1

#2.while
while i <= 5:
    print("Angka:", i)
    i += 1

#3.break
for i in range(10):
    if i == 5:
        break
    print(i)
    
#4.continue
for i in range(5):
    if i == 2:
        continue
    print(i)
    
#5.pass
for i in range(5):
    pass
