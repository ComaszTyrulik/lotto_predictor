class DataConverter:
    MIN_NUMBER_POSITION = 1
    MAX_NUMBER_POSITION = 6

    @staticmethod
    def get_numbers_as_list(data, sort=True):
        numbers_list = []
        for row in data:
            numbers_list.extend(row[2:len(row)])
        if sort:
            numbers_list.sort()

        return numbers_list

    def get_numbers_at_position_as_list(self, position, data, sort=True):
        if position > self.MAX_NUMBER_POSITION:
            raise ValueError(
                'The maximum available position is' + str(self.MAX_NUMBER_POSITION) + ' ' + str(position) + ' given'
            )
        elif position < self.MIN_NUMBER_POSITION:
            raise ValueError(
                'The minimum available position is' + str(self.MIN_NUMBER_POSITION) + ' ' + str(position) + ' given'
            )

        numbers_list = []
        for row in data:
            numbers_list.append(row[position+1])

        if sort:
            numbers_list.sort()

        return numbers_list

    @staticmethod
    def get_numbers_sets(data):
        numbers_sets = []
        for row in data:
            numbers_sets.append(row[2:len(row)])

        return numbers_sets

    @staticmethod
    def get_draws_count(data):
        return len(data)
