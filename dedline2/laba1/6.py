draw_symbol = input("Введите символ для рисования: ")
rect_height = int(input("Введите высоту прямоугольника: "))
rect_width = int(input("Введите ширину прямоугольника: "))
row_counter = 0
while row_counter < rect_height:
    col_counter = 0
    current_row_output = ""
while col_counter < rect_width:
    current_row_output += draw_symbol
    col_counter += 1
    print(current_row_output)
    row_counter += 1

