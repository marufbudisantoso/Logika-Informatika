import itertools

# Definisikan operasi logika khusus yang digunakan
def xor(p, q):
    return p != q  # XOR (True jika p dan q berbeda)

def implication(p, q):
    return not p or q  # Implikasi p → q (False hanya jika p True dan q False)

def biimplication(p, q):
    return p == q  # Bikondisional p ↔ q (True jika p dan q sama)

# Fungsi untuk mengevaluasi ekspresi logika
def evaluate_expression(expression, values, variables):
    # Buat map variabel ke nilai True/False
    local_vars = {var: value for var, value in zip(variables, values)}
    
    # Gantikan fungsi logika khusus dengan panggilan ke fungsinya
    local_vars['xor'] = xor
    local_vars['imp'] = implication
    local_vars['bic'] = biimplication

    # Evaluasi ekspresi dengan nilai-nilai variabel yang diberikan
    return eval(expression, {}, local_vars)

# Fungsi untuk mencetak tabel kebenaran
def truth_table(variables, expression):
    n = len(variables)
    combinations = list(itertools.product([True, False], repeat=n))

    # Header tabel kebenaran
    header = list(variables) + [expression]
    print(f"{' | '.join(header)}")
    print('-' * (len(header) * 12))

    for row in combinations:
        result = evaluate_expression(expression, row, variables)
        
        # Cetak baris tabel kebenaran
        print(f"{' | '.join(map(str, row))} | {result}")

# Input variabel (p, q) dan ekspresi logika dari pengguna
variables = input("Masukkan variabel yang dipisahkan dengan koma (contoh: p,q): ").split(',')
expression = input("Masukkan ekspresi logika (gunakan 'xor', 'imp', 'bic', contoh: xor(p, q) ): ")

# Cetak tabel kebenaran
truth_table(variables, expression)