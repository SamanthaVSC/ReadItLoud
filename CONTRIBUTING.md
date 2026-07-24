# 🗣️ ReadItLoud

A desktop application to help people practice reading, improve their listening skills, and refine their pronunciation — powered by offline Text-to-Speech engines.

---

## 🏗️ Architecture

ReadItLoud follows **Clean Architecture** principles with **MVP** (Model-View-Presenter) at the UI layer:

```
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
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.10**
- **pip** (Python package manager)
- A virtual environment tool (`venv`, `virtualenv`, or `conda`)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/SamanthaVSC/ReadItLout.git
   cd ReadItLout
   ```

2. **Create and activate a virtual environment**

   ```bash
   # Linux / macOS
   python3 -m venv .venv
   source .venv/bin/activate

   # Windows
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**

   ```bash
   python main.py
   ```

---

## 🤝 Contributing

We welcome contributions of all kinds — bug fixes, features, documentation, translations, and more!

Please read our [**Contributing Guide**](CONTRIBUTING.md) to get started, and our [**Code of Conduct**](CODE_OF_CONDUCT.md) to understand our community standards.

### Quick Start for Contributors

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-new-feature`)
3. Make your changes
4. Run tests if available
5. Commit with a clear message (`git commit -m "Add: my new feature"`)
6. Push to your branch (`git push origin feature/my-new-feature`)
7. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

### Third-Party Licenses

This project uses **PySide6** (Qt for Python), which is licensed under the **GNU Lesser General Public License v3 (LGPLv3)**. See [third_party_licenses/LGPLv3.txt](third_party_licenses/LGPLv3.txt) for the full license text.

As a user of this application, you have the right to replace the PySide6 library with a modified version, in accordance with the LGPLv3 license terms.

---

## 📬 Contact

Have questions, suggestions, or want to collaborate?

- **Email:** samanthadesktop324@email.com
- **GitHub Issues:** [Open an issue](https://github.com/SamanthaVSC/ReadItLout/issues)
