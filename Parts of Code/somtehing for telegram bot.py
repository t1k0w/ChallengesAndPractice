import time 
import logging
from aiogram import Bot, Dispatcher, executor, types
from Binance_Values import * 
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


TOKEN = '*********************'

bot = Bot(token= TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    item1 = types.KeyboardButton("Wallet")
    item2 = types.KeyboardButton("Main")
    item3 = types.KeyboardButton("Settings")
    item4 = types.KeyboardButton("GGG")

    button1 = InlineKeyboardButton(text="Check Button 1", callback_data="randomvalue_of10")
    keybord_inline = InlineKeyboardMarkup().add(button1)
    markup.add(item1, item2, item3, item4)
    
    await message.reply(f"Hey! {user_full_name} ", reply_markup= markup)

@dp.message_handler(content_types=['text'])
async def bot_message(message):
    if message.chat.type == "private":
        if message.text == "Wallet":
            await bot.send_message(message.chat.id, "heey", reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton()))

@dp.message_handler()
async def menu_work(message: types.Message):
    if message.text == 'BTC':
        async def btc_handler(message: types.Message):
            btc_value = Binance_BTC_USDT()
            last_btc_price = float(Binance_BTC_USDT.get_BTC_price(btc_value).replace("$", "").replace("," , ""))
            await message.reply(f'Actual BTC price: {last_btc_price} $')
    elif message.text == 'ETH':
        async def eth_handler(message: types.Message):
            eth_value = Binance_ETH_USDT()
            last_eth_price = float(Binance_ETH_USDT.get_ETH_price(eth_value).replace("$", "").replace("," , ""))
            await message.reply(f'Actual ETH price: {last_eth_price} $')
            
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates="True")
