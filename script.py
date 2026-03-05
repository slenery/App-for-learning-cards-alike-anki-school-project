import json as j
import time as t
import flet as ft








def loading():
    try:
        with open('data.json', 'r', encoding='utf-8') as file:
            data=j.load(file)
    except:
        data={}
    return data





# def work():
#     try:
#         with open("data.json", "r", encoding="utf-8") as file:
#             data=j.load(file)
#     except:
#         data={}
#     card = Card()
#     card_data=card.sv(data)
#     data[card_data["main"]] = { 
#     "second" : card_data["second"],
#     "third" : card_data["third"],
#     "translation" : card_data["translation"],
#                               }   
#     print(data)
#     with open("data.json", "w", encoding="utf-8") as file:
#             j.dump(data, file, ensure_ascii=False, indent=4)

        
      

    
        
        
        
        
        
        
        
        
        
        
        
            
        
    
 #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       
        
    
class Card(): #Свойства карточки



    def __init__(self, main="null", f2 = "null", f3 = "null", translation = "null", duplicate = False):
        self.main = main
        self.f2 = f2
        self.f3 = f3 
        self.tr = translation
        self.dup = duplicate
 
 
#     def sv(self, dict, check="null"):  #Функция установки значений для слов
#         while True:
#             #////////////////////////////////
#             print("Первая форма: ") 
#             inp = check_inp_for_words().capitalize()
#             if inp == "Ошибка ввода!":                       #ПОЛУЧАЕМ ПЕРВУЮ ФОРМУ
#                 print(inp)
#                 continue
#             if dict:
#                 if inp in dict.keys():
#                     replace = False
#                     while True:
#                         print("Такая карточка уже есть")
#                         print("1-Ввести заново, 2-заменить карточку")      #ПРОВЕРКА
#                         user_input = check_inp_for_numbers()                                              
#                         if user_input == "Можно вводить только цифры":
#                             print(user_input)
#                             continue
#                         if len(user_input)>1:
#                             print("ОШИБКА! Слишком большой ввод")
#                         if len(user_input)<1:
#                             print("ОШИБКА! Ожидается ввод")                   #В ПЛАНАХ добавить вторую карточку с таким названием 
#                             continue
#                         # good_chars= "12"
#                         # for char in user_input:
#                         #     if char not in good_chars:
#                         #         print("ОШИБКА! Введите 1 или 2")
#                         #         print("1-Ввести заново, 2-заменить карточку")
#                         #         continue
#                         if user_input == "1":
#                             break
#                         if user_input == "2":
#                             replace = True
#                             break
#                         else:
#                             print("ОШИБКА! Неверное значение")
#                             continue
#                     if replace == True:
#                         self.main = inp
#                         break
#                     else:
#                         continue
                            
                            
                        
                            
                                
                        
                    
                    
                        
                            
                    
                    
                
#             self.main = inp
#             break
#             #////////////////////////////////
#         while True:    
#             #////////////////////////////////
#             print("Вторая форма: ") 
#             inp = check_inp_for_words()
#             if inp == "Ошибка ввода!":
#                 print(inp)
#                 continue                                     #ПОЛУЧАЕМ ВТОРУЮ ФОРМУ
#             self.f2 = inp
#             print("Третья форма: ") 
#             break
#             #////////////////////////////////
#         while True:
#             #////////////////////////////////
#             inp = check_inp_for_words()
#             if inp == "Ошибка ввода!":
#                 print(inp)
#                 continue                                     #ПОЛУЧАЕМ ТРЕТЬЮ ФОРМУ
#             self.f3 = inp
#             print("Перевод глагола: ") 
#             break
#             #////////////////////////////////
#         while True:
#             inp = check_inp_for_words()
#             if inp == "Ошибка ввода!":
#                 print(inp)                                   #ПОЛУЧАЕМ ПЕРЕВОД
#                 continue
#             self.tr = inp
#             return {
                
#             "main" : self.main, 
#             "second" : self.f2,             #значения из ввода превращаются в словарь
#             "third" : self.f3,
#             "translation" : self.tr
            
#             } 
            
            
            
#  #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
        













# def check_inp_for_words():    # проверка ввода
#     good_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
#     user_input = input().strip()
#     for char in user_input:       
#         if char not in good_chars:
#             user_input = "Ошибка ввода!"
#             break 
#         if len(user_input) > 20:
#             user_input = "Ошибка ввода!"
#             break
#         if len(user_input) < 2:
#             user_input = "Ошибка ввода!"
#             break
#         else:
#             continue
#     return user_input    


# # ПРОВЕРКА ВВОДА В МЕНЮ ВЫБОРА




# def check_inp_for_numbers():
#     good_chars = "0123456789"
#     user_input = input().strip()
#     for char in user_input:       
#         if char not in good_chars:
#             user_input = "ОШИБКА! Можно вводить только цифры"
#             return user_input

#         else:
#             continue
#     return user_input 




