import pytest
import helpers


@pytest.fixture
#Генерирует данные курьера со случайным логином, паролем и именем.
def courier_data():
    data_courier = helpers.GenerateDataCourier()
    return data_courier.generate_data_courier()


@pytest.fixture
#Создает двух курьеров с одинаковым логином.
def couriers_data():
    data_courier_1 = helpers.GenerateDataCourier()
    data_courier_2 = helpers.GenerateDataCourier()
    return (
        data_courier_1.generate_data_courier_static_login(),
        data_courier_2.generate_data_courier_static_login()
    )


@pytest.fixture
#Создает курьера только с логином и паролем, без имени.
def courier_data_without_firstname(courier_data):
    courier_data['firstName'] = ''
    return courier_data