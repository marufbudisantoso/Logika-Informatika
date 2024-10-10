import sympy as sp

def kalkulator():
    print("Selamat datang di Kalkulator Sederhana!")
    print("Pilih opsi yang diinginkan:")
    print("1. Operasi Dasar (+, -, *, /)")
    print("2. Hitung Derivatif")
    print("3. Hitung Integral")
    print("0. Keluar")

    while True:
        pilihan = input("Masukkan pilihan (1/2/3/0): ")

        if pilihan == '1':
            # Operasi Dasar
            angka1 = float(input("Masukkan angka pertama: "))
            operator = input("Masukkan operator (+, -, *, /): ")
            angka2 = float(input("Masukkan angka kedua: "))
            
            if operator == '+':
                hasil = angka1 + angka2
            elif operator == '-':
                hasil = angka1 - angka2
            elif operator == '*':
                hasil = angka1 * angka2
            elif operator == '/':
                hasil = angka1 / angka2
            else:
                print("Operator tidak valid!")
                continue
            
            print(f"Hasil: {hasil}")

        elif pilihan == '2':
            # Hitung Derivatif
            fungsi_input = input("Masukkan fungsi (gunakan x, contoh: x**2 + 3*x + 2): ")
            x = sp.symbols('x')
            fungsi = sp.sympify(fungsi_input)
            turunan = sp.diff(fungsi, x)
            print(f"Turunan dari {fungsi} adalah {turunan}")

        elif pilihan == '3':
            # Hitung Integral
            fungsi_input = input("Masukkan fungsi (gunakan x, contoh: x**2 + 3*x + 2): ")
            x = sp.symbols('x')
            fungsi = sp.sympify(fungsi_input)
            integral = sp.integrate(fungsi, x)
            print(f"Integral dari {fungsi} adalah {integral}")

        elif pilihan == '0':
            print("Terima kasih telah menggunakan kalkulator.")
            break
        
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

# Menjalankan kalkulator
kalkulator()
