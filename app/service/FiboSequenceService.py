from app.utils.logger_factory import create_logger


class FiboSequenceService:

    def __init__(self, dao) -> None:
        self.dao = dao
        self.logger = create_logger()
        super().__init__()

    def fetch_closest(self, number):
        # request number is in fibonacci's sequence and already in db
        if self.dao.get_fibonacci_number(number) is not None:
            return number
        # request number is not in known fibonacci's sequence, but superior and inferior fibonacci's number are in db
        inferior_fibonacci_number = self.dao.find_inferior_fibonacci_number(number)
        superior_fibonacci_number = self.dao.find_superior_fibonacci_number(number)
        if inferior_fibonacci_number is not None and superior_fibonacci_number is not None:
            return self.calculate_closest(number, [inferior_fibonacci_number, superior_fibonacci_number])
        # request number may be in sequence, but sequence is not extanded enough. Need calculate more.
        last_sequence_dicts = self.dao.get_last_two_documents()
        new_sequence_chunk = self.generate_new_chunk(number,
                                                     [last_sequence_dicts[0]['value'], last_sequence_dicts[1]['value']])
        # request number is in new fibonacci's sequence chunk
        if number in new_sequence_chunk:
            return number
        # request number is not a fibonacci's number, need calculate closest from sequence chunk
        return self.calculate_closest(number, new_sequence_chunk[-2:])

    def generate_new_chunk(self, request_number, new_sequence_chunk):
        new_fibonacci_number = new_sequence_chunk[-2] + new_sequence_chunk[-1]
        new_sequence_chunk.append(new_fibonacci_number)
        self.dao.persist_fibonacci_number(new_fibonacci_number)
        if new_fibonacci_number == request_number or new_fibonacci_number > request_number:
            return new_sequence_chunk
        return self.generate_new_chunk(request_number, new_sequence_chunk)

    @staticmethod
    def calculate_closest(number, boundaries_chunk):
        x = boundaries_chunk[-2]
        y = boundaries_chunk[-1]
        if number - x > y - number:
            return y
        return x
