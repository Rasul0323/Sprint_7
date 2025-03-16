import datetime

class OrderData:
    #Создание заказа
    order_data = {
        "firstName": "Расул",
        "lastName": "Шихвелиев",
        "address": "Баумана, 47",
        "metroStation": "15",
        "phone": "+7 985 564 57 42",
        "rentTime": 4,
        "deliveryDate": datetime.date.today().day,
        "comment": "Нужен новый самокат",
        "color": []
        }

    color_scooter = [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ]

class Response:
    #Запрос с несуществующей парой логин-пароль:
    response_account_not_found = 'Учетная запись не найдена'

    #Запрос без логина или пароля:
    response_no_data_input = 'Недостаточно данных для входа'

    #Запрос без логина или пароля:
    response_no_data_account = 'Недостаточно данных для создания учетной записи'

    #Запрос с повторяющимся логином:
    response_login_used = 'Этот логин уже используется. Попробуйте другой.'

    #Успешное создание учетной записи:
    response_registration_successful = '{"ok":true}'

class LimitPageOrders:

    #Лимит на страницы заказов:
    limit_page_orders = {
        "limit": "5",
        "page": "0"
    }