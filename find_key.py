# given a dictionary in data and a value, return the key
def find_key(data, value):
    chunk1 = data.keys()
    chunk2 = data.values()
    maxValue = max(chunk2)
    maxKey = list(data.keys())[list(data.values()).index(maxValue)]
    return maxValue
