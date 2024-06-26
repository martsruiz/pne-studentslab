from pathlib import Path
class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases = None):
        # Initialize the sequence with the value
        # passed as argument when creating the object

        if strbases == None:
            self.strbases = "NULL"
            print("NULL sequence created!")
        else:
            letters = strbases.count("A") + strbases.count("C") + strbases.count("T") + strbases.count("G")
            if len(strbases) != letters:
                print("INVALID sequence")
                self.strbases = "ERROR"
            else:
                print("New sequence created!")
                self.strbases = strbases


    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        if self.strbases == "ERROR" or self.strbases == "NULL":
            length = 0
        else:
            length = len(self.strbases)
        return  length

    def count_base(self, base):
        if self.strbases == "ERROR" or self.strbases == "NULL":
            seq = ""
        else:
            seq = self.strbases
        count = 0
        for i in seq:
            if i == base:
                count += 1

        return count


    def count(self):
        count_dic = {"A": 0,
                     "C": 0,
                     "G": 0,
                     "T": 0}
        if self.strbases != "ERROR" or self.strbases != "NULL":
            for a in self.strbases:
                if a in count_dic:
                    count_dic[a] += 1
        return count_dic

    def reverse(self) :
        if self.strbases == "ERROR":
            reverse_seq = self.strbases
        elif self.strbases == "NULL":
            reverse_seq = self.strbases
        else:
            reverse_seq = self.strbases[::-1]
        return reverse_seq


    def complement(self):
        dic = {"A": "T",
           "T": "A",
           "C": "G",
           "G": "C"}

        tmp = ""
        if self.strbases == "ERROR" or self.strbases == "NULL":
            tmp = self.strbases
        else:
            for i in self.strbases:
                if i in dic:
                    tmp += dic[i]
        return tmp



    def read_fasta(self, filename):
        file_contents = Path(filename).read_text()
        first_line = file_contents.find("\n")
        new_sequence = file_contents[first_line:]
        self.strbases = new_sequence.replace("\n", "")
        return  self.strbases


# --- Main program
"""s1 = Seq("AGTACACTGGT")
s2 = Seq("CGTAAC")

# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f"  Length: {s1.len()}")
print(f"Sequence 2: {s2}")
print(f"  Length: {s2.len()}")"""
