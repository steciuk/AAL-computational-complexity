import argparse
import time
import synthetic
import matplotlib.pyplot as plt
from hash import HashTable


def words_ready_mode(file_in, file_del=None):
    words = synthetic.read_file(file_in)
    print(words)

    size = input("How many lists should be in the hashmap?: ")
    try:
        size = int(size)
    except ValueError as e:
        print("ERROR: Invalid value was passed to the program.")
        return -1

    hash_table = HashTable(size)
    hash_table.add_all(words)
    for arr in hash_table.array:
        print(arr)

    if file_del is None:
        answer = input("You did not specify .txt file with words to delete. "
                       "Should I use passed in words instead? [Y/N]: ")
        if answer == 'y' or answer == 'Y':
            for word in words:
                hash_table.delete_all(word)
    else:
        words = synthetic.read_file(file_del)
        for word in words:
            hash_table.delete_all(word)

    for arr in hash_table.array:
        print(arr)


def generation_mode(file_in, num, seed, file_del=None):
    words = synthetic.words(file_in, num, seed)

    size = input("How many lists should be in the hashmap?: ")
    try:
        size = int(size)
    except ValueError as e:
        print("ERROR: Invalid value was passed to the program.")
        return -1

    hash_table = HashTable(size)
    begin = time.perf_counter()
    hash_table.add_all(words)
    end = time.perf_counter()
    print("Adding time [s]:", end - begin)

    begin = time.perf_counter()
    for word in words:
        hash_table.find(word)
    end = time.perf_counter()
    print("Enumerating time [s]:", end - begin)

    if file_del is None:
        answer = input("You did not specify .txt file with words to delete."
                       "Should I use generated words instead? [Y/N]: ")
        if answer == 'y' or answer == 'Y':
            begin = time.perf_counter()
            for word in words:
                hash_table.delete_all(word)
            end = time.perf_counter()
            print("Deletion time [s]:", end - begin)
    else:
        words = synthetic.read_file(file_del)
        begin = time.perf_counter()
        for word in words:
            hash_table.delete_all(word)
        end = time.perf_counter()
        print("Deletion time [s]:", end - begin)


def gen_step_mode(file_in, num, seed, file_del=None):
    size = input("How many lists should be in the hashmap?: ")
    step_val = input("Specify the step value (number of words generated additionally): ")
    try:
        size = int(size)
        step_val = int(step_val)
    except ValueError as e:
        print("ERROR: Invalid value was passed to the program.")
        return -1

    with_deletion = True
    if file_del is None:
        answer = None
        answer = input("You did not specify .txt file with words to delete."
                       "Should I use generated words instead? [Y/N]: ")
        if answer not in {'Y', 'y'}:
            with_deletion = False

    words_num = 0
    results = []
    while True:
        words_num += step_val
        if words_num > num:
            break
        print(words_num, " words")
        results.append(words_num)
        words = synthetic.words(file_in, words_num, seed)

        hash_table = HashTable(size)
        begin = time.perf_counter()
        hash_table.add_all(words)
        end = time.perf_counter()
        print("Adding time [s]:", end - begin)
        results.append(end - begin)

        begin = time.perf_counter()
        for word in words:
            hash_table.find(word)
        end = time.perf_counter()
        print("Enumerating time [s]:", end - begin)
        results.append(end - begin)

        if with_deletion is True:
            if file_del is not None:
                words = synthetic.read_file(file_del)

            begin = time.perf_counter()
            for word in words:
                hash_table.delete_all(word)
            end = time.perf_counter()
            print("Deletion time [s]:", end - begin)
            results.append(end - begin)

    plot_data(results, with_deletion)


def plot_data(data, with_deletion):
    i = 0
    modulo = 4 if with_deletion else 3
    name = []
    adding = []
    searching = []
    deleting = []

    for x in data:
        if i % modulo == 0:
            name.append(x)
        elif i % modulo == 1:
            adding.append(x)
        elif i % modulo == 2:
            searching.append(x)
        else:
            deleting.append(x)
        i += 1

    plt.plot(name, adding, label='adding')
    plt.plot(name, searching, label='searching')
    if with_deletion:
        plt.plot(name, deleting, label='deleting')

    plt.xlabel('liczba elementow')
    plt.ylabel('czas [s]')
    plt.legend()

    plt.show()


def setup_parser():
    hash_parser = argparse.ArgumentParser(description="Program which calculates time of adding,"
                                                      "enumerating and optionally deleting elements from hashmap "
                                                      "consisting of singly linked lists", add_help=False)
    group_help = hash_parser.add_argument_group()
    group_help.add_argument("-h", "--help", action="help", help="show this help message and exit")

    group_req = hash_parser.add_argument_group("required arguments")
    group_req.add_argument("-m", "--mode", type=int, choices=[1, 2, 3], required=True,
                           help="specifies the mode in which program will run; "
                                "1 - with words ready to use for testing, 2 - with automatic generation and analysis"
                                "3 - with automatic generation and analysis with step value; all modes ask the user "
                                "how many lists should the hash table have and if it should use the generated/passed in "
                                "words for deletion operation, additionally mode 3 asks for the step value")
    group_req.add_argument("-i", "--input", required=True,
                           help="input file with words (mode 1)/text sample to generate words (mode 2/3)")

    group_opt = hash_parser.add_argument_group('optional arguments')
    group_opt.add_argument("-d", "--delete", default=None,
                           help="input file with words for optional deleting from hashmap; if not specified, "
                                "program will ask if it should use generated/passed words instead")

    group_m = hash_parser.add_argument_group("mode 2/3 specific values")
    group_m.add_argument("-n", "--number", type=int, default=1000,
                         help="maximum number of words to generate (mode 2/3). Default value = 1000")
    group_m.add_argument("-s", "--seed", type=int, default=None,
                         help="seed for random words; if not passed, the seed is randomized")

    return hash_parser


if __name__ == "__main__":
    parser = setup_parser()
    args = parser.parse_args()

    if args.mode == 1:
        words_ready_mode(args.input, args.delete)
    elif args.mode == 2:
        generation_mode(args.input, args.number, args.seed, args.delete)
    else:
        gen_step_mode(args.input, args.number, args.seed, args.delete)

