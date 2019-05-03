import sys

## take a list of view fragments, and merge them together to get rid of any overlapping fragments, 
# as they distract from the UVT metric

# this is the primary solution because it is much more efficient in the result object it creates, though it involves more code
def solutionPrimary(data):
    sortedData = sorted(data, key=lambda tup: tup[0])
    merged = []
    totalUVT = 0
    for higher in sortedData:
        if not merged:
            merged.append(higher)
        else:
            lower = merged[-1]
            if higher[0] <= lower[1]:
                upper_bound = max(lower[1], higher[1])
                merged[-1] = (lower[0], upper_bound)
            else:
                merged.append(higher)
    
    # you end with a new list of unique (non-overlapping) view fragments, then they are converted
    # into a UVT metric
    for interval in merged:
        totalUVT += interval[1] - interval[0]
    return totalUVT



## this is a solution that builds a list of unique numbers that make up the ranges inside each view fragment
# the final list includes a set of numbers that represent every ms that the video was watched
# the length of the list represents the UVT of all fragments, and consequently the solution

# this is the secondary solution because it is much less efficient but still correct, suitable as a testing algorithm
# it eventually generates a list of every millisecond of time that was watched, which can grow quite large depending on view times
def solutionSecondary(data):
    solution = []
    for i in data: 
        solution = solution + [x for x in range(i[0],i[1]) if x not in solution]
    solution.sort()
    return len(solution)



# maps the input file text content into an array of tuples, where each tuple represents a
# 'view fragment', simply two timestamps represented as: (START_TIMESTAMP, END_TIMESTAMP)
def readInputFile(filename):
    file = open(filename, 'r')
    mappedData = [tuple(map(int, x.split('-'))) for x in file.read().split(', ')]
    return mappedData

# a function to take the UVT result and display it a little bit nicer
def convertTime(ms):
    millis = int(ms)
    seconds=(millis/1000)%60
    seconds = int(seconds)
    minutes=(millis/(1000*60))%60
    minutes = int(minutes)
    hours=(millis/(1000*60*60))%24

    print ("UVT (Unique View Time) %d:%d:%d" % (hours, minutes, seconds))

def main():
    if len(sys.argv) < 2:
        print("An argument file was not submitted, exiting program.")
        sys.exit(1)
    
    input = readInputFile(sys.argv[1])
    
    uvt1 = solutionPrimary(input)
    uvt2 = solutionSecondary(input)

    if (uvt1 == uvt2):
        print('The calculated UVT matched across both algorithms')
        convertTime(uvt1)
    else:
        print('Oops, the calculated UVT\'s varied between each algorithm')
        convertTime(uvt1)
        convertTime(uvt2)

main()