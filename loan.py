from datetime import datetime

class Loan:
    def __init__(self, copy, user, borrow_date, return_date):
        self.copy = copy
        self.user = user
        self.borrow_date = borrow_date
        self.return_date = return_date

    @property
    def status(self):
        if self.return_date is None:
            return "Borrowed"
        return "Returned"