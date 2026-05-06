# import json as j
# import time as t
# import flet as ft








# def loading():
#     try:
#         with open('data.json', 'r', encoding='utf-8') as file:
#             data=j.load(file)
#     except:
#         data={}
#     return data





# def work():
#     # try:
#     #     with open("data.json", "r", encoding="utf-8") as file:
#     #         data=j.load(file)
#     # except:
#     #     data={}
#     data = loading()
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

        
      

    
        
        
        
        
        
        
        
        
        
        
        
            
        
    
#  #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       
        
    
# class Card(): #Свойства карточки



#     def __init__(self, title="null", description = "null", description2 = "null", description3 = "null", duplicate = False):
#         self.title = title
#         self.d = description  
#         self.d2 = description2
#         self.d3 = description3
#         self.dup = duplicate
        
#     def create_dict (self):
        
#         return {
                
#         "title" : self.title, 
#         "description" : self.d,             #значения превращаются в словарь
#         "description2" : self.d2,
#         "description3" : self.d3,
#         "dup": self.dup
            
#       } 
            
# #             } 
            
# #             
        
        
        
 
 
#     # def sv(self, dict, check="null"):  #Функция установки значений для слов
#     #     while True:
#     #         #////////////////////////////////
#     #         print("Первая форма: ") 
#     #         inp = check_inp_for_words().capitalize()
#     #         if inp == "Ошибка ввода!":                       #ПОЛУЧАЕМ ПЕРВУЮ ФОРМУ
#     #             print(inp)
#     #             continue
#     #         if dict:
#     #             if inp in dict.keys():
#     #                 replace = False
#     #                 while True:
#     #                     print("Такая карточка уже есть")
#     #                     print("1-Ввести заново, 2-заменить карточку")      #ПРОВЕРКА
#     #                     user_input = check_inp_for_numbers()                                              
#     #                     if user_input == "Можно вводить только цифры":
#     #                         print(user_input)
#     #                         continue
#     #                     if len(user_input)>1:
#     #                         print("ОШИБКА! Слишком большой ввод")
#     #                     if len(user_input)<1:
#     #                         print("ОШИБКА! Ожидается ввод")                   #В ПЛАНАХ добавить вторую карточку с таким названием 
#     #                         continue
#     #                     # good_chars= "12"
#     #                     # for char in user_input:
#     #                     #     if char not in good_chars:
#     #                     #         print("ОШИБКА! Введите 1 или 2")
#     #                     #         print("1-Ввести заново, 2-заменить карточку")
#     #                     #         continue
#     #                     if user_input == "1":
#     #                         break
#     #                     if user_input == "2":
#     #                         replace = True
#     #                         break
#     #                     else:
#     #                         print("ОШИБКА! Неверное значение")
#     #                         continue
#     #                 if replace == True:
#     #                     self.main = inp
#     #                     break
#     #                 else:
#     #                     continue

                            
                            
                        
                            
                                
                        
                    
                    
                        
                            
                    
                    
                
# #             self.main = inp
# #             break
# #             #////////////////////////////////
# #         while True:    
# #             #////////////////////////////////
# #             print("Вторая форма: ") 
# #             inp = check_inp_for_words()
# #             if inp == "Ошибка ввода!":
# #                 print(inp)
# #                 continue                                     #ПОЛУЧАЕМ ВТОРУЮ ФОРМУ
# #             self.f2 = inp
# #             print("Третья форма: ") 
# #             break
# #             #////////////////////////////////
# #         while True:
# #             #////////////////////////////////
# #             inp = check_inp_for_words()
# #             if inp == "Ошибка ввода!":
# #                 print(inp)
# #                 continue                                     #ПОЛУЧАЕМ ТРЕТЬЮ ФОРМУ
# #             self.f3 = inp
# #             print("Перевод глагола: ") 
# #             break
# #             #////////////////////////////////
# #         while True:
# #             inp = check_inp_for_words()
# #             if inp == "Ошибка ввода!":
# #                 print(inp)                                   #ПОЛУЧАЕМ ПЕРЕВОД
# #                 continue
# #             self.tr = inp
# #             return {
                
# #             "main" : self.main, 
# #             "second" : self.f2,             #значения из ввода превращаются в словарь
# #             "third" : self.f3,
# #             "translation" : self.tr
            
# #             } 
            
            
            
# #  #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
        













