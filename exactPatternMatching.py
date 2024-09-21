import argparse

################# Z- VALUES #####################
def zValues(patternText, z):
    n = len(patternText)
    left, right, k = 0, 0, 0
    
    for current in range(1, n):
        
        # CASE 1
        if current > right:

            left, right = current, current
            while right < n and patternText[right - left] == patternText[right]:
                right += 1
            z[current] = right - left
            right -= 1
        
        # CASE 2
        else:

            k = current - left
            if z[k] < right - current + 1:
                z[current] = z[k]

            else:

                left = current
                while right < n and patternText[right - left] == patternText[right]:
                    right += 1
                z[current] = right - left
                right -= 1

################# Z- ALGORITHM #####################
def zAlgorithm(text, pattern, resultNum):

    patternText = pattern + "$" + text
    z = [0] * len(patternText)
    zValues(patternText, z)

    output_file_path = f'sol_{resultNum}'
    with open(output_file_path, 'w') as output_file:
        for i in range(len(patternText)):

            if z[i] == len(pattern):
                print(i - len(pattern))
                output_file.write(f"{i - len(pattern)}\n")

#################### MAIN ##################
if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default='sample_0')
    args = parser.parse_args()
    inputPath =f'samples/{args.input}'

    with open(inputPath, 'r') as input:
        inputParsed=input.readlines()
        text=inputParsed[0].strip()
        pattern=inputParsed[1].strip()
    
    sampleNum=inputPath.split('_')
    zAlgorithm(text, pattern,sampleNum[-1])