from funcs import get_total, get_prices, df_work


# data fetching
total_balance, all_holdings = get_total()
prices = get_prices(total_balance)


if __name__ == "__main__":
    
    # Totals:
    df_work(total_balance)

    # Per Exchange:
    for exchange, totals in all_holdings.items():
        print(f"exchange: {exchange}")
        df_work(totals)


