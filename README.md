# 📖 ReadItLoud

> Desktop application for language learning through document reading, featuring text-to-speech (TTS), pronunciation feedback, and integrated grammar correction.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/) [![PySide6](https://img.shields.io/badge/PySide6-6.11%2B-green.svg)](https://www.qt.io/qt-for-python) [![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://chat.z.ai/c/ad6d15bb-1bbf-40cf-b197-9b70df3a3211)

---

## 🌟 What is ReadItLoud?

ReadItLoud is a free, open-source desktop application that lets you **learn languages ​​while staying productive**. With ReadItLoud, you can upload your own study materials (academic PDFs, EPUB books, text documents) and simultaneously:

- 📚 Read the document within the interface
- 🔊 Listen to correct pronunciation via text-to-speech
- 🗣️ Practice your own pronunciation with real-time feedback
- ✍️ Receive grammar corrections while writing or reading
- 🌐 Translate text snippets without leaving the app

The project's philosophy is simple: **you shouldn't have to choose between studying for your degree and learning a language—with ReadItLoud, you can do both at the same time.**

------

## ✨ Features

### ✅ Implemented (v0.1 demo)

- 📝 Integrated text editor (5,000 characters)
- 📖 PDF and EPUB reader with built-in web viewer
- 🎵 Audio player (WAV/MP3 files)
- 🌙 Dark/light mode (app and reader)
- 📊 Real-time character counter
- 💾 Import/export text files

## 🚧 In development (architecture ready)

- 🗣️ Speech synthesis (TTS) — Factory pattern architecture
- 🌐 Integrated translation
- ✍️ Grammar correction
- 🎤 Audio transcription
- 🗣️ Pronunciation feedback

------

## 🏗️ Architecture

 ReadItLoud follows a **strict MVC** architecture with design patterns that ensure extensibility:

**Patrones de diseño empleados:**

- **MVC** — Separación estricta de responsabilidades
- **Factory** — `ModelFactory` para crear motores TTS por nombre
- **Abstract Base Class** — `TTSEngine(ABC)` para interfaz uniforme de motores
- **Protocol** — Para `TranslateEngine`, `TranscribeEngine`, `GrammarEngine`
- **Dependency Injection** — `TTSModel.set_tts_engine()` para mantener modelos desacoplados

---

## 🚀 Installation

### Requirements

- Python 3.10
- Refer to requirements.txt and pyproject.toml to more details

### Steps

bash

# 1. Clone the repository

git clone https://github.com/SamanthaVSC/ReadItLoud.git

cd ReadItLoud

# 2. Create virtual environment (recommended)

python -m venv venv

source venv/bin/activate # Linux/macOS

# venv\Scripts\activate # Windows

# 3. Instalar dependencias

pip install -r requirements.txt

# 4. Run the application

python main.py

---

## 📂 Structure of the project

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

---

## 🎯 Use cases

### For university students

> "I have to read an IEEE paper for my engineering class. I upload it to ReadItLoud, listen to the correct pronunciation of technical terms, practice my own pronunciation, and get feedback. I study for my degree **and** improve my English at the same time."

### For researchers

> "I read academic articles in English all day long. ReadItLoud lets me listen to them while taking notes, translate unfamiliar terms without switching apps, and check my grammar when writing abstracts."

### For self-learners

> "I want to learn English, but online courses are expensive and rigid. With ReadItLoud, I can upload English books I already own, listen to the pronunciation, and learn at my own pace."

---

## 🌍 Project philosophy

ReadItLoud was born from the conviction that:

1. **Language learning shouldn't be a luxury** — Commercial apps cost $75–$168/year, making them inaccessible to millions of students in Latin America.
2. **Study materials should be your own** — Not decontextualized phrases, but the actual texts each student needs.
3. **Technological sovereignty matters** — 100% offline processing; no data sent to the cloud, no reliance on foreign companies.
4. **Knowledge should be free** — That’s why it’s licensed under GPL v3: anyone can use, learn from, and improve it, but credit always goes back to the community.

---

## 📜 License

text

ReadItLoud — Desktop application for language learning

Copyright (C) 2026 Samantha Alvarez Hechevarría

This program is free software: you can redistribute it and/or modify

it under the terms of the GNU General Public License as published by

the Free Software Foundation, either version 3 of the License, or

(at your option) any later version.

This program is distributed in the hope that it will be useful,

but WITHOUT ANY WARRANTY; without even the implied warranty of

MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the

GNU General Public License for more details.

You should have received a copy of the GNU General Public License

along with this program. If not, see <https://www.gnu.org/licenses/>.

Ver el archivo [LICENSE](https://choosealicense.com/licenses/gpl-3.0/) para el texto completo de la licencia GPL v3.

---

## 👤 Author

**Samantha Alvarez Hechevarría**

- 📧 Email: [samanthadesktop324@gmail.com](mailto:samanthadesktop324@gmail.com)
- 🐙 GitHub: [@SamanthaVSC](https://github.com/SamanthaVSC)
- 📅 Año de creación: 2026

## 🤝 Contributions

Contributions are welcome. Please read [AUTHORS](https://github.com/SamanthaVSC/AUTHORS) and [NOTICE](https://github.com/SamanthaVSC/NOTICE) before contributing. By submitting a pull request, you agree that your contribution will be licensed under GPL v3.

## 🙏 Acknowledgments

- Global open-source community
- faster_whisper - MIT License
- whisper - (OpenAI) MIT License
- piper tts - MIT License (engine is also available under GPL-3.0; voice models may have other licenses like CC0)
- kokoro - Apache License 2.0
- orpheus - Apache License 2.0 (some variants are under CC-BY-NC 4.0)
- languagetool - GNU Lesser General Public License (LGPL) v2.1+
- argos-translate - Dual-licensed under MIT License or Creative Commons CC0

---

*If ReadItLoud has been useful to you, please share it with someone who is learning a language. That is the best way to give back.* 🌎