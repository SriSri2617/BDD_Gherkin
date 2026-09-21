### 🥒 Behavior-Driven Development (BDD) with Python

This project uses **BDD** to write software tests in plain English. This bridges the gap between technical developers and non-technical business teams.

---

## 🛠️ The 3-Layer Architecture

Every BDD feature is built using a simple **1-2-3 folder structure**:

```text
my_project/
│
├── src/                      # 2. APPLICATION LAYER
│   └── logic.py              #    - Pure Python functions and classes.
│                             #    - The actual product logic.
│
└── features/                 # 1. BEHAVIOR LAYER (Gherkin)
    │   └── project.feature   #    - Written in plain English using Given/When/Then.
    │                         #    - Defines the business requirements.
    │
    └── steps/                # 3. TEST LAYER (The "Glue" Code)
        └── project_steps.py  #    - Maps sentences from the feature file
                              #      directly to the Python functions in src/.

```

1. Temperature conversion :
      
        - The core code is in (`src/temp_conversion`) - contains the mathematical function to convert f to c and c to f
        - The Gherkin specification is in (`features\temp_conversion.feature`)
        - The steps "Glue" is in  (`features/steps/temp_conversion_steps.py`)
        