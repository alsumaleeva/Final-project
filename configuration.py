# URL_SERVICE хранит базовый URL веб-сервиса, который используется для доступа к API или другим ресурсам.
URL_SERVICE = "https://c47c73df-c0f2-4607-854c-0fb309aa6359.serverhub.praktikum-services.ru"

# Путь для создания курьера
CREATE_COURIER_PATH = "/api/v1/courier"

# Путь для входа курьера в систему, возвращает id курьера
LOGIN_COURIER_PATH = "/api/v1/courier/login"

# Путь для создания заказа
CREATE_ORDER_PATH = "/api/v1/orders"

# Путь для получения заказа по номеру track
GET_ORDER_PATH = "/api/v1/orders/track"

# Путь для принятия заказа курьером (метод PUT).
# сюда подставляется НЕ track, а внутренний id заказа из таблицы Orders
ACCEPT_ORDER_PATH = "/api/v1/orders/accept"
