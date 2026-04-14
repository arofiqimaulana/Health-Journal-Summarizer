# Health Journal Summarizer - Dokumentasi

## Tujuan Dokumentasi
Dokumentasi ini dibuat dengan tujuan untuk memberikan panduan menyeluruh mengenai arsitektur, cara kerja, konfigurasi, dan panduan operasional dari sistem **Health Journal Summarizer**. Dokumentasi ini akan membantu pengembang maupun pengguna untuk memahami bagaimana *AI Agent* bekerja di balik layar dalam memproses dan menghasilkan ringkasan jurnal kesehatan secara terstruktur.

## Gambaran Sistem
**Health SafeArea Journal Summarizer** adalah sebuah sistem pintar berbasis Multi-Agent System yang dirancang untuk melakukan penelusuran, ekstraksi, analisis, dan penyusunan ringkasan atas jurnal-jurnal ilmu kesehatan atau medis yang kompleks. Sistem ini memanfaatkan agen-agen spesifik seperti *Planner*, *Researcher*, *Summarizer*, dan *Writer* yang saling berkolaborasi agar jurnal-jurnal penelitian mentah bisa diubah menjadi artikel paparan atau draf yang lebih mudah dicerna, seperti ringkasan untuk artikel blog atau Medium.

## Daftar Halaman Docs
Berikut adalah panduan lengkap dokumentasi yang dapat Anda eksplorasi:
- [Getting Started](getting-started.md) — Panduan instalasi dan persiapan awal proyek lokal.
- [Architecture](architecture.md) — Penjelasan mendalam mengenai arsitektur perangkat lunak dan interaksi antar agen.
- [Workflow](workflow.md) — Alur kerja sistem mulai dari pra-pemrosesan pencarian jurnal hingga penulisan hasil akhir.
- [Prompts](prompts.md) — Detail tentang set instruksi atau *prompts* utama untuk *LLM* pada masing-masing agen.
- [Safety](safety.md) — Pedoman dan batasan keamanan (*guardrails*) untuk memastikan informasi kesehatan yang diringkas tidak menimbulkan salah tafsir maupun risiko berbahaya.
- [Roadmap](roadmap.md) — Rencana fitur dan pengembangan platform ke depannya.
- **Examples**:
  - [Example Topic](examples/example-topic.md) — Contoh input topik bahasa JSON/Markdown.
  - [Example Summary](examples/example-summary.md) — Contoh hasil ringkasan teknikal dari sistem.
  - [Example Medium Draft](examples/example-medium-draft.md) — Contoh format siap pakai (*draft*) yang telah disusun *Writer*.

## Siapa Target Pengguna Project Ini
Proyek ini dikembangkan terutama untuk berbagai kalangan yang berinteraksi dengan literatur kesehatan dan inovasi AI, seperti:
- **Tenaga Medis & Peneliti**: Dokter atau saintis yang membutuhkan konklusi dan sintesis cepat dari berbagai bahan literatur utama.
- **AI/Software Engineer**: Pengembang piranti lunak yang tertarik untuk mempelajari implementasi agen cerdas yang saling berkolaborasi (bermain peran).
- **Penulis & Content Creator Medis**: Pemerhati kesehatan yang ingin secara otomatis membuat draf materi tertulis berdasarkan jurnal terpercaya.
- **Mahasiswa Kesehatan**: Mahasiswa yang hendak mendapatkan gambaran ringkas referensi literatur dengan lebih mudah.

## Status Pengembangan
Proyek saat ini berada dalam status **Tahap Awal (*Early In-Development*)**. Fokus saat ini adalah memastikan kestabilan dan keakuratan tiap agen utama, membangun alur kerja solid, dan pengujian kualitas *prompt*. Karenanya, mungkin sering terjadi perubahan perombakan arsitektur dan penambahan fitur secara iteratif.
