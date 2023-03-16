from cgitb import text
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import TOKEN
import buttons

#######################################################################

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

#######################################################################

@dp.message_handler(commands = ['start'])
async def commands_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Здраствуйте, {0.first_name}\n'.format(message.from_user) + 'Выберите действие: ', reply_markup=buttons.mainMenu)
    except:
        await message.reply('Для общения с ботом - напишите ему:\nhttps://t.me/chechenRestaurant_bot')
        # await message.delete()

#######################################################################

# --- Menu ---
@dp.message_handler(text = 'Меню')
async def Menu_answer(message : types.Message):
    await message.answer('Выберите раздел: ', reply_markup=buttons.menu)
    # await message.delete()

#######################################################################

# --- backMarkup ---
@dp.callback_query_handler(text = 'AddToCart')
async def backMrkup_Menu(callback : types.CallbackQuery):
    await callback.message.answer('Выберите раздел: ', reply_markup=buttons.menu)

#######################################################################

# --- sushiMenu ---
@dp.callback_query_handler(text = 'sushi')
async def sushi_answer(callback: types.CallbackQuery):
    await callback.message.answer('Выберите из меню: ', reply_markup=buttons.sushiMenu)

# --- sushiMenuBack ---
@dp.callback_query_handler(text = 'sushiMenuBack')
async def sushiMenuBack_answer(callback: types.CallbackQuery):
    await callback.message.answer('Выберите из меню: ', reply_markup=buttons.sushiMenu)

# shik
@dp.callback_query_handler(text = 'shikMenu')
async def shikMenu_answer(callback : types.CallbackQuery):
    await callback.message.answer(text = 'Горячий шик\n➖➖➖➖➖➖➖\nРис, лосось, тобико, сыр сливочный, огурец, авокадо, фирменный соус, унаги\n➖➖➖➖➖➖➖\nЦена: 370₽', reply_markup=buttons.shikMenu)
@dp.callback_query_handler(text = 'shik')
async def shik_answer(callback : types.CallbackQuery):
    await types.ChatActions.upload_photo()
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('photo/shik.png'))
    await callback.message.answer_media_group(media=media)
    await callback.message.answer(text = 'Горячий шик\n➖➖➖➖➖➖➖\nРис, лосось, тобико, сыр сливочный, огурец, авокадо, фирменный соус, унаги\n➖➖➖➖➖➖➖\nЦена: 370₽', reply_markup=buttons.shikMenu)

# syke_tori
@dp.callback_query_handler(text = 'syke_toriMenu')
async def syke_toriMenu_answer(callback : types.CallbackQuery):
    await callback.message.answer(text = 'Сяке-тори\n➖➖➖➖➖➖➖\nРис, сыр сливочный, темпура, курица, фирменный соус и шапка, соус унаги\n➖➖➖➖➖➖➖\nЦена: 300₽', reply_markup=buttons.syke_toriMenu)
@dp.callback_query_handler(text = 'syke_tori')
async def syke_tori_answer(callback : types.CallbackQuery):
    await types.ChatActions.upload_photo()
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('photo/syke_tori.png'))
    await callback.message.answer_media_group(media=media)
    await callback.message.answer(text = 'Сяке-тори\n➖➖➖➖➖➖➖\nРис, сыр сливочный, темпура, курица, фирменный соус и шапка, соус унаги\n➖➖➖➖➖➖➖\nЦена: 300₽', reply_markup=buttons.syke_toriMenu)

# losos
@dp.callback_query_handler(text = 'lososMenu')
async def lososMenu_answer(callback : types.CallbackQuery):
    await callback.message.answer(text = 'Бешеный лосось\n➖➖➖➖➖➖➖\nРис, тобико, кунжут, сыр сливочный, лосось, фирменный соус, унаги\n➖➖➖➖➖➖➖\nЦена: 320₽', reply_markup=buttons.lososMenu)
@dp.callback_query_handler(text = 'losos')
async def losos_answer(callback : types.CallbackQuery):
    await types.ChatActions.upload_photo()
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('photo/losos.png'))
    await callback.message.answer_media_group(media=media)
    await callback.message.answer(text = 'Бешеный лосось\n➖➖➖➖➖➖➖\nРис, тобико, кунжут, сыр сливочный, лосось, фирменный соус, унаги\n➖➖➖➖➖➖➖\nЦена: 320₽', reply_markup=buttons.lososMenu)

#######################################################################

# --- fastfudMenu ---
@dp.callback_query_handler(text = 'fastfud')
async def fastfud_answer(callback : types.CallbackQuery):
    await callback.message.answer('Выберите из меню: ', reply_markup=buttons.fastfudMenu)

# --- fastfudMenuBack ---
@dp.callback_query_handler(text = 'fastfudMenuBack')
async def fastfudMenuBack_answer(callback: types.CallbackQuery):
    await callback.message.answer('Выберите из меню: ', reply_markup=buttons.fastfudMenu)

