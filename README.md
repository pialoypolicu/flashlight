# flashlight  

##### Описание.

Скрипт обеспечивает контроль работы фонаря.

Для соединения с сервером используются потоки streams async/await.
Что обеспечивает простоту написания и читаемость кода.

#### Стек/зависимости
```
Python3.11
AsyncIO
pytest
loguru
```

##### Запуск скрипта из командной строки
1. склонировать репозиторий выполнив ккоманду 

> `git clone https://github.com/pialoypolicu/flashlight.git`
2. установить вирт окружение 
> `python3 -m venv venv`
3. активируем виртуальное окружение
> `source venv/bin/activate` 
4. обновляем pip пакет
> `pip install --upgrade pip`
5. устанавливаем зависимости
> `pip install -r requirements.txt`
6. запустить скррипт возможно командой 
> `python main.py`

#### Альтернатиный вариант запуска скрипта docker image
для запуска при помощи технологии docker достаточно выполнить команду в терминаде
> `docker run backpydev/flashlight:0.0.1`

#### tests
Для запуска тестов выполните команду 
> `pytest -vv`