def save_result_to_file():
    """
    Сохраняет содержимое виджета «Результат» в выбранный файл.
    Выдает сообщение в виджет «Ход выполнения программы».
    """
    destination_file = QFileDialog.getOpenFileName(filter="*.txt")
    destination_file_path = destination_file[0]

    with open(destination_file_path, "w", encoding="utf-8") as file:
        for i in range(ui.result.count()):
            line = ui.result.item(i).text()
            file.write(line)

    ui.message.addItem(f"Результат сохранен в {destination_file_path}")