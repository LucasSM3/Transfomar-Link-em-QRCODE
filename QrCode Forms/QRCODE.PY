import qrcode

# Link que você quer colocar no QR Code
url = "https://forms.office.com/r/u3n528Cj89?origin=lprLink"

# Criação do QR Code
qr = qrcode.QRCode(
    version=1,  # controla o tamanho do QR Code (1 é o menor)
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,  # tamanho de cada quadradinho
    border=4,     # borda
)

qr.add_data(url)
qr.make(fit=True)

# Geração da imagem
img = qr.make_image(fill_color="black", back_color="white")

# Salvar em arquivo
img.save("qrcode_link.png")

print("QR Code gerado e salvo como 'qrcode_link.png'")
