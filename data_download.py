import yfinance as yf
import numpy as np
import plotly.graph_objs as go
import matplotlib.pyplot as plt

"""- Отвечает за загрузку данных об акциях.
- Содержит функции для извлечения данных об акциях из интернета и расчёта скользящего среднего."""


def fetch_stock_data(ticker, period=None, start=None, end=None):
    """Получает исторические данные об акциях для указанного тикера и временного периода.
    Возвращает DataFrame с данными."""
    stock = yf.Ticker(ticker)
    data = stock.history(period=period, start=start, end=end)
    data = calculate_macd(data)  # Вычисляет MACD
    return data  # Возвращает дата фрейм с данными


def interactive_graph(data, ticker):
    """ Интерактивный график использует plotly

    Функция будет принимать DataFrame и вычислять среднее значение колонки 'Close'.
    Результат будет выводиться в консоль."""
    dates = data.index.to_numpy()
    close_price = round(data['Close'], 2)
    res = go.Scatter(x=dates, y=close_price, text='Data, Close Price')
    fig = go.Figure()
    fig.add_trace(res)
    fig.update_layout(title=f"Интерактивный график {ticker} Цена акций с течением времени",
                      xaxis_title="Дата",
                      yaxis_title="Цена")
    fig.show()


def add_moving_average(data, window_size=5):
    """Добавляет в DataFrame колонку со скользящим средним, рассчитанным на основе цен закрытия."""
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data):
    """Функция принимает DataFrame и вычисляет среднее значение колонки 'Close'.

    Вычисляет и выводит среднюю цену закрытия акций за заданный период."""
    res = data['Close']
    print('Средняя цена закрытия акций за заданный период', round(res.mean(), 2))


def calculate_and_display_average_deviation(data):
    """Вывод средней цены акции

    Функция для расчёта и отображения дополнительных статистических индикаторов,
    например, стандартного отклонения цены закрытия."""
    std = data['Close'].std()
    plt.text(data.index[-1], data['Close'][-1], f"Std: {std:.2f}")
    print(f"Стандартное отклонение цены закрытия акций:{std:.2f}")


def notify_if_strong_fluctuations(data, threshold):
    """Определение порога закрытия

    Функция будет вычислять максимальное и минимальное значения цены закрытия и сравнивать разницу с
    заданным порогом. Если разница превышает порог, пользователь получает уведомление."""
    max_price = round(data['Close'].max(), 2)
    min_price = round(data['Close'].min(), 2)
    percent = round(max_price / min_price * 100 - 100, 2)
    if percent > threshold:
        print(f'Цена акций колебалась более чем на заданный процент "{threshold}%" за период')


def export_data_to_csv(data, filename):
    """Сохраняем загруженные данные об акциях в CSV файл.

    Функция принимает DataFrame и имя файла, после чего сохранять данные в указанный файл."""
    try:
        data.to_csv(filename + '.csv')
        print(f'Файл сохранен в {filename}.csv')
    except Exception as ex:
        print(f'Файл не был сохранен в {filename}.csv возникла ошибка: {ex}')


def calculate_macd(data, n_fast=12, n_slow=26):
    """Рассчитывает индикатор MACD (Moving Average Convergence Divergence).

    Функция для расчёта и отображения на графике дополнительных технических индикаторов MACD."""
    ema_fast = data['Close'].ewm(span=n_fast, adjust=False).mean()
    ema_slow = data['Close'].ewm(span=n_slow, adjust=False).mean()
    macd_line = ema_fast - ema_slow
    signal_line = macd_line.ewm(span=9, adjust=False).mean()
    histogram = macd_line - signal_line
    data['MACD_Line'] = macd_line
    data['Signal_Line'] = signal_line
    data['Histogram'] = histogram
    return data
