import qrcode

url=input("Enter your url")
filename=input("Enter your file name")

if not(filename.endswith(".png")):
    filename=filename+".png"
img=qrcode.make(url)
img.save(filename)