# # def check_inp_for_words():    # проверка ввода
# #     good_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
# #     user_input = input().strip()
# #     for char in user_input:       
# #         if char not in good_chars:
# #             user_input = "Ошибка ввода!"
# #             break 
# #         if len(user_input) > 20:
# #             user_input = "Ошибка ввода!"
# #             break
# #         if len(user_input) < 2:
# #             user_input = "Ошибка ввода!"
# #             break
# #         else:
# #             continue
# #     return user_input    


# # # ПРОВЕРКА ВВОДА В МЕНЮ ВЫБОРА




# # def check_inp_for_numbers():
# #     good_chars = "0123456789"
# #     user_input = input().strip()
# #     for char in user_input:       
# #         if char not in good_chars:
# #             user_input = "ОШИБКА! Можно вводить только цифры"
# #             return user_input

# #         else:
# #             continue
# #     return user_input 




# # №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№
# # ФУНКЦИЯ ГЛАВНОГО МЕНЮ
# # №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№                   


# def main(page : ft.Page):
#     def welcome_page():
#         page.clean()
#         page.vertical_alignment = ft.MainAxisAlignment.CENTER
#         page.horizontal_alignment = ft.MainAxisAlignment.CENTER
#         btn1 = ft.Button(content="Add a card", on_click = add_card_menu)
#         btn2 = ft.Button(content="To review")   #В ПРОЦЕССЕ 
#         btn3 = ft.Button(content="Cards list")  #В ПРОЦЕССЕ   
        
        

        
        
        
        
#         page.add(
#             ft.Column([
        
#                 ft.Text("Hello"),
#                 ft.Text("What are you gonna do?"),
#                 btn1,
#                 btn2,
#                 btn3
                
        
#             ])

        
#     )
        
        
        
#         # №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№


        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№I ФУНКЦИИ I№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№

#     def add_card_menu(e1):
#         nonlocal data, duplicate
        
#         def add_card():
#             page.clean()
#             nonlocal title, main_desc
#             # # data[title.value] = main_desc.value
#             # # print(data)

#             # card = Card()
#             # card.main = title.value
#             # card.d2 = main_desc.value
#             # data.update(card.create_dict())
#             # print(data)
#             # try:
#             #     with open("data.json", "r", encoding="utf-8") as file:
#             #         data=j.load(file)
#             # except:
#             #     data={}
#             card = Card()
#             card.title = title.value
#             dup_id = None 
#             card_exists = False
#             existing_key = None
#             for key, card_data in data.items():
#                 if card_data["title"] == card.title.capitalize():
#                     card_exists = True
#                     existing_key = key
#                     break
            
#             if card_exists and duplicate == False:
#                 del data[existing_key]
            
#             if duplicate == True:
#                 dup_qty = 0
#                 for card_data in data.values():
#                     if card_data["title"] == card.title.capitalize():  
#                         dup_qty += 1
#                 dup_id = dup_qty + 1  
            
#             card.d = main_desc.value
#             card_data = card.create_dict()
            
#             if data:
#                 id = max(int(key) for key in data.keys()) + 1
#             else:
#                 id = 1
            
#             data[id] = {
#                 "dup": card_data["dup"],
#                 "dup_id": dup_id,
#                 "title": (card_data["title"]).capitalize(),
#                 "d": card_data["description"],
#                 "d2": card_data["description2"],
#                 "d3": card_data["description3"]
#             }
            
#             print(data)
#             with open("data.json", "w", encoding="utf-8") as file:
#                 j.dump(data, file, ensure_ascii=False, indent=4)
            
#             welcome_page()
      
            
        
#         # ((((((((((((((((((((((((((((((((((((((((((((((((((((( ФУНКЦИЯ ВЫВОДА КНОПКИ ))))))))))))))))))))))))))))))))))))))))))))))))))))))
#         def add_card_button():
#             nonlocal title, duplicate_error_text
#             # if title.value and len(title.value) > 1 and duplicate_error_text.value == "" : #ВОТ ТУТ ДОБАВИТЬ ПРОВЕРКУ НА ТЕКСТ О СУЩЕСТВУЮЩЕЙ КАРТОЧКЕ
#             if title.value and len(title.value) > 1:
#                 add_card_btn.visible = True
#             else:
#                 add_card_btn.visible = False
#             page.update()
                                             
#         # ((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
        
