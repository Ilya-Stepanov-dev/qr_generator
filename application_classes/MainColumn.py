import flet as ft

class Image(ft.Image):
    def __init__(self, src):
        super().__init__()
        self.width = 300
        self.height = 300
        self.fit = ft.ImageFit.CONTAIN
        self.src = src


class Text(ft.Text):
    def __init__(self, text):
        super().__init__()
        self.value = text
        self.scale = 1.5
        self.alignment = ft.MainAxisAlignment.CENTER


class MainColumn(ft.Column):
    def __init__(self, img_path, text):
        super().__init__()
        # self.img_path = img_path
        # self.text_img = text
        self.alignment=ft.MainAxisAlignment.START, 
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.controls = [Image(img_path), ft.Row(height=10), Text(text)]
        self.mac_controls = [Image(img_path), ft.Row(height=10), Text(text)]
        self.ether_controls = [Image("qr_default\\ETHER.png"), ft.Row(height=10), Text("ETHER")]
        self.internet_controls = [Image("qr_default\\lihp08969fkhjgn.png"), ft.Row(height=10), Text("INTERNET")]
        self.any_controls = [Image(img_path), ft.Row(height=10), Text(text)]
        
    def change_controls(self, new_controls):
        self.controls = new_controls
        self.update()

    def change_controls_to_mac(self):
        self.change_controls(self.mac_controls)
    
    def change_controls_to_ether(self):
        self.change_controls(self.ether_controls)

    def change_controls_to_internet(self):
        self.change_controls(self.internet_controls)

    def change_controls_to_any(self):
        self.change_controls(self.any_controls)

    def update_mac_content(self, img_path, text):
        self.mac_controls = [Image(img_path), ft.Row(height=10), Text(text)]
        self.change_controls_to_mac()

    def update_any_content(self, img_path, text):
        self.any_controls = [Image(img_path), ft.Row(height=10), Text(text)]
        self.change_controls_to_any()