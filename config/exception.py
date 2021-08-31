class InvalidAmount(Exception):
    """Exception raised when the amount is invalid"""
    
    def __init__(self, message="Invalid Amount"):
        self.message = message
        super().__init__(self.message)


class InvalidPortfolio(Exception):
    """Exception raised when the portfolio does not exist"""
    
    def __init__(self, message="Invalid number of Portfolios"):
        self.message = message
        super().__init__(self.message)

class DuplicateDepositPlan(Exception):
    """Exception raised when the deposit plan already exists"""
    
    def __init__(self, message="Duplicate Deposit Plans Detected"):
        self.message = message
        super().__init__(self.message)

class MaximumDepositPlanExceeded(Exception):
    """Exception raised when the deposit plan exceeds the maximum allowed"""

    def __init__(self, message="Maximum allowed Deposit Plan is 2"):
        self.message = message
        super().__init__(self.message)

class InvalidReferenceCode(Exception):
    """Exception raised when the reference code is invalid"""

    def __init__(self, message="Invalid Reference Code"):
        self.message = message
        super().__init__(self.message)

class InSufficientAmount(Exception):
    """Exception raised when the amount is not sufficient"""
    
    def __init__(self, message="Insufficient Amount"):
        self.message = message
        super().__init__(self.message)


class InvalidTargetAmount(Exception):
    """Exception raised when the target amount is 0"""
    
    def __init__(self, message="Invalid Target Amount. Expected amount should be higher than 0"):
        self.message = message
        super().__init__(self.message)