# №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№
# ФУНКЦИЯ ГЛАВНОГО МЕНЮ
# №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№                   


def main(page : ft.Page):
    def welcome_page():
        page.clean()
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.MainAxisAlignment.CENTER
        btn1 = ft.Button(content="Add a card", on_click = add_card_menu)
        btn2 = ft.Button(content="To review")   #В ПРОЦЕССЕ 
        btn3 = ft.Button(content="Cards list")  #В ПРОЦЕССЕ   
        
        

        
        
        
        
        page.add(
            ft.Column([
        
                ft.Text("Hello"),
                ft.Text("What are you gonna do?"),
                btn1,
                btn2,
                btn3
                
        
            ])

        
    )
        
        
        
        # №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№


        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№I ФУНКЦИИ I№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№

    def add_card_menu(e1):
        
        
        def add_card():
            pass
        
        # ((((((((((((((((((((((((((((((((((((((((((((((((((((( ФУНКЦИЯ ВЫВОДА КНОПКИ ))))))))))))))))))))))))))))))))))))))))))))))))))))))
        def add_card_button():
            nonlocal title, duplicate_error_text
            if title.value and len(title.value) > 1 and duplicate_error_text.value == "" : #ВОТ ТУТ ДОБАВИТЬ ПРОВЕРКУ НА ТЕКСТ О СУЩЕСТВУЮЩЕЙ КАРТОЧКЕ
                add_card_btn.visible = True
            else:
                add_card_btn.visible = False
            page.update()
                                             
        # ((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
        
        # (((((((((((((((((((((((((((((((((((((((((((((((((( ФУНКЦИЯ НАСТРОЙКИ ДУБЛИКАТА ))))))))))))))))))))))))))))))))))))))))))))))))))
        
    
        
        
        def dup_button_func(dup_event):
            nonlocal duplicate, duplicate_error_text, duplicate_text, duplicate_button
            duplicate = True
            duplicate_error_text.value = ""
            duplicate_text.visible = True
            duplicate_button.visible = False
            # duplicate = True
            # duplicate.text = True
            
            
                                                                      #ВАЖНАЯ ШТУКАА, надо доделать!!!!                                              
        
        # ((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
        
        # (((((((((((((((((((((((((((((((((((((((((((((((((( ФУНКЦИЯ ПРОВЕРКИ НА ДУБЛИКАТ ))))))))))))))))))))))))))))))))))))))))))))))))))
        
        
          
        def duplicate_check(text):
            nonlocal duplicate_error_text, duplicate
            current_text = str(text.control.value).capitalize()
            
            if current_text in data.keys() and duplicate == False:
                duplicate_error_text.value = "This card is already exists"
                duplicate_button.visible = True
                
            else:
                duplicate_error_text.value = ""
                duplicate_button.visible = False
            add_card_button()          #ВЫЗЫВАЕТ ФУНКЦИЮ ВЫВОДА КНОПКИ 
            page.update()

        # №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№II№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№
        #ОЧИСТКА СТРАНИЦЫ
        page.clean()

        
        # НАСТРОЙКА РАСПОЛОЖЕНИЯ
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.MainAxisAlignment.CENTER
        
        # ПЕРЕМЕННЫЕ 
        title = ft.TextField(label="Card title", hint_text="Enter something", multiline=True, max_length=174, on_change = duplicate_check)
        duplicate_error_text = ft.Text("", color="red")
        duplicate_button = ft.ElevatedButton(content="You can add a duplicate", icon = ft.Icons.ADD, visible = False, on_click = dup_button_func)
        duplicate = False
        duplicate_text = ft.Text("                    DUPLICATE", visible=False, color = "red")
        main_desc = ft.TextField(label="Description", hint_text="Enter something", multiline=True, max_length=319)
        info1 = ft.Text("Enter the card title")
        info2 = ft.Text("You can enter the translation or other")
        info3 =ft.Text("You also can add more descriptions lines")       
        btn1 = ft.IconButton(icon = ft.Icons.ADD)       
        btn2 = ft.ElevatedButton(icon=ft.Icons.ARROW_BACK, content = "Return back", on_click = welcome_page)
        add_card_btn = ft.ElevatedButton(content="Create card", icon = ft.Icons.CHECK, on_click=add_card, visible = False)
        
        #ДОБАВЛЕНИЕ НА ГЛАВНЫЙ ЭКРАН
        page.add(
            ft.Column([
            duplicate_text,
            
            ft.Row([
               
            btn2,
            add_card_btn 
            
            ]),
            
            ft.Row([
            
            title,
            info1,
            duplicate_error_text,
            duplicate_button      
            
            ]),
            ft.Row([
            
            main_desc,
            info2     
            
            ]),
            ft.Row([
                btn1,
                info3
            ])
            
            
            
            ]))

        add_card_button()
        
        
        
        
        
 
    data = loading()
    print(data)
    page.title = "Otriga App"
    welcome_page()

















        

ft.app(main)
    
        