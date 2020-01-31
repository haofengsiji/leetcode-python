def flatten(nested):
    for sublist in nested:
        for element in sublist: 
            return element

if __name__ == "__main__":
    nested = [[1, 2], [3, 4], [5]]
    print(flatten(nested))

