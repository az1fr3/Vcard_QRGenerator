import qrcode

# Define la información de contacto y empresa
nombre = "Tu Nombre"
cargo = "Tu Cargo"
telefono = "123-456-7890"
correo = "tu.correo@example.com"
linkedin = "https://www.linkedin.com/in/tu-perfil-linkedin/"
empresa = "Tu Empresa"
imagen_perfil = "https://ejemplo.com/tu-imagen-de-perfil.jpg"  # Cambia esta URL

# Formato vCard
vcard = f"BEGIN:VCARD\nVERSION:3.0\nFN:{nombre}\nORG:{empresa}\nTITLE:{cargo}\nTEL:{telefono}\nEMAIL:{correo}\nURL:{linkedin}\nPHOTO:{imagen_perfil}\nEND:VCARD"

# Crea el objeto QRCode
codigo_qr_contacto = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Agrega la información de contacto al código QR
codigo_qr_contacto.add_data(vcard)
codigo_qr_contacto.make(fit=True)

# Crea una imagen del código QR
imagen_qr_contacto = codigo_qr_contacto.make_image(fill_color="black", back_color="white")

# Guarda la imagen en un archivo
imagen_qr_contacto.save("contacto_qr.png")

print("Código QR de contacto generado exitosamente.")
