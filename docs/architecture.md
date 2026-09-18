---

## 🚀 Getting Started

### 1. Clone the repository

=    MVC    =
=============

    ├── app/
    │   ├── controllers/
    │   │   ├── main_controller.py
    │   ├── models/
    │   │   ├── book_model.py
    │   │   ├── document_model.py
    │   │   ├── llm_model.py
    │   │   ├── media_model.py
    │   │   ├── record_model.py
    │   │   ├── theme_model.py
    │   │   └── tts_engine_factory.py
    │   └── views/
    │   ├── main_window.py
    │   ├── mainwindow.ui
    │   ├── mainwindow_ui.py
    │   └── ui_mainwindow.py
    ├── cache/
    │   └── records/
    ├── config/
    │   ├── themes/
    │   │   ├── default.txt
    │   │   ├── templates/
    │   │   │   ├── modern_dark.xml
    │   │   │   └── modern_light.xml
    │   │   └── themes.py
    │   └── wallpapers/
    │   ├── light.jpeg
    │   └── night.jpeg

    ├── cores/
    │   ├── audio qualifiers/
    │   │   └── faster-whisper
    │   ├── audio transcription/
    │   │   └── whisper
    │   ├── Engines/
    │   │   ├── kokoro-tts
    │   │   ├── orpheus
    │   │   └── Piper-tts
    │   ├── Grammar models/
    │   │   └── languagetool
    │   ├── model_factory.py
    │   ├── translation models/
    │   │   ├── argos-translate
    ├── docs/
    │   └── │architecture.md
    ├── AUTHORS
    ├── CONTRIBUTING.md
    ├── CODE_OF_CONDUCT.md
    ├── LICENSE
    ├── main.py
    ├── NOTICE
    ├── pyproject.toml
    ├── README.md
    ├── requirements.txt
    ├── tests/
    ├── third_party_licenses/
    │   └── LGPLv3.txt
    └── uv.lock