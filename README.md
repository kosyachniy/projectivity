# projectivity

## Описание
Сервер API и клиент-сайт, соединяющийся с сервисом по API

[Ссылка на клиент Java Android](https://github.com/TyurinI/Projectivity)

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

### 1. Регистрация ``` profile.reg ```
Атрибут | Название | Детали
---|---|---
Логин | ``` login ``` | От 3 до 20 символов включительно<br>Только латинские буквы и цифры<br>Использование букв обязательно<br>Регистр не учитывается
Пароль | ``` pass ``` | От 6 до 40 символов включительно<br>Латинские буквы, цифры и спецсимволы (``` !@#$%^&*()-_+=;:,./?\|`~[]{} ```)<br>Использование букв и цифр обязательно<br>Регистр учитывается
Почта | ``` mail ``` | Стандартная почта
Имя | ``` name ``` | Только буквы<br>Регистр не важен<br>Необязательный параметр
Фамилия | ``` surname ``` | Только буквы<br>Регистр не важен<br>Необязательный параметр

Ответ:
Атрибут | Название
---|---
ID пользователя | ``` id ```
Токен для временной сессии | ``` token ```

Код ответа | Название
---|---
4 | Недопустимый логин
5 | Логин уже зарегистрирован
6 | Недопустимый пароль
7 | Неверно указана почта
8 | Почта уже зарегистрирована
9 | Неправильное имя
10 | Неправильная фамилия

<br>

### 2. Авторизация ``` profile.auth ```
Атрибут | Название
---|---
Логин | ``` login ``` 
Пароль | ``` pass ```

Ответ:
Атрибут | Название
---|---
ID пользователя | ``` id ```
Токен для временной сессии | ``` token ```

Код ответа | Название
---|---
4 | Неправильный логин
5 | Неправильный пароль

<br>

### 3. Личные настройки ``` profile.settings ```
Атрибут | Название | Детали
---|---|---
Токен | ``` token ``` | Полученный при авторизации / регистрации токен
Имя | ``` name ``` | Только буквы<br>Регистр не важен<br>Необязательный параметр
Фамилия | ``` surname ``` | Только буквы<br>Регистр не важен<br>Необязательный параметр
Описание | ``` description ``` | Необязательный параметр
Фото | ``` photo ``` | Base64<br>Необязательный параметр

Ответ: 0

Код ответа | Название
---|---
4 | Несуществующий токен
5 | Неправильное имя
6 | Неправильная фамилия
7 | Ошибка загрузки изображения

<br>

### 4. Закрытие сессии ``` profile.exit ```
Ответ: 0

Код ответа | Название
---|---
4 | Несуществующий токен (? нужно ли)

### 4. Добавить соревнование ``` competions.add ```
Атрибут | Название | Детали
---|---|---
Токен | ``` token ``` | Необязателдьный параметр<br>Полученный при авторизации / регистрации токен
Название | ``` name ``` | 
Краткое описание | ``` description ``` | 
Полное описание | ``` cont ``` | 
Время начала | ``` time ``` | 
Длительность | ``` durability ``` | 
Организатор | ``` author ``` | 
Человек в команде | ``` quantity ``` | 
Тип | ``` type ``` | 
Вознаграждение | ``` prize ``` | 
Ссылка | ``` url ``` | 
Место проведения | ``` geo ``` | 
Этап | ``` stage ``` | 
Изображения | ``` images ``` | JSON список INT id всех используемых изображений / если новое - строка Base64 (будет загружена и заменена id)
Владельцы соревнования | ``` owners ``` | На данный момент не поддерживается

Ответ: id соревнования

Код ответа | Название
---|---
4 | Ошибка загрузки изображения

<br>

### 5. Изменить соревнование ``` competions.edit ```
Атрибуты - как в предыдущем и дополнительные:

Атрибут | Название | Детали
---|---|---
Номер соревнования | ``` id ``` | id конкурса
Отображать в списке | ``` show ``` | Есть доступ у модераторов от 2го уровня

Ответ: '0'

Код ответа | Название
---|---
4 | Неправильный токен
5 | Неправильный id конкурса
6 | Нет прав на редактирование соревнования
7 | Ошибка загрузки изображения
8 | Нет права для отображения соревнования в списке

<br>

### 5. Список всех соревнований ``` competions.gets ```
Ответ: список объектов (JSON)

<br>

### 6. Получить информацию о соревновании ``` competions.get ```
Ответ: объект (JSON)

<br>

### 7. Список всех пользователей ``` participants.gets ```
Ответ: список объектов (JSON)

<br>

### 8. Инфо о пользователе ``` participants.get ```
Ответ: объект (JSON)

<br>

### 9. Список новостей ``` news.gets ```
Ответ: список объектов (JSON)

<br>

### 10. Новость ``` news.get ```
Ответ: объект (JSON)

<br>

### 11. Поиск ``` search ```
Ответ: JSON
``` {'competions': список, 'users': список, 'news': список}

<br>
