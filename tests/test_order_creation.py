import pytest
import allure
import requests
import json
from urls import Urls
from data import OrderData



class TestCreateOrder:
    @allure.title("Тестирование процесса создания заказа с возможностью выбора одного цвета, обоих цветов или без указания цвета")
    #Тест проверяет, что процесс создания заказа работает корректно с различными цветами, и что сервер возвращает ожидаемый статус и данные.
    @allure.description('Согласно требованиям, система должна позволять указать в заказе один цвет самоката, выбрать '
                        'сразу оба или не указывать совсем. В тест по очереди передаются наборы данных с разными '
                        'параметрами: серый, черный, оба цвета, цвет не указан. Проверяются код и тело ответа.')
    @pytest.mark.parametrize('color', OrderData.color_scooter)
    def test_choose_color_get_order(self, color):
        payload = OrderData.order_data
        payload['color'] = color
        payload = json.dumps(payload)
        response = requests.post(Urls.URL_orders_create, data=payload)
        response_json = response.json()

        assert response.status_code == 201 and 'track' in response_json.keys()