def fib_nums(n):
    fib_res = [0, 1, 1]
    res = []
    main_count = 0
    counted_el = 0

    for i in range(3, n ** 2):
        tmp = fib_res[i - 1] + fib_res[i - 2]
        fib_res.append(tmp)

    while main_count != n:

        if fib_res[counted_el] % 2 == 0:
            res.append(fib_res[counted_el])
            main_count += 1
        counted_el += 1

    result = list(map(str, res))

    return ' '.join(result)


numbers = fib_nums(4)
print(numbers)
