import flet as ft

# class TabsName(enum.Enum):
#     MAC = 0
#     ETHER = 1
#     INTERNET = 2
#     ANY = 3

class Tabs(ft.Row):
    def __init__(self, func_on_change):
        super().__init__()
        self.tabs = ft.Tabs(selected_index=0,
                            on_change=func_on_change,
                            tabs=[ft.Tab(text="MAC"), 
                                  ft.Tab(text="ETHER"), 
                                  ft.Tab(text="INTERNET"),
                                  ft.Tab(text="ANY")],
        )
        self.num_tab = 0
        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.START
        self.controls = [self.tabs]