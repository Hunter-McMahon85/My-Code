def max_run(lst: list) -> int:
    """
    finds the max run of same numbers in a row in a given list
    :param lst: (list) the list were finidng runs of numbers in
    :return: (int) the length of the longest run
    >>> max_run([-2, 0, 0, 1, 2, 1, 1, 1, 0])
    3
    """
    # TODO: implement the function, include a proper docstring
    # Optionally, include doctests (not unittests)
    longest_run = 0
    for i in range(len(lst)):
        run_is_on = True
        tracker = 0
        run_counter = 0
        while run_is_on:
            if i + tracker < len(lst):
                if lst[i+ tracker] == lst[i]:
                    run_counter += 1
                    tracker += 1
                else:
                    run_is_on = False
            else:
                run_is_on = False
        print(run_counter, i, tracker)
        if run_counter > longest_run:
            longest_run = run_counter
    return longest_run