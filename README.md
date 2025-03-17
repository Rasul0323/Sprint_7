## **Проект по автоматизации API-тестов для сервиса «Яндекс Самокат»**  
https://qa-scooter.praktikum-services.ru/

**Курс по автоматизации тестирования на Python, «Яндекс Практикум»**  
**Спринт 7, Тестирование API**
____
### **Введение в проект**   
«Яндекс Самокат» — это сервис для аренды самокатов в Москве и Московской области. Приложение создано специально для отработки навыков студентов «Практикума». Для отправки запросов автотесты используют библиотеку Requests. Отчет о тестировании генерируется с помощью фреймворка Allure и библиотеки allure-pytest.

### **Структура репозитория**  
Корневая директория проекта содержит набор тестов и файлы со вспомогательными инструментами:

в директории tests лежат файлы с тестами, для каждого проверяемого эндпоинта — свой файл;  
файл data хранит предопределенные тестовые данные, передаваемые в запросах;
файл helpers содержит функции, генерирующие рандомные тестовые данные;  
в файле urls определены адреса сервиса и его эндпоинтов;  
в файле conftest хранятся фикстуры, которые будут использоваться несколькими файлами тестов   
директория allure_results содержит JSON-файлы с результатами выполнения тестов для генерации отчета;  
в файле requirements.txt перечислены все внешние зависимости исполняемых тестов для удобной установки одной командой;  
файл README объясняет суть происходящего и служит руководством.  
### **Покрытие**  
Создание курьера test_courier_create_acc  
1.Курьера можно создать:  
Проверка успешного создания курьера с корректными данными.  
2.Нельзя создать двух одинаковых курьеров:  
Проверка, что система возвращает ошибку при попытке создать курьера с уже существующим логином.  
3.Обязательные поля:  
Проверка, что для создания курьера необходимо передать все обязательные поля.  
4.Правильный код ответа:  
Проверка, что запрос возвращает правильный код ответа (201).  
5.Успешный запрос возвращает {"ok":true}:  
Проверка, что успешный ответ содержит {"ok":true}.   
6.Ошибка при отсутствии полей:  
Проверка, что если одного из обязательных полей нет, запрос возвращает ошибку.  
7.Ошибка при создании с существующим логином:  
Проверка, что если создать пользователя с логином, который уже есть, возвращается ошибка.  
Логин курьера test_courier_login  
1.Курьер может авторизоваться:  
Проверка успешной авторизации курьера с корректными данными.  
2.Обязательные поля для авторизации:  
Проверка, что для авторизации нужно передать все обязательные поля.  
3.Ошибка при неправильном логине или пароле:  
Проверка, что система вернёт ошибку, если неправильно указать логин или пароль.   
4.Ошибка при отсутствии полей:  
Проверка, что если какого-то поля нет, запрос возвращает ошибку.  
5.Ошибка при авторизации под несуществующим пользователем:  
Проверка, что если авторизоваться под несуществующим пользователем, запрос возвращает ошибку.  
6.Успешный запрос возвращает id:  
Проверка, что успешный запрос возвращает id курьера.  
Создание заказа test_order_creation  
1.Выбор цвета:  
Проверка, что можно указать один из цветов — BLACK или GREY.  
Проверка, что можно указать оба цвета.  
Проверка, что можно совсем не указывать цвет.  
2.Тело ответа содержит track:  
Проверка, что тело ответа содержит track.  
3.Параметризация:  
Для тестирования создания заказа используется параметризация.  
Список заказов test_order_list  
1.Возвращается список заказов:  
Проверка, что в тело ответа возвращается список заказов.

### **Запуск всех тестов**  
Установка всех зависимостей одной командой: pip install -r requirements.txt.

Запуск всех тестов одной командой: pytest -v.

### **Отчет о тестировании**  
Allure-отчет в формате веб-страницы генерируется командой allure serve allure_results.