from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Привет, Я Echo Bot 🤖")


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "Доступные команды: \n\n/start - запустить бота \n/help - показать справку\n/about - информация о боте"
    )


@router.message(Command("about"))
async def cmd_about(message: Message):
    await message.answer(
        "Telegram Echo Bot\n\n"
        "Учебный проект на Python и Aiogram 3.\n"
        "Бот умеет отвечать на команды и повторять текстовые сообщения."
    )
