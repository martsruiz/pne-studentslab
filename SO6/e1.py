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


s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
