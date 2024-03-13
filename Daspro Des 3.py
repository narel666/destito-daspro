# Data dictionary jadwal daspro IF2
jadwal_dasproIF2 = {
    'Senin': '08.00','kamis': '10.50','jumat':'08.00'
}

# Data dictionary jadwal daspro IF3
jadwal_dasproIF3 = {
    'Selasa': '08.00','Rabu': '10.50','Rabu':'15.00'
}

# Menggabungkan dua data dictionary
jadwal_combined = jadwal_dasproIF3.copy()
jadwal_combined.update(jadwal_dasproIF2)

# Menampilkan hasil gabungan
print("Jadwal setelah di gabungan:")
print(jadwal_combined)
