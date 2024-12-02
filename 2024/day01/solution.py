class mylists:
    @staticmethod
    def total_distance(left_list, right_list):
        return sum(
            mylists.difference(left_list[i], right_list[i])
            for i in range(len(left_list))
        )

    @staticmethod
    def difference(first_number, second_number):
        return abs(first_number - second_number)
    
    @staticmethod
    def similarity(left_number, right_list):
        return left_number * right_list.count(left_number)
    
    @staticmethod
    def total_similarity(left_list, right_list):
        return sum(
            mylists.similarity(left_list[i], right_list)
            for i in range(len(left_list))
        )


if __name__ == "__main__":
    left_list = []
    right_list = []
    with open("input.txt") as f:
        for line in f.readlines():
            left, right = line.split('   ')
            left_list.append(int(left))
            right_list.append(int(right))

    print(mylists.total_distance(sorted(left_list), sorted(right_list)))
    print(mylists.total_similarity(sorted(left_list), sorted(right_list)))