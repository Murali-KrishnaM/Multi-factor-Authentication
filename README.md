# MFA Lab – TOTP Authentication using Python

This project demonstrates a simple Multi-Factor Authentication (MFA) system using Time-based One-Time Passwords (TOTP). It generates a QR code for enrollment in an authenticator app (Google Authenticator/Authy) and verifies user-entered codes with clock drift tolerance and retry limits.

---

## Features

- Generates a unique TOTP secret.
- Creates a QR code for easy enrollment.
- Verifies 6-digit OTP codes from an authenticator app.
- Allows ±30 seconds clock drift.
- Limits authentication attempts (rate limiting).
- Logs successful and failed attempts.
- Supports secure secret handling via environment variables.

---

## Requirements

- Fedora / Linux system (works on any OS with Python)
- Python 3.9+
- Authenticator app (Google Authenticator, Authy, etc.)

**Python packages:**
- `pyotp`
- `qrcode[pil]`

---

## Setup Instructions

### 1. Setup Environment

Run these commands in your terminal to prepare your workspace:

```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install required dependencies
pip install --upgrade pip
pip install pyotp qrcode[pil]
```

### 2. The Python Implementation (`MFA.py`)

 the code into a file named `MFA.py`. This script handles secret generation, QR code creation, and the verification loop.

---

## How to use this

1.  **Run the script:** ```bash
    python MFA.py
    ```
2.  **Enroll:** Open your authenticator app and scan the generated `totp-qr.png` image.
3.  **Test Failure:** Enter a random 6-digit number to see it logged as a failure in `verification_log.txt`.
4.  **Test Success:** Enter the current code from your app to grant access.
5.  **Test Rate Limit:** Fail 3 times to see the security lockout trigger.

## Deliverables
- **`totp-qr.png`**: The generated QR code.
- **`verification_log.txt`**: Logs showing success, failure, and lockouts.
- **`MFA.py`**: The main source code.

## Author
Murali Krishna M
