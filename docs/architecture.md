# Architecture

Dokumen ini menjelaskan arsitektur dasar project **Health-Journal-Summarizer**.

Project ini dirancang sebagai sistem agentic sederhana yang membantu mengubah satu topik kesehatan menjadi:

- catatan riset berbasis jurnal ilmiah
- evidence summary
- draft artikel populer bergaya Medium

Arsitektur project ini sengaja dibuat modular agar mudah dipahami, diuji, dan dikembangkan secara bertahap.

## Design Goals

Arsitektur ini dibuat dengan tujuan:

- sederhana dan ramah untuk pemula
- mudah dikembangkan sedikit demi sedikit
- aman untuk domain kesehatan
- memisahkan tahap riset, sintesis, dan penulisan
- memudahkan human review sebelum publikasi

## High-Level Overview

Secara umum, sistem terdiri dari beberapa komponen utama:

1. input topic
2. planner
3. researcher
4. summarizer
5. writer
6. tools pendukung
7. output storage
8. human review

Alur besarnya:

`Topic -> Planner -> Researcher -> Summarizer -> Writer -> Output -> Human Review`

## Main Components

### 1. Topic Input

Komponen ini bertugas menyediakan topik yang akan diproses.

Sumber topik dapat berasal dari:

- file backlog topik, misalnya `data/topics/science-topics.json`
- input manual dari pengguna
- daftar ide artikel dari sumber eksternal seperti `rofiqi.com/science`

Tanggung jawab:
- memilih satu topik
- memastikan topik cukup spesifik
- meneruskan topik ke planner

### 2. Planner

Planner bertugas menentukan langkah kerja untuk satu topik.

Planner tidak harus rumit. Dalam versi awal, planner cukup:

- menerima topik
- menentukan urutan langkah
- menetapkan target output
- mengarahkan proses ke researcher, summarizer, lalu writer

Contoh tanggung jawab planner:
- menentukan bahwa sistem perlu mencari 5 sampai 8 jurnal
- memastikan ada tahap evaluasi bukti
- memastikan proses berhenti setelah output minimum tercapai

File terkait:
- `src/agent/planner.py`

### 3. Researcher

Researcher adalah komponen yang bertugas mencari dan mengumpulkan sumber ilmiah.

Tanggung jawab utama:
- mencari jurnal ilmiah relevan
- mengumpulkan metadata sumber
- menyaring hasil yang tidak relevan
- menyiapkan bahan mentah untuk tahap sintesis

Researcher sebaiknya memprioritaskan:
- systematic review
- meta-analysis
- randomized controlled trial
- cohort study

Output komponen ini:
- daftar referensi ilmiah
- research notes awal

File terkait:
- `src/agent/researcher.py`

### 4. Summarizer

Summarizer bertugas mengubah kumpulan hasil riset menjadi ringkasan bukti yang lebih terstruktur.

Tanggung jawab utama:
- mengekstrak temuan utama
- membandingkan hasil antar studi
- mencatat kekuatan bukti
- mencatat keterbatasan dan ketidakpastian
- menghasilkan evidence summary

Summarizer harus berhati-hati agar:
- tidak overclaim
- tidak menyamakan studi hewan dengan studi manusia
- tidak menarik kesimpulan di luar data yang tersedia

Output komponen ini:
- evidence summary
- poin utama untuk artikel

File terkait:
- `src/agent/summarizer.py`

### 5. Writer

Writer bertugas mengubah evidence summary menjadi draft artikel yang lebih mudah dipahami pembaca umum.

Tanggung jawab utama:
- membuat pembuka yang ramah
- menjelaskan konteks topik
- menyusun isi artikel berdasarkan bukti
- menjaga bahasa tetap populer tetapi akurat
- menambahkan penutup dan referensi

Writer bukan bertugas menciptakan klaim baru, melainkan mengkomunikasikan hasil sintesis secara jelas.

Output komponen ini:
- draft artikel gaya Medium

File terkait:
- `src/agent/writer.py`

## Supporting Components

### 6. Tools Layer

Tools layer berisi fungsi atau modul pendukung yang dipakai oleh agent.

Contoh tools:
- pencarian jurnal
- parsing metadata artikel
- pengelolaan referensi
- formatting output

