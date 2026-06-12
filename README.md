# 🔑 KeyInject — Remote Administration Tool

<p align="center">
  <img src="https://img.shields.io/badge/Version-v1.2-blue?style=for-the-badge&logo=github" alt="Version">
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey?style=for-the-badge&logo=windows" alt="Platform">
  <img src="https://img.shields.io/badge/Language-Python-yellow?style=for-the-badge&logo=python" alt="Language">
  <img src="https://img.shields.io/badge/License-Educational-red?style=for-the-badge" alt="License">
</p>

---

## 📌 Overview

**KeyInject** is a feature-rich Remote Administration Tool (RAT) built exclusively for **educational purposes and authorized penetration testing**. It enables security professionals to remotely control a target machine using keyboard injection, command execution, screen capture, and text-to-speech capabilities over a secure, custom TCP socket connection.

### 🧠 Core Use Cases
* 🔴 **Red Team Assessments:** Simulating advanced user-interaction attacks.
* 🔬 **Security Research:** Proof-of-Concept (PoC) development for input manipulation.
* 📚 **Academic Learning:** Understanding Command & Control (C2) architecture and socket programming.

---

## ✨ Features

| Category | Feature | Description |
| :--- | :--- | :--- |
| ⌨️ **Input Control** | Key Press Injection | Simulate single key presses (`win`, `enter`, `tab`, etc.) |
| | Keyboard Shortcuts | Execute complex hotkeys like `win+d`, `alt+f4`, `ctrl+shift+esc` |
| | Auto Type | Automatically stream and type long strings of text on the target |
| 💻 **System Execution** | CMD/PowerShell | Execute native system commands directly with standard output return |
| | Text-to-Speech | Invoke system audio to make the target speak any text aloud |
| | Screenshot Capture | Live capture and transmission of the target's primary display |
| 🔒 **Security & Build** | Password Protection | Server-side authentication required before accepting any payload |
| | Standalone Binary | Compiled into a single `.exe` using PyInstaller (hidden console window) |
| | Cross-Platform | Multi-OS compatibility supporting both Windows and Linux environments |

---

## 🎮 Command Reference

| Command | Syntax Example | Action / Description |
| :--- | :--- | :--- |
| `speak` | `speak Hello from RAT` | 🔉 Target plays the specified text via audio |
| `press` | `press enter` | ⌨️ Injects a single keystroke |
| `hotkey` | `hotkey win+d` | 🔑 Triggers multi-key combinations |
| `write` | `write Hello World` | ✍️ Emulates realistic human typing on the target |
| `cmd` | `cmd whoami` | 💻 Runs OS-level shell commands |
| `ss` | `ss` | 📸 Takes a screenshot and saves/transfers it |
| `help` | `help` | 📖 Displays the active terminal help menu |
| `clear` | `clear` | 🧹 Wipes the current terminal screen clear |
| `exit` | `exit` | 🚪 Gracefully terminates the connection and exits |

### 🛠️ Common Hotkey Combinations

* `win+d` ➡️ Show/Hide Desktop
* `win+r` ➡️ Open Run Dialog
* `alt+f4` ➡️ Close Active Window
* `ctrl+shift+esc` ➡️ Launch Task Manager
* `win+l` ➡️ Lock Target Workstation

---

## 📥 Installation & Deployment

### 🪟 Windows Setup
```bash
# Clone the repository
git clone [https://github.com/yourusername/KeyInject.git](https://github.com/yourusername/KeyInject.git)
cd KeyInject

# Install dependencies
pip install -r requirements.txt

# Build the executable
python RAT_Builder.py
