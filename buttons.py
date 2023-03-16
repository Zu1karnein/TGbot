from os import close
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, callback_query

#######################################################################

# --- Main Menu ---
btnMenu = KeyboardButton('Меню', callback_data = 'btnMenu')
btnKorzina = KeyboardButton('Корзина', callback_data = 'btnKorzina')
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnMenu, btnKorzina)

#######################################################################

# --- Menu ---
sushi = InlineKeyboardButton(text = '🍣 Суши', callback_data='sushi')
fasfud = InlineKeyboardButton(text = '🍔 Фастфуд', callback_data='fastfud')
pizza = InlineKeyboardButton(text = '🍕 Пицца', callback_data='pizza')
napitki = InlineKeyboardButton(text = '🍹 Напитки', callback_data='napitki')
menu = InlineKeyboardMarkup(callback_data = 'menu')
menu.add(sushi).add(fasfud).add(pizza).add(napitki)

#######################################################################

# --- AddToCart ---
AddToCart =  InlineKeyboardMarkup(text = '➕ Добавить в корзину', callback_data = 'AddToCart')

#######################################################################

# --- backMarkup ---
backMarkup = InlineKeyboardMarkup(text = '🔙Назад', callback_data = 'backMrkup')

#######################################################################

# --- sushiMenu ---
shik = InlineKeyboardButton(text = 'Горячий шик', callback_data='shik')
shikMenu = InlineKeyboardMarkup(callback_data = 'shikMenu')

syke_tori = InlineKeyboardButton(text = 'Сяке-тори', callback_data='syke_tori')
syke_toriMenu = InlineKeyboardMarkup(callback_data = 'syke_toriMenu')

losos = InlineKeyboardButton(text = 'Бешенный лосось', callback_data='losos')
lososMenu = InlineKeyboardMarkup(callback_data = 'lososMenu')

sushiMenu = InlineKeyboardMarkup(callback_data = 'sushiMenu')
sushiMenu.add(shik).add(syke_tori).add(losos).add(backMarkup)

# sushiMenuBack
sushiMenuBack = InlineKeyboardMarkup(text = 'Назад', callback_data = 'sushiMenuBack')
lososMenu.add(AddToCart).add(sushiMenuBack)
syke_toriMenu.add(AddToCart).add(sushiMenuBack)
shikMenu.add(AddToCart).add(sushiMenuBack)

#######################################################################

# --- fastfudMenu ---
dvoynoyChiz = InlineKeyboardMarkup(text = 'Двойной Чизбургер', callback_data = 'dvoynoyChiz')
dvoynoyChizMenu = InlineKeyboardMarkup(callback_data = 'dvoynoyChizMenu')

bigTesti = InlineKeyboardMarkup(text = 'Биг Тейсти Острый', callback_data = 'bigTesti')
bigTestiMenu = InlineKeyboardMarkup(callback_data = 'bigTestiMenu')

chikenBurger = InlineKeyboardMarkup(text = 'Чикен Бургер', callback_data = 'chikenBurger')
chikenBurgerMenu = InlineKeyboardMarkup(callback_data = 'chikenBurgerMenu')

fastfudMenu = InlineKeyboardMarkup(callback_data = 'fastfudMenu')
fastfudMenu.add(dvoynoyChiz).add(bigTesti).add(chikenBurger).add(backMarkup)

# fastfudMenuBack
fastfudMenuBack = InlineKeyboardMarkup(text = 'Назад', callback_data = 'fastfudMenuBack')
dvoynoyChizMenu.add(AddToCart).add(fastfudMenuBack)
bigTestiMenu.add(AddToCart).add(fastfudMenuBack)
chikenBurgerMenu.add(AddToCart).add(fastfudMenuBack)

#######################################################################

# --- pizzaMenu ---
arriva = InlineKeyboardMarkup(text = 'Аррива', callback_data = 'arriva')
arrivaMenu = InlineKeyboardMarkup(callback_data = 'arrivaMenu')

pepperoni = InlineKeyboardMarkup(text = 'Пепперони', callback_data = 'pepperoni')
pepperoniMenu = InlineKeyboardMarkup(callback_data = 'pepperoniMenu')

margarita = InlineKeyboardMarkup(text = 'Маргарита', callback_data = 'margarita')
margaritaMenu = InlineKeyboardMarkup(callback_data = 'margaritaMenu')

pizzaMenu = InlineKeyboardMarkup(callback_data = 'pizzaMenu')
pizzaMenu.add(arriva).add(pepperoni).add(margarita).add(backMarkup)

# pizzaMenuBack
pizzaMenuBack = InlineKeyboardMarkup(text = 'Назад', callback_data = 'pizzaMenuBack')
arrivaMenu.add(AddToCart).add(pizzaMenuBack)
pepperoniMenu.add(AddToCart).add(pizzaMenuBack)
margaritaMenu.add(AddToCart).add(pizzaMenuBack)

#######################################################################

# --- napitkiMenu ---
sprite = InlineKeyboardMarkup(text = 'Sprite', callback_data = 'sprite')
spriteMenu = InlineKeyboardMarkup(callback_data = 'spriteMenu')

fanta = InlineKeyboardMarkup(text = 'Fanta', callback_data = 'fanta')
fantaMenu = InlineKeyboardMarkup(callback_data = 'fantaMenu')

cola = InlineKeyboardMarkup(text = 'Coca-Cola', callback_data = 'cola')
colaMenu = InlineKeyboardMarkup(callback_data = 'colaMenu')

napitkiMenu = InlineKeyboardMarkup(callback_data = 'napitkiMenu')
napitkiMenu.add(sprite).add(fanta).add(cola).add(backMarkup)

# napitkiMenuBack
napitkiMenuBack = InlineKeyboardMarkup(text = 'Назад', callback_data = 'napitkiMenuBack')
spriteMenu.add(AddToCart).add(napitkiMenuBack)
fantaMenu.add(AddToCart).add(napitkiMenuBack)
colaMenu.add(AddToCart).add(napitkiMenuBack)

#######################################################################
