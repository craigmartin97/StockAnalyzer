class Stock:
    gross_margin = None
    net_margin = None
    operating_margin = None

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, gross_margin, net_margin, operating_margin):
        self.gross_margin = gross_margin
        self.net_margin = net_margin
        self.operating_margin = operating_margin
