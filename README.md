🔐 Cryptography with Python
A comprehensive cryptographic toolkit demonstrating essential security operations including file hashing, encryption/decryption, and password management.

Features
File Integrity Verification - Hash files using SHA-256 and compare to detect modifications
AES Encryption/Decryption - Symmetric encryption for secure data protection
RSA Encryption/Decryption - Asymmetric encryption for public-key cryptography
Password Management - Securely hash and verify passwords with industry-standard algorithms
Interactive CLI - User-friendly command-line interface for all cryptographic operations
Technology Stack
Python 3.x
cryptography - Industry-standard cryptographic library
bcrypt - Secure password hashing
zxcvbn - Password strength estimation
Installation

pip install -r requirements.txt
Usage

python main.py
Select from the interactive menu:

Hash a file (SHA-256)
Verify file integrity
AES Encrypt/Decrypt
RSA Encrypt/Decrypt
Password manager
Project Structure

├── main.py                 # Main application entry point├── modules/│   ├── hash.py            # File hashing and integrity verification│   ├── encryption.py      # AES and RSA encryption/decryption│   └── password.py        # Password management utilities├── sample files/          # Test SVG files for integrity verification└── requirements.txt       # Python dependencies
Security Note
This project is for educational purposes. For production use, follow additional security best practices and conduct proper security audits.

