# Data dictionary berisi username dan password mahasiswa
mahasiswa = {
    'Putra': {'password': '012345'},
    'Nabil': {'password': '012345'},
    'Safril': {'password': '012345'},
    'Ilham': {'password': '012345'},
    'Ozan': {'password': '012345'},
    'Arridoh': {'password': '012345'},
    'Agung': {'password': '012345'},
    'Gatsu': {'password': '012345'},
    'Rafaell': {'password': '012345'},
    'Amir': {'password': '012345'}
}

# Meminta pengguna memasukkan username dan password
username = input("Masukkan username: ")
password = input("Masukkan password: ")

# Memeriksa apakah kombinasi tersebut ada dalam dictionary mahasiswa
if username in mahasiswa and mahasiswa[username]['password'] == password:
    print("Login berhasil. Selamat datang, ", username)
else:
    print("Login gagal. Username atau password salah.")
