import hashlib
from deposit.deposit_plan import MonthlyDeposit, OneTimeDeposit
from customer.validator import validate_amount, validate_deposit_plans

class Customer:
    """
      Manages Customer
    """

    def __init__(self, name, email, age):
        self.name = name
        self.reference_code = self.generate_reference_code(name, email)
        self.age = age
        self.deposit_plans = []


    def generate_reference_code(self, name, email):
        """
          Generates a reference code for the customer.
          The reference code is a hash of the name and email.
          and will be unique to the customer.
        """
        return hashlib.md5((name + email).encode()).hexdigest()

    @validate_deposit_plans
    def create_deposit_plan(self, deposit_plan):
        """
          Adds a deposit plan to the customer.
        """
        self.deposit_plans.append(deposit_plan)

    def search_deposit_plan(self, deposit_plan):
        """
          Searches for a deposit plan in the customer.
        """
        return [plan for plan in self.deposit_plans if type(plan) == deposit_plan]


    @validate_amount
    def deposit(self, payload):
        """
          Deposits the amount into the customer portfolio.
        """
        status = False
        one_time = self.search_deposit_plan(OneTimeDeposit)

        if len(one_time):
            if one_time[0].status == 0:
                one_time[0].transfer(payload['amount'])
                status = True
            

        monthly = self.search_deposit_plan(MonthlyDeposit)

        if len(monthly) and not status:
            monthly[0].transfer(payload['amount'])



        
