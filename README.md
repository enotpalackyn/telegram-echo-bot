# Telegram Echo Bot

Простой Telegram-бот на Python и aiogram, который отвечает на команду `/start` и повторяет отправленные ему текстовые сообщения.

## Возможности

- `/start` - приветствие пользователя;
- повторение текстовых сообщений;

## Технологии

- Python 3.13
- aiogram 3.31
- python-dotenv

## Установка

Клонируйте репозиторий:

```
git clone https://github.com/enotpalackyn/telegram-echo-bot.git
cd telegram-echo-bot
```

Создайте виртуальное окружение:

```
python -m venv .venv
```

Активируйте его в Windows:

```
.venv\Scripts\Activate.ps1
```

Установите зависимости:

```
pip install -r requirements.txt
```

## Настройка

Создайте файл `.env` в корне проекта, и пропишите в нем:

```
BOT_TOKEN=your_bot_token
```

Токен можно получить через **BotFather** в Telegram.

## Запуск

Запустите бота командой:

```
python main.py
```

После запуска отправьте боту `/start` или любое текстовое сообщение.