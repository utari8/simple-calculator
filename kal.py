# code by fitri n utari

print("SELAMAT DATANG DI KALKULATOR SEDERHANA")
def kalk():
    x = int(input("Masukkan angka pertama : "))
    y = input("Pilih operator : ")
    z = int(input("Masukkan angka ke dua : "))

    if y == "*":
        a = x * z
        print(a)
    elif y == "/":
        b = x / z
        print(b)
    elif y == "+":
        c = x + z
        print(c)
    elif y == "-":
        d = x - z
        print(d)
    else:
        print("sorry, please try again")

kalk()

q = str(input("Apakah anda ingin melanjutkan? (y/n) : "))
if q == "y":
    while q == "y":
        kalk()
        q = str(input("Apakah anda ingin melanjutkan? (y/n) : "))
        if q == "n":
            print("thank you")
else:
    print("thank you!")

# code by fitri n utari