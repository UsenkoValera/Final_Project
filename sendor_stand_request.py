# Валерий Усенко, 12-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import data

# Создание заказа
def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,
                         json=body)
# Получение заказа по номеру трекера
def get_order(track):
        return requests.get(configuration.URL_SERVICE + configuration.ORDER_INFORMATION_PATH + str(track))

# Автотест
def test_order_creation():
    track_number = create_order(data.order_body).json()["track"]

   # Получение данных заказа по треку
    order_response = get_order(track_number)

    assert order_response.status_code == 200
    order_data = order_response.json()
    print("     Номер заказа:", track_number)
    print(order_data)
