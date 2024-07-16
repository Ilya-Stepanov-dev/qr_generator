import flet as ft

class EntryField(ft.Column):
    def __init__(self, text):
        super().__init__()
        self.text_filed = ft.TextField(value=text, text_align=ft.TextAlign.CENTER)
        self.text = self.text_filed.value
        self.left_button = ft.IconButton(ft.icons.CLEAR, on_click=self.clear_text)
        self.right_button = ft.IconButton(ft.icons.NAVIGATE_NEXT, on_click=self.incrementing_number)
        self.width = 700
        self.alignment = ft.MainAxisAlignment.START
        self.horizontal_alignment = ft.CrossAxisAlignment.START
        self.controls = [
            ft.Row(
                controls=[self.left_button,
                         self.text_filed,
                         self.right_button
                ],
                # horizontal_alignment = ft.CrossAxisAlignment.CENTER
                alignment = ft.MainAxisAlignment.CENTER
            ),
        ] 
    
    def clear_text(self,e):
        # txt_number.value = str(int(txt_number.value) - 1)
        self.text = None
        self.update()

    def incrementing_number(self, e):
        self.text = str(int(self.text) + 1)
        self.update()



def main(page: ft.Page):
    page.title = "QR-generator"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.START


    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=400)

    def clear_text(e):
        # txt_number.value = str(int(txt_number.value) - 1)
        txt_number.value = None
        page.update()

    def incrementing_number(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    # def get_tab_mac_address(text: str, path: str):

    #     text = ft.Text(value=text)
    #     # img = ft.Image(src=path,
    #     #                width=150,
    #     #                height=150,
    #     #                fit=ft.ImageFit.CONTAIN,
    #     #                )
        
    #     return ft.Tab(text = "MAC ADDRESS",
    #                   content=text)
    #                 #   alignment=ft.MainAxisAlignment.CENTER

    # column = ft.Column()

    # column.value.append(ft.Row(
    #                             [   
    #                                 ft.IconButton(ft.icons.CLEAR, on_click=clear_text),
    #                                 txt_number,
    #                                 ft.IconButton(ft.icons.NAVIGATE_NEXT, on_click=incrementing_number),
    #                             ],
    #                             alignment=ft.MainAxisAlignment.CENTER
    #                         ),
    # )

    page.controls = [

        # ft.Row(
        #     [   
        #         ft.IconButton(ft.icons.CLEAR, on_click=clear_text),
        #         txt_number,
        #         ft.IconButton(ft.icons.NAVIGATE_NEXT, on_click=incrementing_number),
        #     ],
        #     alignment=ft.MainAxisAlignment.CENTER
        # ),
        EntryField("0"),

        # ft.Tabs(selected_index=0, 
        #                 on_change=page.update(),
        #                 animation_duration=500, 
        #                 # )
        #                 tabs=[ft.Tab(text="MAC ADDRESS", content=ft.Container(content=ft.Text("This is Tab 1", color="pink600"), alignment=ft.alignment.center, bgcolor="#44CCCC00")), 
        #                       ft.Tab(text="ETHER"), 
        #                       ft.Tab(text="INTERNET"),
        #                       ft.Tab(text="LIST OF RECENT"),
        #                       ft.Tab(text="ANY")],
        #                 clip_behavior = 0,
        #                 indicator_tab_size =True,),
            # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            # vertical_alignment=ft.CrossAxisAlignment.CENTER,
    ]

    page.update()
ft.app(main)
