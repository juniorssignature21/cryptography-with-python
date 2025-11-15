# 🔐 Cryptography with Python

A comprehensive cryptographic toolkit demonstrating essential security operations including file hashing, encryption/decryption, and password management.

## ✨ Features

- **File Integrity Verification** - Hash files using SHA-256 and compare to detect modifications
- **AES Encryption/Decryption** - Symmetric encryption for secure data protection
- **RSA Encryption/Decryption** - Asymmetric encryption for public-key cryptography
- **Password Management** - Securely hash and verify passwords with industry-standard algorithms
- **Interactive CLI** - User-friendly command-line interface for all cryptographic operations

## 🛠 Technology Stack

- **Python 3.x**
- **cryptography** - Industry-standard cryptographic library
- **bcrypt** - Secure password hashing
- **zxcvbn** - Password strength estimation

## 📋 Requirements

See `requirements.txt` for complete dependencies:

```
bcrypt==5.0.0
cffi==2.0.0
cryptography==46.0.3
pycparser==2.23
zxcvbn==4.5.0
```

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/juniorssignature21/cryptography-with-python.git
cd cryptography-with-python
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

Run the application:
```bash
python main.py
```

### Interactive Menu

Once launched, you'll see the following options:

```
Select an option:
1. Hash a file
2. Verify file integrity
3. AES Encrypt/Decrypt
4. RSA Encrypt/Decrypt
5. Password manager
0. Exit
```

### Examples

**Hash a File:**
```
Enter file path: sample files/circle.svg
SHA hash file is: [SHA-256 hash]
```

**Verify File Integrity:**
```
Enter file path 1: sample files/circle.svg
Enter file path 2: sample files/circle.svg
File is intact no modification have been made
```

**AES Encryption:**
```
Enter message: Hello, World!
AES Key: [generated key]
AES ciphertext: [encrypted data]
AES plaintext: [decrypted message]
```

**RSA Encryption:**
```
Enter a message: Secret message
[RSA encrypted and decrypted output]
```

**Password Manager:**
Securely hash and verify passwords with strength analysis.

## 📁 Project Structure

```
cryptography-with-python/
├── main.py                 # Main application entry point
├── modules/
│   ├── hash.py            # File hashing and integrity verification
│   ├── encryption.py      # AES and RSA encryption/decryption
│   └── password.py        # Password management utilities
├── sample files/
│   ├── circle.svg         # Test SVG file for integrity verification
│   └── shapes.svg         # Test SVG file for integrity verification
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── .gitignore             # Git ignore rules
```

## 🔐 Security Note

⚠️ **Educational Purpose**: This project is designed for educational purposes to demonstrate cryptographic concepts and operations. 

For **production use**, please:
- Conduct proper security audits
- Follow industry security best practices
- Implement additional security measures
- Consider using established, battle-tested libraries
- Implement proper key management strategies

## 🎓 Learning Resources

This project demonstrates:
- **Hashing**: SHA-256 algorithm for file integrity
- **Symmetric Encryption**: AES (Advanced Encryption Standard)
- **Asymmetric Encryption**: RSA public-key cryptography
- **Password Security**: Bcrypt hashing and ZXCVBN strength validation

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**juniorssignature21**

---

**Happy Encrypting! 🔒**
