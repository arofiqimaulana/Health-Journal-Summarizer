# Workflow

Dokumen ini menjelaskan alur kerja utama project **Health-Journal-Summarizer**, yaitu proses mengubah satu topik kesehatan menjadi ringkasan berbasis jurnal ilmiah dan draft artikel bergaya Medium.

## Tujuan Workflow

Workflow ini dirancang untuk:

- mengambil satu topik kesehatan dari daftar topik
- mencari referensi dari jurnal ilmiah yang relevan
- merangkum temuan utama secara akurat
- menilai kekuatan dan keterbatasan bukti
- menghasilkan draft artikel populer yang mudah dipahami pembaca umum

## Gambaran Umum

Alur kerja utama project ini terdiri dari 6 tahap:

1. memilih topik
2. mencari jurnal ilmiah
3. menyaring dan memilih sumber
4. mengekstrak temuan utama
5. menyusun evidence summary
6. menulis draft artikel gaya Medium

## 1. Topic Selection

Project dimulai dengan memilih satu topik dari daftar topik yang tersedia, misalnya dari file:

- `data/topics/science-topics.json`

Contoh topik:

- manfaat jalan kaki setelah makan
- pengaruh kurang tidur terhadap hormon lapar
- hubungan olahraga ringan dan kontrol gula darah

Output tahap ini:
- satu topik yang jelas dan cukup spesifik untuk diteliti

## 2. Journal Search

Setelah topik dipilih, sistem mencari jurnal ilmiah yang relevan.

Prioritas sumber:

- systematic review
- meta-analysis
- randomized controlled trial
- cohort study
- case-control study

Tujuan tahap ini:
- menemukan beberapa referensi ilmiah yang relevan
- menghindari sumber non-ilmiah sebagai referensi utama
- mengumpulkan metadata penting seperti judul, penulis, tahun, dan tautan

Output tahap ini:
- daftar awal jurnal ilmiah yang relevan

## 3. Source Filtering

Tidak semua jurnal yang ditemukan akan dipakai.

Pada tahap ini, sumber disaring berdasarkan:

- relevansi terhadap topik
- jenis studi
- kualitas bukti
- tahun publikasi
- kejelasan temuan
- kecocokan dengan target pembaca umum

Jika ada sumber dengan bukti lemah atau konteks yang terlalu sempit, sumber tersebut bisa ditandai atau tidak diprioritaskan.

Output tahap ini:
- daftar sumber terpilih yang akan dipakai untuk sintesis

## 4. Information Extraction

Setelah sumber dipilih, sistem mengekstrak informasi penting dari setiap jurnal, seperti:

- tujuan studi
- metode penelitian
- populasi yang diteliti
- hasil utama
- keterbatasan studi
- kekuatan bukti
- catatan penting atau potensi bias

Tujuan tahap ini adalah mengubah isi jurnal menjadi catatan riset yang lebih terstruktur.

Output tahap ini:
- research notes untuk tiap sumber

## 5. Evidence Summary

Research notes dari beberapa jurnal kemudian digabung menjadi satu ringkasan bukti.

Pada tahap ini, sistem menyusun:

- temuan yang konsisten antar studi
- temuan yang berbeda atau bertentangan
- tingkat kekuatan bukti
- area yang masih belum pasti
- keterbatasan umum dalam literatur

Prinsip utama tahap ini:
- tidak melebih-lebihkan hasil studi
- tidak menarik kesimpulan di luar bukti
- membedakan bukti kuat dan bukti awal

Output tahap ini:
- evidence summary yang akurat dan ringkas

## 6. Medium Draft Writing

Evidence summary kemudian diubah menjadi draft artikel populer dengan gaya yang lebih ramah pembaca umum.

Draft artikel sebaiknya memiliki struktur seperti ini:

- judul
- pembuka yang menarik
- penjelasan singkat konteks topik
- inti temuan dari jurnal
- keterbatasan atau catatan kehati-hatian
- penutup
- daftar referensi

Tujuan tahap ini:
- menjaga akurasi ilmiah
- membuat tulisan tetap nyaman dibaca
- menghasilkan draft awal yang bisa diedit manual sebelum dipublikasikan

Output tahap ini:
- draft artikel gaya Medium

## Human Review

Sebelum dipublikasikan, semua hasil tetap perlu direview oleh manusia.

Hal yang harus diperiksa:

- apakah interpretasi jurnal sudah akurat
- apakah ada overclaim
- apakah bahasa terlalu pasti padahal buktinya masih lemah
- apakah referensi sudah sesuai
- apakah tulisan aman untuk pembaca umum

Human review sangat penting, terutama karena topik project ini berada di domain kesehatan.

## Workflow Summary

Secara ringkas, alur project ini adalah:

`Topik -> Cari Jurnal -> Filter Sumber -> Ekstrak Temuan -> Ringkas Bukti -> Tulis Draft -> Review Manual`

## Output Akhir

Untuk setiap topik, project ini diharapkan menghasilkan:

- daftar referensi ilmiah
- research notes
- evidence summary
- draft artikel gaya Medium

## Catatan Penting

Project ini tidak bertujuan memberikan diagnosis, terapi, atau saran medis personal.

Fungsi utamanya adalah membantu proses belajar, sintesis literatur, dan penulisan konten kesehatan berbasis jurnal ilmiah secara lebih terstruktur.