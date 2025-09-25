


class Loan:
    def __init__(self, id_loan, date_loan , date_return , friend , object, state):
        self._id_loan = id_loan
        self._date_loan = date_loan
        self._date_return = date_return
        self._friend = friend
        self._object = object
        self._state = state

    @property
    def id_loan(self):
        return self._id_loan

    @id_loan.setter
    def id_loan(self, id_loan):
        self._id_loan = id_loan

    @property
    def date_loan(self):
        return self._date_loan

    @date_loan.setter
    def date_loan(self, date_loan):
        self._date_loan = date_loan

    @property
    def date_return(self):
        return self._date_return

    @date_return.setter
    def date_return(self, date_return):
        self._date_return = date_return

    @property
    def friend(self):
        return self._friend

    @friend.setter
    def friend(self, friend):
        self._friend = friend

    @property
    def object(self):
        return self._object

    @object.setter
    def object(self, object):
        self._object = object

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state
