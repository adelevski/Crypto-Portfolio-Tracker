from funcs import get_total, get_prices, df_work



if __name__ == "__main__":
    # data fetching
    print("Fetching data...")
    total_balance, all_holdings = get_total()
    prices = get_prices(total_balance)

    # Totals:
    print("Totals:")
    df_work(total_balance, prices)

    # Per Exchange:
    for exchange, totals in all_holdings.items():
        print(f"Exchange: {exchange}")
        df_work(totals, prices)


