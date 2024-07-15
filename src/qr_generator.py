# from src import create_mac_address
import segno as qr

# count = int(input("enter first count: "))

def create_mac_address(num):
    x = 1
    y = 100
    i = None
    mac = list()
    for _ in range(7):
        i = str((num % y) // x)
        if len(i) < 2:
            i = "0" + i
        mac.append(i)
        y = y*100
        x = x*100
    mac.pop()
    mac.reverse()
    print(mac)
    return ":".join(mac)


def create_qr(value, name_file=None):
    if not name_file:
        name_file = f"qr_png\{value}.png"
    else:
        name_file = f"qr_png\{name_file}.png"
    qrcode = qr.make_qr(value)
    qrcode.save(name_file, scale=4)
    # mac_str = create_mac_address(value)

def create_mac_qr(value):
    mac = create_mac_address(value)
    create_qr(value=mac, name_file=value)


create_qr(123)
create_mac_qr(1234)

# while True:
#     mac_str = create_mac_address(count)
#     path = f"qr_png\{count}.png"
#     qrcode = qr.make_qr(mac_str)
#     qrcode.save(path, scale=4)
#     qrcode.show()
#     input()
#     count += 1