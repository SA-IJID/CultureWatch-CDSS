# CultureWatch-CDSS
> Clinical Decision Support System (CDSS) for Traditional Diagnostic Bacteriology Workflows

CultureWatch-CDSS is an interactive, expert-system-style diagnostic utility written in Python. It mirrors the chronological, multi-phase progression of a traditional clinical microbiology laboratory bench to systematically isolate, evaluate, and identify pathogenic bacteria from culture specimens.

By guiding users through structured phenotypic matching matrices and deterministic biochemical flowcharts, CultureWatch bridges traditional manual laboratory methodologies with computational logic. All biochemical identification rules, critical cellular traits, and empirical antibiotic suggestions are closely aligned with standard Clinical and Laboratory Standards Institute (CLSI) protocols.

---

## 🔬 Repository Architecture & Project Variations

To maximize both educational value and advanced software design, this repository provides two distinct architectural setups of the application side-by-side:

`text
CultureWatch-CDSS/
├── README.md
│
├── 1_standalone_phases/               # Educational Modules (Independent Scripts)
│   ├── phase_1_colonial_morphology.py
│   ├── phase_2_gram_stain.py
│   └── phase_3_biochemical_identification.py
│
└── 2_integrated_system/               # Automated Pipeline (Combined Workflow)
    ├── cdss_main.py                   # Central Application Orchestrator
    ├── phase_1_colonial_morphology.py
    ├── phase_2_gram_stain.py
    └── phase_3_biochemical_identification.py
