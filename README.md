# 🗣️ ReadItLoud

A desktop application to help people practice reading, improve their listening skills, and refine their pronunciation — powered by offline Text-to-Speech engines.

**Built with Python & PySide6**

---

## ✨ Features

- 📝 **Text Input** — Type or paste text for reading practice with real-time editing
- 🔊 **Offline TTS Playback** — Listen to text read aloud using local engines (no internet required)
- 🎙️ **Voice Selection** — Choose from multiple voices and languages
- ⚙️ **Model Selection** — Automatic or manual TTS engine selection (Piper, Kokoro, Coqui)
- 💾 **Save Audio** — Export generated speech as audio files
- 📊 **Progress Feedback** — Real-time progress indicators during speech generation
- 🎯 **Pronunciation Practice** — Tools to help improve your pronunciation
- 🖼️ **Text from Image** — Extract text from images for reading practice (OCR)

---

## 🏗️ Architecture

ReadItLoud follows **Clean Architecture** principles with **MVP** (Model-View-Presenter) at the UI layer:

```
ReadItLoud/
├── cache/                    # Cached audio files
├── config/
│   └── setting.yaml          # Application configuration
├── core/
│   ├── model_factory.py      # Abstract base class / factory pattern
│   ├── audio_text_extractors/ # Extract text from audio
│   ├── pronunciation_checker/ # Pronunciation evaluation
│   ├── text_from_image/      # OCR text extraction
│   └── engines_tts/          # TTS engine implementations
│       ├── piper_engine/
│       ├── kokoro_engine/
│       └── coqui_engine/
├── domain/
│   └── logic.py              # Business logic (framework-independent)
├── presenters/
│   └── presenter.py          # MVP Presenters
├── views/
│   ├── form.ui               # Qt Designer UI file
│   └── mainwindow.py         # Main window (PySide6)
├── resources/
│   ├── icons/
│   ├── themes/
│   └── fonts/
├── tests/
├── third_party_licenses/
│   └── LGPLv3.txt
├── docs/
│   └── architecture.md
├── data/
│   └── text_input.txt
├── main.py                   # Application entry point
├── pyproject.toml
├── requirements.txt
└── README.md
```

### Key Principles

- **Core logic is independent of UI** — Business rules live in `domain/` and `core/`, never in views
- **MVP at the UI layer** — Views (`PySide6`) are passive; Presenters mediate between View and Model
- **Factory Pattern for TTS engines** — New engines can be added without modifying existing code
- **Offline-first** — All TTS engines run locally; no cloud API calls required

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.10+**
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