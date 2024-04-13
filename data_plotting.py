import matplotlib.pyplot as plt
import pandas as pd
import data_download as dd


def create_and_save_plot(data, ticker, period, style, filename=None):
    plt.style.use(style)
    """- Отвечает за визуализацию данных.
    - Содержит функции для создания и сохранения графиков цен закрытия и скользящих средних.
    Создаёт график, отображающий цены закрытия и скользящие средние. Предоставляет возможность сохранения графика в
    файл. Параметр filename опционален; если он не указан, имя файла генерируется автоматически."""
    plt.figure(figsize=(10, 6))

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
            plt.plot(dates, data['MACD_Line'].values, label='MACD Line')
            plt.plot(dates, data['Signal_Line'].values, label='Signal Line')
            plt.bar(dates, data['Histogram'].values, label='Histogram', color='orange')
            period = period if period else str(dates[0])[:10]+'-'+str(dates[-1])[:10]

        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')
        plt.plot(data['Date'], data['MACD_Line'], label='MACD Line')
        plt.plot(data['Date'], data['Signal_Line'], label='Signal Line')
        plt.bar(data['Date'], data['Histogram'], label='Histogram', color='orange')

    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()

    std = dd.calculate_and_display_average_deviation(data)
    plt.text(data.index[-1], data['Close'][-1], f"Std: {std:.2f}")
    print(f"Стандартное отклонение цены закрытия акций:{std:.2f}")

    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")
