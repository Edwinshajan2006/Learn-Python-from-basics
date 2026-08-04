import qrcode
data = "https://instagram.com/edwi__n"
qr=qrcode.make(data)
# num = 1 
# num=num+1
qr.save("qrcode.png")
print("qr success")