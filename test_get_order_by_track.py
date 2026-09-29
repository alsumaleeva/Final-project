# Алсу Малеева, 47-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import data

def test_get_order_by_track():
    # Шаг 1. Клиент создаёт заказ
    order_response = sender_stand_request.post_new_order(data.order_body)
    # Проверяем, что заказ создан успешно (201 Created)
    assert order_response.status_code == 201

    # Шаг 2. Сохраняем номер трека заказа из ответа
    track = order_response.json()["track"]

    # Шаг 3. Выполняем запрос на получение заказа по треку
    get_response = sender_stand_request.get_order_by_track(track)

    # Шаг 4. Проверяем, что код ответа равен 200
    assert get_response.status_code == 200