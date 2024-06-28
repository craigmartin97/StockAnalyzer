import yfinance as yf
import pandas as pd
import stock as s
import stockAnalyzer


class AllStockAnalyzer:

    def analyze(self):
        # Get all the tickers and their data
        tickers_str = self.flatten_tickers(self.get_all_tickers().Symbol)
        ticker_data = yf.Tickers(tickers_str)

        all_stocks = []
        analyzer = stockAnalyzer.StockAnalyzer()
        for ticker in ticker_data.tickers:
            financials = ticker_data.tickers[ticker].financials
            gross_margin = analyzer.calculate_gross_margin(financials)
            net_margin = analyzer.calculate_net_margin(financials)
            operating_margin = analyzer.calculate_operating_margin(financials)
            stock = s.Stock(gross_margin, net_margin, operating_margin)
            is_valid = self.is_stock_valid(stock)
            if is_valid:
                print(f"--- {ticker} ---")
                all_stocks.append(stock)
        print(f"Count: {len(all_stocks)}")

    @staticmethod
    def is_stock_valid(stock):
        nums = [stock.gross_margin, stock.net_margin, stock.operating_margin]
        average = len(nums) / 2
        total_invalid = 0
        for value in nums:
            if value is None:
                total_invalid += 1
        if total_invalid > average:
            return False
        return True

    @staticmethod
    def flatten_tickers(tickers):
        ticker_str = ' '.join(tickers)
        return ticker_str

    @staticmethod
    def get_all_tickers():
        # Read and print the stock tickers that make up S&P500
        return pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
