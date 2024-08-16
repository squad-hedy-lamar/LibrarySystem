class Loan:
    def __init__(self, copy: Copy, user: User, borrow_date: datetime, return_date: Optional[datetime] = None):
        self.copy = copy
        self.user = user
        self.borrow_date = borrow_date
        self.return_date = return_date

    @property
    def status(self):
        if self.return_date is None:
            return "Borrowed"
        return "Returned"