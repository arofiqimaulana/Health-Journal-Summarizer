## Latar Belakang
Aku ingin merangkum hasil penelitian berdasarkan jurnal ilmiah. Biasanya aku tulis rangkumannya di medium.com. untuk list topik mana saja yang ingin aku teliti aku tempatkan di rofiqi.com/science. 

## Goal
Menggunakan agentic AI yang bisa 
- browsing topik kesehatan di rofiqi.com
- memilih topik kesehatan di rofiqi.com
- mencari sumber referensi ilmiah di web
- merangkum hasil referensi ilmiah tsb
- menulis dan posting otomatis ke medium (optional)

## Input
- Topik
- Target pembaca
- panjang artikel
- jumlan minimum artikel

## Tools
- fetch web
- baca daftar topik
- simpan draft

## Constraint
- sumber utama harus jurnal ilmiah
- tidak memberi diagnosis atau saran medis personal
- tidak overclaim
- wajib menyertakan keterbatasan bukti

## Output
- research notes
- evidence summary
- Medium draft
- references

## Struktur Project Ini

health-journal-summarizer/
├── README.md
├── LICENSE
├── .gitignore
├── docs/
│   ├── index.md
│   ├── getting-started.md
│   ├── architecture.md
│   ├── workflow.md
│   ├── prompts.md
│   ├── safety.md
│   ├── roadmap.md
│   └── examples/
│       ├── example-topic.md
│       ├── example-summary.md
│       └── example-medium-draft.md
├── src/
│   ├── main.py
│   ├── agent/
│   │   ├── planner.py
│   │   ├── researcher.py
│   │   ├── summarizer.py
│   │   └── writer.py
│   ├── tools/
│   │   ├── journal_search.py
│   │   ├── parser.py
│   │   └── reference_manager.py
│   └── models/
│       └── schemas.py
├── data/
│   ├── topics/
│   │   └── science-topics.json
│   ├── raw/
│   └── processed/
├── outputs/
│   ├── summaries/
│   └── drafts/
├── tests/
│   ├── test_planner.py
│   ├── test_researcher.py
│   └── test_summarizer.py
├── scripts/
│   ├── run_topic.py
│   └── export_medium_draft.py
└── config/
    ├── settings.example.yaml
    └── prompts.yaml