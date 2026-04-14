Tentu. Ini isi yang bisa kamu pakai untuk `docs/roadmap.md`:

```md
# Roadmap

Dokumen ini menjelaskan rencana pengembangan project **Health-Journal-Summarizer** secara bertahap.

Roadmap ini dibuat agar pengembangan project tetap realistis, terarah, dan cocok untuk pembelajar agentic AI yang ingin membangun sistem secara perlahan tetapi benar.

## Vision

Tujuan jangka panjang project ini adalah membantu mengubah satu topik kesehatan menjadi:

- ringkasan berbasis jurnal ilmiah
- evidence summary yang hati-hati dan akurat
- draft artikel populer yang siap dikembangkan untuk publikasi

Project ini tidak bertujuan menjadi sistem diagnosis atau pengganti tenaga medis profesional.

## Guiding Principles

Pengembangan project ini mengikuti prinsip berikut:

- mulai dari versi kecil yang benar-benar berjalan
- utamakan akurasi dibanding kompleksitas
- utamakan safety dibanding kecepatan
- utamakan struktur workflow yang jelas
- pertahankan human review sebelum publikasi

## Phase 0 - Documentation Foundation

Fase ini fokus pada membangun fondasi dokumentasi dan struktur project.

### Goals

- membuat struktur folder project
- mendefinisikan workflow utama
- mendefinisikan safety guidelines
- mendokumentasikan arsitektur project
- mendokumentasikan prompt design
- menyiapkan konfigurasi awal
- menyiapkan backlog topik

### Deliverables

- `README.md`
- `docs/index.md`
- `docs/getting-started.md`
- `docs/workflow.md`
- `docs/safety.md`
- `docs/architecture.md`
- `docs/prompts.md`
- `docs/roadmap.md`
- `config/prompts.yaml`
- `config/settings.example.yaml`
- `data/topics/science-topics.json`

### Outcome

Pada akhir fase ini, project sudah:
- punya arah yang jelas
- terdokumentasi dengan baik
- siap masuk ke implementasi awal

## Phase 1 - Manual MVP

Fase ini fokus pada membuat versi paling sederhana yang bisa dipakai dari awal sampai akhir.

### Goals

- memilih satu topik secara manual
- mencari sumber jurnal secara sederhana
- menyusun research notes
- membuat evidence summary
- menghasilkan draft artikel awal

### Deliverables

- `src/main.py`
- `src/agent/researcher.py`
- `src/agent/summarizer.py`
- `src/agent/writer.py`
- output contoh di folder `outputs/`

### Outcome

Pada akhir fase ini, project sudah bisa:
- memproses satu topik
- menghasilkan ringkasan awal
- menghasilkan draft artikel sederhana

Walaupun belum otomatis penuh, workflow utama sudah hidup.

## Phase 2 - Structured Workflow

Fase ini fokus pada membuat alur agent lebih modular dan terstruktur.

### Goals

- menambahkan planner sederhana
- memisahkan tanggung jawab antar komponen
- membuat format output yang lebih konsisten
- menghubungkan config dengan workflow

### Deliverables

- `src/agent/planner.py`
- struktur input-output yang lebih rapi
- integrasi `config/prompts.yaml`
- integrasi `config/settings.example.yaml`

### Outcome

Pada akhir fase ini, project akan:
- lebih mudah dipahami
- lebih mudah diuji
- lebih mudah dikembangkan

## Phase 3 - Research Quality Improvements

Fase ini fokus pada meningkatkan kualitas hasil riset.

### Goals

- memperbaiki pemilihan sumber
- menandai jenis studi
- mencatat keterbatasan studi
- membedakan bukti kuat dan bukti lemah
- mengurangi risiko overclaim

### Deliverables

- filtering sumber yang lebih baik
- format research notes yang lebih lengkap
- evidence summary yang lebih hati-hati
- checklist evaluasi kualitas sumber

### Outcome

Pada akhir fase ini, kualitas ilmiah output menjadi lebih baik dan lebih bertanggung jawab.

## Phase 4 - Writing Quality Improvements

Fase ini fokus pada meningkatkan kualitas draft artikel agar lebih nyaman dibaca dan lebih siap dipublikasikan.

### Goals

- memperbaiki struktur tulisan
- membuat gaya tulisan lebih natural
- menjaga keseimbangan antara akurasi dan keterbacaan
- menambahkan template artikel untuk gaya Medium

### Deliverables

- template draft artikel
- format intro dan closing yang lebih baik
- contoh article draft yang lebih matang
- script export draft jika diperlukan

### Outcome

Pada akhir fase ini, hasil artikel akan:
- lebih enak dibaca
- lebih dekat ke format publikasi nyata
- membutuhkan lebih sedikit edit manual

## Phase 5 - Testing and Reliability

Fase ini fokus pada stabilitas sistem.

### Goals

- menambahkan unit tests dasar
- menguji alur untuk beberapa topik
- menangani error input
- menangani sumber yang tidak relevan atau lemah
- meningkatkan konsistensi hasil

### Deliverables

- `tests/test_planner.py`
- `tests/test_researcher.py`
- `tests/test_summarizer.py`
- beberapa test case end-to-end sederhana

### Outcome

Pada akhir fase ini, project akan:
- lebih stabil
- lebih mudah dipelihara
- lebih mudah diperbaiki saat terjadi bug

## Phase 6 - Topic Backlog Management

Fase ini fokus pada mengelola daftar topik secara lebih rapi.

### Goals

- menambahkan status topik
- menambahkan prioritas topik
- menandai topik yang sudah selesai diproses
- memudahkan pemilihan topik berikutnya

### Deliverables

- struktur topik yang lebih kaya metadata
- pembaruan pada `science-topics.json`
- script sederhana untuk memilih topik

### Outcome

Pada akhir fase ini, backlog ide konten akan lebih terorganisir dan lebih mudah dipakai untuk workflow rutin.

## Phase 7 - Advanced Features

Fase ini hanya dikerjakan setelah fondasi project benar-benar cukup kuat.

### Possible Features

- ranking jurnal otomatis
- scoring kualitas bukti
- formatting sitasi otomatis
- review pass tambahan sebelum draft final
- integrasi dengan sistem publishing
- multi-agent orchestration
- dashboard status topik

### Outcome

Project menjadi lebih kuat dan lebih nyaman dipakai, tetapi tanpa mengorbankan prinsip utama: akurasi, safety, dan kejelasan.

## Non-Goals

Agar project tetap fokus, berikut beberapa hal yang bukan target utama saat ini:

- diagnosis medis personal
- rekomendasi terapi individual
- chatbot medis publik
- triase atau penanganan kasus klinis
- publikasi otomatis penuh tanpa review manusia
- sistem agent yang terlalu kompleks sejak awal

## Success Criteria

Project dianggap berjalan ke arah yang benar jika:

- satu topik bisa diproses dari awal sampai draft akhir
- sumber ilmiah yang digunakan jelas
- evidence summary tidak overclaim
- draft artikel mudah dibaca
- semua hasil tetap direview manusia sebelum dipublikasikan

## Current Priority

Prioritas terdekat project ini:

1. menyelesaikan dokumentasi inti
2. menyiapkan backlog topik
3. membuat MVP manual
4. menghasilkan satu contoh workflow end-to-end

## Final Note

Roadmap ini bersifat hidup dan bisa berubah seiring perkembangan project.

Fokus utama project ini bukan membuat sistem yang terlihat canggih, tetapi membangun sistem yang:
- jelas
- aman
- akurat
- berguna
- realistis untuk dipelajari dan dikembangkan
```