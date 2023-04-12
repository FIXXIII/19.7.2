def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid

    return low


def sort_list(lst):
    for i in range(len(lst)):
        min_idx = i
        for j in range(i + 1, len(lst)):
            if lst[min_idx] > lst[j]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst


def main():
    user_input = input("Введите последовательность чисел через пробел: ")
    try:
        num_list = [int(num) for num in user_input.split()]
    except ValueError:
        print("в последовательности присутствуют нечисловые значения")
        return

    user_num = input("Введите любое число: ")
    try:
        user_num = int(user_num)
    except ValueError:
        print("введено нечисловое значение")
        return

    sorted_list = sort_list(num_list)

    pos = binary_search(sorted_list, user_num)

    if pos == len(sorted_list):
        print("Заданное число больше всех чисел в последовательности")
    elif sorted_list[pos] == user_num:
        print(f"Заданное число находится на позиции {pos}")
    else:
        print(f"Заданное число находится между позициями {pos - 1} и {pos}")


if __name__ == '__main__':
    main()
