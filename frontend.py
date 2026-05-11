import flet as ft
import backend

def main(page: ft.Page):
    page.title = "News Explorer"
    page.window.width = 500
    page.window.height = 
    page.scroll = "auto"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_center()
    page.padding=25
    page.bgcolor = "#1E1E2C"

    
    def haber_sayfasi(site_adi):
        page.clean()
        page.add(ft.Text(f"{site_adi} ", size=25, weight="bold"))
        
        yukleme_mesaji = ft.Text("Please wait while news is loading...", color="blue")
        page.add(yukleme_mesaji)
        page.update()
        
        gelen_haberler = backend.haberleri_getir(site_adi)
        

        page.remove(yukleme_mesaji)
        
        for h in gelen_haberler:

            haber_linki = h[1] 
            
            page.add(
                ft.Row([
                    ft.Text(h[0], expand=True, size=14), 
                    ft.IconButton(
                        icon=ft.icons.ARROW_FORWARD, 
                        on_click=lambda e, l=haber_linki: backend.siteyi_ac(l)
                    )
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
            )
        
        page.add(ft.ElevatedButton("BACK", on_click=lambda _: ana_menu()))
        page.update()

    def ana_menu():
        page.clean()
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        
        page.add(
            ft.Text("NEWS EXPLORER", size=30, weight="bold"),
            ft.Row([ft.Text("BBC NEWS", size=20), ft.ElevatedButton("Read Now", on_click=lambda _: haber_sayfasi("BBC"))], alignment="spaceBetween"),
            ft.Row([ft.Text("KARAR NEWS", size=20), ft.ElevatedButton("Read Now", on_click=lambda _: haber_sayfasi("KARAR"))], alignment="spaceBetween"),
            ft.Row([ft.Text("INDEPENDENT NEWS", size=20), ft.ElevatedButton("Read Now", on_click=lambda _: haber_sayfasi("INDEPENDENT"))], alignment="spaceBetween")
        )
        page.update()

    ana_menu()

ft.app(target=main)
