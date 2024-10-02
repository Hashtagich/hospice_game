# Игра в рамках Хакатона «IT-Песочница» для ЧУЗ «Елизаветинский детский хоспис».

![not images!!!](foto_for_readme/logo.jpg)

<details>
<summary>

## Описание проекта

</summary>

### Требования

***Текст***

</details>

<details>
<summary>

### Целевая аудитория

</summary>

___


*Текс.*


</details>

___
<details>
<summary>

## Команда «Spark of Hope - Искра надежды»

</summary>

| №  | ФИО                  | Должность                              | Никнейм в телеграмме  | Ссылка на проекты                   |
|----|----------------------|----------------------------------------|-----------------------|-------------------------------------|
| 1  | Михаил Кирсанов      | Тимлид                                 | @MichaelKirss         | https://github.com/MichaelKirss     |
| 2  | Мария Дранникова     | UX / UI дизайнер                       | @tonivvi              |                                     |
| 3  | Кирилл Руденко       | UX / UI дизайнер                       | @kiryarud88           |                                     |
| 4  | Мочалова Анастасия   | UX / UI дизайнер                       | @nas_mochalova        |                                     |
| 5  | Татьяна Колегаева    | UX / UI дизайнер                       | @Pozazik              |                                     |
| 6  | Дягилева Анастасия   | UX / UI дизайнер, Графический дизайнер | @AnastasiyaDyagileva  |                                     |
| 7  | Александра Кузнецова | Графический дизайнер                   | @whitegrom            |                                     |
| 8  | Анастасия Куликова   | Графический дизайнер                   | @minaychenkoa         |                                     |
| 9  | Анна Ворошилова      | Графический дизайнер                   | @Annett0552           |                                     |
| 10 | Пилипон Юлия         | Графический дизайнер                   | @ZulusY               |                                     |
| 11 | Ветошкина Светлана   | Графический дизайнер                   | @vetoshkina_s         |                                     |
| 12 | Наталия Кустова      | Графический дизайнер                   | @Talimor              |                                     |
| 13 | Алина Мишнина        | Motion design                          | @mishmalina           |                                     |
| 14 | Михайлина Кира       | Интернет-маркетолог                    | @G_Mih                |                                     |
| 15 | Елена Пчельникова    | Продакт менеджер                       | @Elena_Pchelnikova    |                                     |
| 16 | Кудрякова Виктория   | Режиссер видеомонтажа                  | @vikiklos12           |                                     |
| 17 | Надежда Пачина       | Data Scince                            | @NadezdaPachina       | https://github.com/NadezdaNN        |
| 18 | Абрашов Андрей       | Data Scince                            | @Axewyl               |                                     |
| 19 | Коковин Георгий      | Data Scientist/Analyst                 | @jirimorionow973      |                                     |
| 20 | Альберт Петцольд     | Аналитик данных                        | @palbert1984          |                                     |
| 21 | Марина Лунева        | Аналитик данных                        | @MarinaVLuneva        |                                     |
| 22 | Роман Поспелов       | Пентестер                              | @Riman93              |                                     |
| 23 | Журавлёва Елена      | Ручное тестирование                    | @EKB_Elena_Zhuravleva |                                     |
| 24 | Светлана Федотова    | Ручное тестирование                    | @ImGoldilocks         |                                     |
| 25 | Антон Зайцев         | Backend разработчик (Python)           | @BlackMarvel          | https://github.com/Hashtagich       |
| 26 | Нияз Минникаев       | Backend разработчик (Python)           | @Akviro               | https://github.com/Akvir1stone      |
| 27 | Калинкин Константин  | Backend разработчик (Python)           | @Lord_tech0110        | https://github.com/Konstantin-sama  |
| 28 | Тимур Абдулин        | Backend разработчик (GO)               | @Timurka_223          | https://github.com/Timur965         |
| 29 | Руслан Гадельшин     | Android-разработчик                    | @roxoluz              | https://github.com/GRuslan53        |
| 30 | Вадим Рогов          | Java-разработчик                       | @Diego0686            | https://github.com/VadimRogov       |
| 31 | Иван Корольков       | Frontend разработчик                   | @biorival             | https://github.com/bioRival         |
| 32 | Андрей Батан         | Frontend разработчик                   | @Andrei_Batan         | https://github.com/BatanAndrei      |
| 33 | Мейрамбек Мухтаров   |                                        | @                     |                                     |
| 34 | Юлия Соколова        |                                        | @                     |                                     |
| 36 | Болдырев Дмитрий     |                                        | @                     |                                     |
| 36 | Плаксий Вероника     |                                        | @                     |                                     |
| 37 | Яна Алексеева        |                                        | @                     |                                     |
| 38 | Алексей Григоренко   |                                        | @                     |                                     |

