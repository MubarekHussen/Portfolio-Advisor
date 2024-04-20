import yfinance as yf
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)


def fetch_historical_data(symbol, start_date, end_date):
    """Fetch historical data for a ticker symbol."""
    try:
        ticker = yf.Ticker(symbol)
        data = ticker.history(start=start_date, end=end_date)
    except Exception as e:
        logging.error(f"Failed to fetch data for {symbol}: {e}")
        return None

    return data


def calculate_price_change(data, symbol):
    """Calculate and return the price change for the fetched data."""
    if data is None:
        return None

    try:
        price_change = (data['Close'].iloc[-1] - data['Close'].iloc[0]) / data['Close'].iloc[0] * 100
    except Exception as e:
        logging.error(f"Failed to calculate price change for {symbol}: {e}")
        return None

    return price_change


def calculate_portfolio_change(price_changes, portfolio_weights):
    """Calculate and return the weighted average change for the portfolio."""
    try:
        portfolio_change = sum(price_changes[symbol] * weight for symbol, weight in portfolio_weights.items())
    except Exception as e:
        logging.error(f"Failed to calculate portfolio change: {e}")
        return None

    return portfolio_change


def main():
    ticker_symbols = ["TSLA", "NVDA", "AAPL", "GOOG", "^TNX"]
    start_date = "2024-03-01"
    end_date = "2024-03-31"
    portfolio_weights = {"TSLA": 0.20, "NVDA": 0.20, "AAPL": 0.20, "GOOG": 0.20, "^TNX": 0.20}

    price_changes = {}
    results = {}
    for symbol in ticker_symbols:
        data = fetch_historical_data(symbol, start_date, end_date)
        price_change = calculate_price_change(data, symbol)
        if price_change is not None:
            price_changes[symbol] = price_change
            results[symbol] = {
                'data': data,
                'price_change': price_change
            }

    portfolio_change = calculate_portfolio_change(price_changes, portfolio_weights)
    if portfolio_change is not None:
        results['portfolio_change'] = portfolio_change
    else:
        return None

    results['price_changes'] = price_changes

    logging.info("\nPrice changes for March 2024:")
    for symbol, data in results.items():
        if symbol != 'portfolio_change' and symbol != 'price_changes':
            logging.info(f"{symbol}: {data['price_change']:.2f}%")
    logging.info(f"\nWeighted average change for the portfolio: {results['portfolio_change']:.2f}%")

    return results


if __name__ == "__main__":
    main()