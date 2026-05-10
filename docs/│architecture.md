
---

## 🚀 Getting Started

### 1. Clone the repository

=============
=    MVP    =
=============

    tts-app/  
    ├── cache/
    │   ├── hash(text)_kokoro.wav
    │   └── hash(text)_piper.wav
    │ 
    ├── config/
    │   └── settings.yaml
    │
    ├── data/
    │   └── text_input.txt
    │
    ├── docs/
    │   └── architecture.md
    │
    ├── core/
    │   ├── models_factory.py # abstract base class or factory
    │   │   │
    │   │   ├── audio_text_extractors/
    │   │   │   └── sample
    │   │   │
    │   │   ├── pronunciation_qualifiter/
    │   │   │   └── sample
    │   │   │
    │   │   └── text_from_image/
    │   │       └── sample
    │   │
    │   └── engines_tss/
    │       ├── piper_engine/
    │       │   ├── venv/
    │       │   ├── voices/
    │       │   └── sample
    │       │
    │       ├── kokoro_engine/
    │       │   ├── venv/
    │       │   ├── voices/
    │       │   └── sample
    │       │
    │       └── coquis_engine/
    │                ├── venv/
    │                ├── voices/
    │                └── sample
    ├── domain/
    │   └── logic.py
    │
    ├── tests/
    │
    ├── Presenters
    │   └── Presenter.py
    │
    ├── resources/
    │   ├── icons/
    │   ├── themes/
    │   └── fonts/
    │
    ├── views/
    │      ├── form.ui
    │      ├── form.py
    │      └── main_window.py
    │       
    │
    ├── third_party_licenses/
    │   └──LGPLv3.txt
    │
    ├── .gitignore
    │
    ├── main.py
    │
    ├── requirements.txt
    │
    └── README.md