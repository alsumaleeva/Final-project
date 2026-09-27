# Заголовки для запроса — тело в формате JSON
headers = {
    "Content-Type": "application/json"
}

# Тело запроса на создание курьера.
courier_body = {
    "login": "kurier1",
    "password": "1234",
    "firstName": "Ivan"
}

# Тело запроса на вход тем же курьером — логин и пароль должны совпадать с courier_body
courier_login_body = {
    "login": "kurier1",
    "password": "1234"
}

# Тело запроса на создание заказа
order_body = {
    "firstName": "Батон",
    "lastName": "Булкин",
    "address": "Москва, улица Ленина, 15",
    "metroStation": 4,
    "phone": "+7 800 555 35 35",
    "rentTime": 5,
    "deliveryDate": "2026-09-18",
    "comment": "Позвонить перед доставкой",
    "color": ["BLACK"]
}