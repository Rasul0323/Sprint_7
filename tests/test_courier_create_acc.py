import allure
import pytest
import requests
import data
from data import Response
from urls import Urls

@allure.story("Создание курьера")
class TestCourierCreate:
    @allure.title('Проверка успешного создания аккаунта курьера с валидными данными')
    @allure.description('Happy path. Проверяются код и тело ответа.')
    def test_create_courier_account_success(self, courier_data):
        response = requests.post(Urls.URL_courier_create, data=courier_data)
        assert response.status_code == 201 and response.text == Response.response_registration_successful

    @allure.title("Тестирование создания курьера с использованием только обязательных полей, таких как логин и пароль")
    @allure.description('Проверяются код и тело ответа.')
    def test_create_courier_success(self, courier_data_without_firstname):
        response = requests.post(Urls.URL_courier_create, data=courier_data_without_firstname)
        assert response.status_code == 201 and response.text == Response.response_registration_successful


    @allure.title('Проверка получения ошибки при повторном использовании логина, пароля и имени для создания курьера')
    @allure.description('Проверяются код и тело ответа.')
    def test_create_courier_account_login_taken_conflict(self, courier_data):
        # Создание первого курьера
        requests.post(Urls.URL_courier_create, data=courier_data)
        # Создание повторно курьера
        response2 = requests.post(Urls.URL_courier_create, data=courier_data)
        assert response2.status_code == 409 and response2.json()["message"] == Response.response_login_used


    @allure.title("Тестирование, невозможно создать двух курьеров с идентичными логинами")
    @allure.description('Проверяются код и тело ответа.')
    def test_not_create_double_login_courier(self, couriers_data):
        requests.post(Urls.URL_courier_create, data=couriers_data[0])
        response2 = requests.post(Urls.URL_courier_create, data=couriers_data[1])
        assert response2.status_code == 409 and response2.json()["message"] == Response.response_login_used


    @allure.title('Проверка получения ошибки при создании курьера с незаполненными обязательными полями')
    @allure.description('В тест по очереди передаются наборы данных с пустым логином или паролем. ' 'Проверяются код и тело ответа.')
    @pytest.mark.parametrize('key, value', [('login', ''), ('password', '')])
    def test_create_courier_account_with_empty_required_fields(self, courier_data, key, value):
        courier_data[key] = value
        currier_resp = requests.post(Urls.URL_courier_create, data=courier_data)
        assert currier_resp.status_code == 400 and currier_resp.json()[
        "message"] == data.Response.response_no_data_account