import sys

# get the dict file into a dict - done
word_dict = {}
dict_file = open("diction10k.txt", "r")
for line in dict_file:
    if line not in word_dict:
        word_dict[line.strip()] = line.strip()
dict_file.close()

def decode(encoded_string):
    encode_len = len(encoded_string)
    decode_array = [None] * (encode_len + 1)
    decode_array[encode_len] = []
    for i in range(encode_len - 1, -1, -1):
        words = []
        # starting at the end of the string, we build a list of all words contained in the encoded string
        for j in range(i, encode_len):
            word = encoded_string[i:j + 1]
            if (word in word_dict) and (decode_array[j + 1] is not None):
                words.append(word)
                words.extend(decode_array[j + 1])
        if len(words) > 0:
            decode_array[i] = words

    if decode_array[0] is None:
        return "NO, cannot split.\n"
    else:
        decode_string = []
        # since we gather them in order, we just need to extract a few of the elements from the list of all word
        # subsequences up until the point where the words, when joined, match the initial string
        for i in decode_array[0]:
            decode_string.append(i)
            if "".join(decode_string) == encoded_string:
                break
        return "YES, can split.\n" + " ".join(decode_string)


# evaluate stdin
n = 1
next(sys.stdin)
for line in sys.stdin:
    print(f'phrase {n} \n{line}')
    line_decoded = decode(line.strip())
    print(f"output {n}\n{line_decoded}\n")

    n += 1
