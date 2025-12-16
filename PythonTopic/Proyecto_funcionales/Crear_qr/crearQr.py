import qrcode
import random

data = 'https://www.youtube.com/watch?v=H5PqK9BCbZI'


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image 

img.save("example_qr.png")



# aleatorio = random.randint(1,8)
# colores = ["red" , "black" , "yellow", "blue"]
# for i in range(9):
#     color = random.choice(colores)
#     try:
#         qr.add_data(data)
#         img = qr.make_image(fill_color=color, back_color="white")
#         img.save(f"example_qr{i}.png")
        
#     except NameError:
#         print("errr")
