from Seq1 import Seq
def info_response(msg):
    seq = msg.replace("INFO ", "")
    sequence = Seq(seq)
    print(f" Sequence: {sequence}\n Total length: {sequence.len()}\n {sequence.count()} ")
    return sequence

info_response("INFO ATATACT")


