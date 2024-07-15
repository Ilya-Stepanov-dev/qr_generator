from src import create_mac_adress
import segno as qr

count = int(input("enter first count: "))

while True:
    mac_str = create_mac_adress(count)
    path = f"qr_png\{count}.png"
    qrcode = qr.make_qr(mac_str)
    qrcode.save(path, scale=4)
    qrcode.show()
    input()
    count += 1
