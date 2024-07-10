class Buah:
    def __init__(self, nama, warna, vitamin):
        self.nama = nama
        self.warna = warna
        self.vitamin = vitamin

    def deskripsi(self):
        return f"{self.nama} berwarna {self.warna}."

    def set_warna(self, warna):
        self.warna = warna

    def set_vitamin(self, vitamin):
        self.vitamin = vitamin

    def informasi(self):
        return f"{self.nama} berwarna {self.warna} dan mengandung vitamin {self.vitamin}."
    
class Mangga(Buah):
    def __init__(self, nama, warna, vitamin, rasa):
        super().__init__(nama, warna, vitamin)
        self.rasa = rasa

    def deskripsi_rasa(self):
        return f"{self.nama} berwarna {self.warna} dan rasanya {self.rasa}."

    def set_rasa(self, rasa):
        self.rasa = rasa

mangga_harum_manis = Mangga("Mangga Harum Manis", "Hijau", "C", "Manis")

print(mangga_harum_manis.nama)         
print(mangga_harum_manis.warna)        
print(mangga_harum_manis.vitamin)      
print(mangga_harum_manis.rasa)         

print(mangga_harum_manis.deskripsi())  
print(mangga_harum_manis.deskripsi_rasa())  
print(mangga_harum_manis.informasi())  

mangga_harum_manis.set_warna("Kuning")
mangga_harum_manis.set_rasa("Asam Manis")
mangga_harum_manis.set_vitamin("A dan C")

print(mangga_harum_manis.deskripsi()) 
print(mangga_harum_manis.deskripsi_rasa())  
print(mangga_harum_manis.informasi())  
