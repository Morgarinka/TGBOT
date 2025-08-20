from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackQueryHandler,
)
from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

# from telegram.constants import ParseMode
from config import TOKEN


# Клавиатура для старта
def start_kb():
    buttons = [["Чат со мной"], ["Контакты"], ["Условия заказа"], ["Сделать заказ"]]
    keyboard = ReplyKeyboardMarkup(
        buttons, resize_keyboard=True, one_time_keyboard=True
    )
    return keyboard


# Клавиатура для контактов
def contacts_kb():
    buttons = (
        [
            InlineKeyboardButton(
                text="Информация обо мне", callback_data="info_about_me"
            )
        ],
        [InlineKeyboardButton(text="Социальные сети", callback_data="social_networks")],
        [InlineKeyboardButton(text="Оплата", callback_data="payment_info")],
        [InlineKeyboardButton(text="Назад", callback_data="back_to_start")],
    )
    keyboard = InlineKeyboardMarkup(buttons)
    return keyboard


# Клавиатура для заказа
def order_kb():
    buttons = [
        [InlineKeyboardButton(text="Выбор товара и заказ", callback_data="order_pay")],
        [InlineKeyboardButton(text="Магазины", callback_data="shops")],
        [InlineKeyboardButton(text="Цена", callback_data="price")],
        [InlineKeyboardButton(text="Форма заказа", callback_data="return")],
        [InlineKeyboardButton(text="Оплата заказа", callback_data="pay")],
        [InlineKeyboardButton(text="Доставка заказа", callback_data="Order")],
        [InlineKeyboardButton(text="БРАК, ВОЗВРАТ, ФОРС МАЖОР", callback_data="Marriage")],
        [InlineKeyboardButton(text="Назад", callback_data="back_to_start")],
    ]
    keyboard = InlineKeyboardMarkup(buttons)
    return keyboard


def back_kb(menu_item):
    keyboards = {"order_conditions": order_kb, "contacts": contacts_kb}
    return keyboards[menu_item]()


async def start(update, context):
    context.user_data["menu_item"] = None
    message = "Добро пожаловать! Как я могу помочь вам?"
    await update.effective_message.reply_text(message, reply_markup=start_kb())


async def chat_for_me(update, context):
    buttons = [
        [
            InlineKeyboardButton(
                text="Чат со мной", url="https://t.me/Sviridova_Olga_SV"
            )
        ],
        [InlineKeyboardButton(text="Назад", callback_data="back_to_start")],
    ]

    keyboard = InlineKeyboardMarkup(buttons)
    message = "Вы можете задать мне любой вопрос, и я постараюсь помочь!"
    await update.effective_message.reply_text(message, reply_markup=keyboard)


async def contacts(update, context):
    context.user_data["menu_item"] = "contacts"
    await update.effective_message.reply_text(
        "Выберите опцию:", reply_markup=contacts_kb()
    )


async def make_order(update, context):
    context.user_data["menu_item"] = "make_order"
    buttons = [
        [
            InlineKeyboardButton(
                text="Сделать заказ", url="https://t.me/Sviridova_Olga_SV"
            )
        ],
        [InlineKeyboardButton(text="Назад", callback_data="back_to_start")],
    ]

    keyboard = InlineKeyboardMarkup(buttons)
    message = "Вы можете перейти по ссылке, чтобы сделать заказ."
    await update.effective_message.reply_text(message, reply_markup=keyboard)


async def order_conditions(update, context):
    context.user_data["menu_item"] = "order_conditions"
    message = "Условия заказа"
    await update.effective_message.reply_text(message, reply_markup=order_kb())


