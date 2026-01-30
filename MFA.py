import pyotp
import qrcode
import time
import os



secret = pyotp.random_base32()
print("Generated Secret (store securely):", secret)

totp = pyotp.TOTP(secret)

uri = totp.provisioning_uri(
    name="student@example.com",
    issuer_name="AD23631-MFA-Lab"
)

qrcode.make(uri).save("totp-qr.png")
print("QR code saved as totp-qr.png")

MAX_ATTEMPTS = 3
attempts = 0

with open("verification_log.txt", "a") as log:
    while attempts < MAX_ATTEMPTS:
        code = input("Enter the 6-digit code: ")

        if totp.verify(code, valid_window=1):
            print("Authentication Successful")
            log.write(f"{time.ctime()} SUCCESS\n")
            break
        else:
            attempts += 1
            print("Invalid code. Attempts left:", MAX_ATTEMPTS - attempts)
            log.write(f"{time.ctime()} FAILURE\n")
    else:
        print("Too many failures — account locked")
        log.write(f"{time.ctime()} ACCOUNT LOCKED\n")

