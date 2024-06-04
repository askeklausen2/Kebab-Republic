def readCSV(filepath: str):
    with open(filepath) as file:
        data = file.readlines()
        keys = enumerate(data.pop().split(","))
        kebabs = []
        for line in data:
            data_points = line.split(",")
            kebab = {}
            for key, i in keys:
                kebab[key] = data_points[i]
            kebabs.append(kebab)