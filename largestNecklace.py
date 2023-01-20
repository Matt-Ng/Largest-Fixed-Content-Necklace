from collections import defaultdict

def createPartition(inputNums):
    # content inserted as a list
    diff = 0
    zeroes = int(inputNums[0])
    # partitions of zeroes are generated
    patterns = [["0"] for i in range(zeroes)]
    n = sum(inputNums)
    
    # two cases for multiwayPartition, if zeroes makes up most of list and otherwise
    if zeroes <= n/2:
        for i in range(len(inputNums) - 1, 0, -1):
            keeptrack = 0
            # place numbers between differentiated number and end of list
            for j in range(int(inputNums[i])):
                j%(len(patterns) - diff) + diff
                patterns[j%(len(patterns) - diff) + diff].append(str(i))
                keeptrack = j%(len(patterns) - diff ) + diff
            diff = keeptrack + 1 if (keeptrack + 1) < len(patterns) else diff
    else:
        # optimization for multiwayPartition
        j = n - zeroes
        patterns = [["0"] for i in range(j)]
        for i in range(zeroes - len(patterns)):
            patterns[i%len(patterns)].append("0")
        k = 0
        for i in range(len(inputNums) - 1, 0, -1):
            for l in range(inputNums[i]):
                patterns[k].append(str(i))
                k += 1

    # maps each partition to amount of occurances
    tableOfPatterns = defaultdict(int)
    # maps the original pattern to its occurances
    sortedListOfPatterns = []
    for pattern in patterns:
        strPattern = ''.join(pattern)
        tableOfPatterns[strPattern] += 1
    for key in tableOfPatterns:
        sortedListOfPatterns.append(str(key))
    sortedListOfPatterns.sort()
    newContent = []
    # create new pattern
    for i in range(len(sortedListOfPatterns)):
        newContent.append(tableOfPatterns[sortedListOfPatterns[i]])
    mapOfContent = {}
    # create a mapping of new symbols to the constituent pattern
    for i in range(len(sortedListOfPatterns)):
        mapOfContent[i] = sortedListOfPatterns[i]

    return newContent, mapOfContent
            
        

def construct(necklace, mapOfContent):
    # split into all patterns
    patterns = ["" for i in range(len(necklace))]
    for i in range(len(patterns)):
        # substitute every subbed symbol into its constituent pattern at this point in the recursion
        patterns[i] = str(mapOfContent[int(necklace[i])])
    resultNecklace = ""
    # reconstruct the necklace string
    for pattern in patterns:
        resultNecklace += str(pattern)
    return resultNecklace

def recurseNeck(content):
    # should return a hashmap containing a sorted list of the patterns and a map containing each pattern and the occurances
    newContent, mapOfContent = createPartition(content)
    # base case is if there is only one zero or if the only symbol is zero
    if len(newContent) == 1:
        newNecklace = "0" * newContent[0]
        return construct(newNecklace, mapOfContent)
    if newContent[0] == 1:
        newNecklace = "0"
        for i in range(len(newContent) - 1, 0, -1):
            for j in range(newContent[i]):
                newNecklace += str(i)
        return construct(newNecklace, mapOfContent)
    # return the necklace constructed when moving up call stack
    return construct(recurseNeck(newContent), mapOfContent)

def go():
    print("enter k: ")
    n = int(input())
    content = []
    for i in range(n):
        print("enter n for", i)
        curr = input()
        content.append(curr)
    if len(content) == 1:
        print('0'*content[0])
    else:
        observed = []
        for i in range(len(content)):
            for j in range(content[i]):
                observed.append(str(i))
        observed = observed[::-1]
        print("content:", observed)
        print(recurseNeck(content))

go()