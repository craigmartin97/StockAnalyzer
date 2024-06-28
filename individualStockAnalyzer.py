import yfinance as yf
import stockAnalyzer
import stock


class IndividualStockAnalyzer:

    stock = stock.Stock
    analyzer = stockAnalyzer.StockAnalyzer()

    def analyze(self, ticker):
        """
        :param ticker: The tracking, ticker symbol of the stock to search and analyse for
        """
        financials = yf.Ticker(ticker).financials
        self.stock.gross_margin = self.analyzer.calculate_gross_margin(financials)
        self.stock.net_margin = self.analyzer.calculate_net_margin(financials)
        self.stock.operating_margin = self.analyzer.calculate_operating_margin(financials)
        self._output()

    def _output(self):
        print(f"Gross Margin: {self.stock.gross_margin}%")
        print(f"Net Margin: {self.stock.net_margin}%")
        print(f"Operating Margin: {self.stock.operating_margin}%")