File terkait:
- `src/tools/journal_search.py`
- `src/tools/parser.py`
- `src/tools/reference_manager.py`

Tujuan pemisahan tools:
- memisahkan logika agent dari logika utilitas
- memudahkan pengujian
- memudahkan penggantian implementasi di masa depan

### 7. Data Layer

Data layer menyimpan data input, bahan mentah, dan hasil olahan.

Contoh struktur:
- `data/topics/` untuk backlog topik
- `data/raw/` untuk hasil mentah pencarian atau ekstraksi
- `data/processed/` untuk data yang sudah dibersihkan atau disusun

Tujuan:
- menjaga data terorganisir
- memisahkan data dari source code
- mempermudah reproduksibilitas proses

### 8. Output Layer

Output layer menyimpan hasil akhir project.

Contoh:
- `outputs/summaries/`
- `outputs/drafts/`

Jenis output:
- research notes
- evidence summaries
- draft artikel

Dengan pemisahan ini, hasil kerja agent lebih mudah diperiksa dan direvisi.

### 9. Configuration Layer

Configuration layer menyimpan pengaturan project.

Contoh:
- `config/settings.example.yaml`
- `config/prompts.yaml`

Yang bisa disimpan di sini:
- jumlah minimum sumber
- gaya output
- aturan prompt
- parameter workflow

Tujuannya agar pengaturan tidak tersebar di banyak file kode.

## Data Flow

Berikut alur data utama dalam sistem:

1. pengguna atau backlog memberikan topik
2. planner menyusun langkah kerja
3. researcher mencari dan menyaring jurnal
4. summarizer mengekstrak dan menyusun evidence summary
5. writer membuat draft artikel populer
6. hasil disimpan ke folder output
7. manusia melakukan review sebelum publikasi

Representasi singkat:

`Input Topic -> Plan -> Search -> Filter -> Summarize Evidence -> Write Draft -> Review`

## Safety as a Cross-Cutting Layer

Dalam project ini, safety bukan hanya satu file atau satu modul, tetapi prinsip yang harus berlaku di semua komponen.

Contoh penerapan safety:
- researcher memprioritaskan sumber ilmiah
- summarizer menandai bukti lemah
- writer menghindari bahasa yang terlalu pasti
- human review memeriksa potensi overclaim

Artinya, safety berjalan melintasi seluruh arsitektur.

Lihat juga:
- `docs/safety.md`

## Human-in-the-Loop

Meskipun sistem ini bersifat agentic, keputusan akhir tetap berada pada manusia.

Human review diperlukan untuk:
- memverifikasi interpretasi jurnal
- memeriksa kualitas tulisan
- menghindari klaim yang menyesatkan
- memastikan output layak dipublikasikan

Pendekatan ini dipilih karena domain kesehatan memerlukan kehati-hatian yang lebih tinggi dibanding domain umum.

## Minimal Viable Architecture

Untuk versi awal, implementasi tidak perlu langsung kompleks.

Versi minimal cukup memiliki:

- satu input topic
- satu researcher sederhana
- satu summarizer sederhana
- satu writer sederhana
- penyimpanan output
- review manual

Arsitektur minimal:

`Topic -> Researcher -> Summarizer -> Writer -> Output`

Planner dan tools layer bisa dibuat sederhana terlebih dahulu lalu ditingkatkan secara bertahap.

## Future Extensions

Jika project berkembang, arsitektur ini bisa ditambah dengan:

- ranking jurnal otomatis
- scoring kualitas bukti
- citation formatting otomatis
- template artikel untuk berbagai gaya tulisan
- multi-agent workflow
- integrasi dengan CMS atau Medium publishing pipeline
- dashboard untuk memantau status topik

Namun untuk tahap awal, fokus utama tetap:
- kejelasan alur
- akurasi ilmiah
- kemudahan belajar
- keamanan output

## Summary

Arsitektur **Health-Journal-Summarizer** dibangun sebagai sistem modular sederhana dengan empat peran utama:

- planner
- researcher
- summarizer
- writer

Didukung oleh tools, data storage, output storage, configuration, dan human review.

Pendekatan ini membantu project tetap:
- mudah dipahami
- aman untuk pemula
- cocok untuk domain kesehatan
- siap dikembangkan secara bertahap