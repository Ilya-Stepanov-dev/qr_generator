import flet as ft
from src import get_counter
from app import App



def main(page: ft.Page):
    page.title = "QR-generator"
    # page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.window.width = 550
    page.window.height = 900

    page.add(App(get_counter()))

ft.app(main)
ft.app(target=main)

# ----------

# def main(page: ft.Page):
#     page.title = "Images Example"
#     page.theme_mode = ft.ThemeMode.LIGHT
#     # page.padding = 50
#     # page.update()

#     img = ft.Image(
#         src=f"qr_png\\1111.png",
#         width=100,
#         height=100,
#         fit=ft.ImageFit.CONTAIN,
#     )

#     page.controls = [
#         ft.Tabs(selected_index=0, 
#             on_change=page.update,
#             animation_duration=500, 
#             tabs=[ft.Tab(text="MAC ADDRESS", 
#                          content=ft.Container(content=ft.Text("This is Tab 1"), alignment=ft.alignment.center)), 
#                 ft.Tab(text="ETHER"), 
#                 ft.Tab(text="INTERNET"),
#                 ft.Tab(text="LIST OF RECENT"),
#                 ft.Tab(text="ANY")],
#             clip_behavior = 0,
#             indicator_tab_size =True,),
#         # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
#         # vertical_alignment=ft.CrossAxisAlignment.CENTER,
#     ]

#     page.add(img)

#     # for i in range(0, 30):
#     #     images.controls.append(
#     #         ft.Image(
#     #             src=f"https://picsum.photos/200/200?{i}",
#     #             width=200,
#     #             height=200,
#     #             fit=ft.ImageFit.NONE,
#     #             repeat=ft.ImageRepeat.NO_REPEAT,
#     #             border_radius=ft.border_radius.all(10),
#     #         )
#     #     )
#     page.update()

# def main(page: ft.Page):

#     img = ft.Image(
#         src=f"qr_png\\1111.png",
#         width=200,
#         height=200,
#         fit=ft.ImageFit.CONTAIN,
#     )

#     t = ft.Tabs(
#         selected_index=1,
#         animation_duration=300,
#         tabs=[
#             ft.Tab(
#                 text="Tab 1",
                # content=ft.Container(
                #     content=ft.Column(controls = [ft.Text(value="dud"), img]), alignment=ft.alignment.center
                # ),
#             ),
#             ft.Tab(
#                 text="Tab 2",
#                 content=ft.Column(controls = [ft.Text(value="dud"), img], alignment=ft.alignment.center
#                 ),
#             ),
#             ft.Tab(
#                 tab_content=ft.Icon(ft.icons.SEARCH),
#                 content=ft.Text("This is Tab 2"),
#             ),
#             ft.Tab(
#                 text="Tab 3",
#                 icon=ft.icons.SETTINGS,
#                 content=ft.Text("This is Tab 3"),
#             ),
#         ],
#         expand=1,
#     )

#     page.add(t)

