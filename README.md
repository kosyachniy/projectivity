# projectivity

## Описание
Сервер API и клиент-сайт, соединяющийся с сервисом по API

[Ссылка на клиент Java Android]()

<br><br>

## API
Адрес: [``` http://167.99.128.56/ ```](http://167.99.128.56/)

Код ответа для всех методов | Название
---|---
0 | Успешно
1 | Ошибка сервера
2 | Неправильный запрос
3 | Не все поля заполнены

<br>

### 1. Регистрация ``` reg ```
Атрибут | Название | Детали
---|---|---
Логин | ``` login ``` | От 3 до 20 символов включительно<br>Только латинские буквы и цифры<br>Использование букв обязательно<br>Регистр не учитывается
Пароль | ``` pass ``` | От 6 до 40 символов включительно<br>Латинские буквы, цифры и спецсимволы (``` !@#$%^&*()-_+=;:,./?\|`~[]{} ```)<br>Использование букв и цифр обязательно<br>Регистр учитывается
Почта | ``` mail ``` | Стандартная почта

Код ответа | Название
---|---
4 | Недопустимый логин
5 | Логин уже зарегистрирован
6 | Недопустимый пароль
7 | Неверно указана почта
8 | Почта уже зарегистрирована

<br>

### 2. Авторизация ``` auth ```
Атрибут | Название
---|---
Логин | ``` login ``` 
Пароль | ``` pass ```

Код ответа | Название
---|---
4 | Неправильный логин
5 | Неправильный пароль

<br>

### 3. Запрос публичного ключа ``` key ```
Ответ - ``` modulus,exponent ``` (RSA шифрование с открытым ключом)

<br>

### 4. Добавить соревнование ``` competions.add ```
Ответ - id соревнования

### 5. Список всех соревнований ``` competions.gets ```
Ответ - список объектов (JSON)

### 6. Получить информацию о соревновании ``` competions.get ```
Ответ - объект (JSON)
