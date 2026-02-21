import json as j
import time as t





# def work():
#     try:
#         with open("data.json", "r+", encoding="utf-8") as file:
#             data = j.load(file) #вытаскивает данные из джейсона
#             card = Card()
#             card_data = card.sv()
#             data[card_data["main"]] = { 
#             "second" : card_data["second"],
#             "third" : card_data["third"],
#             "translation" : card_data["translation"],
#                                       }   
#             print(data)
#             file.seek(0)
#             j.dump(data, file, indent=4)
#             file.truncate()
#             # dict_data[card.main]=("main" : self.main, 
#             # "second" : self.f2,             #значения из ввода превращаются в словарь
#             # "third" : self.f3,
#             # "translation" : self.tr
                
                
                
#             # )
#     except:
#         data = {}
#         card = Card()
#         card_data = card.sv()
#         data[card_data["main"]] = { 
#             "second" : card_data["second"],
#             "third" : card_data["third"],
#             "translation" : card_data["translation"],
#                                   }     
#         with open("data.json", "w", encoding="utf-8" ) as file:
#             j.dump(data, file, indent=4)
#             print(data)
def work():
    try:
        with open("data.json", "r", encoding="utf-8") as file:
            data=j.load(file)
    except:
        data={}
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

        
      
#             card_data = card.sv()
#             data[card_data["main"]] = { 
#             "second" : card_data["second"],
#             "third" : card_data["third"],
#             "translation" : card_data["translation"],
#                                       }   
#             print(data)
#             file.seek(0)
#             j.dump(data, file, indent=4)
#             file.truncate()
#             # dict_data[card.main]=("main" : self.main, 
#             # "second" : self.f2,             #значения из ввода превращаются в словарь
#             # "third" : self.f3,
#             # "translation" : self.tr
    
        
        
        
        
        
        
        
        
        
        
        
            
        
    
 #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       
        
    
class Card(): #Свойства карточки



    def __init__(self, main="null", f2 = "null", f3 = "null", translation = "null"):
        self.main = main
        self.f2 = f2
        self.f3 = f3 
        self.tr = translation
 
 
    def sv(self, dict, check="null"):  #Функция установки значений для слов
        while True:
            #////////////////////////////////
            print("Первая форма: ") 
            inp = check_inp_for_words().capitalize()
            if inp == "Ошибка ввода!":                       #ПОЛУЧАЕМ ПЕРВУЮ ФОРМУ
                print(inp)
                continue
            if dict:
                if inp in dict.keys():
                    replace = False
                    while True:
                        print("Такая карточка уже есть")
                        print("1-Ввести заново, 2-заменить карточку")      #ПРОВЕРКА
                        user_input = check_inp_for_numbers()                                              
                        if user_input == "Можно вводить только цифры":
                            print(user_input)
                            continue
                        if len(user_input)>1:
                            print("ОШИБКА! Слишком большой ввод")
                        if len(user_input)<1:
                            print("ОШИБКА! Ожидается ввод")                   #В ПЛАНАХ добавить вторую карточку с таким названием 
                            continue
                        # good_chars= "12"
                        # for char in user_input:
                        #     if char not in good_chars:
                        #         print("ОШИБКА! Введите 1 или 2")
                        #         print("1-Ввести заново, 2-заменить карточку")
                        #         continue
                        if user_input == "1":
                            break
                        if user_input == "2":
                            replace = True
                            break
                    if replace == True:
                        self.main = inp
                        break
                    else:
                        continue
                            
                            
                        
                            
                                
                        
                    
                    
                        
                            
                    
                    
                
            self.main = inp
            break
            #////////////////////////////////
        while True:    
            #////////////////////////////////
            print("Вторая форма: ") 
            inp = check_inp_for_words()
            if inp == "Ошибка ввода!":
                print(inp)
                continue                                     #ПОЛУЧАЕМ ВТОРУЮ ФОРМУ
            self.f2 = inp
            print("Третья форма: ") 
            break
            #////////////////////////////////
        while True:
            #////////////////////////////////
            inp = check_inp_for_words()
            if inp == "Ошибка ввода!":
                print(inp)
                continue                                     #ПОЛУЧАЕМ ТРЕТЬЮ ФОРМУ
            self.f3 = inp
            print("Перевод глагола: ") 
            break
            #////////////////////////////////
        while True:
            inp = check_inp_for_words()
            if inp == "Ошибка ввода!":
                print(inp)                                   #ПОЛУЧАЕМ ПЕРЕВОД
                continue
            self.tr = inp
            return {
                
            "main" : self.main, 
            "second" : self.f2,             #значения из ввода превращаются в словарь
            "third" : self.f3,
            "translation" : self.tr
            
            } 
            
            
            
 #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
        













def check_inp_for_words():    # проверка ввода
    good_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    user_input = input().strip()
    for char in user_input:       
        if char not in good_chars:
            user_input = "Ошибка ввода!"
            break 
        if len(user_input) > 20:
            user_input = "Ошибка ввода!"
            break
        if len(user_input) < 2:
            user_input = "Ошибка ввода!"
            break
        else:
            continue
    return user_input    


# ПРОВЕРКА ВВОДА В МЕНЮ ВЫБОРА




def check_inp_for_numbers():
    good_chars = "0123456789"
    user_input = input().strip()
    for char in user_input:       
        if char not in good_chars:
            user_input = "ОШИБКА! Можно вводить только цифры"
            return user_input
        # if len(user_input) > 1:
        #     user_input = "Выбирать можно только одно"
        #     return False
        # if len(user_input) < 1:
        #     user_input = "Поле должно быть заполненно"
        #     return False
        else:
            continue
    return user_input 
        



# def card_add(): #Функция добавления карты
#     w = card()
#     w.sv() #Установка значения  
#     word={}
#     word[w.main] = (w.f2, w.f3, w.tr) 
#     # with open("data.json", "w", encoding="utf-8") as data:
#     #     j.load(data)
#     #     j.dump(card, data, ensure_ascii=False, indent=4)
#     print(f"{w.main} - {w.f2} - {w.f3} = {w.tr}")




        
    
# def addition():
#       dictionary = sv() # функция для установки значений карточке
#       return dictionary #словарь возращается дальше  
        
        
        
        
        
        
work()
              

        
# verbs = {}  
# word_add()
# print(verbs)



    
        