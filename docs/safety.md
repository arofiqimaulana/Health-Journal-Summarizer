# Safety Guidelines

Dokumen ini menjelaskan prinsip keamanan, kehati-hatian, dan batasan penggunaan untuk project **Health-Journal-Summarizer**.

Karena project ini bekerja di domain kesehatan, akurasi dan kehati-hatian lebih penting daripada kecepatan atau gaya penulisan.

## Tujuan Safety

Safety guidelines ini dibuat untuk:

- mengurangi risiko misinformasi kesehatan
- mencegah overclaim dari hasil studi ilmiah
- menjaga agar output tetap sesuai dengan kekuatan bukti
- memastikan project tidak diposisikan sebagai pengganti tenaga medis profesional

## Core Principles

Project ini harus selalu mengikuti prinsip berikut:

- utamakan akurasi dibanding kecepatan
- utamakan kehati-hatian dibanding klaim yang terdengar meyakinkan
- utamakan bukti ilmiah dibanding opini atau popularitas
- nyatakan ketidakpastian jika bukti belum kuat
- hindari menyederhanakan hasil studi secara berlebihan

## Allowed Sources

Sumber utama yang boleh diprioritaskan:

- peer-reviewed journal articles
- systematic reviews
- meta-analyses
- randomized controlled trials
- cohort studies
- case-control studies
- official medical or public health organizations, hanya sebagai sumber pendukung

Sumber yang tidak boleh dijadikan dasar utama:

- blog pribadi
- thread media sosial
- konten promosi suplemen atau produk kesehatan
- artikel populer tanpa referensi ilmiah yang jelas
- testimoni pribadi

## Evidence Hierarchy

Saat beberapa jenis sumber tersedia, prioritaskan sumber dengan kekuatan bukti yang lebih tinggi.

Urutan prioritas umum:

1. systematic review dan meta-analysis
2. randomized controlled trial
3. cohort study
4. case-control study
5. cross-sectional study
6. animal study
7. in vitro or mechanistic study

Jika bukti utama hanya berasal dari studi hewan, studi sel, atau studi awal, hal tersebut harus disebutkan dengan jelas di output.

## Medical Safety Boundaries

Project ini tidak boleh:

- memberikan diagnosis medis
- memberikan resep pengobatan
- menggantikan konsultasi dokter atau tenaga kesehatan profesional
- memberikan saran medis personal berdasarkan kondisi individu
- menyatakan bahwa suatu intervensi pasti efektif tanpa dukungan bukti kuat

Output project harus diposisikan sebagai:
- ringkasan literatur
- bahan belajar
- draft konten edukasi
- bukan nasihat medis individual

## Overclaim Prevention

Sistem harus menghindari klaim seperti:

- “terbukti pasti”
- “pasti menyembuhkan”
- “selalu efektif”
- “tidak ada risiko”
- “ini solusi terbaik untuk semua orang”

Sebagai gantinya, gunakan bahasa yang lebih aman seperti:

- “beberapa studi menunjukkan”
- “terdapat indikasi bahwa”
- “bukti saat ini mendukung”
- “hasilnya masih terbatas”
- “masih diperlukan penelitian lebih lanjut”

## Human vs Animal vs Early Evidence

Output harus membedakan dengan jelas apakah temuan berasal dari:

- studi pada manusia
- studi pada hewan
- studi laboratorium atau in vitro
- studi observasional
- uji klinis
- meta-analysis atau systematic review

Jangan menyampaikan hasil studi hewan seolah-olah sudah terbukti berlaku langsung pada manusia.

## Uncertainty Handling

Jika literatur tidak konsisten atau bukti lemah, sistem harus:

- menyebutkan bahwa hasil masih campuran
- tidak memaksa satu kesimpulan final
- menjelaskan keterbatasan studi
- menandai area yang masih membutuhkan riset lanjutan

Jika tidak cukup sumber berkualitas, sistem harus lebih baik mengatakan:
- bukti belum cukup
- data masih terbatas
- belum ada konsensus yang jelas

Daripada membuat kesimpulan yang terlalu percaya diri.

## Writing Safety for Public Audience

Karena output akhir ditujukan untuk pembaca umum, sistem harus:

- menggunakan bahasa yang mudah dipahami
- tetap menjaga akurasi makna ilmiah
- menghindari judul clickbait
- tidak menakut-nakuti pembaca
- tidak mendorong self-diagnosis
- tidak mendorong self-medication

## Reference Transparency

Setiap ringkasan sebaiknya menyertakan:

- daftar referensi utama
- jenis studi
- tahun publikasi
- catatan singkat jika bukti masih lemah atau terbatas

Transparansi sumber penting agar pembaca dan penulis dapat memverifikasi klaim utama.

## Human Review Requirement

Semua output harus direview manusia sebelum dipublikasikan.

Checklist review manual:

- apakah sumber benar-benar ilmiah
- apakah kesimpulan sesuai dengan isi studi
- apakah ada klaim yang terlalu mutlak
- apakah perbedaan kekuatan bukti sudah dijelaskan
- apakah ada kalimat yang bisa disalahartikan sebagai nasihat medis

Human review adalah lapisan safety utama dari project ini.

## Scope Limitation

Project ini cocok untuk:

- rangkuman literatur kesehatan
- edukasi umum
- draft artikel populer berbasis jurnal
- bahan belajar pribadi

Project ini tidak cocok untuk:

- pengambilan keputusan medis klinis
- diagnosis personal
- triase pasien
- rekomendasi terapi individual
- respons darurat kesehatan

## Recommended Disclaimer

Gunakan disclaimer seperti ini pada README atau output publik:

> Konten ini disusun untuk tujuan edukasi dan ringkasan literatur ilmiah. Konten ini bukan nasihat medis, diagnosis, atau pengganti konsultasi dengan tenaga kesehatan profesional.

## Final Principle

Jika ada konflik antara tulisan yang terdengar menarik dan tulisan yang akurat, pilih yang akurat.

Jika ada konflik antara kesimpulan yang tegas dan bukti yang terbatas, pilih kejujuran tentang keterbatasan bukti.