import allure
import pytest
import requests
import data
import helpers
from urls import Urls


class TestCourierLogin:

    @allure.title('Проверка успешной аутентификации курьера при заполнении необходимых полей')
    @allure.description('Проверяется что в ответ он получит уникальный идентификатор id')
    def test_courier_login_success(self, courier_data_without_firstname):
        requests.post(Urls.URL_courier_create, data=courier_data_without_firstname)
        response_login = requests.post(Urls.URL_courier_login, data=courier_data_without_firstname)
        assert response_login.status_code == 200 and response_login.json()["id"] != []

    @allure.title('Проверка получения ошибки аутентификации курьера при вводе невалидных данных')
    @allure.description('В тест по очереди передаются наборы данных с несуществующим логином или неверным паролем. '
                        'Проверяются код и тело ответа.')
    @pytest.mark.parametrize('key, value', [('login', helpers.GenerateString.generate_random_string(10)),
                                            ('password', helpers.GenerateString.generate_random_string(10))])
    def test_courier_login_nonexistent_data_not_found(self, courier_data, key, value):
        requests.post(Urls.URL_courier_create, data=courier_data)
        courier_data[key] = value
        currier_resp = requests.post(Urls.URL_courier_login, data=courier_data)
        assert currier_resp.status_code == 404 and currier_resp.json()[
            "message"] == data.Response.response_account_not_found

    @allure.title('Проверка получения ошибки аутентификации курьера с пустым полем логина или пароля')
    @allure.description('В тест по очереди передаются наборы данных с пустым логином или паролем. '
                        'Проверяются код и тело ответа.')
    @pytest.mark.parametrize('key, value', [('login', ''), ('password', '')])
    def test_courier_login_empty_credentials_bad_request(self, courier_data, key, value):
        courier_data[key] = value
        currier_resp = requests.post(Urls.URL_courier_login, data=courier_data)
        assert currier_resp.status_code == 400 and currier_resp.json()[
            "message"] == data.Response.response_no_data_input
