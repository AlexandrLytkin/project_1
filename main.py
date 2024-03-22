import data_download as dd
import data_plotting as dplt


def main():
    """- Является точкой входа в программу.
    - Запрашивает у пользователя тикер акции и временной период, загружает данные,
    обрабатывает их и выводит результаты в виде графика.
    - main(): Основная функция, управляющая процессом загрузки, обработки данных и их визуализации. Запрашивает у
    пользователя ввод данных, вызывает функции загрузки и обработки данных, а затем передаёт результаты на визуализацию.
    """
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print(
        "Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть:"
        " AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation),"
        " AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print(
        "Общие периоды времени для данных о запасах включают:"
        " 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")

    #  Тикер акции
    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")

    #  Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    period = input("Введите период для данных (например, '1mo' для одного месяца): ")

    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, period)

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, period)

    # Сalculates and displays the low closing price of shares for a given period
    dd.calculate_and_display_average_price(stock_data)


if __name__ == "__main__":
    main()
