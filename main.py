import data_download as dd
import data_plotting as dplt
import datetime
import style_variants as st


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
        " 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.\n")

    #  Тикер акции
    # ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):")
    ticker = "GOOGL"  # short for dev

    period, start_date, end_date = '', '', ''
    way = input("Введите число 1 или 2, какой именно вариант вы хотите использовать для вывода биржевых данных period(1) или конкретные даты(2):")
    if way == '1':
        valid_periods = "1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max"
        # period = input(f"Введите период для данных (например, '1mo' для одного месяца, а также варианты {valid_periods}):")
        period = '1y'  # short for dev
    else:
        # Start date for the analysis (optional)
        start_date = input("Введите начало даты (YYYY-MM-DD) для анализа биржевых данных (или оставить пустым для значения по умолчанию): ")
        # start_date = '2023-01-01'  # short for dev

        # End date for the analysis (optional)
        end_date = input("Введите конец даты (YYYY-MM-DD) для анализа биржевых данных (или оставить пустым для значения по умолчанию): ")
        # today = datetime.date.today()  # short for dev
        # end_date = today  # short for dev

    # Check max and min values in percent threshold
    # threshold = int(input("Введите процентный порог колебания акции от мин к мак (например 1, 3, 5, ...):"))
    threshold = 10  # short for dev

    # File name for CSV файла
    # filename = input("Введите имя файла (например, aapl, googl, ...)для сохранения загруженных данных об акциях:")
    filename = 'googl'  # short for dev

    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, period, start=start_date, end=end_date)

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    # Adding an option to select a graph style
    style = input("Введите стиль оформления графика (например, dark_background, bmh, fast, ggplot и др.) или оставь пустым для классики:")
    style = style if style in st.style_variant else '_classic_test_patch'

    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, period, style)

    # Calculates and displays the low closing price of shares for a given period
    dd.calculate_and_display_average_price(stock_data)

    # Notification about strong hesitates
    dd.notify_if_strong_fluctuations(stock_data, threshold)

    # Saves data to the specified file
    dd.export_data_to_csv(stock_data, filename)


if __name__ == "__main__":
    main()
