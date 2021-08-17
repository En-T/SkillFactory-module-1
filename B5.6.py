def greet():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")

def show():
    print("  | 0 | 1 | 2 |")
    print("---------------")
    for i in range(3):
        print (f"{i} | {field[i * 3]} | {field[i * 3 + 1]} | {field[i * 3 + 2]} |")
        print("---------------")

def ask():
    while True:
        cords = input("         Ваш ход: ").split()        
        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue        
        x,y = cords        
        if not(x.isdigit()) or not(y.isdigit()):
            print(" Введите числа! ")
            continue        
        x, y = int(x), int(y)        
        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue  
        x_y = x * 3 + y
        if field[x_y] != " ":
            print(" Клетка занята! ")
            continue        
        return x_y    

def check_win():    
    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for coord in win_coord:
        if field[coord[0]] == field[coord[1]] == field[coord[2]] != " ":
            return field[coord[0]]
    return False

field = [" "] * 9
num = 0
greet()
while True:
    num += 1
    show()
    if num > 4:
        tmp = check_win()
        if tmp:
            print(tmp, "выйграл!")
            break    
    
    if num % 2 == 1:
        print ("Ходит крестик!")
    else:
        print("Ходит нолик")
    x_y = ask()
    if num % 2 == 1:
        field[x_y] = "X"
    else:
        field[x_y] = "0"    
    
    if num == 9:
        print("Ничья")
        break
