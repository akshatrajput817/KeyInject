🔑 KeyInject - Remote Administration Tool
⚠️ IMPORTANT: This tool is for educational and authorized penetration testing ONLY. You must have explicit written permission before using it on any system. Unauthorized access is illegal and unethical.

📋 Table of Contents
Overview
Features
Architecture
Command Reference
Download
Legal Disclaimer
Author
📌 Overview
KeyInject is a feature-rich Remote Administration Tool (RAT) built for educational purposes and authorized penetration testing. It enables you to remotely control a target machine using keyboard injection, command execution, screen capture, and text-to-speech — all over a custom TCP socket connection.

🧠 Perfect for:

Red team assessments
Security research & PoC development
Learning about remote access trojans & C2 architecture
✨ Features


Feature	Description
🎯 Key Press Injection	Simulate single key presses (win, enter, tab, etc.)
⌨️ Keyboard Shortcuts	Execute hotkeys like win+d, alt+f4, ctrl+shift+esc
✍️ Auto Type	Automatically type text on target machine
🖥️ CMD Execution	Run system commands (cmd/PowerShell) on target
🎙️ Text-to-Speech	Make target speak any text aloud
📸 Screenshot Capture	Capture live screenshot of target screen
🔐 Password Protection	Server requires password before accepting commands
🗂️ One-File Executable	Build a standalone .exe via PyInstaller (no console window)
🔄 Cross-Platform Server	Works on Windows & Linux
🏗️ Architecture



┌─────────────────────┐         TCP Socket         ┌─────────────────────┐
│                     │ ◄──────────────────────► │                     │
│   🎮 Client (You)   │        ip:port            │   🖥️ Server (Target)│
│                     │     password auth          │                     │
│  - Send commands    │                            │  - Execute commands │
│  - Receive output   │                            │  - Return results   │
│  - Capture screens  │                            │  - Take screenshots │
└─────────────────────┘                            └─────────────────────┘
🎮 Command Reference


Command	Example	Description
speak <text>	speak Hello from RAT	🔉 Target speaks the text aloud
press <key>	press enter	⌨️ Press a single key (win, enter, tab, esc, shift, ctrl, alt, backspace, space, etc.)
hotkey <k1>+<k2>	hotkey win+d	🔑 Execute keyboard shortcut
write <text>	write Hello World	✍️ Type text automatically
cmd <command>	cmd whoami	💻 Execute system command (cmd/PowerShell)
ss	ss	📸 Capture screenshot (saved as screen.png)
help	help	📖 Show help menu
clear	clear	🧹 Clear terminal
exit	exit	🚪 Disconnect and exit
⌨️ Hotkey Examples


Shortcut	Action
win+d	Show desktop
win+r	Open Run dialog
alt+f4	Close active window
ctrl+shift+esc	Task Manager
win+l	Lock screen
📥 Download
🪟 Windows
bash



# Clone the repository
git clone https://github.com/yourusername/KeyInject.git

# Go to project directory
cd KeyInject

# Install dependencies
pip install -r requirements.txt

# Run the builder
python RAT_Builder.py
🐧 Linux (Kali/Ubuntu)
bash



# Clone the repository
git clone https://github.com/yourusername/KeyInject.git

# Go to project directory
cd KeyInject

# Install dependencies
pip3 install -r requirements.txt

# For pyttsx3 on Linux (optional but recommended)
sudo apt install espeak -y

# Run the builder
python3 RAT_Builder.py
⚖️ Legal Disclaimer



╔══════════════════════════════════════════════════════════════╗
║  ⚠️  LEGAL DISCLAIMER                                        ║
╠══════════════════════════════════════════════════════════════╣
║  This tool is provided for EDUCATIONAL & AUTHORIZED          ║
║  penetration testing purposes ONLY.                          ║
║                                                              ║
║  - Do NOT deploy on systems you do not own                   ║
║  - Do NOT deploy without explicit written permission         ║
║  - Unauthorized access is a CRIMINAL OFFENSE                 ║
║  - The author assumes ZERO liability for misuse              ║
║  - You are responsible for complying with all laws           ║
╚══════════════════════════════════════════════════════════════╝
👨‍💻 Author
Akshat Rajput

🔐 Security Researcher & Penetration Tester
🛠️ Version: 1.2
💻 Working OS: Windows / Linux
⭐ Support
If you find this project useful for your security research, give it a ⭐ on GitHub!
