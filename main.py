import asyncio

from aiogram import Bot, Dispatcher
from config import BOT_TOKEN

from handlers.commands import router
from handlers.echo import router as echo_router


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(router)
    dp.include_router(echo_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())