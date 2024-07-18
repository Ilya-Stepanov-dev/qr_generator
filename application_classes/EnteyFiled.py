import flet as ft
from src import save_counter

class EntryField(ft.Row):
    def __init__(self, text ,func_left_button, func_right_button):
        super().__init__()
        self.counter = text
        self.text_filed = ft.TextField(value=text, text_align=ft.TextAlign.CENTER, label="Number MAC to generate QR code", on_focus=self.clear_text)
        self.left_button = ft.IconButton(ft.icons.CLEAR, on_click=func_left_button)
        self.right_button = ft.IconButton(ft.icons.NAVIGATE_NEXT, on_click=func_right_button)
        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.START
        self.controls = [self.left_button, self.text_filed, self.right_button]

    def incrementing_number(self):
        self.text_filed.value = str(int(self.text_filed.value) + 1)
        self.counter = self.text_filed.value
        save_counter(self.text_filed.value)
        self.update()

    def change_text_label(self, text):
        self.text_filed.label = text
        self.update()
    
    def change_to_mac(self):
        self.text_filed.value = self.counter
        self.change_text_label("Number MAC to generate QR code")
    
    def change_to_any(self):
        self.change_text_label("Text to generate QR code")

    def clear_text(self,e):
        self.text_filed.value = None
        self.update()