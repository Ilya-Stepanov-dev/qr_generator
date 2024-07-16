import flet as ft

class EntryField(ft.Row):
    def __init__(self, text):
        super().__init__()
        self.text_filed = ft.TextField(value=text, text_align=ft.TextAlign.CENTER)
        self.left_button = ft.IconButton(ft.icons.CLEAR, on_click=self.clear_text)
        self.right_button = ft.IconButton(ft.icons.NAVIGATE_NEXT, on_click=self.incrementing_number)
        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.START
        self.controls = [self.left_button, self.text_filed, self.right_button]

    def clear_text(self,e):
        self.text_filed.value = None
        self.update()

    def incrementing_number(self, e):
        self.text_filed.value = str(int(self.text_filed.value) + 1)
        self.update()

class Tabs(ft.Row):
    def __init__(self):
        super().__init__()
        self.tabs = ft.Tabs(selected_index=0,
                            on_change=self.update_tab,
                            tabs=[ft.Tab(text="MAC"), 
                                  ft.Tab(text="ETHER"), 
                                  ft.Tab(text="INTERNET"),
                                  ft.Tab(text="LIST OF RECENT"),
                                  ft.Tab(text="ANY")],
        )
        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.START
        self.controls = [self.tabs]

    def update_tab(self):
        self.update()


class App(ft.Column):
    def __init__(self, text: str):
        super().__init__()
        self.alignment=ft.MainAxisAlignment.START, 
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.entry_field = EntryField(text=text)
        self.tabs = Tabs()

        self.controls = [
            ft.Row(
                controls = [ft.Text(value="QR Generator", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM)],
                alignment = ft.MainAxisAlignment.CENTER,
            ),
            
            self.entry_field,
            self.tabs,
            ft.Column(controls = [img, ft.Text(value="dud")], alignment=ft.MainAxisAlignment.START, horizontal_alignment = ft.CrossAxisAlignment.CENTER)
        ]