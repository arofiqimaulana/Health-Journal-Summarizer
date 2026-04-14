# Prompts

Dokumen ini menjelaskan desain prompt yang digunakan dalam project **Health-Journal-Summarizer**.

Project ini menggunakan pendekatan modular, di mana setiap komponen agent memiliki tugas yang berbeda. Karena itu, prompt juga dipisahkan berdasarkan peran agar perilaku sistem lebih konsisten dan lebih mudah dikembangkan.

## Why Prompts Matter

Dalam project ini, prompt berfungsi untuk:

- menjelaskan tugas setiap komponen agent
- menjaga fokus tiap tahap workflow
- mengurangi output yang terlalu bebas atau tidak relevan
- membantu sistem tetap akurat dan hati-hati, terutama di domain kesehatan

Prompt yang baik tidak membuat sistem sempurna, tetapi membantu sistem bekerja lebih terarah.

## Prompt Design Principles

Semua prompt dalam project ini sebaiknya mengikuti prinsip berikut:

- jelas tentang tugasnya
- spesifik tentang output yang diharapkan
- membatasi ruang lingkup kerja
- menghindari overclaim
- menyebutkan kehati-hatian ilmiah
- memisahkan fakta, interpretasi, dan ketidakpastian

## Prompt Roles

Project ini memiliki empat peran utama:

1. planner
2. researcher
3. summarizer
4. writer

Masing-masing memiliki tanggung jawab yang berbeda.

---

## 1. Planner Prompt

### Purpose

Planner bertugas menyusun langkah kerja untuk satu topik.

Planner tidak perlu menghasilkan artikel atau ringkasan ilmiah. Fokus utamanya adalah menentukan urutan proses yang harus dijalankan.

### Input

- topik kesehatan
- target output
- batasan jumlah sumber
- aturan keselamatan dasar

### Expected Output

Planner menghasilkan rencana kerja sederhana, misalnya:
- cari 5 sampai 8 jurnal relevan
- prioritaskan meta-analysis dan systematic review
- ekstrak temuan utama
- buat evidence summary
- ubah menjadi draft artikel populer

### Example Prompt

```text
You are a planning agent for a health literature summarization workflow.

Your job is to create a simple step-by-step plan for processing one health topic into:
1. scientific research notes
2. evidence summary
3. a readable Medium-style draft

Rules:
- prioritize scientific journal sources
- keep the workflow concise and practical
- include a step for identifying study limitations
- do not produce the final article
- do not make medical claims

Return a short structured plan.