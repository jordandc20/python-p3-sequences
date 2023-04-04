#!/usr/bin/env python3


def print_fibonacci(length):
    sequence = []
    if length > 0:
        sequence.append(0)
        if length >1:
            sequence.append(1)
            if length > 2:
                i = 2
                while i < length:
                    last = sequence[-1]
                    second_last = sequence[-2]
                    new_int = last+second_last
                    sequence.append(new_int)
                    i += 1

                # ###instead of while could do a range for loop. can also use i-1  or -1
                # for i in range(2, length):
                #     sequence.append(
                #         sequence[i - 1] + sequence[i - 2])    
   
    print(sequence)


print_fibonacci(10)    


# def print_fibonacci(length):
#     sequence = []
#     if length == 0:
#         pass
#     elif length == 1:
#         sequence = [0]
#     elif length == 2:
#         sequence = [0,1]
#     elif length > 2:
#         i = 2
#         sequence = [0,1]
#         while i < length:
#             last = sequence[-1]
#             second_last = sequence[-2]
#             new_int = last+second_last
#             sequence.append(new_int)
#             i += 1
   
#     print(sequence)