#         # (((((((((((((((((((((((((((((((((((((((((((((((((( ФУНКЦИЯ НАСТРОЙКИ ДУБЛИКАТА ))))))))))))))))))))))))))))))))))))))))))))))))))
        
    
        
        
#         def dup_button_func(dup_event):
#             nonlocal duplicate, duplicate_error_text, duplicate_text, duplicate_button
#             duplicate = True
#             duplicate_error_text.value = ""
#             duplicate_text.visible = True
#             duplicate_button.visible = False
#             # duplicate = True
#             # duplicate.text = True
            
            
#                                                                       #ВАЖНАЯ ШТУКАА, надо доделать!!!!                                              
        
#         # ((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
        
#         # (((((((((((((((((((((((((((((((((((((((((((((((((( ФУНКЦИЯ ПРОВЕРКИ НА ДУБЛИКАТ ))))))))))))))))))))))))))))))))))))))))))))))))))
        
        
          
#         def duplicate_check(text):
#             nonlocal duplicate_error_text, duplicate
#             current_text = str(text.control.value).capitalize()
            
#             card_exist = False
#             for card_data in data.values():
#                 if card_data["title"] == current_text:
#                     card_exist = True
#                     break
#             if card_exist and duplicate == False:
#                 duplicate_error_text.value = "This card is already exists"
#                 duplicate_button.visible = True
#             else:
#                 duplicate_error_text.value = ""
#                 duplicate_button.visible = False
                
            
            
#             # if current_text in data.values() and duplicate == False:
#             #     duplicate_error_text.value = "This card is already exists"
#             #     duplicate_button.visible = True
                
#             # else:
#             #     duplicate_error_text.value = ""
#             #     duplicate_button.visible = False
#             add_card_button()          #ВЫЗЫВАЕТ ФУНКЦИЮ ВЫВОДА КНОПКИ 
#             page.update()

#         # №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№II№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№
#         #ОЧИСТКА СТРАНИЦЫ
#         page.clean()

        
#         # НАСТРОЙКА РАСПОЛОЖЕНИЯ
#         page.vertical_alignment = ft.MainAxisAlignment.CENTER
#         page.horizontal_alignment = ft.MainAxisAlignment.CENTER
        
#         # ПЕРЕМЕННЫЕ 
#         title = ft.TextField(label="Card title", hint_text="Enter something", multiline=True, max_length=174, on_change = duplicate_check)
#         duplicate_error_text = ft.Text("", color="red")
#         duplicate_button = ft.ElevatedButton(content="You can add a duplicate", icon = ft.Icons.ADD, visible = False, on_click = dup_button_func)
#         duplicate = False
#         duplicate_text = ft.Text("                    DUPLICATE", visible=False, color = "red")
#         main_desc = ft.TextField(label="Description", hint_text="Enter something", multiline=True, max_length=319)
#         info1 = ft.Text("Enter the card title")
#         info2 = ft.Text("You can enter the translation or other")
#         info3 =ft.Text("You also can add more descriptions lines")       
#         btn1 = ft.IconButton(icon = ft.Icons.ADD)       
#         btn2 = ft.ElevatedButton(icon=ft.Icons.ARROW_BACK, content = "Return back", on_click = welcome_page)
#         add_card_btn = ft.ElevatedButton(content="Create card", icon = ft.Icons.CHECK, on_click=add_card, visible = False)
        
#         #ДОБАВЛЕНИЕ НА ГЛАВНЫЙ ЭКРАН
#         page.add(
#             ft.Column([
#             duplicate_text,
            
#             ft.Row([
               
#             btn2,
#             add_card_btn 
            
#             ]),
            
#             ft.Row([
            
#             title,
#             info1,
#             duplicate_error_text,
#             duplicate_button      
            
#             ]),
#             ft.Row([
            
#             main_desc,
#             info2     
            
#             ]),
#             ft.Row([
#                 btn1,
#                 info3
#             ])
            
            
            
#             ]))

#         add_card_button()
        
        
        
        
        
 
#     data = loading()
#     print(data)
#     page.title = "Otriga App"
#     welcome_page()

















        

# ft.app(main)






# 2






# import json as j
# import random as r
# import flet as ft

# def loading():
#     try:
#         with open('data.json', 'r', encoding='utf-8') as file:
#             data=j.load(file)
#     except:
#         data={}
#     return data

# def work():
#     data = loading()
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

# #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       
    
# class Card(): #Свойства карточки
#     def __init__(self, title="null", description = "null", description2 = "null", description3 = "null", duplicate = False):
#         self.title = title
#         self.d = description  
#         self.d2 = description2
#         self.d3 = description3
#         self.dup = duplicate
        
#     def create_dict (self):
#         return {
#             "title" : self.title, 
#             "description" : self.d,
#             "description2" : self.d2,
#             "description3" : self.d3,
#             "dup": self.dup
#         }

