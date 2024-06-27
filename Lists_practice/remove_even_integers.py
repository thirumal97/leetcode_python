def remove_even(lst):
    new_lst = []
    # Replace this placeholder return statement with your code
    for i in range(len(lst)):
        #print(lst[i])
        if lst[i] % 2 != 0:
            new_lst.append(lst[i])
    return new_lst


def remove_even_actual_sol(lst):
    odds = []

    for number in lst:  
        # Check if the item in the list is not even
        if number % 2 != 0:
            odds.append(number)  # // If it isn't even, append it to the odds list

    return odds

def remove_even_actual_sol_01(lst):
    # List comprehension to iterate over list and add to a new list if not even
    return [number for number in lst if number % 2 != 0]

def main():

    inputs = [
            [3, 2, 41, 3, 34],
            [-5, -4, -3, -2, -1],
            [-1, 2, 3, -4, -10],
            [1, 2, 3, 7],
            [2, 4, 6, 8, 10],

    ]

    for i in range(len(inputs)):
        print(i + 1, ".\tInput list: ", inputs[i], sep="")
        print("\n\tFinal list: ", remove_even(inputs[i]), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()