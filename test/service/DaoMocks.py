class DaoWithMatchingBddResult:

    def __init__(self, fibonacci_mock_return) -> None:
        self.fibonacci_mock_return = fibonacci_mock_return
        super().__init__()

    def get_fibonacci_number(self, number):
        return self.fibonacci_mock_return

    def get_last_two_documents(self):
        return [None]

    def persist_fibonacci_number(self, number):
        return None

    def find_inferior_fibonacci_number(self, number):
        return None

    def find_superior_fibonacci_number(self, number):
        return None


class DaoWithMatchingBddBoundaries:

    def __init__(self, inferior_number, superior_number) -> None:
        self.inferior_number = inferior_number
        self.superior_number = superior_number
        super().__init__()

    def get_fibonacci_number(self, number):
        return None

    def get_last_two_documents(self):
        return None

    def find_inferior_fibonacci_number(self, number):
        return self.inferior_number

    def find_superior_fibonacci_number(self, number):
        return self.superior_number


class DaoWithNoBddResults:

    def __init__(self, dict_mock) -> None:
        self.dict_mock = dict_mock
        super().__init__()

    def get_fibonacci_number(self, number):
        return None

    def get_last_two_documents(self):
        return self.dict_mock

    def persist_fibonacci_number(self, number):
        return None

    def find_inferior_fibonacci_number(self, number):
        return None

    def find_superior_fibonacci_number(self, number):
        return None