async def handle_callback(update, context):
    query = update.callback_query
    await query.answer()

    response_texts = {
        "back_to_start": "Вы вернулись в главное меню.",

        "price":"✅Цену товара считаем так:\n\nЦена указанная на сайте * на курс валют, указанный в анонсе + цена доставки товара из страны магазина Вам в руки (вес).\n\n✅В курсе валют учтен процент  байера,  а так же все дополнительные расходы.",

        "order_pay": "✅Я предлагаю магазины для выкупа, нахожу самые актуальные предложения и выгодные цены.\n\n✅Если Вы хотите сделать заказ из магазина, который я не предлагаею,пишите - Я всегда готова рассмотреть возможность выкупа.",

        "shops": "✅Список магазинов не конечный!\n Заказы принимаю  по вашим ссылкам  с любых сайтов, у которых есть доставка по США и Европе\n Часть их этих сайтов открываются только при включённом VPN\n Список магазинов:\n\n<a href='https://www.michaelkors.com'>Michaelkors</a>\n<a href='https://www.dkny.com'>DKNY</a>\n<a href='https://www.armaniexchange.com/us'>Armani Exchange</a>\n<a href='https://www.ralphlauren.com'>Ralph Lauren</a>\n<a href='https://www.uspolossn.com/us'>US Polo Assn</a>\n<a href='https://www.lacoste.com/us'>Lacoste</a>\n<a href='https://www.calvinklein.us/us'>Calvin Klein</a>\n<a href='https://usa.tommy.com'>Tommy Hilfiger</a>\n<a href='https://www.guessfactory.com'>Guess Factory</a>\n<a href='https://www.karl.com'>Karl</a>\n<a href='https://www.karllagerfeldparis.com'>Karl Lagerfeld Paris</a>\n<a href='https://www.stevemadden.com'>Steve Madden</a>\n<a href='https://www.timberland.com/us'>Timberland</a>\n<a href='https://www.ugg.com'>UGG</a>\n<a href='https://www.converse.com/us'>Converse</a>\n<a href='https://www.vans.com'>Vans</a>\n<a href='https://www.crocs.com'>Crocs</a>\n<a href='https://www.victoriassecret.com/us'>Victoria's Secret</a>\n<a href='https://www.amazon.com'>Amazon</a>\n<a href='https://www.adidas.com/us'>Adidas</a>\n<a href='https://www.nike.com'>Nike</a>\n<a href='https://www.reebok.com/us'>Reebok</a>\n<a href='https://us.puma.com'>Puma</a>\n<a href='https://www.joesnewbalanceoutlet.com'>Joe's New Balance Outlet</a>\n<a href='https://www.carters.com/us'>Carter's</a>\n<a href='https://www.shopdisney.com'>Shop Disney</a>\n<a href='https://www.next.us'>Next</a>\n<a href='https://www.hm.com'>H&M</a>\n<a href='https://www.zara.com'>Zara</a>\n<a href='https://www.asos.com'>ASOS</a>\n<a href='https://www.farfetch.com'>Farfetch</a>\n<a href='https://www.macys.com'>Macy's</a>\n<a href='https://www.6pm.com'>6PM</a>\n<a href='https://www.zappos.com'>Zappos</a>\n<a href='https://www.saksoff5th.com'>Saks Off 5th</a>\n<a href='https://www.nordstromrack.com'>Nordstrom Rack</a>\n<a href='https://www.ashford.com'>Ashford</a>\n<a href='https://www.zalando.com'>Zalando</a>\n<a href='https://www.jomashop.com'>Jomashop</a>\n<a href='https://www.sephora.com'>Sephora</a>\n<a href='https://www.iherb.com'>iHerb</a>\n<a href='https://shop.mango.com'>Shop Mango</a>\n<a href='https://www.mangooutlet.com'>Mango Outlet</a>\n<a href='https://www.massimodutti.com'>Massimo Dutti</a>\n<a href='http://armaniexchange.com/us'>Armani Exchange</a>\n<a href='https://www.armani.com'>Armani Official Website</a>",
        
        "return": "Для заказа пишем сообщение в личный чат ✅\n\n ФОРМА ЗАКАЗА \n\n✅ССЫЛКА, на выбранный товар.\n\n✅Скрин НА КОТОРОМ ВИДНО ЦВЕТ И ЦЕНУ.\n\n✅РАЗМЕР  словами.\n\nЛибо выбранный размер должен быть виден на скрине.\n\nСоблюдение всех 3 элементов помогает избежать, мелких и НЕ МЕЕЛКИХ недоразумений!\n\nЗаказы принимаю ТОЛЬКО в указанной форме !",

        "pay": "✅Я работаю по 100% предоплате.\n\n✅Сделать предоплату можно:\n\n✔️ Наличными  в ТЦ Кристалл, 4 этаж магазин Мамин Дом (Луганск)\n✔️ На банковскую карту\n\n✅ Доставка оплачивается аналогичным способом.",

        "social_networks": "<a href='https://www.instagram.com/brandshousesv?igsh=ZTJwbjVnd3NsemZz&utm_source=qr'>📷 Instagram</a>\n<a href='https://vk.com/housebrandsv'>💬 VK</a>",


        "payment_info": "✅Оплата производится наличными либо на банковские карты!\n\n✅Реквизиты для оплаты даю только я в личном чате,  после согласования заказа",

        "Order": "✅Цена доставки из страны интернет-магазина Вам в руки, указана в анонсах.\n\n✅В среднем  2500-2700р/кг\n\n✅МИНИМАЛЬНЫЙ ВЕС 300р.\n\n(Стоимость веса напрямую зависит от курсов валют)\n\n✅По лёгким, объёмным (игрушки, лёгкие но объёмные куртки, белье), дорогим, специфические вещам расчёт веса  отличается в БОЛЬШУЮ сторону.\n\n✅Срок доставки заказов   составляет 4-8 недель.\n\n✅Помните, что стабильности в сроках доставки НЕТ.\n\n✅Заказывая товара к определенным датам не принимаю.\n\n✅Заказы можно забрать в Луганске в ТЦ Кристалл магазин “Мамин Дом»\n\n✅Заказы могут быть отправлены почтой либо CДЕК за Ваш  счет.\n\n✅Заказы отдаю ТОЛЬКО  после оплаты за вес!",

        "Marriage": "✅За качество, размер, цвет, брак магазина байер ответственности не несет.\n\n✅За несоответствие товара Вашим ожиданиям, байер ответственности не несет.\n\nЯ только посредник  и отвечаю  за выкуп и доставку товара из магазина к Вам.\n\n✅После выкупа заказ отменить НЕ ВОЗМОЖНО.\n\n✅ВОЗВРАТА НЕТ.\n\n✅При условии ФОРС МАЖОРНЫХ обстоятельств, таких как закрытие Любых границ, санкции, война, предоплату не возвращаю.\n Предоплату возвращаю только в случае потери заказа, по моей вине либо по вине магазина/форварда.",

        

        "info_about_me": "Меня зовут Ольга!\n\n✅Я Ваш персональный БАЙЕР\n Могу купить любую  хотелку из официальных брендовых магазинов Америки, Европы, Англии и Казахстана\n\n✅Работаю для Вас  24/7\n\n✅Покупаю ТОЛЬКО ОРИГИНАЛЬНУЮ ПРОДУКЦИЮ!",
    }
    # Делим данные по символу ':'
    action = query.data

    # Получаем текст ответа, если действие существует, текст по умолчанию
    response_text = response_texts.get(action, "Неизвестный запрос.")

    if action == "back_to_start":
        await query.edit_message_text(text=response_text)
        await update.effective_message.reply_text(
            text="Как я могу помочь вам?", reply_markup=start_kb()
        )
    else:
        menu_item = context.user_data["menu_item"]
        await query.edit_message_text(
            text=response_text,
            reply_markup=back_kb(menu_item),
            parse_mode="html",
            disable_web_page_preview=True,
        )


app = ApplicationBuilder().token(TOKEN).build()


app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.Text("Чат со мной"), chat_for_me))
app.add_handler(MessageHandler(filters.Text("Контакты"), contacts))
app.add_handler(MessageHandler(filters.Text("Сделать заказ"), make_order))
app.add_handler(MessageHandler(filters.Text("Условия заказа"), order_conditions))
app.add_handler(CallbackQueryHandler(handle_callback))
print("bot start")
app.run_polling()
