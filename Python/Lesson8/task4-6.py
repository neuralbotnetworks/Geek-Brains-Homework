"""
4.)
 Начните работу над проектом 
  «Office equipment warehouse». 
  
  Создайте класс, описывающий склад. 
 
 А также класс «Оргтехника»,
    который будет базовым для классов-наследников.
  
 Эти классы — конкретные типы оргтехники 
   (printer, scanner, copier).
    
 В базовом классе определить параметры, 
    общие для приведенных типов. 
    
 В классах-наследниках реализовать параметры,
    уникальные для каждого типа оргтехники.
## 5.)
 Продолжить работу над первым заданием. 

 Разработать методы, 
 отвечающие за 
 приём оргтехники на склад и 
 передачу в определенное подразделение компании. 

 Для хранения данных 
 о наименовании и количестве единиц оргтехники, 
 а также других данных, 
 можно использовать любую подходящую структуру, 
 например словарь.
 
 6.)
 Продолжить работу над вторым заданием. 

 Реализуйте механизм валидации 
 вводимых пользователем данных. 

 Например, для указания 
 количества принтеров, 
 отправленных на склад, 
 нельзя использовать 
 строковый тип данных.

  Подсказка: 
постарайтесь по возможности 
реализовать в проекте 

«Office equipment warehouse» 
максимум возможностей, 
изученных на уроках по ООП.

"""

'''
class WareHouse:
   def __init__(self)

class OfficeEquipment:
   def __init__(self, name, quantity, color, price):
      self.name = name
      self.quantity = quantity
      self.color = color
      self.price = price

class Printer(OfficeEquipment):
      def get_print()

class Scanner(OfficeEquipment):
      def get_scan()
      
class Copier(OfficeEquipment):
      def get_copy()
'''
from tkinter import *
from tkinter.messagebox import *

class WareHouse:

    def __init__(self, main):

        self.entry1 = Entry(main, width=3, font=13)
        self.button1 = Button(main, text='Добавить')
        self.label1 = Label(main, width=27, font=15)

        self.entry1.grid(row=0, pady=3 , column=0)
        self.button1.grid(row=0, column=1)
        self.label1.grid(row=0, column=2)

        self.button1.bind("<Button-1>", self.add_office_equipment)
        self.button1.bind("<Button-2>", self.move_office_equipment)

    def add_office_equipment(self, event):

        txt = self.entry1.get()

        try:
            if int(txt) < 0:
                self.label1["text"] = "Нечего добавлять"
            else:
                self.label1["text"] = "Товар добавлен на склад."  
        except ValueError:
            self.label1["text"] = "Введите корректное количество: "
    
    def move_office_equipment(self, event):

        txt = self.move1.get()

        try:
            if int(txt) < 0:
                self.label1["text"] = "Нечего добавлять"
            else:
                self.label1["text"] = "Товар отправлен в магазин."  
        except ValueError:
            self.label1["text"] = "Введите корректное количество: "



def overview():
    win = Toplevel(root)
    overview_win = Label(win, text="Обзор товаров", font=("Ubuntu", 13))
    overview_win.pack()


def exit_app():
    root.destroy()


root = Tk()
root.title("Склад оргтехники")
root.geometry("800x600")
main_menu = Menu(root)
root.configure(menu=main_menu)

warehouse = Menu(main_menu,tearoff=0)
main_menu.add_cascade(label="Склад", menu=warehouse)
warehouse.add_command(label="Обзор", command=overview)
warehouse.add_command(label="Принять на Склад", command=add_office_equipment)
warehouse.add_command(label="Переместить в Розницу", command=move_office_equipment)


retail = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Розничная Торговля", menu=retail)
main_menu.add_separator()
retail.add_command(label="Обзор", command=overview)
retail.add_command(label="Реализация", command=move_office_equipment)

office_equipment = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Офисная техника", menu=office_equipment)
office_equipment.add_command(label="Принтеры")
office_equipment.add_separator()
office_equipment.add_command(label="Сканеры")
office_equipment.add_separator()
office_equipment.add_command(label="Копиры")

exit_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Выход", menu=exit_menu)
exit_menu.add_command(label="Выйти", command=exit_app)

tool_bar = Frame(root, bg="#A1A1A1")
tool_bar.pack(side=TOP, fill=X)

wh_btn = Button(tool_bar, text="Продажи", font=("Ubuntu", 13))
wh_btn.grid(row=0, column=0, padx=2, pady=2)

rt_btn = Button(tool_bar, text="Реализация", font=("Ubuntu", 13))
rt_btn.grid(row=0, column=1, padx=2, pady=2)

oe_btn = Button(tool_bar, text="Заявка", font=("Ubuntu", 13))
oe_btn.grid(row=0, column=2, padx=2, pady=2)

status_bar = Label(root, relief=SUNKEN, anchor=W, text="За принтерами будущее =) ")
status_bar.pack(side=BOTTOM, fill=X)


root.mainloop()

