Project Real-Time Automated Data Pipeline (WeatherStack API)

Sistem ini merupakan solusi Automated Data Pipeline yang dirancang untuk mengelola siklus hidup data cuaca secara end-to-end tanpa intervensi manual. Dibangun di atas lingkungan Docker, sistem ini mengintegrasikan serangkaian teknologi open-source di mana Apache Airflow bertindak sebagai orkestrator utama yang menjadwalkan penarikan data mentah dari Weatherstack API secara berkala untuk disimpan ke dalam database PostgreSQL. Data tersebut kemudian diproses dan ditransformasi strukturnya menjadi data analitik yang bersih menggunakan dbt (data build tool), sebelum akhirnya divisualisasikan menjadi informasi yang mudah dipahami melalui dashboard interaktif di Apache Superset. Keseluruhan alur ini bertujuan untuk mengubah proses pengelolaan data yang sebelumnya manual dan rentan kesalahan menjadi sistem yang otomatis, terpusat, dan andal untuk mendukung kebutuhan analisis data cuaca.

Team Roles & Responsibilities

----------------------------------------------------------------------------------------
- Ahmad Maulana — PM & Data Engineer


   Bertanggung jawab atas pengelolaan proyek dan implementasi teknis sistem, meliputi:
  
 - Menyusun proposal proyek dan dokumen perencanaan pengembangan
 - Membagi tugas dan mengoordinasikan pekerjaan antar anggota tim
 - Menyusun laporan pendahuluan dan perencanaan proyek
 - Menyusun timeline pengerjaan dan memastikan proyek berjalan sesuai jadwal
 - Membangun end-to-end data pipeline
 - Implementasi API ingestion dari Weatherstack API
 - Perancangan dan implementasi skema database PostgreSQL
 - Workflow orchestration menggunakan Apache Airflow
 - Transformasi data menggunakan dbt
 - Pembangunan dan pengelolaan infrastruktur berbasis Docker (Dockerized infrastructure)

----------------------------------------------------------------------------------------
- Alya Gustasya — Data Analyst

  
  Bertanggung jawab pada analisis dan penyajian data, meliputi:

 - Perancangan dataset analitik berdasarkan hasil transformasi data
 - Analisis data cuaca untuk menghasilkan insight yang relevan
 - Pembuatan dan pengembangan dashboard interaktif menggunakan Apache Superset
 - Penyajian visualisasi data yang informatif dan mudah dipahami

----------------------------------------------------------------------------------------
- Gilang Damar Pamungkas - Technical Writer

  
  Bertanggung jawab dalam penyusunan dan pengelolaan dokumentasi proyek, meliputi:

  - Penyusunan Progress Report
  - Penyusunan Final Project Report
  - Dokumentasi teknis sistem dan alur kerja data pipeline
  - Menerjemahkan implementasi teknis yang kompleks ke dalam dokumentasi yang jelas, terstruktur, dan mudah dipahami
  
