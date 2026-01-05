import flet as ft
from engine import rsa_engine, aes_engine, blowfish_engine
import os
import hashlib
import json
from pathlib import Path
import webbrowser

def main(page: ft.Page):
    page.window.height=700
    page.window.width=1050
    page.window.icon='vertex.png'
    page.theme_mode=ft.ThemeMode.DARK
    page.theme=ft.Theme(color_scheme_seed="#FF8800")

    with open(Path("docs/basics.md").resolve(), "r", encoding="UTF-8") as basics_markdown_file:
        basics_markdown_text=basics_markdown_file.read()

    with open(Path("docs/about_algorithms.md").resolve(), "r", encoding="UTF-8") as about_algorithms_markdown_file:
        about_algorithms_markdown_text=about_algorithms_markdown_file.read()

    with open(Path("docs/aes.md").resolve(), "r", encoding="UTF-8") as aes_markdown_file:
        aes_markdown_text=aes_markdown_file.read()

    with open(Path("docs/blowfish.md").resolve(), "r", encoding="UTF-8") as blowfish_markdown_file:
        blowfish_markdown_text=blowfish_markdown_file.read()

    with open(Path("docs/rsa.md").resolve(), "r", encoding="UTF-8") as rsa_markdown_file:
        rsa_markdown_text=rsa_markdown_file.read()

    with open(Path("docs/sha256.md").resolve(), "r", encoding="UTF-8") as sha256_markdown_file:
        sha256_markdown_text=sha256_markdown_file.read()

    with open(Path("docs/md5.md").resolve(), "r", encoding="UTF-8") as md5_markdown_file:
        md5_markdown_text=md5_markdown_file.read()

    with open(Path("docs/tips.md").resolve(), "r", encoding="UTF-8") as tips_markdown_file:
        tips_markdown_text=tips_markdown_file.read()

    def open_storage(e):
        global previous
        previous=page.route
        if os.path.exists(Path('files/keys.json').resolve()):
            page.open(storage_password_dialog)
            page.update()
        else:
            page.open(setup_storage_dialog)
            page.update()

    def open_basics(e):
        global previous
        previous=page.route
        page.go("/basics")

    def open_docs(e):
        global previous
        previous=page.route
        page.go("/docs")

    key_button=ft.Container(ft.IconButton(icon=ft.Icons.KEY, on_click=open_storage), width=50, height=50, padding=2)
    docs_button=ft.Container(ft.IconButton(icon=ft.Icons.QUESTION_MARK, on_click=open_docs), width=50, height=50, padding=2)
    home_button=ft.Container(ft.IconButton(icon=ft.Icons.HOME, on_click=lambda e: page.go('/')), width=50, height=50, padding=2)
    appbar=ft.AppBar(title=ft.Text('Vertex Security', weight=ft.FontWeight.BOLD), elevation=2, actions=[docs_button, key_button, home_button], automatically_imply_leading=False, elevation_on_scroll=False)
    

    algorithms_label = ft.Text('Алгоритмы', size=24, weight=ft.FontWeight.BOLD)

    aes_page_button=ft.TextButton(content=ft.Container(content=ft.Text('AES', size=24, weight=ft.FontWeight.BOLD), alignment=ft.alignment.center_left),
            width=170,
            height=50,
            on_click=lambda e: page.go('/aes')
    )

    blowfish_page_button=ft.TextButton(content=ft.Container(content=ft.Text('Blowfish', size=24, weight=ft.FontWeight.BOLD), alignment=ft.alignment.center_left),
            width=170,
            height=50,
            on_click=lambda e: page.go('/blowfish')
    )

    rsa_page_button=ft.TextButton(content=ft.Container(content=ft.Text('RSA', size=24, weight=ft.FontWeight.BOLD), alignment=ft.alignment.center_left),
            width=170,
            height=50,
            on_click=lambda e: page.go('/rsa')
        )
    
    
    sha256_page_button=ft.TextButton(content=ft.Container(content=ft.Text('SHA-256', size=24, weight=ft.FontWeight.BOLD), alignment=ft.alignment.center_left),
            width=170,
            height=50,
            on_click=lambda e: page.go('/sha256')
        )
    
    md5_page_button=ft.TextButton(content=ft.Container(content=ft.Text('MD5', size=24, weight=ft.FontWeight.BOLD), alignment=ft.alignment.center_left),
            width=170,
            height=50,
            on_click=lambda e: page.go('/md5')
        )
    
    side_column = ft.Column(controls=[algorithms_label, aes_page_button, blowfish_page_button, rsa_page_button, sha256_page_button, md5_page_button])




    basics_card=ft.Container(ft.Card(content=ft.Container(ft.Column(controls=[
        ft.Container(content=ft.Text('Изучение основ', weight=ft.FontWeight.BOLD, size=19), alignment=ft.alignment.top_left, padding=ft.padding.only(left=10, right=10, top=7, bottom=1)), 
        ft.Container(content=ft.Text('Основы работы с Vertex', weight=ft.FontWeight.BOLD, size=14.5), alignment=ft.alignment.center_left, padding=ft.padding.only(left=10, right=10, top=1, bottom=1)), 
        ft.Container(content=ft.TextButton(content=ft.Container(content=ft.Text('Начать', size=15, weight=ft.FontWeight.BOLD)), on_click=open_basics), alignment=ft.alignment.bottom_right, padding=ft.padding.only(left=7, right=7, top=1, bottom=7))], 
        expand=True), expand=True), expand=True), width=220, height=130)
    
    docs_card=ft.Container(ft.Card(content=ft.Container(ft.Column(controls=[
        ft.Container(content=ft.Text('Документация', weight=ft.FontWeight.BOLD, size=19), alignment=ft.alignment.top_left, padding=ft.padding.only(left=10, right=10, top=7, bottom=1)), 
        ft.Container(content=ft.Text('Подробная инструкция', weight=ft.FontWeight.BOLD, size=14.5), alignment=ft.alignment.center_left, padding=ft.padding.only(left=10, right=10, top=1, bottom=1)), 
        ft.Container(content=ft.TextButton(content=ft.Container(content=ft.Text('Изучить', size=15, weight=ft.FontWeight.BOLD)), on_click=open_docs), alignment=ft.alignment.bottom_right, padding=ft.padding.only(left=7, right=7, top=1, bottom=7))], 
        expand=True), expand=True), expand=True), width=220, height=130)
    
    github_card=ft.Container(ft.Card(content=ft.Container(ft.Column(controls=[
        ft.Container(content=ft.Text('GitHub проекта', weight=ft.FontWeight.BOLD, size=19), alignment=ft.alignment.top_left, padding=ft.padding.only(left=10, right=10, top=7, bottom=1)), 
        ft.Container(content=ft.Text('Репозиторий', weight=ft.FontWeight.BOLD, size=14.5), alignment=ft.alignment.center_left, padding=ft.padding.only(left=10, right=10, top=1, bottom=1)), 
        ft.Container(content=ft.TextButton(content=ft.Container(content=ft.Text('Перейти', size=15, weight=ft.FontWeight.BOLD)), on_click=lambda e: webbrowser.open("https://github.com/maxstepashka/Vertex-Security")), alignment=ft.alignment.bottom_right, padding=ft.padding.only(left=7, right=7, top=1, bottom=7))], 
        expand=True), expand=True), expand=True), width=220, height=130)

    logo=ft.Container(content=ft.Row([ft.Image(src='vertex.png', width=130, height=130), ft.Text('Vertex Security', size=30, weight=ft.FontWeight.BOLD)]))

    home_column=ft.Container(content=ft.Column(controls=[logo, ft.Row(controls=[basics_card, docs_card, github_card])], alignment=ft.MainAxisAlignment.CENTER), expand=True)




    storage_password_field=ft.TextField(hint_text='Пароль', width=330, password=True)

    setup_storage_password_field=ft.TextField(hint_text='Пароль', width=330, password=True)

    storage_password_dialog = ft.AlertDialog(
            title=ft.Text("Пароль", weight=ft.FontWeight.BOLD),
            content=storage_password_field,
            actions=[ft.TextButton("Отменить", on_click=lambda e: page.close(storage_password_dialog)), ft.TextButton("Подтвердить", on_click=lambda e: derypt_keys())]
        )
    
    setup_storage_dialog = ft.AlertDialog(
            title=ft.Text("Настройка хранилища", weight=ft.FontWeight.BOLD),
            content=ft.Text("Необходимо задать пароль для шифрования."),
            actions=[ft.TextButton("Отменить", on_click=lambda e: page.close(setup_storage_dialog)), ft.TextButton("Настроить", on_click=lambda e: page.open(setup_storage_password_dialog))]
        )
    
    setup_storage_password_dialog=ft.AlertDialog(
            title=ft.Text("Пароль", weight=ft.FontWeight.BOLD),
            content=setup_storage_password_field,
            actions=[ft.TextButton("Отменить", on_click=lambda e: page.close(setup_storage_password_dialog)), ft.TextButton("Подтвердить", on_click=lambda e: setup_keys())]
        )
    


    
    storage_search_field=ft.TextField(hint_text='Запрос', width=600, on_submit=lambda e: storage_search())

    storage_search_button=ft.ElevatedButton(icon=ft.Icons.SEARCH, text='Найти', on_click=lambda e: storage_search())

    storage_clear_button=ft.ElevatedButton(icon=ft.Icons.CLEAR, text='Очистить', on_click=lambda e: storage_clear())


    storage_add_button=ft.ElevatedButton(icon=ft.Icons.ADD, text='Добавить', on_click=lambda e: create_add_block())

    storage_add_type_field=ft.Dropdown(hint_text='Тип', options=[ft.DropdownOption('Связка ключей RSA'), ft.DropdownOption('Публичный ключ RSA'), ft.DropdownOption('Ключ AES'), ft.DropdownOption('Ключ Blowfish'), ft.DropdownOption('Хеш SHA-256'), ft.DropdownOption('Хеш MD5'), ft.DropdownOption('Пароль')], width=330, on_change=lambda e: update_add_block())

    storage_add_name_field=ft.TextField(hint_text='Название', width=330)


    def pick_storage_add_rsa_pub_file(e: ft.FilePickerResultEvent):
        storage_add_rsa_pub_field.value = (
            "".join(map(lambda f: f.path, e.files)) if e.files else None
        )
        page.update()

    def pick_storage_add_rsa_priv_file(e: ft.FilePickerResultEvent):
        storage_add_rsa_priv_field.value = (
            "".join(map(lambda f: f.path, e.files)) if e.files else None
        )
        page.update()

    def pick_storage_add_rsa_pub_single_file(e: ft.FilePickerResultEvent):
        storage_add_rsa_pub_single_field.value = (
            "".join(map(lambda f: f.path, e.files)) if e.files else None
        )
        page.update()

    def pick_storage_add_sha256_file(e: ft.FilePickerResultEvent):
        storage_add_sha256_file_field.value = (
            "".join(map(lambda f: f.path, e.files)) if e.files else None
        )
        page.update()

    def pick_storage_add_md5_file(e: ft.FilePickerResultEvent):
        storage_add_md5_file_field.value = (
            "".join(map(lambda f: f.path, e.files)) if e.files else None
        )
        page.update()

    storage_add_rsa_pub_dialog = ft.FilePicker(on_result=pick_storage_add_rsa_pub_file)
    page.overlay.append(storage_add_rsa_pub_dialog)
    
    storage_add_rsa_priv_dialog = ft.FilePicker(on_result=pick_storage_add_rsa_priv_file)
    page.overlay.append(storage_add_rsa_priv_dialog)

    storage_add_rsa_pub_single_dialog = ft.FilePicker(on_result=pick_storage_add_rsa_pub_single_file)
    page.overlay.append(storage_add_rsa_pub_single_dialog)

    storage_add_sha256_file_dialog = ft.FilePicker(on_result=pick_storage_add_sha256_file)
    page.overlay.append(storage_add_sha256_file_dialog)

    storage_add_md5_file_dialog = ft.FilePicker(on_result=pick_storage_add_md5_file)
    page.overlay.append(storage_add_md5_file_dialog)
    
    storage_add_rsa_pub_button=ft.ElevatedButton(icon=ft.Icons.FOLDER_OPEN, text='Обзор', on_click=lambda e: storage_add_rsa_pub_dialog.pick_files(dialog_title='Файл публичного ключа', allow_multiple=False))

    storage_add_rsa_priv_button=ft.ElevatedButton(icon=ft.Icons.FOLDER_OPEN, text='Обзор', on_click=lambda e: storage_add_rsa_priv_dialog.pick_files(dialog_title='Файл приватного ключа', allow_multiple=False))

    storage_add_rsa_pub_single_button=ft.ElevatedButton(icon=ft.Icons.FOLDER_OPEN, text='Обзор', on_click=lambda e: storage_add_rsa_pub_single_dialog.pick_files(dialog_title='Файл публичного ключа', allow_multiple=False))

    storage_add_sha256_file_button=ft.ElevatedButton(icon=ft.Icons.FOLDER_OPEN, text='Обзор', on_click=lambda e: storage_add_sha256_file_dialog.pick_files(dialog_title='Файл', allow_multiple=False))

    storage_add_md5_file_button=ft.ElevatedButton(icon=ft.Icons.FOLDER_OPEN, text='Обзор', on_click=lambda e: storage_add_md5_file_dialog.pick_files(dialog_title='Файл', allow_multiple=False))

    storage_add_rsa_pub_field=ft.TextField(hint_text='Публичный ключ RSA', width=330)

    storage_add_rsa_priv_field=ft.TextField(hint_text='Приватный ключ RSA', width=330)

    storage_add_rsa_pub_single_field=ft.TextField(hint_text='Публичный ключ RSA', width=330)

    storage_add_sha256_hash_field=ft.TextField(hint_text='Хеш SHA-256', width=330)

    storage_add_sha256_file_field=ft.TextField(hint_text='Путь', width=330)

    storage_add_md5_hash_field=ft.TextField(hint_text='Хеш MD5', width=330)

    storage_add_md5_file_field=ft.TextField(hint_text='Путь', width=330)
    
    storage_add_password_field=ft.TextField(hint_text='Пароль', width=330)

    storage_add_aes_field=ft.TextField(hint_text='Ключ AES', width=330)
    
    storage_add_blowfish_field=ft.TextField(hint_text='Ключ Blowfish', width=330)


    storage_add_submit_button=ft.ElevatedButton(icon=ft.Icons.SAVE, text='Сохранить', on_click=lambda e: storage_add())

    storage_add_cancel_button=ft.ElevatedButton(icon=ft.Icons.CLEAR, text='Отмена', on_click=lambda e: remove_add_block())



    def pick_storage_edit_rsa_pub_file(e: ft.FilePickerResultEvent):
        storage_edit_rsa_pub_field.value = (
            "".join(map(lambda f: f.path, e.files)) if e.files else None
        )
        page.update()

    def pick_storage_edit_rsa_priv_file(e: ft.FilePickerResultEvent):
        storage_edit_rsa_priv_field.value = (
            "".join(map(lambda f: f.path, e.files)) if e.files else None
        )
        page.update()

    def pick_storage_edit_rsa_pub_single_file(e: ft.FilePickerResultEvent):
        storage_edit_rsa_pub_single_field.value = (
            "".join(map(lambda f: f.path, e.files)) if e.files else None
        )
        page.update()

    def pick_storage_edit_sha256_file(e: ft.FilePickerResultEvent):
        storage_edit_sha256_file_field.value = (
            "".join(map(lambda f: f.path, e.files)) if e.files else None
        )
        page.update()

    def pick_storage_edit_md5_file(e: ft.FilePickerResultEvent):
        storage_edit_md5_file_field.value = (
            "".join(map(lambda f: f.path, e.files)) if e.files else None
        )
        page.update()
        

    storage_edit_rsa_pub_dialog = ft.FilePicker(on_result=pick_storage_edit_rsa_pub_file)
    page.overlay.append(storage_edit_rsa_pub_dialog)
    
    storage_edit_rsa_priv_dialog = ft.FilePicker(on_result=pick_storage_edit_rsa_priv_file)
    page.overlay.append(storage_edit_rsa_priv_dialog)

    storage_edit_rsa_pub_single_dialog = ft.FilePicker(on_result=pick_storage_edit_rsa_pub_single_file)
    page.overlay.append(storage_edit_rsa_pub_single_dialog)
    
    storage_edit_sha256_file_dialog = ft.FilePicker(on_result=pick_storage_edit_sha256_file)
    page.overlay.append(storage_edit_sha256_file_dialog)

    storage_edit_md5_file_dialog = ft.FilePicker(on_result=pick_storage_edit_md5_file)
    page.overlay.append(storage_edit_md5_file_dialog)

    storage_edit_rsa_pub_button=ft.TextButton(icon=ft.Icons.FOLDER_OPEN, text='Обзор', on_click=lambda e: storage_edit_rsa_pub_dialog.pick_files(dialog_title='Файл публичного ключа', allow_multiple=False))

    storage_edit_rsa_priv_button=ft.TextButton(icon=ft.Icons.FOLDER_OPEN, text='Обзор', on_click=lambda e: storage_edit_rsa_priv_dialog.pick_files(dialog_title='Файл приватного ключа', allow_multiple=False))

    storage_edit_rsa_pub_single_button=ft.TextButton(icon=ft.Icons.FOLDER_OPEN, text='Обзор', on_click=lambda e: storage_edit_rsa_pub_single_dialog.pick_files(dialog_title='Файл публичного ключа', allow_multiple=False))

    storage_edit_sha256_file_button=ft.ElevatedButton(icon=ft.Icons.FOLDER_OPEN, text='Обзор', on_click=lambda e: storage_edit_sha256_file_dialog.pick_files(dialog_title='Файл', allow_multiple=False))

    storage_edit_md5_file_button=ft.ElevatedButton(icon=ft.Icons.FOLDER_OPEN, text='Обзор', on_click=lambda e: storage_edit_md5_file_dialog.pick_files(dialog_title='Файл', allow_multiple=False))

    storage_edit_rsa_pub_field=ft.TextField(hint_text='Публичный ключ RSA', width=330)

    storage_edit_rsa_priv_field=ft.TextField(hint_text='Приватный ключ RSA', width=330)

    storage_edit_rsa_pub_single_field=ft.TextField(hint_text='Публичный ключ RSA', width=330)

    storage_edit_sha256_hash_field=ft.TextField(hint_text='Хеш SHA-256', width=330)

    storage_edit_sha256_file_field=ft.TextField(hint_text='Путь', width=330)

    storage_edit_md5_hash_field=ft.TextField(hint_text='Хеш MD5', width=330)

    storage_edit_md5_file_field=ft.TextField(hint_text='Путь', width=330)
    
    storage_edit_password_field=ft.TextField(hint_text='Пароль', width=330)

    storage_edit_aes_field=ft.TextField(hint_text='Ключ AES', width=330)

    storage_edit_blowfish_field=ft.TextField(hint_text='Ключ Blowfish', width=330)
     
    def derypt_keys():
        try:
            keys_json=json.loads(aes_engine.decrypt_text(aes_engine.read_file(Path('files/keys.json').resolve()), hashlib.sha256(storage_password_field.value.encode('UTF-8')).hexdigest()).replace('\\', '\\\\'))
            page.close(storage_password_dialog)
            print('PAGE UPDATING')
            page.update()
            make_keys_blocks(keys_json)
            page.go('/key_storage')
        except:
            page.open(ft.SnackBar(content=ft.Text('Неверный пароль.'), show_close_icon=True, bgcolor=ft.Colors.RED))
            page.close(storage_password_dialog)
            print('PAGE UPDATING')
            page.update()

    def setup_keys():
        aes_engine.write_file(Path('files/keys.json').resolve(), aes_engine.encrypt_text("{}", hashlib.sha256(setup_storage_password_field.value.encode('UTF-8')).hexdigest()))
        page.close(setup_storage_password_dialog)
        print('PAGE UPDATING')
        page.update()
        storage_password_field.value=setup_storage_password_field.value
        setup_storage_password_field.value=None
        global storage_listview
        storage_listview=ft.ListView(controls=[ft.Column([ft.Text('Хранилище ключей', weight=ft.FontWeight.BOLD, size=24), ft.Row([storage_search_field, storage_search_button, storage_clear_button]), storage_add_button, ft.Divider()])])
        page.go('/key_storage')

    def make_keys_blocks(keys_json: dict):
        keys_blocks=[]
        global storage_listview
        storage_listview=ft.ListView(controls=[ft.Column([ft.Text('Хранилище ключей', weight=ft.FontWeight.BOLD, size=24), ft.Row([storage_search_field, storage_search_button, storage_clear_button]), storage_add_button, ft.Divider()])])
        for name in keys_json:
            block = {'name': ft.Text(name, weight=ft.FontWeight.BOLD, size=23)}
            match keys_json[name]['type']:
                case 'RSA_PUB':
                    block['type'] = ft.Text('Публичный ключ RSA', weight=ft.FontWeight.BOLD, size=19)
                    block['text'] = ft.Text('Публичный ключ: ' + keys_json[name]['value']['pub'], weight=ft.FontWeight.BOLD, size=18, selectable=True)
                case 'RSA_PAIR':
                    block['type'] = ft.Text('Связка ключей RSA', weight=ft.FontWeight.BOLD, size=19)
                    block['text'] = ft.Text('Публичный ключ: ' + keys_json[name]['value']['pub'] + '\n' + 'Приватный ключ: ' + keys_json[name]['value']['priv'], size=18, weight=ft.FontWeight.BOLD, selectable=True)
                case 'SHA-256':
                    block['type'] = ft.Text('Хеш SHA-256', weight=ft.FontWeight.BOLD, size=19)
                    block['text'] = ft.Text('Хеш: ' + keys_json[name]['value']['hash'] + '\n' + 'Файл: ' + keys_json[name]['value']['file'], weight=ft.FontWeight.BOLD, size=18, selectable=True)
                case 'MD5':
                    block['type'] = ft.Text('Хеш MD5', weight=ft.FontWeight.BOLD, size=19)
                    block['text'] = ft.Text('Хеш: ' + keys_json[name]['value']['hash'] + '\n' + 'Файл: ' + keys_json[name]['value']['file'], weight=ft.FontWeight.BOLD, size=18, selectable=True)
                case 'Password':
                    block['type'] = ft.Text('Пароль', weight=ft.FontWeight.BOLD, size=19)
                    block['text'] = ft.Text('Пароль: ' + keys_json[name]['value']['password'], weight=ft.FontWeight.BOLD, size=18, selectable=True)
                case _:
                    block['type'] = ft.Text('Ключ ' + keys_json[name]['type'], weight=ft.FontWeight.BOLD, size=19)
                    block['text'] = ft.Text('Ключ: ' + keys_json[name]['value']['key'], weight=ft.FontWeight.BOLD, size=18, selectable=True)
                    
            keys_blocks.append(block)
            storage_listview.controls.append(ft.Column([block['name'], block['type'], block['text'], ft.Row([ft.ElevatedButton('Изменить', icon=ft.Icons.EDIT, on_click=lambda e: open_storage_edit(e.control.data), data=name), ft.ElevatedButton('Удалить', icon=ft.Icons.DELETE, color=ft.Colors.RED_500, on_click=lambda e: storage_delete(e.control.data), data=name)]), ft.Divider()]))
        

    def storage_search():
        to_remove=[]
        keys_json=json.loads(aes_engine.decrypt_text(aes_engine.read_file(Path('files/keys.json').resolve()), hashlib.sha256(storage_password_field.value.encode('UTF-8')).hexdigest()).replace('\\', '\\\\'))
        for name in keys_json:
            if storage_search_field.value.lower() not in name.lower():
                to_remove.append(name)
        for name in to_remove:
            keys_json.pop(name)
        make_keys_blocks(keys_json)
        page.views.clear()
        page.views.append(
            ft.View(
                "/key_storage",
                [
                    appbar, ft.Container(storage_listview, expand=8, padding=7)
                ],
            )
        )
        page.update()

    def storage_clear():  
        keys_json=json.loads(aes_engine.decrypt_text(aes_engine.read_file(Path('files/keys.json').resolve()), hashlib.sha256(storage_password_field.value.encode('UTF-8')).hexdigest()).replace('\\', '\\\\'))
        make_keys_blocks(keys_json)
        page.views.clear()
        storage_search_field.value=None
        page.views.append(
            ft.View(
                "/key_storage",
                [
                    appbar, ft.Container(storage_listview, expand=8, padding=7)
                ],
            )
        )
        page.update()

    def storage_delete(name):
        keys_json=json.loads(aes_engine.decrypt_text(aes_engine.read_file(Path('files/keys.json').resolve()), hashlib.sha256(storage_password_field.value.encode('UTF-8')).hexdigest()).replace('\\', '\\\\'))
        keys_json.pop(name)
        aes_engine.write_file(Path('files/keys.json').resolve(), aes_engine.encrypt_text(str(keys_json).replace("'", '"').replace('\\\\', '\\'), hashlib.sha256(storage_password_field.value.encode('UTF-8')).hexdigest()))
        make_keys_blocks(keys_json)
        page.views.clear()
        page.views.append(
            ft.View(
                "/key_storage",
                [
                    appbar, ft.Container(storage_listview, expand=8, padding=7)
                ],
            )
        )
        page.update()

    def create_add_block():
        storage_add_button.visible=False
        storage_listview.controls.insert(1, ft.Column([ft.Text('Добавление', weight=ft.FontWeight.BOLD, size=23), ft.Text('Тип', weight=ft.FontWeight.BOLD, size=18), storage_add_type_field, storage_add_cancel_button, ft.Divider()]))
        page.views.clear()
        page.views.append(
            ft.View(
                "/key_storage",
                [
                    appbar, ft.Container(storage_listview, expand=8, padding=7)
                ],
            )
        )
        page.update()

    def update_add_block():
        match storage_add_type_field.value:
            case 'Связка ключей RSA':
                storage_listview.controls[1]=ft.Column([ft.Text('Добавление', weight=ft.FontWeight.BOLD, size=23), ft.Text('Тип', weight=ft.FontWeight.BOLD, size=18), storage_add_type_field, ft.Text('Название', weight=ft.FontWeight.BOLD, size=18), storage_add_name_field, ft.Text('Значение', weight=ft.FontWeight.BOLD, size=18), ft.Row([storage_add_rsa_pub_field, storage_add_rsa_pub_button]), ft.Row([storage_add_rsa_priv_field, storage_add_rsa_priv_button]), ft.Row([storage_add_submit_button, storage_add_cancel_button]), ft.Divider()])
            case 'Публичный ключ RSA':
                storage_listview.controls[1]=ft.Column([ft.Text('Добавление', weight=ft.FontWeight.BOLD, size=23), ft.Text('Тип', weight=ft.FontWeight.BOLD, size=18), storage_add_type_field, ft.Text('Название', weight=ft.FontWeight.BOLD, size=18), storage_add_name_field, ft.Text('Значение', weight=ft.FontWeight.BOLD, size=18), ft.Row([storage_add_rsa_pub_single_field, storage_add_rsa_pub_single_button]), ft.Row([storage_add_submit_button, storage_add_cancel_button]), ft.Divider()])
            case 'Ключ AES':
                storage_listview.controls[1]=ft.Column([ft.Text('Добавление', weight=ft.FontWeight.BOLD, size=23), ft.Text('Тип', weight=ft.FontWeight.BOLD, size=18), storage_add_type_field, ft.Text('Название', weight=ft.FontWeight.BOLD, size=18), storage_add_name_field, ft.Text('Значение', weight=ft.FontWeight.BOLD, size=18), storage_add_aes_field, ft.Row([storage_add_submit_button, storage_add_cancel_button]), ft.Divider()])
            case 'Ключ Blowfish':
                storage_listview.controls[1]=ft.Column([ft.Text('Добавление', weight=ft.FontWeight.BOLD, size=23), ft.Text('Тип', weight=ft.FontWeight.BOLD, size=18), storage_add_type_field, ft.Text('Название', weight=ft.FontWeight.BOLD, size=18), storage_add_name_field, ft.Text('Значение', weight=ft.FontWeight.BOLD, size=18), storage_add_blowfish_field, ft.Row([storage_add_submit_button, storage_add_cancel_button]), ft.Divider()])
            case 'Хеш SHA-256':
                storage_listview.controls[1]=ft.Column([ft.Text('Добавление', weight=ft.FontWeight.BOLD, size=23), ft.Text('Тип', weight=ft.FontWeight.BOLD, size=18), storage_add_type_field, ft.Text('Название', weight=ft.FontWeight.BOLD, size=18), storage_add_name_field, ft.Text('Значение', weight=ft.FontWeight.BOLD, size=18), storage_add_sha256_hash_field, ft.Row([storage_add_sha256_file_field, storage_add_sha256_file_button]), ft.Row([storage_add_submit_button, storage_add_cancel_button]), ft.Divider()])
            case 'Хеш MD5':
                storage_listview.controls[1]=ft.Column([ft.Text('Добавление', weight=ft.FontWeight.BOLD, size=23), ft.Text('Тип', weight=ft.FontWeight.BOLD, size=18), storage_add_type_field, ft.Text('Название', weight=ft.FontWeight.BOLD, size=18), storage_add_name_field, ft.Text('Значение', weight=ft.FontWeight.BOLD, size=18), storage_add_md5_hash_field, ft.Row([storage_add_md5_file_field, storage_add_md5_file_button]), ft.Row([storage_add_submit_button, storage_add_cancel_button]), ft.Divider()])
            case 'Пароль':
                storage_listview.controls[1]=ft.Column([ft.Text('Добавление', weight=ft.FontWeight.BOLD, size=23), ft.Text('Тип', weight=ft.FontWeight.BOLD, size=18), storage_add_type_field, ft.Text('Название', weight=ft.FontWeight.BOLD, size=18), storage_add_name_field, ft.Text('Значение', weight=ft.FontWeight.BOLD, size=18), storage_add_password_field, ft.Row([storage_add_submit_button, storage_add_cancel_button]), ft.Divider()])
            
        page.views.clear()
        page.views.append(
            ft.View(
                "/key_storage",
                [
                    appbar, ft.Container(storage_listview, expand=8, padding=7)
                ],
            )
        )
        page.update()

    def remove_add_block():
        storage_add_button.visible=True
        storage_listview.controls.pop(1)
        storage_add_type_field.value=None
        page.views.clear()
        page.views.append(
            ft.View(
                "/key_storage",
                [
                    appbar, ft.Container(storage_listview, expand=8, padding=7)
                ],
            )
        )
        page.update()
    
    def storage_add():
        storage_add_button.visible=True
        keys_json=json.loads(aes_engine.decrypt_text(aes_engine.read_file(Path('files/keys.json').resolve()), hashlib.sha256(storage_password_field.value.encode('UTF-8')).hexdigest()).replace('\\', '\\\\'))
        match storage_add_type_field.value:
            case 'Связка ключей RSA':
                key={storage_add_name_field.value: {"type": "RSA_PAIR", "value": {"priv": storage_add_rsa_priv_field.value, "pub": storage_add_rsa_pub_field.value}}}
            case 'Публичный ключ RSA':
               key={storage_add_name_field.value: {"type": "RSA_PUB", "value": {"pub": storage_add_rsa_pub_single_field.value}}}
            case 'Ключ AES':
                key={storage_add_name_field.value: {"type": "AES", "value": {"key": storage_add_aes_field.value}}}
            case 'Ключ Blowfish':
                key={storage_add_name_field.value: {"type": "Blowfish", "value": {"key": storage_add_blowfish_field.value}}}
            case 'Хеш SHA-256':
                key={storage_add_name_field.value: {"type": "SHA-256", "value": {"hash": storage_add_sha256_hash_field.value, "file": storage_add_sha256_file_field.value}}}
            case 'Хеш MD5':
                key={storage_add_name_field.value: {"type": "MD5", "value": {"hash": storage_add_md5_hash_field.value, "file": storage_add_md5_file_field.value}}}
            case 'Пароль':
                key={storage_add_name_field.value: {"type": "Password", "value": {"password": storage_add_password_field.value}}}
        keys_json = key | keys_json
        aes_engine.write_file(Path('files/keys.json').resolve(), aes_engine.encrypt_text(str(keys_json).replace("'", '"').replace('\\\\', '\\'), hashlib.sha256(storage_password_field.value.encode('UTF-8')).hexdigest()))
        make_keys_blocks(keys_json)
        page.views.clear()
        page.views.append(
            ft.View(
                "/key_storage",
                [
                    appbar, ft.Container(storage_listview, expand=8, padding=7)
                ],
            )
        )
        page.update()

    def open_storage_edit(key_name):
        keys_json=json.loads(aes_engine.decrypt_text(aes_engine.read_file(Path('files/keys.json').resolve()), hashlib.sha256(storage_password_field.value.encode('UTF-8')).hexdigest()).replace('\\', '\\\\'))
        key_type=keys_json[key_name]['type']
        storage_edit_dialog.title=ft.Text(f"{key_name}", weight=ft.FontWeight.BOLD, size=23)
        match key_type:
            case "AES":
                storage_edit_dialog.content=ft.Column([ft.Text('Ключ AES' , weight=ft.FontWeight.BOLD, size=19), storage_edit_aes_field], height=80)
                storage_edit_aes_field.value=keys_json[key_name]['value']['key']
            case "Blowfish":
                storage_edit_dialog.content=ft.Column([ft.Text('Ключ Blowfish' , weight=ft.FontWeight.BOLD, size=19), storage_edit_blowfish_field], height=80)
                storage_edit_blowfish_field.value=keys_json[key_name]['value']['key']
            case "RSA_PUB":
                storage_edit_dialog.content=ft.Column([ft.Text('Публичный ключ RSA' , weight=ft.FontWeight.BOLD, size=19), ft.Row([storage_edit_rsa_pub_single_field, storage_edit_rsa_pub_single_button], width=420)], height=80)
                storage_edit_rsa_pub_single_field.value=keys_json[key_name]['value']['pub']
            case "RSA_PAIR":
                storage_edit_dialog.content=ft.Column([ft.Text('Публичный ключ' , weight=ft.FontWeight.BOLD, size=19), ft.Row([storage_edit_rsa_pub_field, storage_edit_rsa_pub_button], width=420), ft.Text('Приватный ключ' , weight=ft.FontWeight.BOLD, size=19), ft.Row([storage_edit_rsa_priv_field, storage_edit_rsa_priv_button], width=420)], height=175)
                storage_edit_rsa_pub_field.value=keys_json[key_name]['value']['pub']
                storage_edit_rsa_priv_field.value=keys_json[key_name]['value']['priv']
            case "SHA-256":
                storage_edit_dialog.content=ft.Column([ft.Text('Хеш SHA-256' , weight=ft.FontWeight.BOLD, size=19), storage_edit_sha256_hash_field, ft.Text('Файл' , weight=ft.FontWeight.BOLD, size=19), ft.Row([storage_edit_sha256_file_field, storage_edit_sha256_file_button], width=420)], height=175)
                storage_edit_sha256_hash_field.value=keys_json[key_name]['value']['hash']
                storage_edit_sha256_file_field.value=keys_json[key_name]['value']['file']
            case "MD5":
                storage_edit_dialog.content=ft.Column([ft.Text('Хеш MD5' , weight=ft.FontWeight.BOLD, size=19), storage_edit_md5_hash_field, ft.Text('Файл' , weight=ft.FontWeight.BOLD, size=19), ft.Row([storage_edit_md5_file_field, storage_edit_md5_file_button], width=420)], height=175)
                storage_edit_md5_hash_field.value=keys_json[key_name]['value']['hash']
                storage_edit_md5_file_field.value=keys_json[key_name]['value']['file']
            case "Password":
                storage_edit_dialog.content=ft.Column([ft.Text('Пароль' , weight=ft.FontWeight.BOLD, size=19), storage_edit_password_field], height=80)
                storage_edit_password_field.value=keys_json[key_name]['value']['password']
        storage_edit_dialog.data={'name': key_name, 'type': key_type}
        page.open(storage_edit_dialog)
        page.update()

    storage_edit_dialog = ft.AlertDialog(
            actions=[ft.TextButton("Отменить", on_click=lambda e: page.close(storage_edit_dialog)), ft.TextButton("Подтвердить", on_click=lambda e: storage_edit())]
        )
    
    def storage_edit():
        keys_json=json.loads(aes_engine.decrypt_text(aes_engine.read_file(Path('files/keys.json').resolve()), hashlib.sha256(storage_password_field.value.encode('UTF-8')).hexdigest()).replace('\\', '\\\\'))
        match storage_edit_dialog.data['type']:
            case "AES":
                keys_json[storage_edit_dialog.data['name']]['value']['key']=storage_edit_aes_field.value
            case "Blowfish":
                keys_json[storage_edit_dialog.data['name']]['value']['key']=storage_edit_blowfish_field.value
            case "RSA_PUB":
                keys_json[storage_edit_dialog.data['name']]['value']['pub']=storage_edit_rsa_pub_single_field.value
            case "RSA_PAIR":
                keys_json[storage_edit_dialog.data['name']]['value']['pub']=storage_edit_rsa_pub_field.value
                keys_json[storage_edit_dialog.data['name']]['value']['priv']=storage_edit_rsa_priv_field.value
            case "SHA-256":
                keys_json[storage_edit_dialog.data['name']]['value']['hash']=storage_edit_sha256_hash_field.value
                keys_json[storage_edit_dialog.data['name']]['value']['file']=storage_edit_sha256_file_field.value
            case "MD5":
                keys_json[storage_edit_dialog.data['name']]['value']['hash']=storage_edit_md5_hash_field.value
                keys_json[storage_edit_dialog.data['name']]['value']['file']=storage_edit_md5_file_field.value
            case "Password":
                keys_json[storage_edit_dialog.data['name']]['value']['password']=storage_edit_password_field.value
        aes_engine.write_file(Path('files/keys.json').resolve(), aes_engine.encrypt_text(str(keys_json).replace("'", '"').replace('\\\\', '\\'), hashlib.sha256(storage_password_field.value.encode('UTF-8')).hexdigest()))
        page.close(storage_edit_dialog)
        print("PAGE UPDATING")
        page.update()
        make_keys_blocks(keys_json)
        page.views.clear()
        page.views.append(
            ft.View(
                "/key_storage",
                [
                    appbar, ft.Container(storage_listview, expand=8, padding=7)
                ],
            )
        )
        page.update()



    def pick_aes_enc_inp_file(e: ft.FilePickerResultEvent):
        aes_enc_inp_file_field.value = (
            "".join(map(lambda f: f.path, e.files)) if e.files else None
        )
        aes_enc_inp_file_field.update()

    def pick_aes_enc_out_file(e: ft.FilePickerResultEvent):
        aes_enc_out_file_field.value = (
            "".join(map(lambda f: f.path, e.files)) if e.files else None
        )
        aes_enc_out_file_field.update()

    
    aes_enc_inp_file_dialog = ft.FilePicker(on_result=pick_aes_enc_inp_file)
    page.overlay.append(aes_enc_inp_file_dialog)
    
    aes_enc_out_file_dialog = ft.FilePicker(on_result=pick_aes_enc_out_file)
    page.overlay.append(aes_enc_out_file_dialog)


    def aes_encrypt():
        match aes_enc_key_type_field.value:
            case '16-ричная строка':
                try:
                    aes_engine.write_file(aes_enc_out_file_field.value, aes_engine.encrypt_file(aes_enc_inp_file_field.value, aes_enc_key_field.value))
                    page.open(ft.SnackBar(content=ft.Text('Операция завершена.'), show_close_icon=True, bgcolor=ft.Colors.PRIMARY, action='Показать в папке', on_action=lambda e: os.system(f'explorer {os.path.dirname(aes_enc_out_file_field.value)}')))
                except FileNotFoundError:
                    page.open(ft.SnackBar(content=ft.Text('Файл не найден.'), show_close_icon=True, bgcolor=ft.Colors.RED))
                except ValueError:
                    page.open(ft.SnackBar(content=ft.Text('Некорректный ключ.'), show_close_icon=True, bgcolor=ft.Colors.RED))

            case 'Пароль':
                try:
                    aes_engine.write_file(aes_enc_out_file_field.value, aes_engine.encrypt_file(aes_enc_inp_file_field.value, hashlib.sha256(aes_enc_key_field.value.encode('UTF-8')).hexdigest()))
                    page.open(ft.SnackBar(content=ft.Text('Операция завершена.'), show_close_icon=True, bgcolor=ft.Colors.PRIMARY, action='Показать в папке', on_action=lambda e: os.system(f'explorer {os.path.dirname(aes_enc_out_file_field.value)}')))
                except FileNotFoundError:
                    page.open(ft.SnackBar(content=ft.Text('Файл не найден.'), show_close_icon=True, bgcolor=ft.Colors.RED))
                except ValueError:
                    page.open(ft.SnackBar(content=ft.Text('Некорректный ключ.'), show_close_icon=True, bgcolor=ft.Colors.RED))
                    

    aes_enc_label = ft.Text('Шифрование AES', size=24, weight=ft.FontWeight.BOLD) 

    aes_enc_key_type_label=ft.Text('Тип ключа', size=18, weight=ft.FontWeight.BOLD)

    aes_enc_key_type_field=ft.Dropdown(label='Тип ключа', options=[ft.DropdownOption('16-ричная строка'), ft.DropdownOption('Пароль')], width=330)

    aes_enc_key_label=ft.Text('Ключ', size=18, weight=ft.FontWeight.BOLD)

    aes_enc_key_field=ft.TextField(hint_text='Ключ', width=330, password=True)

    aes_enc_inp_file_label=ft.Text('Файл для шифрования', size=18, weight=ft.FontWeight.BOLD)

    aes_enc_inp_file_field=ft.TextField(hint_text='Путь', width=330)

    aes_enc_inp_file_button=ft.ElevatedButton(icon=ft.Icons.FOLDER_OPEN, text='Обзор', on_click=lambda e: aes_enc_inp_file_dialog.pick_files(dialog_title='Файл для шифрования', allow_multiple=False))

    aes_enc_out_file_label=ft.Text('Файл для сохранения результата', size=18, weight=ft.FontWeight.BOLD)
    
    aes_enc_out_file_field=ft.TextField(hint_text='Путь', width=330)
    aes_enc_out_file_button=ft.ElevatedButton(icon=ft.Icons.FOLDER_OPEN, text='Обзор', on_click=lambda e: aes_enc_out_file_dialog.pick_files(dialog_title='Файл для сохранения результата', allow_multiple=False))

    aes_enc_button=ft.ElevatedButton(icon=ft.Icons.PLAYLIST_PLAY, text='Запустить', on_click=lambda e: aes_encrypt())

    aes_enc_column=ft.Column(controls=[
        aes_enc_label, aes_enc_key_type_label, aes_enc_key_type_field, aes_enc_key_label, aes_enc_key_field, aes_enc_inp_file_label, ft.Row(controls=[aes_enc_inp_file_field, aes_enc_inp_file_button]), aes_enc_out_file_label, ft.Row(controls=[aes_enc_out_file_field, aes_enc_out_file_button]), aes_enc_button
    ])



    def pick_aes_dec_inp_file(e: ft.FilePickerResultEvent):
        aes_dec_inp_file_field.value = (
            "".join(map(lambda f: f.path, e.files)) if e.files else None
        )
        aes_dec_inp_file_field.update()

    def pick_aes_dec_out_file(e: ft.FilePickerResultEvent):
        aes_dec_out_file_field.value = (
            "".join(map(lambda f: f.path, e.files)) if e.files else None
        )
        aes_dec_out_file_field.update()

    
    aes_dec_inp_file_dialog = ft.FilePicker(on_result=pick_aes_dec_inp_file)
    page.overlay.append(aes_dec_inp_file_dialog)
    
    aes_dec_out_file_dialog = ft.FilePicker(on_result=pick_aes_dec_out_file)
    page.overlay.append(aes_dec_out_file_dialog)

    def aes_decrypt():
        match aes_dec_key_type_field.value:
            case '16-ричная строка':
                try:
                    aes_engine.write_file(aes_dec_out_file_field.value, aes_engine.decrypt_file(aes_dec_inp_file_field.value, aes_dec_key_field.value))
                    page.open(ft.SnackBar(content=ft.Text('Операция завершена.'), show_close_icon=True, bgcolor=ft.Colors.PRIMARY, action='Показать в папке', on_action=lambda e: os.system(f'explorer {os.path.dirname(aes_dec_out_file_field.value)}')))
                except FileNotFoundError:
                    page.open(ft.SnackBar(content=ft.Text('Файл не найден.'), show_close_icon=True, bgcolor=ft.Colors.RED))
                except ValueError:
                    page.open(ft.SnackBar(content=ft.Text('Некорректный ключ.'), show_close_icon=True, bgcolor=ft.Colors.RED))

            case 'Пароль':
                try:
                    aes_engine.write_file(aes_dec_out_file_field.value, aes_engine.decrypt_file(aes_dec_inp_file_field.value, hashlib.sha256(aes_dec_key_field.value.encode('UTF-8')).hexdigest()))
                    page.open(ft.SnackBar(content=ft.Text('Операция завершена.'), show_close_icon=True, bgcolor=ft.Colors.PRIMARY, action='Показать в папке', on_action=lambda e: os.system(f'explorer {os.path.dirname(aes_dec_out_file_field.value)}')))
                except FileNotFoundError:
                    page.open(ft.SnackBar(content=ft.Text('Файл не найден.'), show_close_icon=True, bgcolor=ft.Colors.RED))
                except ValueError:
                    page.open(ft.SnackBar(content=ft.Text('Некорректный ключ.'), show_close_icon=True, bgcolor=ft.Colors.RED))
                    

    aes_dec_label = ft.Text('Дешифрование AES', size=24, weight=ft.FontWeight.BOLD) 

    aes_dec_key_type_label=ft.Text('Тип ключа', size=18, weight=ft.FontWeight.BOLD)

    aes_dec_key_type_field=ft.Dropdown(label='Тип ключа', options=[ft.DropdownOption('16-ричная строка'), ft.DropdownOption('Пароль')], width=330)

    aes_dec_key_label=ft.Text('Ключ', size=18, weight=ft.FontWeight.BOLD)

    aes_dec_key_field=ft.TextField(hint_text='Ключ', width=330, password=True)

    aes_dec_inp_file_label=ft.Text('Файл для дешифрования', size=18, weight=ft.FontWeight.BOLD)

    aes_dec_inp_file_field=ft.TextField(hint_text='Путь', width=330)

    aes_dec_inp_file_button=ft.ElevatedButton(icon=ft.Icons.FOLDER_OPEN, text='Обзор', on_click=lambda e: aes_dec_inp_file_dialog.pick_files(dialog_title='Файл для шифрования', allow_multiple=False))

    aes_dec_out_file_label=ft.Text('Файл для сохранения результата', size=18, weight=ft.FontWeight.BOLD)
    
    aes_dec_out_file_field=ft.TextField(hint_text='Путь', width=330)

    aes_dec_out_file_button=ft.ElevatedButton(icon=ft.Icons.FOLDER_OPEN, text='Обзор', on_click=lambda e: aes_dec_out_file_dialog.pick_files(dialog_title='Файл для сохранения результата', allow_multiple=False))

    aes_dec_button=ft.ElevatedButton(icon=ft.Icons.PLAYLIST_PLAY, text='Запустить', on_click=lambda e: aes_decrypt())

    aes_dec_column=ft.Column(controls=[
        aes_dec_label, aes_dec_key_type_label, aes_dec_key_type_field, aes_dec_key_label, aes_dec_key_field, aes_dec_inp_file_label, ft.Row(controls=[aes_dec_inp_file_field, aes_dec_inp_file_button]), aes_dec_out_file_label, ft.Row(controls=[aes_dec_out_file_field, aes_dec_out_file_button]), aes_dec_button
    ])



    def aes_keygen():
        aes_keygen_output_label.value=aes_engine.generate_key(int(aes_keygen_key_length_field.value))
        aes_keygen_result_label.visible=True
        aes_keygen_output_label.visible=True
        aes_keygen_result_label.update()
        aes_keygen_output_label.update()


    aes_keygen_label = ft.Text('Генерация ключей AES', size=24, weight=ft.FontWeight.BOLD) 

    aes_keygen_key_length_label=ft.Text('Тип ключа', size=18, weight=ft.FontWeight.BOLD)

    aes_keygen_key_length_field=ft.Dropdown(label='Длина ключа', options=[ft.DropdownOption('128'), ft.DropdownOption('192'), ft.DropdownOption('256')], width=330)

    aes_keygen_button=aes_dec_button=ft.ElevatedButton(icon=ft.Icons.PLAYLIST_PLAY, text='Запустить', on_click=lambda e: aes_keygen())

    aes_keygen_result_label=ft.Text('Результат', size=18, weight=ft.FontWeight.BOLD, visible=False)

    aes_keygen_output_label=ft.Text('', size=18, weight=ft.FontWeight.BOLD, visible=False, selectable=True)

    aes_keygen_column=ft.Column(controls=[
        aes_keygen_label, aes_keygen_key_length_label, aes_keygen_key_length_field, aes_keygen_button, aes_keygen_result_label, aes_keygen_output_label
    ])




    def pick_blowfish_enc_inp_file(e: ft.FilePickerResultEvent):
        blowfish_enc_inp_file_field.value = (
            "".join(map(lambda f: f.path, e.files)) if e.files else None
        )
        blowfish_enc_inp_file_field.update()

    def pick_blowfish_enc_out_file(e: ft.FilePickerResultEvent):
        blowfish_enc_out_file_field.value = (
            "".join(map(lambda f: f.path, e.files)) if e.files else None
        )
        blowfish_enc_out_file_field.update()


    blowfish_enc_inp_file_dialog = ft.FilePicker(on_result=pick_blowfish_enc_inp_file)
    page.overlay.append(blowfish_enc_inp_file_dialog)

    blowfish_enc_out_file_dialog = ft.FilePicker(on_result=pick_blowfish_enc_out_file)
    page.overlay.append(blowfish_enc_out_file_dialog)


    def blowfish_encrypt():
        match blowfish_enc_key_type_field.value:
            case '16-ричная строка':
                try:
                    blowfish_engine.write_file(blowfish_enc_out_file_field.value, blowfish_engine.encrypt_file(blowfish_enc_inp_file_field.value, blowfish_enc_key_field.value))
                    page.open(ft.SnackBar(content=ft.Text('Операция завершена.'), show_close_icon=True, bgcolor=ft.Colors.PRIMARY, action='Показать в папке', on_action=lambda e: os.system(f'explorer {os.path.dirname(blowfish_enc_out_file_field.value)}')))
                except FileNotFoundError:
                    page.open(ft.SnackBar(content=ft.Text('Файл не найден.'), show_close_icon=True, bgcolor=ft.Colors.RED))
                except ValueError:
                    page.open(ft.SnackBar(content=ft.Text('Некорректный ключ.'), show_close_icon=True, bgcolor=ft.Colors.RED))

            case 'Пароль':
                try:
                    blowfish_engine.write_file(blowfish_enc_out_file_field.value, blowfish_engine.encrypt_file(blowfish_enc_inp_file_field.value, hashlib.sha256(blowfish_enc_key_field.value.encode('UTF-8')).hexdigest()))
                    page.open(ft.SnackBar(content=ft.Text('Операция завершена.'), show_close_icon=True, bgcolor=ft.Colors.PRIMARY, action='Показать в папке', on_action=lambda e: os.system(f'explorer {os.path.dirname(blowfish_enc_out_file_field.value)}')))
                except FileNotFoundError:
                    page.open(ft.SnackBar(content=ft.Text('Файл не найден.'), show_close_icon=True, bgcolor=ft.Colors.RED))
                except ValueError:
                    page.open(ft.SnackBar(content=ft.Text('Некорректный ключ.'), show_close_icon=True, bgcolor=ft.Colors.RED))

    blowfish_enc_label = ft.Text('Шифрование Blowfish', size=24, weight=ft.FontWeight.BOLD) 

    blowfish_enc_key_type_label=ft.Text('Тип ключа', size=18, weight=ft.FontWeight.BOLD)

    blowfish_enc_key_type_field=ft.Dropdown(label='Тип ключа', options=[ft.DropdownOption('16-ричная строка'), ft.DropdownOption('Пароль')], width=330)

    blowfish_enc_key_label=ft.Text('Ключ', size=18, weight=ft.FontWeight.BOLD)

    blowfish_enc_key_field=ft.TextField(hint_text='Ключ', width=330, password=True)

    blowfish_enc_inp_file_label=ft.Text('Файл для шифрования', size=18, weight=ft.FontWeight.BOLD)

    blowfish_enc_inp_file_field=ft.TextField(hint_text='Путь', width=330)

    blowfish_enc_inp_file_button=ft.ElevatedButton(icon=ft.Icons.FOLDER_OPEN, text='Обзор', on_click=lambda e: blowfish_enc_inp_file_dialog.pick_files(dialog_title='Файл для шифрования', allow_multiple=False))

    blowfish_enc_out_file_label=ft.Text('Файл для сохранения результата', size=18, weight=ft.FontWeight.BOLD)

    blowfish_enc_out_file_field=ft.TextField(hint_text='Путь', width=330)

    blowfish_enc_out_file_button=ft.ElevatedButton(icon=ft.Icons.FOLDER_OPEN, text='Обзор', on_click=lambda e: blowfish_enc_out_file_dialog.pick_files(dialog_title='Файл для сохранения результата', allow_multiple=False))

    blowfish_enc_button=ft.ElevatedButton(icon=ft.Icons.PLAYLIST_PLAY, text='Запустить', on_click=lambda e: blowfish_encrypt())

    blowfish_enc_column=ft.Column(controls=[
        blowfish_enc_label, blowfish_enc_key_type_label, blowfish_enc_key_type_field, blowfish_enc_key_label, blowfish_enc_key_field, blowfish_enc_inp_file_label, ft.Row(controls=[blowfish_enc_inp_file_field, blowfish_enc_inp_file_button]), blowfish_enc_out_file_label, ft.Row(controls=[blowfish_enc_out_file_field, blowfish_enc_out_file_button]), blowfish_enc_button
    ])



    def pick_blowfish_dec_inp_file(e: ft.FilePickerResultEvent):
        blowfish_dec_inp_file_field.value = (
            "".join(map(lambda f: f.path, e.files)) if e.files else None
        )
        blowfish_dec_inp_file_field.update()

    def pick_blowfish_dec_out_file(e: ft.FilePickerResultEvent):
        blowfish_dec_out_file_field.value = (
            "".join(map(lambda f: f.path, e.files)) if e.files else None
        )
        blowfish_dec_out_file_field.update()


    blowfish_dec_inp_file_dialog = ft.FilePicker(on_result=pick_blowfish_dec_inp_file)
    page.overlay.append(blowfish_dec_inp_file_dialog)

    blowfish_dec_out_file_dialog = ft.FilePicker(on_result=pick_blowfish_dec_out_file)
    page.overlay.append(blowfish_dec_out_file_dialog)

    def blowfish_decrypt():
        match blowfish_dec_key_type_field.value:
            case '16-ричная строка':
                try:
                    blowfish_engine.write_file(blowfish_dec_out_file_field.value, blowfish_engine.decrypt_file(blowfish_dec_inp_file_field.value, blowfish_dec_key_field.value))
                    page.open(ft.SnackBar(content=ft.Text('Операция завершена.'), show_close_icon=True, bgcolor=ft.Colors.PRIMARY, action='Показать в папке', on_action=lambda e: os.system(f'explorer {os.path.dirname(blowfish_dec_out_file_field.value)}')))
                except FileNotFoundError:
                    page.open(ft.SnackBar(content=ft.Text('Файл не найден.'), show_close_icon=True, bgcolor=ft.Colors.RED))
                except ValueError:
                    page.open(ft.SnackBar(content=ft.Text('Некорректный ключ.'), show_close_icon=True, bgcolor=ft.Colors.RED))

            case 'Пароль':
                try:
                    blowfish_engine.write_file(blowfish_dec_out_file_field.value, blowfish_engine.decrypt_file(blowfish_dec_inp_file_field.value, hashlib.sha256(blowfish_dec_key_field.value.encode('UTF-8')).hexdigest()))
                    page.open(ft.SnackBar(content=ft.Text('Операция завершена.'), show_close_icon=True, bgcolor=ft.Colors.PRIMARY, action='Показать в папке', on_action=lambda e: os.system(f'explorer {os.path.dirname(blowfish_dec_out_file_field.value)}')))
                except FileNotFoundError:
                    page.open(ft.SnackBar(content=ft.Text('Файл не найден.'), show_close_icon=True, bgcolor=ft.Colors.RED))
                except ValueError:
                    page.open(ft.SnackBar(content=ft.Text('Некорректный ключ.'), show_close_icon=True, bgcolor=ft.Colors.RED))
                    

    blowfish_dec_label = ft.Text('Дешифрование Blowfish', size=24, weight=ft.FontWeight.BOLD) 

    blowfish_dec_key_type_label=ft.Text('Тип ключа', size=18, weight=ft.FontWeight.BOLD)

    blowfish_dec_key_type_field=ft.Dropdown(label='Тип ключа', options=[ft.DropdownOption('16-ричная строка'), ft.DropdownOption('Пароль')], width=330)

    blowfish_dec_key_label=ft.Text('Ключ', size=18, weight=ft.FontWeight.BOLD)

    blowfish_dec_key_field=ft.TextField(hint_text='Ключ', width=330, password=True)

    blowfish_dec_inp_file_label=ft.Text('Файл для дешифрования', size=18, weight=ft.FontWeight.BOLD)

    blowfish_dec_inp_file_field=ft.TextField(hint_text='Путь', width=330)

    blowfish_dec_inp_file_button=ft.ElevatedButton(icon=ft.Icons.FOLDER_OPEN, text='Обзор', on_click=lambda e: blowfish_dec_inp_file_dialog.pick_files(dialog_title='Файл для шифрования', allow_multiple=False))

    blowfish_dec_out_file_label=ft.Text('Файл для сохранения результата', size=18, weight=ft.FontWeight.BOLD)

    blowfish_dec_out_file_field=ft.TextField(hint_text='Путь', width=330)

    blowfish_dec_out_file_button=ft.ElevatedButton(icon=ft.Icons.FOLDER_OPEN, text='Обзор', on_click=lambda e: blowfish_dec_out_file_dialog.pick_files(dialog_title='Файл для сохранения результата', allow_multiple=False))

    blowfish_dec_button=ft.ElevatedButton(icon=ft.Icons.PLAYLIST_PLAY, text='Запустить', on_click=lambda e: blowfish_decrypt())

    blowfish_dec_column=ft.Column(controls=[
        blowfish_dec_label, blowfish_dec_key_type_label, blowfish_dec_key_type_field, blowfish_dec_key_label, blowfish_dec_key_field, blowfish_dec_inp_file_label, ft.Row(controls=[blowfish_dec_inp_file_field, blowfish_dec_inp_file_button]), blowfish_dec_out_file_label, ft.Row(controls=[blowfish_dec_out_file_field, blowfish_dec_out_file_button]), blowfish_dec_button
    ])



    def blowfish_keygen():
        blowfish_keygen_output_label.value=blowfish_engine.generate_key(int(blowfish_keygen_key_length_field.value))
        blowfish_keygen_result_label.visible=True
        blowfish_keygen_output_label.visible=True
        blowfish_keygen_result_label.update()
        blowfish_keygen_output_label.update()


    blowfish_keygen_label = ft.Text('Генерация ключей Blowfish', size=24, weight=ft.FontWeight.BOLD) 

    blowfish_keygen_key_length_label=ft.Text('Тип ключа', size=18, weight=ft.FontWeight.BOLD)

    blowfish_keygen_key_length_field=ft.Dropdown(label='Длина ключа', options=[ft.DropdownOption(str(i)) for i in range(32, 480, 32)], width=330)

    blowfish_keygen_button=blowfish_dec_button=ft.ElevatedButton(icon=ft.Icons.PLAYLIST_PLAY, text='Запустить', on_click=lambda e: blowfish_keygen())

    blowfish_keygen_result_label=ft.Text('Результат', size=18, weight=ft.FontWeight.BOLD, visible=False)

    blowfish_keygen_output_label=ft.Text('', size=18, weight=ft.FontWeight.BOLD, visible=False, selectable=True)

    blowfish_keygen_column=ft.Column(controls=[
        blowfish_keygen_label, blowfish_keygen_key_length_label, blowfish_keygen_key_length_field, blowfish_keygen_button, blowfish_keygen_result_label, blowfish_keygen_output_label
    ])




    def pick_pub_key_file(e: ft.FilePickerResultEvent):
        pub_key_file_field.value = (
            "".join(map(lambda f: f.path, e.files)) if e.files else None
        )
        pub_key_file_field.update()

    def pick_rsa_enc_inp_file(e: ft.FilePickerResultEvent):
        rsa_enc_inp_file_field.value = (
            "".join(map(lambda f: f.path, e.files)) if e.files else None
        )
        rsa_enc_inp_file_field.update()

    def pick_rsa_enc_out_file(e: ft.FilePickerResultEvent):
        rsa_enc_out_file_field.value = (
            "".join(map(lambda f: f.path, e.files)) if e.files else None
        )
        rsa_enc_out_file_field.update()


    def get_pub_key():
        return rsa_engine.load_public_key(pub_key_file_field.value)
    
    def rsa_encrypt():
        try:
            rsa_engine.write_file(rsa_enc_out_file_field.value, rsa_engine.encrypt_file(rsa_enc_inp_file_field.value, get_pub_key()))
            page.open(ft.SnackBar(content=ft.Text('Операция завершена.'), show_close_icon=True, bgcolor=ft.Colors.PRIMARY, action='Показать в папке', on_action=lambda e: os.system(f'explorer {os.path.dirname(rsa_enc_out_file_field.value)}')))
        except FileNotFoundError:
            page.open(ft.SnackBar(content=ft.Text('Файл не найден.'), show_close_icon=True, bgcolor=ft.Colors.RED))
        except ValueError:
            page.open(ft.SnackBar(content=ft.Text('Ошибка.'), show_close_icon=True, bgcolor=ft.Colors.RED))


    pub_key_file_dialog = ft.FilePicker(on_result=pick_pub_key_file)
    page.overlay.append(pub_key_file_dialog)

    rsa_enc_inp_file_dialog = ft.FilePicker(on_result=pick_rsa_enc_inp_file)
    page.overlay.append(rsa_enc_inp_file_dialog)

    rsa_enc_out_file_dialog = ft.FilePicker(on_result=pick_rsa_enc_out_file)
    page.overlay.append(rsa_enc_out_file_dialog)


    rsa_enc_label = ft.Text('Шифрование RSA', size=24, weight=ft.FontWeight.BOLD) 

    pub_key_label=ft.Text('Файл публичного ключа', size=18, weight=ft.FontWeight.BOLD)

    pub_key_file_field=ft.TextField(hint_text='Путь', width=330)

    pub_key_file_button = ft.ElevatedButton(icon=ft.Icons.FOLDER_OPEN, text='Обзор', on_click=lambda e: pub_key_file_dialog.pick_files(dialog_title='Файл публичного ключа', allow_multiple=False))
    
    rsa_enc_inp_file_label=ft.Text('Файл для шифрования', size=18, weight=ft.FontWeight.BOLD)

    rsa_enc_inp_file_field=ft.TextField(hint_text='Путь', width=330)

    rsa_enc_inp_file_button=ft.ElevatedButton(icon=ft.Icons.FOLDER_OPEN, text='Обзор', on_click=lambda e: rsa_enc_inp_file_dialog.pick_files(dialog_title='Файл для шифрования', allow_multiple=False))

    rsa_enc_out_file_label=ft.Text('Файл для сохранения результата', size=18, weight=ft.FontWeight.BOLD)

    rsa_enc_out_file_field=ft.TextField(hint_text='Путь', width=330)

    rsa_enc_out_file_button=ft.ElevatedButton(icon=ft.Icons.FOLDER_OPEN, text='Обзор', on_click=lambda e: rsa_enc_out_file_dialog.pick_files(dialog_title='Файл для сохранения результата', allow_multiple=False))

    rsa_enc_button=ft.ElevatedButton(icon=ft.Icons.PLAYLIST_PLAY, text='Запустить', on_click=lambda e: rsa_encrypt())

    rsa_enc_column=ft.Column(controls=[
        rsa_enc_label, pub_key_label, ft.Row(controls=[pub_key_file_field, pub_key_file_button]), rsa_enc_inp_file_label, ft.Row(controls=[rsa_enc_inp_file_field, rsa_enc_inp_file_button]), rsa_enc_out_file_label, ft.Row(controls=[rsa_enc_out_file_field, rsa_enc_out_file_button]), rsa_enc_button
    ])


    def pick_priv_key_file(e: ft.FilePickerResultEvent):
        priv_key_file_field.value = (
            "".join(map(lambda f: f.path, e.files)) if e.files else None
        )
        priv_key_file_field.update()

    def pick_rsa_dec_inp_file(e: ft.FilePickerResultEvent):
        rsa_dec_inp_file_field.value = (
            "".join(map(lambda f: f.path, e.files)) if e.files else None
        )
        rsa_dec_inp_file_field.update()

    def pick_rsa_dec_out_file(e: ft.FilePickerResultEvent):
        rsa_dec_out_file_field.value = (
            "".join(map(lambda f: f.path, e.files)) if e.files else None
        )
        rsa_dec_out_file_field.update()

    
    def get_priv_key():
        return rsa_engine.load_private_key(priv_key_file_field.value, priv_key_load_password_field.value)

    def rsa_decrypt():
        try:
            rsa_engine.write_file(rsa_dec_out_file_field.value, rsa_engine.decrypt_file(rsa_dec_inp_file_field.value, get_priv_key()))
            page.open(ft.SnackBar(content=ft.Text('Операция завершена.'), show_close_icon=True, bgcolor=ft.Colors.PRIMARY, action='Показать в папке', on_action=lambda e: os.system(f'explorer {os.path.dirname(rsa_dec_out_file_field.value)}')))
        except FileNotFoundError:
            page.open(ft.SnackBar(content=ft.Text('Файл не найден.'), show_close_icon=True, bgcolor=ft.Colors.RED))
        except ValueError:
            page.open(ft.SnackBar(content=ft.Text('Ошибка.'), show_close_icon=True, bgcolor=ft.Colors.RED))

    priv_key_file_dialog = ft.FilePicker(on_result=pick_priv_key_file)
    page.overlay.append(priv_key_file_dialog)

    rsa_dec_inp_file_dialog = ft.FilePicker(on_result=pick_rsa_dec_inp_file)
    page.overlay.append(rsa_dec_inp_file_dialog)

    rsa_dec_out_file_dialog = ft.FilePicker(on_result=pick_rsa_dec_out_file)
    page.overlay.append(rsa_dec_out_file_dialog)


    rsa_dec_label=ft.Text('Дешифрование RSA', size=24, weight=ft.FontWeight.BOLD) 

    priv_key_label=ft.Text('Файл приватного ключа', size=18, weight=ft.FontWeight.BOLD)

    priv_key_file_field=ft.TextField(hint_text='Путь', width=330)

    pick_priv_key_file_button=ft.ElevatedButton(icon=ft.Icons.FOLDER_OPEN, text='Обзор', on_click=lambda e: priv_key_file_dialog.pick_files(dialog_title='Файл приватного ключа', allow_multiple=False))

    priv_key_load_password_field=ft.TextField(hint_text='Пароль файла приватного ключа', width=330, password=True)

    rsa_dec_inp_file_label=ft.Text('Файл для дешифрования', size=18, weight=ft.FontWeight.BOLD)

    rsa_dec_inp_file_field=ft.TextField(hint_text='Путь', width=330)

    rsa_dec_inp_file_button=ft.ElevatedButton(icon=ft.Icons.FOLDER_OPEN, text='Обзор', on_click=lambda e: rsa_dec_inp_file_dialog.pick_files(dialog_title='Файл для дешифрования', allow_multiple=False))
    
    rsa_dec_out_file_label=ft.Text('Файл для сохранения результата', size=18, weight=ft.FontWeight.BOLD)

    rsa_dec_out_file_field=ft.TextField(hint_text='Путь', width=330)

    rsa_dec_out_file_button=ft.ElevatedButton(icon=ft.Icons.FOLDER_OPEN, text='Обзор', on_click=lambda e: rsa_dec_out_file_dialog.pick_files(dialog_title='Файл для сохранения результата', allow_multiple=False))

    rsa_dec_button=ft.ElevatedButton(icon=ft.Icons.PLAYLIST_PLAY, text='Запустить', on_click=lambda e: rsa_decrypt())

    rsa_dec_column=ft.Column(controls=[
        rsa_dec_label, priv_key_label, ft.Row(controls=[priv_key_file_field, pick_priv_key_file_button]), priv_key_load_password_field, rsa_dec_inp_file_label, ft.Row(controls=[rsa_dec_inp_file_field, rsa_dec_inp_file_button]), rsa_dec_out_file_label, ft.Row(controls=[rsa_dec_out_file_field, rsa_dec_out_file_button]), rsa_dec_button
    ])



    def pick_rsa_keygen_out_folder(e: ft.FilePickerResultEvent):
        rsa_keygen_out_folder_field.value = (
            rsa_keygen_out_folder_dialog.result.path
        )
        rsa_keygen_out_folder_field.update()

    def rsa_keygen():
        try:
            keys=rsa_engine.generate_keys(int(rsa_key_length_field.value))
            rsa_engine.write_keys(keys[0], keys[1], rsa_keygen_out_folder_field.value, rsa_priv_key_save_password_field.value)
            keys=None
            page.open(ft.SnackBar(content=ft.Text('Операция завершена.'), show_close_icon=True, bgcolor=ft.Colors.PRIMARY, action='Показать в папке', on_action=lambda e: os.system(f'explorer {rsa_keygen_out_folder_field.value}')))
        except FileNotFoundError:
            page.open(ft.SnackBar(content=ft.Text('Папка не найдена.'), show_close_icon=True, bgcolor=ft.Colors.RED))

    rsa_keygen_out_folder_dialog = ft.FilePicker(on_result=pick_rsa_keygen_out_folder)
    page.overlay.append(rsa_keygen_out_folder_dialog)

    rsa_keygen_label=ft.Text('Генерация ключей RSA', size=24, weight=ft.FontWeight.BOLD)

    rsa_key_length_label=ft.Text('Длина ключа', size=18, weight=ft.FontWeight.BOLD)

    rsa_key_length_field=ft.Dropdown(label='Длина ключа', options=[ft.DropdownOption('1024'), ft.DropdownOption('2048'), ft.DropdownOption('4096'), ft.DropdownOption('8192')], width=330)

    rsa_keygen_out_folder_label=ft.Text('Папка для сохранения ключей', size=18, weight=ft.FontWeight.BOLD)

    rsa_keygen_out_folder_field=ft.TextField(hint_text='Путь', width=330)

    rsa_keygen_out_folder_button=ft.ElevatedButton(icon=ft.Icons.FOLDER_OPEN, text='Обзор', on_click=lambda e: rsa_keygen_out_folder_dialog.get_directory_path(dialog_title='Папка для сохранения ключей'))

    rsa_priv_key_save_password_label=ft.Text('Пароль приватного ключа', size=18, weight=ft.FontWeight.BOLD)

    rsa_priv_key_save_password_field=ft.TextField(hint_text='Пароль приватного ключа', width=330, password=True)

    rsa_keygen_button=ft.ElevatedButton(icon=ft.Icons.PLAYLIST_PLAY, text='Запустить', on_click=lambda e: rsa_keygen())

    rsa_keygen_column=ft.Column(controls=[
        rsa_keygen_label, rsa_key_length_label, rsa_key_length_field, rsa_keygen_out_folder_label, ft.Row(controls=[rsa_keygen_out_folder_field, rsa_keygen_out_folder_button]), rsa_priv_key_save_password_label, rsa_priv_key_save_password_field, rsa_keygen_button
    ])




    def pick_sha256_inp_file(e: ft.FilePickerResultEvent):
        sha256_inp_file_field.value = (
            "".join(map(lambda f: f.path, e.files)) if e.files else None
        )
        sha256_inp_file_field.update()

    
    sha256_inp_file_dialog = ft.FilePicker(on_result=pick_sha256_inp_file)
    page.overlay.append(sha256_inp_file_dialog)


    def sha256():
        with open(sha256_inp_file_field.value, 'rb') as f:
            byte_str=f.read()
        
        sha256_output_label.value=hashlib.sha256(byte_str).hexdigest()
        sha256_result_label.visible=True
        sha256_output_label.visible=True
        sha256_result_label.update()
        sha256_output_label.update()

    sha256_label = ft.Text('Хеширование SHA-256', size=24, weight=ft.FontWeight.BOLD) 

    sha256_inp_file_label=ft.Text('Файл для хеширования', size=18, weight=ft.FontWeight.BOLD)

    sha256_inp_file_field=ft.TextField(hint_text='Путь', width=330)

    sha256_inp_file_button=ft.ElevatedButton(icon=ft.Icons.FOLDER_OPEN, text='Обзор', on_click=lambda e: sha256_inp_file_dialog.pick_files(dialog_title='Файл для хеширования', allow_multiple=False))
    
    sha256_result_label=ft.Text('Результат', size=18, weight=ft.FontWeight.BOLD, visible=False)

    sha256_output_label=ft.Text('', size=18, weight=ft.FontWeight.BOLD, visible=False, selectable=True)

    sha256_button=ft.ElevatedButton(icon=ft.Icons.PLAYLIST_PLAY, text='Запустить', on_click=lambda e: sha256())


    sha256_column=ft.Column(controls=[
        sha256_label, sha256_inp_file_label, ft.Row(controls=[sha256_inp_file_field, sha256_inp_file_button]), sha256_button, sha256_result_label, sha256_output_label
    ])




    def pick_md5_inp_file(e: ft.FilePickerResultEvent):
        md5_inp_file_field.value = (
            "".join(map(lambda f: f.path, e.files)) if e.files else None
        )
        md5_inp_file_field.update()

    
    md5_inp_file_dialog = ft.FilePicker(on_result=pick_md5_inp_file)
    page.overlay.append(md5_inp_file_dialog)


    def md5():
        with open(md5_inp_file_field.value, 'rb') as f:
            byte_str=f.read()
        
        md5_output_label.value=hashlib.md5(byte_str).hexdigest()
        md5_result_label.visible=True
        md5_output_label.visible=True
        md5_result_label.update()
        md5_output_label.update()

    md5_label = ft.Text('Хеширование MD5', size=24, weight=ft.FontWeight.BOLD) 

    md5_inp_file_label=ft.Text('Файл для хеширования', size=18, weight=ft.FontWeight.BOLD)

    md5_inp_file_field=ft.TextField(hint_text='Путь', width=330)

    md5_inp_file_button=ft.ElevatedButton(icon=ft.Icons.FOLDER_OPEN, text='Обзор', on_click=lambda e: md5_inp_file_dialog.pick_files(dialog_title='Файл для хеширования', allow_multiple=False))
    
    md5_result_label=ft.Text('Результат', size=18, weight=ft.FontWeight.BOLD, visible=False)

    md5_output_label=ft.Text('', size=18, weight=ft.FontWeight.BOLD, visible=False, selectable=True)

    md5_button=ft.ElevatedButton(icon=ft.Icons.PLAYLIST_PLAY, text='Запустить', on_click=lambda e: md5())


    md5_column=ft.Column(controls=[
        md5_label, md5_inp_file_label, ft.Row(controls=[md5_inp_file_field, md5_inp_file_button]), md5_button, md5_result_label, md5_output_label
    ])




    
    basics_markdown=ft.Markdown(value=basics_markdown_text, md_style_sheet=ft.MarkdownStyleSheet(p_text_style=ft.TextStyle(size=16), h2_text_style=ft.TextStyle(color="#FFB781"), h1_text_style=ft.TextStyle(color="#FFB781"), h2_padding=ft.padding.only(left=10, right=10)), selectable=True)
    basics_markdown_card=ft.Container(content=ft.Column([basics_markdown], expand=True, scroll="hidden"), padding=ft.padding.only(left=10, bottom=10), expand=True)
    


    def open_doc(text_name):
        docs_markdown_renderer.value=text_name
        docs_markdown_renderer.update()

    docs_label = ft.Text('Документация', size=24, weight=ft.FontWeight.BOLD)

    about_algorithms_docs_button=ft.TextButton(content=ft.Container(content=ft.Text('Основы', size=24, weight=ft.FontWeight.BOLD), alignment=ft.alignment.center_left),
            width=170,
            height=50,
            on_click=lambda e: open_doc(about_algorithms_markdown_text)
    )

    aes_docs_button=ft.TextButton(content=ft.Container(content=ft.Text('AES', size=24, weight=ft.FontWeight.BOLD), alignment=ft.alignment.center_left),
            width=170,
            height=50,
            on_click=lambda e: open_doc(aes_markdown_text)
    )

    blowfish_docs_button=ft.TextButton(content=ft.Container(content=ft.Text('Blowfish', size=24, weight=ft.FontWeight.BOLD), alignment=ft.alignment.center_left),
            width=170,
            height=50,
            on_click=lambda e: open_doc(blowfish_markdown_text)
    )

    rsa_docs_button=ft.TextButton(content=ft.Container(content=ft.Text('RSA', size=24, weight=ft.FontWeight.BOLD), alignment=ft.alignment.center_left),
            width=170,
            height=50,
            on_click=lambda e: open_doc(rsa_markdown_text)
    )

    sha256_docs_button=ft.TextButton(content=ft.Container(content=ft.Text('SHA-256', size=24, weight=ft.FontWeight.BOLD), alignment=ft.alignment.center_left),
            width=170,
            height=50,
            on_click=lambda e: open_doc(sha256_markdown_text)
    )

    md5_docs_button=ft.TextButton(content=ft.Container(content=ft.Text('MD5', size=24, weight=ft.FontWeight.BOLD), alignment=ft.alignment.center_left),
            width=170,
            height=50,
            on_click=lambda e: open_doc(md5_markdown_text)
    )

    tips_docs_button=ft.TextButton(content=ft.Container(content=ft.Text('Советы', size=24, weight=ft.FontWeight.BOLD), alignment=ft.alignment.center_left),
            width=170,
            height=50,
            on_click=lambda e: open_doc(tips_markdown_text)
    )


    docs_markdown_renderer=ft.Markdown(value=about_algorithms_markdown_text, md_style_sheet=ft.MarkdownStyleSheet(p_text_style=ft.TextStyle(size=16), h2_text_style=ft.TextStyle(color="#FFB781"), h1_text_style=ft.TextStyle(color="#FFB781"), h1_padding=ft.padding.only(top=10), h2_padding=ft.padding.only(top=7)), selectable=True)

    docs_side_column=ft.Column(controls=[docs_label, about_algorithms_docs_button, aes_docs_button, blowfish_docs_button, rsa_docs_button, sha256_docs_button, md5_docs_button, tips_docs_button])

    def route_change(e):
        if page.route == "/":
            page.views.clear()
            appbar.leading=None
            appbar.actions=[docs_button, key_button, home_button]
            page.views.append(
                ft.View(
                    "/",
                    [
                        appbar, ft.Row(expand=True, controls=[ft.Container(alignment=ft.alignment.center, content=side_column, padding=7, expand=False), ft.VerticalDivider(width=0.1, color=ft.Colors.GREY_800), home_column])
                    ],
                )
            )

        elif page.route == "/aes":
            page.views.clear()
            appbar.leading=None
            appbar.actions=[docs_button, key_button, home_button]
            page.views.append(
                ft.View(
                    "/aes",
                    [
                        appbar, ft.Row(expand=True, controls=[ft.Container(alignment=ft.alignment.center, content=side_column, padding=7, expand=False), ft.VerticalDivider(width=0.1, color=ft.Colors.GREY_800), ft.Tabs(padding=7, animation_duration=330, expand=8, tabs=[ft.Tab(text='Шифрование', content=ft.Container(adaptive=True, content=aes_enc_column, padding=7)), ft.Tab(text='Дешифрование', content=ft.Container(content=aes_dec_column, padding=7)), ft.Tab(text='Генерация ключей', content=ft.Container(content=aes_keygen_column, padding=7))])])
                    ],
                )
            )

        elif page.route == "/blowfish":
            page.views.clear()
            appbar.leading=None
            appbar.actions=[docs_button, key_button, home_button]
            page.views.append(
                ft.View(
                    "/blowfish",
                    [
                        appbar, ft.Row(expand=True, controls=[ft.Container(alignment=ft.alignment.center, content=side_column, padding=7, expand=False), ft.VerticalDivider(width=0.1, color=ft.Colors.GREY_800), ft.Tabs(padding=7, animation_duration=330, expand=8, tabs=[ft.Tab(text='Шифрование', content=ft.Container(adaptive=True, content=blowfish_enc_column, padding=7)), ft.Tab(text='Дешифрование', content=ft.Container(content=blowfish_dec_column, padding=7)), ft.Tab(text='Генерация ключей', content=ft.Container(content=blowfish_keygen_column, padding=7))])])
                    ],
                )
            )

        elif page.route == "/rsa":
            page.views.clear()
            appbar.leading=None
            appbar.actions=[docs_button, key_button, home_button]
            page.views.append(
                ft.View(
                    "/rsa",
                    [
                        appbar, ft.Row(expand=True, controls=[ft.Container(alignment=ft.alignment.center, content=side_column, padding=7, expand=False), ft.VerticalDivider(width=0.1, color=ft.Colors.GREY_800), ft.Tabs(padding=7, animation_duration=330, expand=8, tabs=[ft.Tab(text='Шифрование', content=ft.Container(adaptive=True, content=rsa_enc_column, padding=7)), ft.Tab(text='Дешифрование', content=ft.Container(content=rsa_dec_column, padding=7)), ft.Tab(text='Генерация ключей', content=ft.Container(content=rsa_keygen_column, padding=7))])])
                    ],
                )
            )

        elif page.route == "/sha256":
            page.views.clear()
            appbar.leading=None
            appbar.actions=[docs_button, key_button, home_button]
            page.views.append(
                ft.View(
                    "/sha256",
                    [
                        appbar, ft.Row(expand=True, controls=[ft.Container(alignment=ft.alignment.center, content=side_column, padding=7, expand=False), ft.VerticalDivider(width=0.1, color=ft.Colors.GREY_800), ft.Container(alignment=ft.alignment.center, content=sha256_column, padding=7, expand=8)])
                    ],
                )
            )

        elif page.route == "/md5":
            page.views.clear()
            appbar.leading=None
            appbar.actions=[docs_button, key_button, home_button]
            page.views.append(
                ft.View(
                    "/md5",
                    [
                        appbar, ft.Row(expand=True, controls=[ft.Container(alignment=ft.alignment.center, content=side_column, padding=7, expand=False), ft.VerticalDivider(width=0.1, color=ft.Colors.GREY_800), ft.Container(alignment=ft.alignment.center, content=md5_column, padding=7, expand=8)])
                    ],
                )
            )

        elif page.route == "/key_storage":
            appbar.actions=None
            appbar.leading=ft.Container(ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: close_storage()), width=50, height=50, padding=2)
            page.views.append(
                ft.View(
                    "/key_storage",
                    [
                        appbar, ft.Container(storage_listview, expand=8, padding=7)
                    ],
                )
            )

        elif page.route == "/basics":
            appbar.actions=None
            appbar.leading=ft.Container(ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go(previous)), width=50, height=50, padding=2)
            page.views.append(
                ft.View(
                    "/basics",
                    [
                        appbar, ft.Container(basics_markdown_card, expand=8, padding=7)
                    ],
                )
            )

        elif page.route == "/docs":
            appbar.actions=None
            appbar.leading=ft.Container(ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go(previous)), width=50, height=50, padding=2)
            page.views.append(
                ft.View(
                    "/docs",
                    [
                        appbar, ft.Row(expand=True, controls=[ft.Container(alignment=ft.alignment.center_left, content=docs_side_column, padding=7, expand=False), ft.VerticalDivider(width=0.1, color=ft.Colors.GREY_800), ft.Container(content=ft.Column([docs_markdown_renderer], expand=True, scroll="hidden"), expand=8, alignment=ft.alignment.top_left, padding=ft.padding.only(left=10, bottom=10))])
                    ],
                )
            )

        page.update()

        
        
    
    page.on_route_change = route_change
    page.add(
        appbar, ft.Row(expand=True, controls=[ft.Container(alignment=ft.alignment.center, content=side_column, padding=7, expand=False), ft.VerticalDivider(width=0.1, color=ft.Colors.GREY_800), home_column])
    )

    def close_storage():
        page.go(previous)
        storage_password_field.value=None

ft.app(target=main, assets_dir="assets")