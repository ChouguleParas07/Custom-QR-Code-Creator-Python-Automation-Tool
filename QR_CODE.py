import qrcode
from PIL import Image
from datetime import datetime
import os

# Get link from user
link = input("Enter the link to generate QR code: ").strip()

# Ask if user wants a logo
logo_path = input("Enter path to logo image (press Enter to skip): ").strip() or None

# Create QR code object with custom settings
qr = qrcode.QRCode(
    version=1,  # Controls QR size (1 is smallest, higher = more data)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
    box_size=12,  # Size of each box
    border=4  # Thickness of border
)
qr.add_data(link)
qr.make(fit=True)

# Create image with custom colors
img = qr.make_image(fill_color="blue", back_color="white").convert("RGB")

# Add logo in the center if provided
if logo_path and os.path.exists(logo_path):
    logo = Image.open(logo_path)
    qr_width, qr_height = img.size
    logo_size = qr_width // 4  # 25% of QR code size
    logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
    pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
    img.paste(logo, pos, mask=logo if logo.mode == "RGBA" else None)

# Save with unique filename
filename = f"QR_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
img.save(filename)

print(f"✅ QR Code generated and saved as {filename}")
