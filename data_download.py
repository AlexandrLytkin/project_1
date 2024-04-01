import yfinance as yf
import numpy as np

"""- Отвечает за загрузку данных об акциях.
- Содержит функции для извлечения данных об акциях из интернета и расчёта скользящего среднего."""


def fetch_stock_data(ticker, period='1mo'):
    """Получает исторические данные об акциях для указанного тикера и временного периода.
    Возвращает DataFrame с данными."""
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data  # Возвращает дата фрейм с данными


def add_moving_average(data, window_size=5):
    """Добавляет в DataFrame колонку со скользящим средним, рассчитанным на основе цен закрытия."""
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data):
    """Функция принимает DataFrame и вычисляет среднее значение колонки 'Close'.
    Результат будет выводиться в консоль.
    Вычисляет и выводит среднюю цену закрытия акций за заданный период."""
    res = data['Close']
    print('Средняя цена закрытия акций за заданный период', round(res.mean(), 2))


def notify_if_strong_fluctuations(data, threshold):
    """Функция будет вычислять максимальное и минимальное значения цены закрытия и сравнивать разницу с
    заданным порогом. Если разница превышает порог, пользователь получает уведомление."""
    max_price = round(data['Close'].max(), 2)
    min_price = round(data['Close'].min(), 2)
    percent = round(max_price / min_price * 100 - 100, 2)
    if percent > threshold:
        print(f'Цена акций колебалась более чем на заданный процент "{threshold}%" за период')
