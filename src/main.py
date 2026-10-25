from dataclasses import dataclass

import flet as ft


def main(page: ft.Page):
    page.title = "Arq"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.width = 576
    page.window.height = 576
    page.window.always_on_top = True
    page.update()

    file_picker = ft.FilePicker()
    picked_file = ft.Text(text_align=ft.TextAlign.CENTER)

    async def on_pick_file(_: ft.Event[ft.Button]) -> None:
        files = await file_picker.pick_files(
            allow_multiple=False,
            file_type=ft.FilePickerFileType.CUSTOM,
            allowed_extensions=["txt"],
        )

        picked_file.value = files[0].path or "" if files else picked_file.value
        print(f"{picked_file.value}")

    page.add(
        ft.SafeArea(
            ft.ListView(
                [
                    ft.Button(
                        ft.Text(
                            "Selecionar arquivo ECD (.txt)",
                            max_lines=1,
                            overflow=ft.TextOverflow.ELLIPSIS,
                        ),
                        on_click=on_pick_file,
                        icon=ft.Icons.FILE_UPLOAD_ROUNDED,
                        width=64,
                        height=32,
                    ),
                    ft.Card(
                        ft.Container(
                            ft.Column(
                                [
                                    ft.ListTile(
                                        # bgcolor=ft.Colors.PRIMARY_CONTAINER,
                                        title=ft.Text(
                                            "",
                                            text_align=ft.TextAlign.CENTER,
                                            overflow=ft.TextOverflow.ELLIPSIS,
                                        ),
                                        subtitle=ft.Text(
                                            "",
                                            text_align=ft.TextAlign.CENTER,
                                            overflow=ft.TextOverflow.ELLIPSIS,
                                        ),
                                    ),
                                    ft.ListTile(
                                        # bgcolor=ft.Colors.PRIMARY_CONTAINER,
                                        title=ft.Text(
                                            "",
                                            text_align=ft.TextAlign.CENTER,
                                            overflow=ft.TextOverflow.ELLIPSIS,
                                        ),
                                        subtitle=ft.Text(
                                            "",
                                            text_align=ft.TextAlign.CENTER,
                                            overflow=ft.TextOverflow.ELLIPSIS,
                                        ),
                                    ),
                                    ft.ListTile(
                                        title=ft.Text(
                                            "",
                                            text_align=ft.TextAlign.CENTER,
                                            overflow=ft.TextOverflow.ELLIPSIS,
                                        ),
                                        subtitle=picked_file,
                                    ),
                                ]
                            ),
                            padding=ft.Padding.all(8),
                            height=210,
                        ),
                    ),
                    ft.Button(
                        ft.Text(
                            "Exportar plano de contas (.csv)",
                            overflow=ft.TextOverflow.ELLIPSIS,
                        ),
                        on_click=on_pick_file,
                        icon=ft.Icons.DOWNLOAD_ROUNDED,
                        width=64,
                        height=32,
                    ),
                    ft.Button(
                        ft.Text(
                            "Exportar balanço patrimonial (.csv)",
                            overflow=ft.TextOverflow.ELLIPSIS,
                        ),
                        on_click=on_pick_file,
                        icon=ft.Icons.DOWNLOAD_ROUNDED,
                        width=64,
                        height=32,
                    ),
                    ft.Button(
                        ft.Text(
                            "Exportar demonstração de resultado (.csv)",
                            overflow=ft.TextOverflow.ELLIPSIS,
                        ),
                        on_click=on_pick_file,
                        icon=ft.Icons.DOWNLOAD_ROUNDED,
                        width=64,
                        height=32,
                    ),
                    ft.Button(
                        ft.Text(
                            "Exportar saldos periódicos (.csv)",
                            overflow=ft.TextOverflow.ELLIPSIS,
                        ),
                        on_click=on_pick_file,
                        icon=ft.Icons.DOWNLOAD_ROUNDED,
                        width=64,
                        height=32,
                    ),
                    ft.Button(
                        ft.Text(
                            "Exportar livro diário (.csv)",
                            overflow=ft.TextOverflow.ELLIPSIS,
                        ),
                        on_click=on_pick_file,
                        icon=ft.Icons.DOWNLOAD_ROUNDED,
                        width=64,
                        height=32,
                    ),
                ],
                padding=ft.Padding.all(8),
                spacing=16,
            ),
            expand=True,
        )
    )


if __name__ == "__main__":
    # ft.run(lambda page: page.render(App))
    ft.run(main)
