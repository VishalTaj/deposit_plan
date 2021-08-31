from deposit.validator import validate_portfolios
from config.exception import InvalidAmount, InSufficientAmount

class DepositPlan:
    """
      Defines the Deposit Plan mainly we have 2 types of deposit plans:
      1. Recurrent - deposit is done monthly
      2. One Time - deposit is done once
    """

    @validate_portfolios
    def __init__(self, recurring, reference_code, portfolios):
        self.portfolios = portfolios
        self.reference_code = reference_code
        self.recurring = recurring
        self.find_ratio()


    def find_ratio(self):
        for portfolio in self.portfolios:
            portfolio['ratio'] = portfolio['amount'] / float(self.total_amount())


    def total_ratio(self):
        return sum(portfolio['ratio'] for portfolio in self.portfolios)

    def total_amount(self):
        return sum(portfolio['amount'] for portfolio in self.portfolios)


    def allocate(self, amount, portfolio, ratio):
        portfolio.topup(((ratio / self.total_ratio()) * amount), self.reference_code)


class OneTimeDeposit(DepositPlan):
    """
    Defines the deposit plan for one time deposit
    """

    def __init__(self, reference_code, portfolios):
        self.status = 0
        super().__init__(False, reference_code, portfolios)


    def transfer(self, amount):
        """
            Transfer the amount to the portfolios
        """
        if self.status == 1: return amount

        for portfolio in self.portfolios:
            if portfolio['amount'] <= amount:
                self.allocate(amount, portfolio['portfolio'], portfolio['ratio'])
                self.status = 1
            else:
                raise InvalidAmount()
            


class MonthlyDeposit(DepositPlan):
    """
    Defines the deposit plan for recurrent deposit
    """

    def __init__(self, reference_code, portfolios):
        super().__init__(True, reference_code, portfolios)

    def transfer(self, amount):
        """
            Transfer the amount to the portfolios
        """

        for portfolio in self.portfolios:
            if portfolio['amount'] >= amount:
                self.allocate(amount, portfolio['portfolio'], portfolio['ratio'])
            else:
                if portfolio['amount'] != 0: raise InSufficientAmount()


