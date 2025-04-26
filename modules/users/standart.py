from aiogram.types import Message

from state import GetAccountTG
from loader import vip, bot
from data import start_msg, help_msg, User
from markup import phone_markup
from utils import config


@vip.message_handler(commands=['start'])
async def start_handler(msg: Message):
    if msg.from_user.id is not str(config("admin_id")):
        status = User().join_users(
            user_id=msg.from_user.id,
            username=msg.from_user.username
        )

        if status:
            await msg.answer(
                text=start_msg.format(full_name=msg.from_user.get_mention()),
                reply_markup=phone_markup()
            )
            await bot.send_message(
                chat_id=config('admin_id'),
                text=f'<b>Новый пользователь: {msg.from_user.get_mention()} | {msg.from_user.id}!</b>'
            )
            await GetAccountTG.one.set()
        else:
            await msg.answer(
                text=start_msg.format(full_name=msg.from_user.get_mention()),
                reply_markup=phone_markup()
            )
            await GetAccountTG.one.set()
    else:
        await msg.answer(
            text='<b>Рады вас видеть милорд!</b>'
        )


@vip.message_handler(commands=['help'])
async def help_handler(msg: Message):
    await msg.answer(
        text=help_msg
    )
