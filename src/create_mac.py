def create_mac_adress(num):
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
