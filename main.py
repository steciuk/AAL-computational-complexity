import argparse
import synthetic
from hash import HashTable, LinkedList

def words_ready_mode(file_in, file_del = None):
    words = synthetic.read_file(file_in)
    print(words)

    size = input("How many lists should be in the hashmap?: ")
    hash_table = HashTable(int(size))
    hash_table.add_all(words)

    if file_del is not None:
        print("to implement")

    for arr in hash_table.array:
        print(arr)

def generation_mode(file_in, num, seed, file_del = None):
    words = synthetic.words(file_in, num, seed)
    print(words)

    size = input("How many lists should be in the hashmap?: ")
    hash_table = HashTable(int(size))
    hash_table.add_all(words)

    if file_del is not None:
        print("to implement")

    for arr in hash_table.array:
        print(arr)

def setup_parser():
    parser = argparse.ArgumentParser(description="Program which calculates time of adding, enumerating and optionally "
                                                 "deleting elements from hashmap consisting of singly linked lists",
                                     add_help=False)
    group_help = parser.add_argument_group()
    group_help.add_argument("-h", "--help", action="help", help="show this help message and exit")

    group_req = parser.add_argument_group("required arguments")
    group_req.add_argument("-m", "--mode", type=int, choices=[1, 2, 3, 4], required=True,
                           help="specifies the mode in which program will run; 1 - with words ready to use, "
                                "2 - with automatic generation, 3 - with words ready to use and analysis, "
                                "4 - with automatic generation and analysis")
    group_req.add_argument("-i", "--input", required=True,
                           help="input file with words (mode 1/3)/text sample to generate words (mode 2/4)")

    group_opt = parser.add_argument_group('optional arguments')
    group_opt.add_argument("-d", "--delete", default=None,
                           help="input file with words for optional deleting from hashmap")

    group_m = parser.add_argument_group("mode 2/4 specific values")
    group_m.add_argument("-n", "--number", type=int, default=1000,
                         help="number of words to generate (mode 2/4). Default value = 1000")
    group_m.add_argument("-s", "--seed", type=int, default=None,
                         help="seed for random words; if not passed, the seed is randomized")

    return parser

if __name__ == "__main__":
    parser = setup_parser()
    args = parser.parse_args()

    if args.mode == 1 or args.mode == 3:
        words_ready_mode(args.input, args.delete)
    else:
        generation_mode(args.input, args.number, args.seed, args.delete)