</details>

___
<details>
<summary>

## Реализация проекта

</summary>

Текст

</details>

___

## Запуск проекта
___

<details>

<summary>

### Первый способ, через Docker compose
</summary>

### 1. Клонирование репозиторий
```bash
git clone https://github.com/Hashtagich/hospice_game.git
```

### 2. Установка переменных окружения
***В корен проекта заполняем файл template.db.env и переименовываем его в db.env или просто создаём файл db.env и заполняем его***
```bash
POSTGRES_DB=Например, db
POSTGRES_USER=Например, db
POSTGRES_PASSWORD=Например, db
```

***В папке backend заполняем файл template.env и переименовываем его в .env или просто создаём файл .env и заполняем его***
 ```bash
 SECRET_KEY='Ваш секретный ключ проекта'
 DEBUG=Булевое значение True или False
 ALLOWED_HOSTS='Разрешенные хосты'
 LANGUAGE_CODE='Язык, например, ru'
 TIME_ZONE='Временная зона, например, UTC'

 DB_NAME='Имя Базы данных (БД), например, db'
 DB_LOGIN='Логин БД, например, db'
 DB_PASS='Пароль БД, например, db'
 DB_HOST='Хост БД, например, db'
 DB_PORT='Порт БД, например, 5432'
 
 EMAIL_BACKEND='Сервис для почты, например, django.core.mail.backends.smtp.EmailBackend'
 EMAIL_HOST='Хост почты, например для gmail smtp.gmail.com или smtp.mail.ru для mail'
 EMAIL_PORT=Порт почты, например, 587
 DEFAULT_FROM_EMAIL='Почта с которой будет отправлять письма youremail@gmail.com если выбрали smtp.gmail.com'
 EMAIL_USE_TLS=Булевое значение True или False причём EMAIL_USE_TLS не равен EMAIL_USE_SSL
 EMAIL_USE_SSL=Булевое значение True или False причём EMAIL_USE_TLS не равен EMAIL_USE_SSL
 EMAIL_HOST_PASSWORD='Пароль для внешнего приложения для доступа к почте, подробнее тут https://help.mail.ru/mail/security/protection/external/'
 NOTIFICATION_EMAIL='Перечень почт куда будут отправлять письма, пишите через пробел, можно указать одну'

 CELERY_BROKER_URL='URL-адрес брокера сообщений, например,redis://localhost:6379'
 CELERY_RESULT_BACKEND='Место хранения результатов выполнения задач, например,redis://localhost:6379'
 CELERY_ACCEPT_CONTENT='Список форматов, которые Celery будет принимать в качестве контента для задач, например,application/json'
 CELERY_TASK_SERIALIZER='Сериализатор, который будет использоваться для сериализации задач перед их отправкой, например,json'
 CELERY_RESULT_SERIALIZER='Сериализатор, который будет использоваться для сериализации результатов задач, например,json'
 ```
   

### 3. Сборка и запуск контейнеров
```bash
docker-compose up --build -d
```

### 4. Создание суперпользователя
```bash
docker-compose exec web python manage.py createsuperuser
```

</details>

<details>

<summary>

### Второй способ, без использования Docker compose
</summary>

### 1. Клонируйте репозиторий:
```bash
git clone https://github.com/Hashtagich/hospice_game.git
```

