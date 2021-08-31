import unittest


from customer.customer import Customer
from customer.portfolio import HighRiskPortfolio, RetirementPortfolio
from deposit.deposit_plan import OneTimeDeposit, MonthlyDeposit
from config.exception import MaximumDepositPlanExceeded, DuplicateDepositPlan, InvalidAmount, InvalidReferenceCode, InvalidTargetAmount

class TestCase(unittest.TestCase):

    def create_customer(self):
        return Customer("Vishal", "vishal@yahoo.com", 30)
      
    def sample1(self):
        customers = [self.create_customer()]

        reference_code = customers[0].reference_code
        port1 = HighRiskPortfolio(reference_code, 10000)
        port2 = RetirementPortfolio(reference_code, 1000)

        customers[0].create_deposit_plan(OneTimeDeposit(reference_code, [{ 'portfolio': port1, 'amount': 10000}, {'portfolio': port2, 'amount': 500}]))
        customers[0].create_deposit_plan(MonthlyDeposit(reference_code, [{ 'portfolio': port1, 'amount': 0}, {'portfolio': port2, 'amount': 100}]))

        return customers, reference_code

    def setUp(self):
        """
            Running Test
        """
        if self.shortDescription() is not None: print(self.shortDescription())

    def test_happycase(self):
        """
            Checking the flow
        """
        
        customers, reference_code = self.sample1()
        customers[0].deposit({'reference_code': reference_code, 'amount': 10500})
        customers[0].deposit({'reference_code': reference_code, 'amount': 100})

        self.assertEqual(customers[0].deposit_plans[1].portfolios[0]['portfolio'].balance, 10000)
        self.assertEqual(customers[0].deposit_plans[1].portfolios[1]['portfolio'].balance, 600)


    def test_invalid_reference_code_in_portfolio(self):
        """
            Checking Invalid Reference Code
        """
        with self.assertRaises(InvalidReferenceCode) : HighRiskPortfolio("", 0)

    def test_invalid_target_amount(self):
        """ 
            Checking Invalid Target Amount
        """
        customer = self.create_customer()
        with self.assertRaises(InvalidTargetAmount) : HighRiskPortfolio(customer.reference_code, 0)

    def test_duplicate_deposit_plan(self):
        """ 
            Checking Duplicate Deposit Plan
        """
        customer = self.create_customer()
        customer.create_deposit_plan(OneTimeDeposit(customer.reference_code, [{ 'portfolio': HighRiskPortfolio("123", 10000), 'amount': 10000}]))
        with self.assertRaises(DuplicateDepositPlan) : customer.create_deposit_plan(OneTimeDeposit(customer.reference_code, 
        [ { 'portfolio': HighRiskPortfolio("123", 10000), 'amount': 10000}]))

    def test_max_deposit_plan(self):
        """
            Checking Deposit Plan Limit
        """
        customer = self.create_customer()
        customer.create_deposit_plan(OneTimeDeposit(customer.reference_code, [{ 'portfolio': HighRiskPortfolio("123", 10000), 'amount': 10000}]))
        customer.create_deposit_plan(MonthlyDeposit(customer.reference_code, [{ 'portfolio': HighRiskPortfolio("123", 10000), 'amount': 10000}]))
        with self.assertRaises(MaximumDepositPlanExceeded) : customer.create_deposit_plan(OneTimeDeposit("123", 
        [ { 'portfolio': HighRiskPortfolio("123", 10000), 'amount': 10000}]))


    def test_invalid_amount(self):
        """
            Checking Invalid Amount
        """
        customers, reference_code = self.sample1()
        with self.assertRaises(InvalidAmount) : customers[0].deposit({'reference_code': reference_code, 'amount': 0})

    def test_invalid_reference_code_in_deposit_plan(self):
        """
            Checking Invalid Reference Code in Deposit Plan
        """
        customers = self.sample1()[0]
        with self.assertRaises(InvalidReferenceCode) : customers[0].deposit({'reference_code': 'wrong reference code', 'amount': 10})


if __name__ == '__main__':
    unittest.main()