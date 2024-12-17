import pandas as pd

# Data teks dan label yang relevan
data = {
    'text': [
        "Saya sangat senang", "Hari ini buruk", "Cinta banget sama kamu",
        "Sangat kecewa dengan hasilnya", "Semangat terus!", "Tidak puas dengan layanan",
        "Pekerjaan saya luar biasa", "Malam yang sangat buruk", "Saya merasa hebat",
        "Produk ini luar biasa", "Sangat kecewa dengan pelayanan", "Senang bisa belajar hal baru",
        "Tidak ada yang lebih buruk dari ini", "Buat saya ini sangat menyenangkan",
        "Tidak bagus sama sekali", "Ini benar-benar menyenangkan", "Saya sangat suka!",
        "Hari yang buruk", "Puas dengan hasilnya", "Semua hal baik", "Terima kasih untuk dukungannya",
        "Tidak menyukai hal ini", "Sangat bahagia", "Menyenangkan sekali!",
        "Pekerjaan ini sangat buruk", "Cinta banget sama hasilnya", "Hari yang menyenankan",
        "Kecewa dengan kualitas", "Sangat puas", "Ini adalah hari yang bagus",
        "Saya merasa kecewa", "Menyenankan banget", "Hasilnya memuaskan",
        "Saya tidak akan kembali lagi", "Saya tidak menyukai pengalaman ini", "Hari yang cerah",
        "Sangat suka dengan produknya", "Luar biasa!", "Tidak tertarik sama sekali",
        "Bagus banget", "Kurang memuaskan", "Saya benar-benar tidak suka", "Hasilnya bagus",
        "Menangis karena kecewa", "Jauh lebih baik", "Lebih buruk dari yang saya bayangkan",
        "Suka banget", "Hasilnya luar biasa", "Sangat puas", "Tidak ada yang lebih baik dari ini",
        "Sangat tidak puas", "Terbaik!", "Mengecewakan sekali"
    ],
    'label': [
        'positif', 'negatif', 'positif', 'negatif', 'positif', 'negatif',
        'positif', 'negatif', 'positif', 'positif', 'negatif', 'positif',
        'negatif', 'positif', 'negatif', 'positif', 'positif', 'negatif',
        'positif', 'positif', 'positif', 'positif', 'negatif', 'positif',
        'negatif', 'positif', 'negatif', 'negatif', 'positif', 'positif',
        'negatif', 'positif', 'positif', 'negatif', 'positif', 'negatif',
        'positif', 'positif', 'negatif', 'positif', 'negatif', 'negatif',
        'positif', 'negatif', 'positif', 'positif', 'negatif', 'positif',
        'negatif', 'positif', 'positif'
    ]
}

# Menghapus elemen berlebih di 'text' jika panjangnya lebih dari 'label'
data['text'] = data['text'][:len(data['label'])]

# Memastikan panjang data 'text' dan 'label' sama
assert len(data['text']) == len(data['label']), "Panjang text dan label tidak sama!"

# Membuat DataFrame dari dictionary data
df = pd.DataFrame(data)

# Menyimpan DataFrame ke dalam file CSV
df.to_csv('text_data.csv', index=False)

print("Dataset disimpan di text_data.csv")
