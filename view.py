import flet as ft

from controller import SpellChecker




class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None
        self.__tendina= None
        self.__textIn = None
        self.__type = None
        self.__evevatedBtn = None
        self._output_area = None

        # define the UI elements and populate the page
    def tendina(self):
        return str(self.__tendina.value)
    def textIn(self):
        return str(self.__textIn.value)
    def type(self):
        return str(self.__type.value)
    def elevatedBtn(self):
        return self.__evevatedBtn
    def output_area(self):
        return self._output_area

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )
        self.page.update()
        # Add your stuff here
        self.__tendina = ft.Dropdown(label="choose language", value="english", options=[
        ft.dropdown.Option("english"),
        ft.dropdown.Option("italian"),
        ft.dropdown.Option("spanish")
        ], width=800)
        row1 = ft.Row([self.__tendina])#la Row è una lista di elementi anche eterogenei
        self.page.add(row1)

        self.__type = ft.Dropdown(label="choose modality", value="default", options=[ft.dropdown.Option("default"),
                                                                    ft.dropdown.Option("linear"),
                                                                    ft.dropdown.Option("dicotomic")], width=200)
        self.__textIn = ft.TextField(label="add your sentence here", width=500)

        self.__evevatedBtn = ft.ElevatedButton(text="Spell Check", on_click=self.__controller.handleButton, width=100)
        row2 = ft.Row([self.__type, self.__textIn, self.__evevatedBtn])
        self.page.add(row2)
        self._output_area = ft.ListView(auto_scroll=True)
        self.page.add(self._output_area)

    def update(self):
        self.page.update()

    def setController(self, controller):
        self.__controller = controller

    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
