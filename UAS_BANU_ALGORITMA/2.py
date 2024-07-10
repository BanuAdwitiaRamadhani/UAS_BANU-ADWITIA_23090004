import pandas as pd
import numpy  as  np
  
data = [
    ["Mahasiswa1", 90, 80],
    ["Mahasiswa2", 50, 60],
    ["Mahasiswa3", 65, 70]
]

mata_kuliah = ["Nama", "Algoritma dan struktur Data 2", "Matetamtika Numerik"]

df = pd.DataFrame(data, columns=mata_kuliah)

rata_rata_mata_kuliah = df.mean(axis=0, numeric_only=True)
print("Rata-rata nilai untuk setiap mata kuliah:")
print(rata_rata_mata_kuliah)

df["Rata-rata"] = df.mean(axis=1, numeric_only=True)
rata_rata_mahasiswa = df[["Nama", "Rata-rata"]]
print("\nRata-rata nilai untuk setiap mahasiswa:")
print(rata_rata_mahasiswa)