# #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# # ФУНКЦИЯ ГЛАВНОГО МЕНЮ
# #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def main(page : ft.Page):
#     data = loading()
#     print(data)
    
#     def welcome_page():
#         page.clean()
#         page.vertical_alignment = ft.MainAxisAlignment.CENTER
#         page.horizontal_alignment = ft.MainAxisAlignment.CENTER
#         btn1 = ft.ElevatedButton(content="Add a card", on_click = add_card_menu)
#         btn2 = ft.ElevatedButton(content="Random review", on_click = random_review)
#         btn3 = ft.ElevatedButton(content="Cards list", on_click = cards_list)
        
#         page.add(
#             ft.Column([
#                 ft.Text("Otriga App"),
#                 ft.Text("What are you gonna do?"),
#                 btn1,
#                 btn2,
#                 btn3
#             ])
#         )
    
#     #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#     # СПИСОК КАРТОЧЕК
#     #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    
#     def cards_list(e):
#         if not data:
#             page.clean()
#             page.add(
#                 ft.Column([
#                     ft.Text("No cards yet"),
#                     ft.ElevatedButton("Back", on_click=welcome_page)
#                 ])
#             )
#             return
        
#         page.clean()
#         page.scroll = ft.ScrollMode.AUTO
        
#         for card_id, card in data.items():
#             # ПОКАЗЫВАЕМ ДОПОЛНИТЕЛЬНЫЕ ПОЛЯ ЕСЛИ ОНИ ЕСТЬ
#             desc_text = card.get('d', 'No description')
#             if card.get('d2') and card['d2'] != "null":
#                 desc_text += f"\nAdditional: {card['d2']}"
#             if card.get('d3') and card['d3'] != "null":
#                 desc_text += f"\nAdditional: {card['d3']}"
            
#             page.add(
#                 ft.Container(
#                     content=ft.Column([
#                         ft.Text(f"Title: {card['title']}", size=18, weight=ft.FontWeight.BOLD),
#                         ft.Text(f"Description: {desc_text}")
#                     ]),
#                     padding=10,
#                     border=ft.border.all(1, ft.Colors.GREY),
#                     margin=5
#                 )
#             )
        
#         page.add(ft.ElevatedButton("Back", on_click=welcome_page))
    
#     #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#     # СЛУЧАЙНОЕ ПОВТОРЕНИЕ
#     #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    
#     def random_review(e):
#         if not data:
#             page.clean()
#             page.add(
#                 ft.Column([
#                     ft.Text("No cards to review"),
#                     ft.ElevatedButton("Back", on_click=welcome_page)
#                 ])
#             )
#             return
        
#         # ВЫБИРАЕМ СЛУЧАЙНУЮ КАРТОЧКУ
#         card_list = []
#         for key in data.keys():
#             card_list.append(key)
        
#         random_id = r.choice(card_list)
#         current_card = data[random_id]
        
#         page.clean()
#         page.vertical_alignment = ft.MainAxisAlignment.CENTER
#         page.horizontal_alignment = ft.MainAxisAlignment.CENTER
        
#         question = ft.Text(current_card["title"], size=24)
#         answer_field = ft.TextField(label="Your answer", hint_text="Type here...", width=400)
#         result_text = ft.Text("")
        
#         def check_answer(e):
#             if answer_field.value.lower().strip() == current_card["d"].lower():
#                 result_text.value = "Correct!"
#                 result_text.color = "green"
#             else:
#                 result_text.value = f"Wrong! Correct: {current_card['d']}"
#                 result_text.color = "red"
            
#             answer_field.disabled = True
#             check_btn.disabled = True
#             next_btn.visible = True
#             page.update()
        
#         def next_card(e):
#             random_review(e)
        
#         check_btn = ft.ElevatedButton("Check", on_click=check_answer)
#         next_btn = ft.ElevatedButton("Next card", on_click=next_card, visible=False)
#         back_btn = ft.ElevatedButton("Back", on_click=welcome_page)
        
#         page.add(
#             ft.Column([
#                 ft.Text("Random Review"),
#                 ft.Divider(),
#                 question,
#                 answer_field,
#                 ft.Row([check_btn, next_btn]),
#                 result_text,
#                 back_btn
#             ])
#         )
    
