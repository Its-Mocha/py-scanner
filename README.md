# 🛡️ Python Network Port Scanner

![Language](https://img.shields.io/badge/language-Python%203.9-blue)
![Platform](https://img.shields.io/badge/platform-RHEL%209-red)
![Docker](https://img.shields.io/badge/container-Docker-2496ED)

## 📋 Overview
A lightweight, containerized network scanning utility designed to audit open ports on local or remote servers. 

Built and tested on **Red Hat Enterprise Linux 9**, this tool leverages Python's low-level `socket` library to perform TCP connect scans, useful for verifying firewall rules and service availability in a DevOps environment.

## 🚀 How It Works
* **Input Validation:** The script verifies command-line arguments to ensure a valid target IP is provided.
* **Socket Management:** Utilizes Python Context Managers (`with` statements) to safely handle network resources and prevent memory leaks.
* **Error Handling:** Catches connection timeouts and filtered ports efficiently.

## 🛠️ Usage

### Option 1: Run via Docker (Recommended)
You can run this tool instantly without installing Python, thanks to the Docker image.

```bash
# Build the image
docker build -t my-scanner .

# Scan a target (Replace IP with your target)
docker run --rm my-scanner 192.168.0.1
