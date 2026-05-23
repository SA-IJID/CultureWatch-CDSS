# CultureWatch-CDSS (Standalone Edition)
> Independent Decision Support Modules for Traditional Diagnostic Bacteriology Workflows

CultureWatch-CDSS is a suite of interactive, expert-system-style diagnostic utilities written in Python. It is designed to mirror the chronological benchmarks of a traditional clinical microbiology laboratory bench—allowing laboratory professionals, students, and trainees to evaluate and identify pathogenic bacteria from clinical specimens step-by-step.

Unlike linked pipelines, this version of CultureWatch treats each phase of the diagnostic workflow as a completely independent tool. This standalone architecture is ideal for educational environments, focused bench-work simulations, and reference checks where you only need to evaluate a single testing criterion at a time. All underlying identification mechanics, key physiological traits, and baseline empirical antibiotic selections strictly adhere to Clinical and Laboratory Standards Institute (CLSI) guidelines.

---

## 🗂️ Repository Architecture

Every script file in this repository functions as a completely standalone application. There are no cross-module dependencies or mandatory import hierarchies. 

`text
CultureWatch-CDSS/
├── README.md                           # Project documentation
├── phase_1_colonial_morphology.py       # Standalone Phenotypic Trait Matcher
├── phase_2_gram_stain.py               # Standalone Microscopic Classifier
└── phase_3_biochemical_identification.py # Standalone CLSI Biochemical Trees