#     #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#     # ДОБАВЛЕНИЕ КАРТОЧКИ 
#     #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#     def add_card_menu(e1):
#         # ПЕРЕМЕННЫЕ
#         title = ft.TextField(label="Card title", hint_text="Enter something", multiline=True, max_length=174)
#         main_desc = ft.TextField(label="Main description", hint_text="Enter translation", multiline=True, max_length=319)
#         desc2 = ft.TextField(label="Additional description", hint_text="Optional", multiline=True, max_length=319, visible=False)
#         desc3 = ft.TextField(label="Another description", hint_text="Optional", multiline=True, max_length=319, visible=False)
        
#         duplicate = False
#         duplicate_text = ft.Text("DUPLICATE MODE ACTIVE", visible=False, color="orange")
#         duplicate_error_text = ft.Text("", color="red")
#         duplicate_button = ft.ElevatedButton(content="Add as duplicate", icon=ft.Icons.ADD, visible=False)
#         add_card_btn = ft.ElevatedButton(content="Create card", icon=ft.Icons.CHECK, visible=False)
        
#         # СЧЁТЧИК ДЛЯ ДОПОЛНИТЕЛЬНЫХ ПОЛЕЙ
#         extra_fields_count = 0
        
#         def add_extra_field(e):
#             nonlocal extra_fields_count
#             extra_fields_count += 1
#             if extra_fields_count == 1:
#                 desc2.visible = True
#             elif extra_fields_count == 2:
#                 desc3.visible = True
#             page.update()
        
#         def check_duplicate(e):
#             nonlocal duplicate, duplicate_text, duplicate_button, duplicate_error_text
#             current_text = title.value.capitalize()
            
#             # ПРОВЕРЯЕМ ЕСТЬ ЛИ ТАКАЯ КАРТОЧКА
#             card_exists = False
#             for card_data in data.values():
#                 if card_data.get("title") == current_text:
#                     card_exists = True
#                     break
            
#             if card_exists and duplicate == False:
#                 duplicate_error_text.value = "This card already exists! Click button to add duplicate"
#                 duplicate_button.visible = True
#                 duplicate_text.visible = False
#             else:
#                 duplicate_error_text.value = ""
#                 if duplicate == True:
#                     duplicate_button.visible = False
#                     duplicate_text.visible = True
#                 else:
#                     duplicate_button.visible = False
#                     duplicate_text.visible = False
            
#             # ПРОВЕРЯЕМ КНОПКУ СОЗДАНИЯ
#             if title.value and len(title.value) > 1 and main_desc.value:
#                 add_card_btn.visible = True
#             else:
#                 add_card_btn.visible = False
            
#             page.update()
        
#         def enable_duplicate(e):
#             nonlocal duplicate, duplicate_text, duplicate_button, duplicate_error_text
#             duplicate = True
#             duplicate_text.visible = True
#             duplicate_button.visible = False
#             duplicate_error_text.value = ""
            
#             if title.value and len(title.value) > 1 and main_desc.value:
#                 add_card_btn.visible = True
            
#             page.update()
        
#         def add_card(e):
#             nonlocal duplicate
            
#             card = Card()
#             card.title = title.value
#             card.d = main_desc.value
#             card.d2 = desc2.value if desc2.value else "null"
#             card.d3 = desc3.value if desc3.value else "null"
#             card.dup = duplicate
            
#             card_data = card.create_dict()
            
#             # ПРОВЕРЯЕМ ЕСТЬ ЛИ ТАКАЯ КАРТОЧКА
#             card_exists = False
#             existing_key = None
#             for key, card_data_in_data in data.items():
#                 if card_data_in_data.get("title") == card.title.capitalize():
#                     card_exists = True
#                     existing_key = key
#                     break
            
#             # ЕСЛИ ДУБЛИКАТ НЕ РАЗРЕШЕН И КАРТОЧКА ЕСТЬ - УДАЛЯЕМ СТАРУЮ
#             if card_exists and duplicate == False:
#                 del data[existing_key]
            
#             # СЧИТАЕМ ДУБЛИКАТЫ
#             dup_id = None
#             if duplicate == True:
#                 dup_count = 0
#                 for card_data_in_data in data.values():
#                     if card_data_in_data.get("title") == card.title.capitalize():
#                         dup_count += 1
#                 dup_id = dup_count + 1
            
#             # НОВЫЙ ID
#             new_id = len(data) + 1
            
#             data[new_id] = {
#                 "title": (card_data["title"]).capitalize(),
#                 "d": card_data["description"],
#                 "d2": card_data["description2"],
#                 "d3": card_data["description3"],
#                 "dup": duplicate,
#                 "dup_id": dup_id
#             }
            
