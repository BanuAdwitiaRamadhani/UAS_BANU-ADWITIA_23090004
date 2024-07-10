class AntrianRestoran:
    def __init__(self):
        self.antrian = []

    def enqueue(self, pesanan):
        self.antrian.append(pesanan)
        print(f"Pesanan '{pesanan}' telah ditambahkan ke antrian.")

    def dequeue(self):
        if len(self.antrian) > 0:
            pesanan = self.antrian.pop(0)
            print(f"Pesanan '{pesanan}' telah diambil dari antrian.")
            return pesanan
        else:
            print("Antrian kosong. Tidak ada pesanan untuk diambil.")
            return None

    def tampilkan_antrian(self):
        if len(self.antrian) > 0:
            print("Daftar antrian pesanan:")
            for idx, pesanan in enumerate(self.antrian, start=1):
                print(f"{idx}. {pesanan}")
        else:
            print("Antrian kosong.")

restoran = AntrianRestoran()

restoran.enqueue("Nasi Goreng")
restoran.enqueue("Mie Ayam")
restoran.enqueue("Sate Ayam")

restoran.tampilkan_antrian()

restoran.dequeue()
restoran.dequeue()

restoran.tampilkan_antrian()

restoran.dequeue()
restoran.dequeue()  