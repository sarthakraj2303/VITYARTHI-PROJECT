def readrow(filename):
    try:
        with open(filename) as f:
            rows = []
            for line in f:
                if line.strip():
                    value = line.strip().split(",")
                    rows.append(value)
            return rows
    except FileNotFoundError:
        return []

def addrow(filename, row):
    with open(filename, "a") as f:
        values = []
        for x in row:
            values.append(str(x))
        line = ",".join(values)
        f.write(line + "\n")