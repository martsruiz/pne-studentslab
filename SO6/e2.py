class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):

        valid_sequence = ["A","C","T","G"]
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

def print_seqs(seq_list):
    for i, seq in enumerate(seq_list):
        print(f"Index: {i}, Length: {seq.len()}, Sequence: {seq}")

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seqs(seq_list)
