from aiogram import Bot, Dispatcher, executor, types

TOKEN = "6060410692:AAHJ9Rp9nOjs5Sm3b0kFa4AsoGnZM6p7Chg"
CHANEL_ID = "-1001639588096"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

def give_product(pizza):
    fin_raw = ""
    for i in pizza:
        fin_raw = fin_raw + f"{i['title']}, {i['count']} шт\n"
    return fin_raw

def give_addres(addres, type):
    if type == 2:
        return "\nСпособ доставки: Самовывоз"
    fin_raw = "🏠 Адрес:\n"
    if addres['street'] != "":
        fin_raw = fin_raw + f"🏠 Улица: {addres['street']}\n"
    if addres['entrance'] != "":
        fin_raw = fin_raw + f"🏠 Подъезд: {addres['entrance']}\n"
    if addres['floor'] != "":
        fin_raw = fin_raw + f"🏠 Этаж: {addres['floor']}\n"
    if addres['apartment'] != "":
        fin_raw = fin_raw + f"🏠 Квартира: {addres['apartment']}\n"
    return fin_raw

def give_paytype(paytype):
    if paytype == "cash":
        return "💸 Оплата: наличными\n"
    elif paytype == "cart":
        return f"💳 Оплата: переводом на карту\n"

async def send_order_to_telegram(obj):
    await bot.send_message(chat_id=CHANEL_ID,
                           text=f"✅ ID заказа: {obj['id']}\n"
                                f"📱 Номер: {obj['number']}\n"
                                f"🙍‍ Имя: {(obj['name'])}\n"
                                f"🙍‍ Почта: {(obj['email'])}\n"
                                f"\n"
                                f"{give_product(obj['items'])}\n"
                                f"{give_addres(obj['addres'], obj['deliverType'])}\n\n"
                                f"{give_paytype(obj['paytype'])}\n"
                                f"Количество персон: {(obj['personCount'])}\n\n"
                                f"💰 Сумма: {obj['total_sum']}₽")