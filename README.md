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

## Код
Создайте python-файл и скачайте библиотеку <b>discord.py</b>
```bash
pip install discord.py
```
