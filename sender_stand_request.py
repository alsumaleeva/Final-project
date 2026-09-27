import requests
import configuration
import data


# Отправка POST-запроса на регистрацию нового курьера
def post_new_courier(courier_body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_COURIER_PATH, 
        json=courier_body,
        headers=data.headers 
    )


# Отправка POST-запроса на вход курьера, возвращает ответ с id в теле
def post_courier_login(login_body):
    return requests.post(
        configuration.URL_SERVICE + configuration.LOGIN_COURIER_PATH,
        json=login_body,
        headers=data.headers
    )


# Отправка POST-запроса на создание заказа
def post_new_order(order_body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=order_body,
        headers=data.headers
    )


# Отправка GET-запроса на получение заказа по номеру track.
# track передаётся как query-параметр ?t=<track>
def get_order_by_track(track):
    return requests.get(
        configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
        params={"t": track}  # requests сам соберёт строку вида ?t=123456
    )


# Отправка PUT-запроса на принятие заказа курьером.
def put_accept_order(order_id, courier_id):
    url = f"{configuration.URL_SERVICE}{configuration.ACCEPT_ORDER_PATH}/{order_id}"
    return requests.put(
        url,
        params={"courierId": courier_id}
    )

