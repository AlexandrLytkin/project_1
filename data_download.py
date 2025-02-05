import yfinance as yf

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
    res = data['Moving_Average'] = data['Close']
    print('Средняя цена закрытия акций за заданный период', round(sum(res) / len(res), 2))
