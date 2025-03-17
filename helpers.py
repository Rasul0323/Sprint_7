import random
import string
import allure
import requests
import data
from urls import Urls


class GenerateString:
    @staticmethod
    #Генерирует случайную строку из букв нижнего регистра заданной длины.
    def generate_random_string(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))


class GenerateDataCourier:
    @allure.step('Генерация данных курьера с случайным логином, паролем и именем')
    def generate_data_courier(self):
        return {
            "login": GenerateString.generate_random_string(10),
            "password": GenerateString.generate_random_string(10),
            "firstName": GenerateString.generate_random_string(10)
        }

    @allure.step('Генерация данных курьера с заданным логином и случайным паролем и именем')
    def generate_data_courier_static_login(self):
        return {
            "login": "Rasslle",
            "password": GenerateString.generate_random_string(10),
            "firstName": GenerateString.generate_random_string(10)
        }


class GetOrder:
    @allure.step('Получение списка заказов')
    def get_orders_list(self, params=None):
        return requests.get(Urls.URL_orders_create, params=params)

    @allure.step('Возвращает параметры для получения списка заказов.')
    def set_param_order_list(self):
        return data.LimitPageOrders.limit_page_orders