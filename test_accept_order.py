# Алсу Малеева, 47-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import data

def test_create_courier_order_and_accept():
    # Шаг 1. Регистрируем нового курьера
    courier_response = sender_stand_request.post_new_courier(data.courier_body)
    # Проверяем, что курьер создан успешно (201 Created по документации)
    assert courier_response.status_code == 201

    # Шаг 2. Логинимся этим курьером, чтобы получить его id
    login_response = sender_stand_request.post_courier_login(data.courier_login_body)
    # Успешный вход возвращает 200 и тело {"id": ...}
    assert login_response.status_code == 200
    courier_id = login_response.json()["id"]

    # Шаг 3. Создаём новый заказ
    order_response = sender_stand_request.post_new_order(data.order_body)
    # Успешное создание — 201 Created, в теле номер track
    assert order_response.status_code == 201
    track = order_response.json()["track"]

    # Шаг 4. Получаем полные данные заказа по track, чтобы узнать его внутренний id.
    # Это нужно, потому что метод accept принимает именно id, а не track
    order_info_response = sender_stand_request.get_order_by_track(track)
    assert order_info_response.status_code == 200
    order_id = order_info_response.json()["order"]["id"]

    # Шаг 5. Курьер принимает заказ по его id
    accept_response = sender_stand_request.put_accept_order(order_id, courier_id)
    # Успешное принятие — 200 и {"ok": true}
    assert accept_response.status_code == 200