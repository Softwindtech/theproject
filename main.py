from usgs import printResults

result = printResults()

if __name__ == "__main__":
    length = len(result)
    for x in range(length): 
        print (result[x])