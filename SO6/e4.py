import termcolor


class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):

        valid_sequence = ["A", "C", "T", "G"]
        for i in strbases:
            if i not in valid_sequence:
                strbases = "ERROR"
            else:
                pass
        if strbases == "ERROR":
            print("ERROR!!")
        else:
            print("New sequence created!")

        self.strbases = strbases

    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)


def print_seqs(seq_list, colour):
    for i, seq in enumerate(seq_list):
        termcolor.cprint(f"Index: {i}, Length: {seq.len()}, Sequence: {seq}", colour)


def generate_seqs(pattern, number):
    seq_list = []
    for i in range(1, number + 1):
        seq_list.append(Seq(pattern * i))
    return seq_list


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1, "blue")

print()
print("List 2:")
print_seqs(seq_list2, "green")