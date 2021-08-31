from config.exception import InvalidPortfolio

def validate_portfolios(func):
    def wrapper(self, *args, **kwargs):
        portfolios = args[2]
        if len(portfolios) > 2 or len(portfolios) < 1:
            raise InvalidPortfolio()

        return func(self, *args, **kwargs)
    
    return wrapper