import xlsxwriter
from get_info import get_info_for_recording

# импортируем функцию get_info_for_recording которая возвращает данные по каждой карточке с товаром
# создаем Excel файл
# задаем размеры полей в таблице (ширина колонок)
# загружаем данные в таблицу по очереди, карточку за карточкой
def writer(parametrs):
    book = xlsxwriter.Workbook(r"C:\Studies\BS4\from_website_to_Excel\dresses.xlsx")
    page = book.add_worksheet('Товар')

    row = 0
    column = 0

    page.set_column("A:A", 30)
    page.set_column("B:B", 20)
    page.set_column("C:C", 50)
    page.set_column("D:D", 50)

    for item in parametrs:
        page.write(row, column, item[0])
        page.write(row, column+1, item[1])
        page.write(row, column+2, item[2])
        page.write(row, column+3, item[3])
        row += 1

    book.close()

writer(get_info_for_recording())