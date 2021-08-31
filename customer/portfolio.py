from customer.validator import validate_portfolio

class Portfolio:
    """
        Customer Portfolio is starts by setting the goal and then this will keep track of
        amount we have invested to the goal.
    """

    @validate_portfolio
    def __init__(self, reference_code, target_amount, initial_balance):
        self.reference_code = reference_code
        self.balance = initial_balance
        self.target_amount = target_amount
        self.target_achieved = False


    def topup(self, amount, reference_code):
        if reference_code == self.reference_code:
            self.balance += amount
            self.target_achieved = self.check_if_reached_target()
        else:
            raise("Invalid Reference Code")


    def check_if_reached_target(self):
        if self.balance >= self.target_amount:
            return True


class HighRiskPortfolio(Portfolio):
    """
        HighRiskPortfolio is a child of Portfolio.
    """
    def __init__(self, reference_code, target_amount, initial_balance=0):
        super().__init__(reference_code, target_amount, initial_balance)


class RetirementPortfolio(Portfolio):
    """
        Retirement is a subclass of Portfolio.
    """
    def __init__(self, reference_code, target_amount, initial_balance=0):
        super().__init__(reference_code, target_amount, initial_balance)
