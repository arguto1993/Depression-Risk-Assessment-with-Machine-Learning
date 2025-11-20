# Mengidentifikasi Risiko Depresi dengan Pembelajaran Mesin

## Tujuan
Projek ini bertujuan untuk menjawab pertanyaan berikut:
1. Apa saja faktor utama yang berkontribusi terhadap risiko depresi pada individu?
2. Bagaimana model klasifikasi dapat digunakan untuk mengidentifikasi individu yang berisiko tinggi mengalami depresi?

## Hasil Yang Diharapkan
1. Insight yang menjawab pertanyaan bisnis di atas berdasarkan analisis data yang dilakukan.
2. Model prediksi yang dapat mengklasifikasikan individu menjadi dua kategori: depresi (label 1) dan tidak depresi (label 0), berdasarkan faktor-faktor yang relevan. Model ini dapat digunakan oleh berbagai lembaga pendidikan, perusahaan, dan organisasi untuk memberikan perhatian lebih kepada individu yang berisiko tinggi mengalami depresi, sehingga intervensi dapat dilakukan lebih awal.
3. Website yang mendemonstrasikan kemampuan model dalam memprediksi risiko depresi seseorang.

## Dataset
- https://www.kaggle.com/datasets/hopesb/student-depression-dataset.

## Link website aplikasi
- https://depression-risk-assessment.streamlit.app/

## Video demo penggunaan aplikasi
- https://youtu.be/qTZRZB-TxGE

## Video presentasi projek
- https://youtu.be/DQWeNKIEiIo

## Struktur Proyek

Proyek ini mengikuti praktik terbaik Streamlit untuk organisasi kode:

```
.
├── app.py                      # Titik masuk aplikasi utama
├── .streamlit/
│   └── config.toml            # Konfigurasi Streamlit
├── models/                     # Model pembelajaran mesin
│   ├── logistic_regression_model.pkl
│   ├── label_encoders.pkl
│   └── sleep_duration_mapping.pkl
├── pages/                      # Komponen halaman
│   ├── risk_assessment.py     # Halaman penilaian risiko
│   ├── dashboard.py           # Halaman dashboard
│   └── about.py               # Halaman tentang
├── utils/                      # Modul utilitas
│   ├── config.py              # Konstanta konfigurasi
│   ├── data_loader.py         # Pemuatan model dan data
│   └── prediction.py          # Logika prediksi
├── dataset/                    # File dataset
├── documentation/              # Dokumentasi proyek
└── requirements.txt           # Dependensi Python
```

## Menjalankan Aplikasi

1. Instal dependensi:
```bash
pip install -r requirements.txt
```

2. Jalankan aplikasi Streamlit:
```bash
streamlit run app.py
```

3. Buka browser Anda dan navigasi ke URL lokal yang disediakan (biasanya http://localhost:8501)
