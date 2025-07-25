import flet as ft
from datetime import datetime
import random

def main(page: ft.Page):
    page.title = 'мое первое приложение flet'

    page.theme_mode = ft.ThemeMode.DARK
    greeting_text = ft.Text("Привет, мир!")
    history_text = ft.Text('История приветствий')
    greeting_history = []
    name = ('Дмитрий', 'Александр', 'Мария', 'Наталия')

    def hide_history(e):
        history_text.visible = not history_text.visible
        page.update()

    def random_choose_name(e):
        name_input.value = random.choice(name)
        page.update()

    def on_button_click(e):
        name = name_input.value.strip()
        timestamp = datetime.now()
        if name:
            if 12 > timestamp.hour > 6:
                greeting_text.value = f'Доброе утро, {name}'
                greeting_text.color = ft.Colors.YELLOW
            elif 18 > timestamp.hour > 12:
                greeting_text.value = f'Добрый день, {name}'
                greeting_text.color = ft.Colors.ORANGE
            elif 24 > timestamp.hour > 18:
                greeting_text.value = f'Добрый вечер, {name}'
                greeting_text.color = ft.Colors.RED
            else:
                greeting_text.value = f'Доброй ночи, {name}'
                greeting_text.color = ft.Colors.BLUE    
            name_input.value = ''
            # greet_button.text = 'Поздороваться еще раз'
            
            greeting_history.append(f"{timestamp} - {name}")
            history_text.value = 'История приветствии\n' + '\n'.join(greeting_history)
        else:
            greeting_text.value = 'Пожайлуста, введите ваше имя.'

        page.update()
    
    def change_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()

    def clear_history(e):
        greeting_history.clear()
        history_text.value = "История приветствии: "
        page.update()
    
    def cope_greeting(e):
        page.set_clipboard(greeting_text.value)

    clear_button = ft.ElevatedButton("Очистить историю", on_click=clear_history, icon=ft.Icons.DELETE)

    name_input = ft.TextField(label="Введите ваше имя", autofocus=True, on_submit=on_button_click)

    theme_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, tooltip='Сменить тему' , on_click=change_theme)

    hide_history_button = ft.ElevatedButton('Скрыть историю', on_click=hide_history)

    random_name_button = ft.ElevatedButton("Случайное имя", on_click=random_choose_name)

    greet_button = ft.ElevatedButton("Поздороваться ",icon=ft.Icons.HANDSHAKE, on_click=on_button_click)

    copy_button = ft.IconButton(icon=ft.Icons.COPY, tooltip='Копировать', on_click=cope_greeting)

    page.add(ft.Row([theme_button, copy_button, clear_button], alignment=ft.MainAxisAlignment.CENTER),
             ft.Row([greeting_text]),
             name_input,
             ft.Row([greet_button,random_name_button]),
             hide_history_button,
             history_text
             )
    # page.add(greeting_text, name_input, greet_button, theme_button, clear_button , history_text,copy_button)

ft.app(main)