#             with open("data.json", "w", encoding="utf-8") as file:
#                 j.dump(data, file, ensure_ascii=False, indent=4)
            
#             welcome_page()
        
#         # НАСТРАИВАЕМ СОБЫТИЯ
#         title.on_change = check_duplicate
#         main_desc.on_change = check_duplicate
#         duplicate_button.on_click = enable_duplicate
#         add_card_btn.on_click = add_card
        
#         # КНОПКИ
#         add_field_btn = ft.IconButton(icon=ft.Icons.ADD, on_click=add_extra_field)
#         back_btn = ft.ElevatedButton(icon=ft.Icons.ARROW_BACK, content="Return back", on_click=welcome_page)
        
#         page.clean()
#         page.vertical_alignment = ft.MainAxisAlignment.CENTER
#         page.horizontal_alignment = ft.MainAxisAlignment.CENTER
        
#         page.add(
#             ft.Column([
#                 duplicate_text,
#                 ft.Row([back_btn, add_card_btn]),
#                 title,
#                 duplicate_error_text,
#                 duplicate_button,
#                 main_desc,
#                 ft.Row([add_field_btn, ft.Text("Add more descriptions")]),
#                 desc2,
#                 desc3
#             ])
#         )
    
#     page.title = "Otriga App"
#     welcome_page()

# ft.app(main)




# 3


import json as j
import random as r
import flet as ft

def loading():
    try:
        with open('data.json', 'r', encoding='utf-8') as file:
            data=j.load(file)
    except:
        data={}
    return data

def work():
    data = loading()
    card = Card()
    card_data=card.sv(data)
    data[card_data["main"]] = { 
    "second" : card_data["second"],
    "third" : card_data["third"],
    "translation" : card_data["translation"],
                              }   
    print(data)
    with open("data.json", "w", encoding="utf-8") as file:
            j.dump(data, file, ensure_ascii=False, indent=4)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       
    
