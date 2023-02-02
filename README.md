# Сайт для управления картами лояльности

Функционал приложения
* список карт с полями: серия, номер, дата выпуска, дата окончания активности, статус
* поиск по этим же полям
* просмотр профиля карты с историей покупок по ней
* активация/деактивация карты
* удаление карты

Реализован генератор карт, с указанием серии и количества генерируемых карт, а также "срок окончания активности" со значениями "1 год", "6 месяцев" "1 месяц". После истечения срока активности карты, у карты проставляется статус "просрочена".


## Запуск проекта
1) Клонировать репозиторий:

```
git clone https://github.com/Vendetta-source/card_manager.git
```

2) Создать виртуальное окружение:

```
python -m venv venv
```

3) Активировать окружение:

Windows: 
```
venv/scripts/activate
```

Linux: 
```
source\venv\bin\activate
```

4) Установить зависимости:

```
pip install -r requirements.txt
```

5) В файле settings.py заполнить необходимые данные.

6) Создать и применить миграции БД:

```
python manage.py makemigrations
python manage.py migrate
```

7) Запустить сервер:

```
python manage.py runserver
```
----
### Скриншоты
![image](https://user-images.githubusercontent.com/63292154/216410830-ed634d3b-c2e8-43a5-a1ca-8959214ce100.png)
![image](https://user-images.githubusercontent.com/63292154/216411199-786c2c9b-c3b7-4041-ac73-967aa222f171.png)
![image](https://user-images.githubusercontent.com/63292154/216411446-cf486b60-b85a-45a4-89cb-a2697c6342cf.png)
![image](https://user-images.githubusercontent.com/63292154/216411702-5887f188-3fe2-46d2-8d74-13aac48ff6a8.png)