# dvoynoyChiz
@dp.callback_query_handler(text = 'dvoynoyChizMenu')
async def dvoynoyChizMenu_answer(callback : types.CallbackQuery):
    await callback.message.answer(text = 'Двойной Чизбургер\n➖➖➖➖➖➖➖\nДва рубленых бифштекса из натуральной говядины на карамелизованной булочке, с двумя ломтиками сыра «Чеддер», кетчупом, горчицей, луком и маринованными огурчиками\n➖➖➖➖➖➖➖\nЦена: 125₽', reply_markup=buttons.dvoynoyChizMenu)
@dp.callback_query_handler(text = 'dvoynoyChiz')
async def dvoynoyChiz_answer(callback : types.CallbackQuery):
    await types.ChatActions.upload_photo()
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('photo/dvoynoyChiz.png'))
    await callback.message.answer_media_group(media=media)
    await callback.message.answer(text = 'Двойной Чизбургер\n➖➖➖➖➖➖➖\nДва рубленых бифштекса из натуральной говядины на карамелизованной булочке, с двумя ломтиками сыра «Чеддер», кетчупом, горчицей, луком и маринованными огурчиками\n➖➖➖➖➖➖➖\nЦена: 125₽', reply_markup=buttons.dvoynoyChizMenu)

# bigTesti
@dp.callback_query_handler(text = 'bigTestiMenu')
async def bigTestiMenu_answer(callback : types.CallbackQuery):
    await callback.message.answer(text = 'Биг Тейсти Острый\n➖➖➖➖➖➖➖\nБиг тейсти острый с бифштексом из 100% рубленой говядины, сыром Эмменталь, пикантным соусом Чураско и знаменитым соусом с дымком\n➖➖➖➖➖➖➖\nЦена: 259₽', reply_markup=buttons.bigTestiMenu)
@dp.callback_query_handler(text = 'bigTesti')
async def bigTesti_answer(callback : types.CallbackQuery):
    await types.ChatActions.upload_photo()
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('photo/bigTesti.png'))
    await callback.message.answer_media_group(media=media)
    await callback.message.answer(text = 'Биг Тейсти Острый\n➖➖➖➖➖➖➖\nБиг тейсти острый с бифштексом из 100% рубленой говядины, сыром Эмменталь, пикантным соусом Чураско и знаменитым соусом с дымком\n➖➖➖➖➖➖➖\nЦена: 259₽', reply_markup=buttons.bigTestiMenu)

# chikenBurger
@dp.callback_query_handler(text = 'chikenBurgerMenu')
async def chikenBurgerMenu_answer(callback : types.CallbackQuery):
    await callback.message.answer(text = 'Чикен Бургер\n➖➖➖➖➖➖➖\nСочная куриная котлета в хрустящей панировке заправленная ароматным соусом с нотками чеснока, сыр "Чеддер", ломтик помидора, свежий салат, лук, маринованные огурчики и булочка с кунжутом\n➖➖➖➖➖➖➖\nЦена: 165₽', reply_markup=buttons.chikenBurgerMenu)
@dp.callback_query_handler(text = 'chikenBurger')
async def chikenBurger_answer(callback : types.CallbackQuery):
    await types.ChatActions.upload_photo()
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('photo/chikenBurger.png'))
    await callback.message.answer_media_group(media=media)
    await callback.message.answer(text = 'Чикен Бургер\n➖➖➖➖➖➖➖\nСочная куриная котлета в хрустящей панировке заправленная ароматным соусом с нотками чеснока, сыр "Чеддер", ломтик помидора, свежий салат, лук, маринованные огурчики и булочка с кунжутом\n➖➖➖➖➖➖➖\nЦена: 165₽', reply_markup=buttons.chikenBurgerMenu)


#######################################################################

# --- pizzaMenu ---
@dp.callback_query_handler(text = 'pizza')
async def pizza_answer(callback : types.CallbackQuery):
    await callback.message.answer('Выберите из меню: ', reply_markup=buttons.pizzaMenu)

# --- pizzaMenuBack ---
@dp.callback_query_handler(text = 'pizzaMenuBack')
async def pizzaMenuBack_answer(callback: types.CallbackQuery):
    await callback.message.answer('Выберите из меню: ', reply_markup=buttons.pizzaMenu)

# arriva
@dp.callback_query_handler(text = 'arrivaMenu')
async def arrivaMenu_answer(callback : types.CallbackQuery):
    await callback.message.answer(text = 'Аррива\n➖➖➖➖➖➖➖\nЦыпленок, острая чоризо, соус бургер, сладкий перец, красный лук, томаты, моцарелла, соус ранч, чеснок\n➖➖➖➖➖➖➖\nЦена: 345₽', reply_markup=buttons.arrivaMenu)
@dp.callback_query_handler(text = 'arriva')
async def arriva_answer(callback : types.CallbackQuery):
    await types.ChatActions.upload_photo()
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('photo/arriva.png'))
    await callback.message.answer_media_group(media=media)
    await callback.message.answer(text = 'Аррива\n➖➖➖➖➖➖➖\nЦыпленок, острая чоризо, соус бургер, сладкий перец, красный лук, томаты, моцарелла, соус ранч, чеснок\n➖➖➖➖➖➖➖\nЦена: 345₽', reply_markup=buttons.arrivaMenu)

