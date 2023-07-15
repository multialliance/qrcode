import qrcode

# texto a codificar
texto = input("Ingresa el texto que quires convertir: ")

# crea un objeto QRCode
qr = qrcode.QRCode(version=1, box_size=8, border=1)

# agrega los datos a codificar al objeto QRCode
qr.add_data(texto)

# compila el QRCode en una imagen
qr.make(fit=True)

# crea una imagen PIL
img = qr.make_image(fill_color="blue", back_color="white")

# guarda la imagen como un archivo
img.save("codigoqr1.png")
