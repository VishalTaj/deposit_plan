from config.exception import MaximumDepositPlanExceeded, DuplicateDepositPlan, InvalidAmount, InvalidReferenceCode, InvalidTargetAmount

def validate_amount(func):
    def wrapper(self, *args, **kwargs):
        payload = args[0]
        if self.reference_code != payload['reference_code']:
            raise InvalidReferenceCode()

        if payload['amount'] < 1:
            raise InvalidAmount()

        return func(self, *args, **kwargs)
    
    return wrapper


def validate_deposit_plans(func):
    def wrapper(self, *args, **kwargs):
        deposit_plans = self.deposit_plans  + [args[0]]
        search_plan  = lambda dp: [plan for plan in deposit_plans if str(type(plan).__name__) == dp]
        count_of = lambda dp: len(search_plan(dp))
        if len(deposit_plans) > 2 or len(deposit_plans) < 1:
            raise MaximumDepositPlanExceeded()

        if count_of("OneTimeDeposit") > 1 or count_of("MonthlyDeposit") > 1:
            raise DuplicateDepositPlan()
        
        return func(self, *args, **kwargs)

    return wrapper


def validate_portfolio(func):
    def wrapper(self, *args, **kwargs):
        if args[0] == "":
            raise InvalidReferenceCode()

        if args[1] == 0:
            raise InvalidTargetAmount()

        return func(self, *args, **kwargs)

    return wrapper