# pepperoni
@dp.callback_query_handler(text = 'pepperoniMenu')
async def pepperoniMenu_answer(callback : types.CallbackQuery):
    await callback.message.answer(text = 'Пепперони\n➖➖➖➖➖➖➖\nПикантная пепперони, увеличенная порция моцареллы, томатный соус\n➖➖➖➖➖➖➖\nЦена: 315₽', reply_markup=buttons.pepperoniMenu)
@dp.callback_query_handler(text = 'pepperoni')
async def pepperoni_answer(callback : types.CallbackQuery):
    await types.ChatActions.upload_photo()
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('photo/pepperoni.png'))
    await callback.message.answer_media_group(media=media)
    await callback.message.answer(text = 'Пепперони\n➖➖➖➖➖➖➖\nПикантная пепперони, увеличенная порция моцареллы, томатный соус\n➖➖➖➖➖➖➖\nЦена: 315₽', reply_markup=buttons.pepperoniMenu)

# margarita
@dp.callback_query_handler(text = 'margaritaMenu')
async def margaritaMenu_answer(callback : types.CallbackQuery):
    await callback.message.answer(text = 'Маргарита\n➖➖➖➖➖➖➖\nУвеличенная порция моцареллы, томаты, итальянские травы, томатный соус\n➖➖➖➖➖➖➖\nЦена: 300₽', reply_markup=buttons.margaritaMenu)
@dp.callback_query_handler(text = 'margarita')
async def margarita_answer(callback : types.CallbackQuery):
    await types.ChatActions.upload_photo()
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('photo/margarita.png'))
    await callback.message.answer_media_group(media=media)
    await callback.message.answer(text = 'Маргарита\n➖➖➖➖➖➖➖\nУвеличенная порция моцареллы, томаты, итальянские травы, томатный соус\n➖➖➖➖➖➖➖\nЦена: 300₽', reply_markup=buttons.margaritaMenu)

#######################################################################

# --- napitkiMenu ---
@dp.callback_query_handler(text = 'napitki')
async def napitki_answer(callback: types.CallbackQuery):
    await callback.message.answer('Выберите из меню: ', reply_markup=buttons.napitkiMenu)

# --- napitkiMenuBack ---
@dp.callback_query_handler(text = 'napitkiMenuBack')
async def napitkiMenuBack_answer(callback: types.CallbackQuery):
    await callback.message.answer('Выберите из меню: ', reply_markup=buttons.napitkiMenu)

# sprite
@dp.callback_query_handler(text = 'spriteMenu')
async def spriteMenu_answer(callback : types.CallbackQuery):
    await callback.message.answer(text = 'Sprite\n➖➖➖➖➖➖➖\nSprite 0.5\n➖➖➖➖➖➖➖\nЦена: 85₽', reply_markup=buttons.spriteMenu)
@dp.callback_query_handler(text = 'sprite')
async def sprite_answer(callback : types.CallbackQuery):
    await types.ChatActions.upload_photo()
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('photo/sprite.png'))
    await callback.message.answer_media_group(media=media)
    await callback.message.answer(text = 'Sprite\n➖➖➖➖➖➖➖\nSprite 0.5\n➖➖➖➖➖➖➖\nЦена: 85₽', reply_markup=buttons.spriteMenu)

# fanta
@dp.callback_query_handler(text = 'fantaMenu')
async def fantaMenu_answer(callback : types.CallbackQuery):
    await callback.message.answer(text = 'Fanta\n➖➖➖➖➖➖➖\nFanta 0.5\n➖➖➖➖➖➖➖\nЦена: 70₽', reply_markup=buttons.fantaMenu)
@dp.callback_query_handler(text = 'fanta')
async def fanta_answer(callback : types.CallbackQuery):
    await types.ChatActions.upload_photo()
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('photo/fanta.png'))
    await callback.message.answer_media_group(media=media)
    await callback.message.answer(text = 'Fanta\n➖➖➖➖➖➖➖\nFanta 0.5\n➖➖➖➖➖➖➖\nЦена: 70₽', reply_markup=buttons.fantaMenu)

# cola
@dp.callback_query_handler(text = 'colaMenu')
async def colaMenu_answer(callback : types.CallbackQuery):
    await callback.message.answer(text = 'Coca-Cola\n➖➖➖➖➖➖➖\nCoca-Cola 0.5\n➖➖➖➖➖➖➖\nЦена: 90₽', reply_markup=buttons.colaMenu)
@dp.callback_query_handler(text = 'cola')
async def cola_answer(callback : types.CallbackQuery):
    await types.ChatActions.upload_photo()
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('photo/cola.png'))
    await callback.message.answer_media_group(media=media)
    await callback.message.answer(text = 'Coca-Cola\n➖➖➖➖➖➖➖\nCoca-Cola 0.5\n➖➖➖➖➖➖➖\nЦена: 90₽', reply_markup=buttons.colaMenu)

#######################################################################

executor.start_polling(dp, skip_updates=True)
