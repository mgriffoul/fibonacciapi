from tinydb import TinyDB, Query


class Dao:
    db = None

    def __init__(self) -> None:
        self.db = TinyDB("./app/bdd/fibonacci_sequence.json")
        super().__init__()

    def init_db(self):
        if len(self.db.all()) < 2:
            self.db.purge_tables()
            self.db.insert({'value': 0})
            self.db.insert({'value': 1})

    def get_fibonacci_number(self, number):
        number_query = Query()
        result = self.db.get(number_query.value == number)
        return result

    def get_last_two_documents(self):
        db_len = len(self.db)
        dict1 = self.db.all()[db_len - 2]
        dict2 = self.db.all()[db_len - 1]
        return [dict1, dict2]

    def persist_fibonacci_number(self, number):
        self.db.insert({'value': number})

    def find_inferior_fibonacci_number(self, number):
        inferior_query = Query()
        results = self.db.search(inferior_query.value < number)
        number_results = []
        for dict_result in results:
            number_results.append(dict_result['value'])
        if not number_results:
            return None
        return max(number_results)

    def find_superior_fibonacci_number(self, number):
        superior_query = Query()
        results = self.db.search(superior_query.value > number)
        number_results = []
        for dict_result in results:
            number_results.append(dict_result['value'])
        if not number_results:
            return None
        return min(number_results)