class Card(): #Свойства карточки
    def __init__(self, title="null", description = "null", description2 = "null", description3 = "null", duplicate = False):
        self.title = title
        self.d = description  
        self.d2 = description2
        self.d3 = description3
        self.dup = duplicate
        
    def create_dict (self):
        return {
            "title" : self.title, 
            "description" : self.d,
            "description2" : self.d2,
            "description3" : self.d3,
            "dup": self.dup
        }

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# ФУНКЦИЯ ГЛАВНОГО МЕНЮ
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def main(page : ft.Page):
    data = loading()
    print(data)
    
    def welcome_page():
        page.clean()
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.MainAxisAlignment.CENTER
        btn1 = ft.ElevatedButton(content="Add a card", on_click = add_card_menu)
        btn2 = ft.ElevatedButton(content="Random review", on_click = random_review)
        btn3 = ft.ElevatedButton(content="Cards list", on_click = cards_list)
        
        page.add(
            ft.Column([
                ft.Text("Otriga App"),
                ft.Text("What are you gonna do?"),
                btn1,
                btn2,
                btn3
            ])
        )
    
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # СПИСОК КАРТОЧЕК 
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    
    def delete_card(card_id):
        """Удаляет карточку"""
        if str(card_id) in data:
            del data[str(card_id)]
            with open("data.json", "w", encoding="utf-8") as file:
                j.dump(data, file, ensure_ascii=False, indent=4)
    
    def cards_list(e):
        if not data:
            page.clean()
            page.add(
                ft.Column([
                    ft.Text("No cards yet"),
                    ft.ElevatedButton("Back", on_click=welcome_page)
                ])
            )
            return
        
        page.clean()
        page.scroll = ft.ScrollMode.AUTO
        
        for card_id, card in data.items():
            # ПОКАЗЫВАЕМ ДОПОЛНИТЕЛЬНЫЕ ПОЛЯ ЕСЛИ ОНИ ЕСТЬ
            desc_text = card.get('d', 'No description')
            if card.get('d2') and card['d2'] != "null":
                desc_text += f"\nAdditional: {card['d2']}"
            if card.get('d3') and card['d3'] != "null":
                desc_text += f"\nAdditional: {card['d3']}"
            
            # КНОПКА УДАЛЕНИЯ
            def make_delete_func(cid):
                def delete_click(e):
                    delete_card(cid)
                    cards_list(e)  # ОБНОВЛЯЕМ СПИСОК
                return delete_click
            
            delete_btn = ft.IconButton(
                icon=ft.Icons.DELETE,
                on_click=make_delete_func(card_id),
                icon_color="red"
            )
            
            page.add(
                ft.Container(
                    content=ft.Row([
                        ft.Column([
                            ft.Text(f"Title: {card['title']}", size=18, weight=ft.FontWeight.BOLD),
                            ft.Text(f"Description: {desc_text}"),
                            ft.Text(f"ID: {card_id}", size=10, color=ft.Colors.GREY)
                        ], expand=True),
                        delete_btn
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    padding=10,
                    border=ft.border.all(1, ft.Colors.GREY),
                    margin=5
                )
            )
        
        page.add(ft.ElevatedButton("Back", on_click=welcome_page))
    
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # СЛУЧАЙНОЕ ПОВТОРЕНИЕ 
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    
    def random_review(e):
        if not data:
            page.clean()
            page.add(
                ft.Column([
                    ft.Text("No cards to review"),
                    ft.ElevatedButton("Back", on_click=welcome_page)
                ])
            )
            return
        
        # ВЫБИРАЕМ СЛУЧАЙНУЮ КАРТОЧКУ
        card_list = []
        for key in data.keys():
            card_list.append(key)
        
        random_id = r.choice(card_list)
        current_card = data[random_id]
        
        # СОБИРАЕМ ВСЕ ПОЛЯ ДЛЯ ПРОВЕРКИ
        all_fields = [current_card.get('d', '')]
        if current_card.get('d2') and current_card['d2'] != "null":
            all_fields.append(current_card['d2'])
        if current_card.get('d3') and current_card['d3'] != "null":
            all_fields.append(current_card['d3'])
        
        page.clean()
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.MainAxisAlignment.CENTER
        
        question = ft.Text(current_card["title"], size=24)
        answer_field = ft.TextField(label="Your answer", hint_text="Type here...", width=400)
        result_text = ft.Text("")
        
        # ПОКАЗЫВАЕМ СКОЛЬКО ПОЛЕЙ НУЖНО ЗНАТЬ
        fields_count = len(all_fields)
        if fields_count > 1:
            hint_text = ft.Text(f"This card has {fields_count} fields to remember", size=12, color=ft.Colors.GREY)
        else:
            hint_text = ft.Text("")
        
        def check_answer(e):
            user_answer = answer_field.value.lower().strip()
            
            # ПРОВЕРЯЕМ СОВПАДАЕТ ЛИ С ЛЮБЫМ ИЗ ПОЛЕЙ
            is_correct = False
            correct_answer = ""
            for field in all_fields:
                if user_answer == field.lower():
                    is_correct = True
                    correct_answer = field
                    break
            
            if is_correct:
                result_text.value = "Correct!"
                result_text.color = "green"
            else:
                # ПОКАЗЫВАЕМ ВСЕ ПРАВИЛЬНЫЕ ОТВЕТЫ
                all_answers = " / ".join(all_fields)
                result_text.value = f"Wrong! Correct: {all_answers}"
                result_text.color = "red"
            
            answer_field.disabled = True
            check_btn.disabled = True
            next_btn.visible = True
            page.update()
        
        def next_card(e):
            random_review(e)
        
        check_btn = ft.ElevatedButton("Check", on_click=check_answer)
        next_btn = ft.ElevatedButton("Next card", on_click=next_card, visible=False)
        back_btn = ft.ElevatedButton("Back", on_click=welcome_page)
        
        page.add(
            ft.Column([
                ft.Text("Random Review"),
                ft.Divider(),
                question,
                hint_text,
                answer_field,
                ft.Row([check_btn, next_btn]),
                result_text,
                back_btn
            ])
        )
    
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # ДОБАВЛЕНИЕ КАРТОЧКИ 
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    def add_card_menu(e1):
        # ПЕРЕМЕННЫЕ
        title = ft.TextField(label="Card title", hint_text="Enter something", multiline=True, max_length=174)
        main_desc = ft.TextField(label="Main description", hint_text="Enter translation", multiline=True, max_length=319)
        desc2 = ft.TextField(label="Additional description", hint_text="Optional", multiline=True, max_length=319, visible=False)
        desc3 = ft.TextField(label="Another description", hint_text="Optional", multiline=True, max_length=319, visible=False)
        
        duplicate = False
        duplicate_text = ft.Text("DUPLICATE MODE ACTIVE", visible=False, color="orange")
        duplicate_error_text = ft.Text("", color="red")
        duplicate_button = ft.ElevatedButton(content="Add as duplicate", icon=ft.Icons.ADD, visible=False)
        add_card_btn = ft.ElevatedButton(content="Create card", icon=ft.Icons.CHECK, visible=False)
        
        # СЧЁТЧИК ДЛЯ ДОПОЛНИТЕЛЬНЫХ ПОЛЕЙ
        extra_fields_count = 0
        
        def add_extra_field(e):
            nonlocal extra_fields_count
            extra_fields_count += 1
            if extra_fields_count == 1:
                desc2.visible = True
            elif extra_fields_count == 2:
                desc3.visible = True
            page.update()
        
        def check_duplicate(e):
            nonlocal duplicate, duplicate_text, duplicate_button, duplicate_error_text
            current_text = title.value.capitalize()
            
            # ПРОВЕРЯЕМ ЕСТЬ ЛИ ТАКАЯ КАРТОЧКА
            card_exists = False
            for card_data in data.values():
                if card_data.get("title") == current_text:
                    card_exists = True
                    break
            
            if card_exists and duplicate == False:
                duplicate_error_text.value = "This card already exists! Click button to add duplicate"
                duplicate_button.visible = True
                duplicate_text.visible = False
            else:
                duplicate_error_text.value = ""
                if duplicate == True:
                    duplicate_button.visible = False
                    duplicate_text.visible = True
                else:
                    duplicate_button.visible = False
                    duplicate_text.visible = False
            
            # ПРОВЕРЯЕМ КНОПКУ СОЗДАНИЯ
            if title.value and len(title.value) > 1 and main_desc.value:
                add_card_btn.visible = True
            else:
                add_card_btn.visible = False
            
            page.update()
        
        def enable_duplicate(e):
            nonlocal duplicate, duplicate_text, duplicate_button, duplicate_error_text
            duplicate = True
            duplicate_text.visible = True
            duplicate_button.visible = False
            duplicate_error_text.value = ""
            
            if title.value and len(title.value) > 1 and main_desc.value:
                add_card_btn.visible = True
            
            page.update()
        
        def add_card(e):
            nonlocal duplicate
            
            card = Card()
            card.title = title.value
            card.d = main_desc.value
            card.d2 = desc2.value if desc2.value else "null"
            card.d3 = desc3.value if desc3.value else "null"
            card.dup = duplicate
            
            card_data = card.create_dict()
            
            # ПРОВЕРЯЕМ ЕСТЬ ЛИ ТАКАЯ КАРТОЧКА
            card_exists = False
            existing_key = None
            for key, card_data_in_data in data.items():
                if card_data_in_data.get("title") == card.title.capitalize():
                    card_exists = True
                    existing_key = key
                    break
            
            # ЕСЛИ ДУБЛИКАТ НЕ РАЗРЕШЕН И КАРТОЧКА ЕСТЬ - УДАЛЯЕМ СТАРУЮ
            if card_exists and duplicate == False:
                del data[existing_key]
            
            # СЧИТАЕМ ДУБЛИКАТЫ
            dup_id = None
            if duplicate == True:
                dup_count = 0
                for card_data_in_data in data.values():
                    if card_data_in_data.get("title") == card.title.capitalize():
                        dup_count += 1
                dup_id = dup_count + 1
            
            # НОВЫЙ ID
            new_id = len(data) + 1
            
            data[new_id] = {
                "title": (card_data["title"]).capitalize(),
                "d": card_data["description"],
                "d2": card_data["description2"],
                "d3": card_data["description3"],
                "dup": duplicate,
                "dup_id": dup_id
            }
            
            with open("data.json", "w", encoding="utf-8") as file:
                j.dump(data, file, ensure_ascii=False, indent=4)
            
            welcome_page()
        
        # НАСТРАИВАЕМ СОБЫТИЯ
        title.on_change = check_duplicate
        main_desc.on_change = check_duplicate
        duplicate_button.on_click = enable_duplicate
        add_card_btn.on_click = add_card
        
        # КНОПКИ
        add_field_btn = ft.IconButton(icon=ft.Icons.ADD, on_click=add_extra_field)
        back_btn = ft.ElevatedButton(icon=ft.Icons.ARROW_BACK, content="Return back", on_click=welcome_page)
        
        page.clean()
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.MainAxisAlignment.CENTER
        
        page.add(
            ft.Column([
                duplicate_text,
                ft.Row([back_btn, add_card_btn]),
                title,
                duplicate_error_text,
                duplicate_button,
                main_desc,
                ft.Row([add_field_btn, ft.Text("Add more descriptions")]),
                desc2,
                desc3
            ])
        )
    
    page.title = "Otriga App"
    welcome_page()

ft.app(main)
    
        