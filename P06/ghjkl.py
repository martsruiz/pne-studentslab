from Seq1 import Seq

def info_response(msg):
    s1 = Seq(str(msg))
    length = s1.len()
    base_counts = s1.count()

    total_bases = sum(base_counts.values())

    # Construye una cadena de texto formateada con la longitud y los conteos de bases
    result_str = f"Length: {length}\n"
    for base, count in base_counts.items():
        percentage = round(count / total_bases * 100, 1)
        result_str += f"{base}: {count} ({percentage}%)\n"

    return result_str

print(info_response("ATGTAA"))


