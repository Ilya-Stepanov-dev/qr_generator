import flet as ft
from src import create_qr as cr_qr
from src import create_mac_qr as cr_qr_mac
# from src import save_counter

from application_classes import EntryField, Tabs, MainColumn, Text, Image, History

class App(ft.Column):
    def __init__(self, text: str):
        super().__init__()
        self.alignment=ft.MainAxisAlignment.START, 
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.entry_field = EntryField(text=text, func_left_button=self.clear_text, func_right_button=self.create_qr)
        self.row_tabs = Tabs(func_on_change=self.func_on_change_tab)
        self.main_column = MainColumn("qr_default\\welcome.png", "Welcome to the QR Generator")
        self.history = History(self.view_history)

        self.controls = [
            ft.Row(
                controls = [ft.Text(value="QR Generator", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM)],
                alignment = ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(height=20),
            self.entry_field,
            self.row_tabs,
            self.main_column,
            ft.Row(height=10),
            self.history,
        ]

    def view_history(self, file_name):
        self.main_column.change_controls([Image(f"qr_png\{file_name}"), ft.Row(height=20), Text(file_name)])

    def clear_text(self,e):
        self.entry_field.text_filed.value = None
        self.update()

    def create_qr(self,e):
        qr = None
        num_tab = self.row_tabs.num_tab
        if num_tab == 1 or num_tab == 2:
            return 0
        else:
            value = self.entry_field.text_filed.value
            if num_tab == 0:
                qr = cr_qr_mac(value=int(value))
                self.entry_field.incrementing_number()
                self.main_column.update_mac_content(img_path=qr['file_name'], text=qr['value'])
            elif num_tab == 3:
                qr = cr_qr(value=value)
                self.main_column.update_any_content(img_path=qr['file_name'], text=qr['value'])
            self.history.update_content()

    
    def func_on_change_tab(self, e):
        self.row_tabs.num_tab = self.row_tabs.tabs.selected_index
        num_tab = self.row_tabs.num_tab
        if num_tab == 0:
            self.entry_field.change_to_mac()
            self.main_column.change_controls_to_mac()
        elif num_tab == 1:
            self.main_column.change_controls_to_ether()
        elif num_tab == 2:
            self.main_column.change_controls_to_internet()            
        elif num_tab == 3:
            self.entry_field.change_to_any()
            self.main_column.change_controls_to_any()        
