import yfinance as yf


class StockAnalyzer:

    @staticmethod
    def calculate_gross_margin(financials):
        try:
            revenue = financials.loc['Total Revenue'].iloc[0]
            cogs = financials.loc['Cost Of Revenue'].iloc[0]
            gross_profit = revenue - cogs
            gross_margin = round((gross_profit / revenue) * 100, 2)
        except KeyError:
            gross_margin = None
        return gross_margin

    @staticmethod
    def calculate_net_margin(financials):
        try:
            net_income = financials.loc["Net Income"].iloc[0]
            revenue = financials.loc['Total Revenue'].iloc[0]
            net_margin = round((net_income / revenue) * 100, 2)
        except KeyError:
            net_margin = None
        return net_margin

    @staticmethod
    def calculate_operating_margin(financials):
        try:
            operating_income = financials.loc['Operating Income'].iloc[0]
            revenue = financials.loc['Total Revenue'].iloc[0]
            operating_margin = round((operating_income / revenue) * 100, 2)
        except KeyError:
            operating_margin = None
        return operating_margin

