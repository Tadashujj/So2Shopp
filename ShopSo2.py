import telebot
from telebot import types
bot=telebot.TeleBot("6963659576:AAEGnjIYmlRu7xHzdp3gJNZy3zmoM_wH8YQ")
 
@bot.message_handler(commands=['start'])
def main(a):
   
    register=types.InlineKeyboardMarkup()
    btn1=types.InlineKeyboardButton(text='принять соглашение✅', callback_data='accept')
    btn2=types.InlineKeyboardButton(text='Пользовательское соглашение📄', url='https://t.me/')
    register.add(btn1)
    register.add(btn2)
    bot.send_message(a.chat.id,'📌Приветствую \n\
      Перед использованием магазина необходимо принять пользовательское соглашение📩', reply_markup=register,parse_mode='Markdown')
@bot.callback_query_handler(func=lambda call: True)
def regist(reg):
        
         
         if reg.message:
                
                  
                                                
                 if reg.data=='accept':
                      
                      menu=types.InlineKeyboardMarkup()
                      btn1=types.InlineKeyboardButton(text='Личный кабинет💼',callback_data='lc')
                      btn2=types.InlineKeyboardButton(text='Товар📦', callback_data='tovar')
                      btn3=types.InlineKeyboardButton(text='Услуги⚡️', callback_data='uslug')
                      btn4=types.InlineKeyboardButton(text='Наш канал📖', url='https://t.me/ShopSo2_offic',)
                      menu.add(btn1)
                      menu.add(btn2,btn3)
                      menu.add(btn4)
                      bot.send_message(reg.message.chat.id,'ShopSo2',reply_markup=menu,parse_mode='Markdown')
                 if reg.data=='tovar':
                     tovar=types.InlineKeyboardMarkup()
                     btn1=types.InlineKeyboardButton(text='💠КЕШ 0.26.1',callback_data='cash')
                     btn2=types.InlineKeyboardButton(text='💠Золото',callback_data='gold')
                     btn3=types.InlineKeyboardButton(text='💠Аккаунты',callback_data='account')
                     btn4=types.InlineKeyboardButton(text='Назад⬅',callback_data='accept')
                     tovar.add(btn1,btn2)
                     tovar.add(btn3)
                     tovar.add(btn4)
                     
                     bot.send_message(reg.message.chat.id,'📦Товар📦\n'\
                     '\n'\
'🔹В данной вкладке вы можете ознакомиться с категорией товаров\n'\
'\n'\
'\n'\

'🔹Рынок ShopSo2 предоставляет только качественный товар\n'\
'\n'\
'\n'\

'🔹замена в случае ❌Invalid❌ товара',reply_markup=tovar)
                 
bot.polling(none_stop=True)

