from usgs import printResults

result = printResults(4)

if __name__ == "__main__":
    length = len(result)
    for x in range(length): 
        print (result[x])