from funcs import get_total, get_prices, get_df



if __name__ == "__main__":
    # data fetching
    print("Fetching data...")
    total_balance, all_holdings = get_total()
    prices = get_prices(total_balance)

    # Totals:
    print("Totals:")
    df, total_value = get_df(total_balance, prices, form=True)
    print(df)
    print(f"Total value: ${total_value:.2f}\n")

    # Per Exchange:
    for exchange, totals in all_holdings.items():
        print(f"Exchange: {exchange}")
        df, total_value = get_df(totals, prices, form=True)
        print(df)
        print(f"Total value: ${total_value:.2f}\n")


