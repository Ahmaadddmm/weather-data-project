Project Real-Time Automated Data Pipeline (WeatherStack API)

Sistem ini merupakan solusi *Automated Data Pipeline* yang dirancang untuk mengelola siklus hidup data cuaca secara *end-to-end* tanpa intervensi manual. Dibangun di atas lingkungan Docker, sistem ini mengintegrasikan serangkaian teknologi *open-source* di mana Apache Airflow bertindak sebagai orkestrator utama yang menjadwalkan penarikan data mentah dari Weatherstack API secara berkala untuk disimpan ke dalam database PostgreSQL. Data tersebut kemudian diproses dan ditransformasi strukturnya menjadi data analitik yang bersih menggunakan dbt (*data build tool*), sebelum akhirnya divisualisasikan menjadi informasi yang mudah dipahami melalui *dashboard* interaktif di Apache Superset. Keseluruhan alur ini bertujuan untuk mengubah proses pengelolaan data yang sebelumnya manual dan rentan kesalahan menjadi sistem yang otomatis, terpusat, dan andal untuk mendukung kebutuhan analisis data cuaca.

- Ahmad Maulana — Data Engineer

  Built end-to-end data pipeline, API ingestion, database design, workflow orchestration using Airflow, data transformation with dbt, and Dockerized infrastructure.

- Alya Gustasya — Data Analyst  
  Designed analytical datasets and built interactive dashboards using Apache Superset.

- Gilang Damar Pamungkas - Technical Writer
  Authored and maintained project documentation, including:
  - Progress Report
  - Final Project Report
  - Translated complex technical implementations into clear, structured, and readable documentation
  