2. Запускаем backend

    2.1. Установите и активируйте виртуальное окружение:
    ```bash
    python -m venv venv
    venv/Scripts/activate  - для Windows
    venv/bin/activate - для Linux
    ```

    2.2 Перейдите в папку backend и установите зависимости:
    ```bash
    cd backend
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

    2.3 Находясь в папке backend создайте файл *.env* или заполните файл *template.env* и переименуйте его в *.env*:
    ```bash
    SECRET_KEY='Ваш секретный ключ проекта'
    DEBUG=Булевое значение True или False
    ALLOWED_HOSTS='Разрешенные хосты'
    LANGUAGE_CODE='Язык, например, ru'
    TIME_ZONE='Временная зона, например, UTC'
   
    DB_NAME='Имя Базы данных (БД)'
    DB_LOGIN='Логин БД'
    DB_PASS='Пароль БД'
    DB_HOST='Хост БД'
    DB_PORT='Порт БД, например, 5432'
    
    EMAIL_BACKEND='Сервис для почты, например, django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST='Хост почты, например для gmail smtp.gmail.com или smtp.mail.ru для mail'
    EMAIL_PORT=Порт почты, например, 587
    DEFAULT_FROM_EMAIL='Почта с которой будет отправлять письма youremail@gmail.com если выбрали smtp.gmail.com'
    EMAIL_USE_TLS=Булевое значение True или False причём EMAIL_USE_TLS не равен EMAIL_USE_SSL
    EMAIL_USE_SSL=Булевое значение True или False причём EMAIL_USE_TLS не равен EMAIL_USE_SSL
    EMAIL_HOST_PASSWORD='Пароль для внешнего приложения для доступа к почте, подробнее тут https://help.mail.ru/mail/security/protection/external/'
    NOTIFICATION_EMAIL='Перечень почт куда будут отправлять письма, пишите через пробел, можно указать одну'
   
    CELERY_BROKER_URL='URL-адрес брокера сообщений, например,redis://localhost:6379'
    CELERY_RESULT_BACKEND='Место хранения результатов выполнения задач, например,redis://localhost:6379'
    CELERY_ACCEPT_CONTENT='Список форматов, которые Celery будет принимать в качестве контента для задач, например,application/json'
    CELERY_TASK_SERIALIZER='Сериализатор, который будет использоваться для сериализации задач перед их отправкой, например,json'
    CELERY_RESULT_SERIALIZER='Сериализатор, который будет использоваться для сериализации результатов задач, например,json'
    ```
   
    2.3.1 В файле backend/backend/settings.py находим переменную DATABASES и заменяем на:
    ```bash
    DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': BASE_DIR / 'db.sqlite3',
     },
    ```
    
    2.4 Находясь в папке backend выполните миграции:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
    
    2.5 Находясь в папке backend создайте суперпользователя:
    ```bash
    python manage.py createsuperuser
    ```
    
    2.6 Находясь в папке backend запустите проект:
    ```bash
    python manage.py runserver
    ```

3. Запускаем frontend

    3.1 Откройте второй терминал, перейдите в папку frontend и установите зависимости:
    ```bash
    cd frontend
    npm install
    ```
   
    3.2 Запустите frontend:
    ```bash
    npm start
    ```
</details>

___

### API



<font color="red">Информация может быть изменена</font>

***URL***

При запуске через Docker compose, например, http://127.0.0.1 или http://localhost т.е. без :8000

При запуске вторым способом, без Docker compose http://127.0.0.1:8000

***Страница Админ панели***

<code>{{URL}}/admin/</code>

***Страница с документацией по API***

<code>{{URL}}/api/v1/swagger/</code>

***API Регистрация и логирование***
<details>
<summary><code>POST/api/v1/auth/users/</code></summary>



*Регистрация пользователя. Необходимо ввести почту, никнейм и пароль. Пароль должен быть не менее 8 символов и содержать минимум одну заглавную и строчную латинскую букву и цифры.*

```
{
  "email": "user@example.com",
  "username": "string",
  "password": "string",
  "re_password": "string"
}
```

</details>
<details>
<summary><code>POST/api/v1/auth/users/activation/</code></summary>



*Активация пользователя. Необходимо ввести uid и token, приходят на почту в виде ссылки после регистрации.*

```
{
  "uid": "string",
  "token": "string"
}
```

</details>
<details>
<summary><code>POST/api/v1/auth/jwt/create/</code></summary>

*Логирование пользователя и генерация токена. Необходимо ввести никнейм и пароль пользователя.*

```
{
  "username": "string",
  "password": "string"
}
```

</details>
<details>
<summary><code>GET/api/ссылка_на_апи/</code></summary>

*Описание API*

```
Код
```

</details>
<details>
<summary><code>GET/api/ссылка_на_апи/</code></summary>

*Описание API*

```
Код
```

</details>
<details>
<summary><code>GET/api/ссылка_на_апи/</code></summary>

*Описание API*

```
Код
```

</details>
<details>
<summary><code>GET/api/ссылка_на_апи/</code></summary>

*Описание API*

```
Код
```

</details>
<details>
<summary><code>GET/api/ссылка_на_апи/</code></summary>

*Описание API*

```
Код
```

</details>
<details>
<summary><code>GET/api/ссылка_на_апи/</code></summary>

*Описание API*

```
Код
```

</details>
<details>
<summary><code>GET/api/ссылка_на_апи/</code></summary>

*Описание API*

```
Код
```

</details>
<details>
<summary><code>GET/api/ссылка_на_апи/</code></summary>

*Описание API*

```
Код
```

</details>
<details>
<summary><code>GET/api/ссылка_на_апи/</code></summary>

*Описание API*

```
Код
```

</details>

___

<details>
<summary>

## Дополнительная информация

</summary>

+ ***Дизайн игры на биханс — .***

</details>