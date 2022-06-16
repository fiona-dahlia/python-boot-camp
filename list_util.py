def two_sum(in_list, target):
    # print('test')
    target_numbers = []
    for num in in_list:
        # print(num)
        to_check = target - num
        if num in target_numbers:
            return True
        target_numbers.append(to_check)
    return False


if __name__ == '__main__':
    num_list = [3, 5, 1, 8, 7, 2]
    print(two_sum(num_list, 19))
