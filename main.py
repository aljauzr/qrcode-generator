import qrcode

# Loop untuk setiap employees_code dari 1 sampai 31
for code in range(1, 32):
    qr = qrcode.make(str(code))  # isi QR adalah string dari code
    filename = f"{code}.jpg"
    qr.save(filename)
    print(f"QR code untuk {code} disimpan sebagai {filename}")