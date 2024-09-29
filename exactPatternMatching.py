import argparse

################# Z- VALUES #####################
def zValues(patternText, z):
    n = len(patternText)
    left, right, k,match,mismatch= 0,0,0,0,0
    
    for current in range(1, n):
        
        # CASE 1
        if current > right:

            left, right = current, current
            while right < n and patternText[right - left] == patternText[right]:
                right += 1
                match+=1
            if right < n and patternText[right - left] != patternText[right]:
                mismatch+=1
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
                    match+=1
                if right < n and patternText[right - left] != patternText[right]:
                    mismatch+=1
                z[current] = right - left
                right -= 1
    
    return match,mismatch

################# Z- ALGORITHM #####################
def zAlgorithm(text, pattern, resultNum):

    patternText = pattern + "$" + text
    z = [0] * len(patternText)
    match,mismatch=zValues(patternText, z)

    output_file_path = f'sol_{resultNum}'
    with open(output_file_path, 'w') as output_file:
        for i in range(len(patternText)):

            if z[i] == len(pattern):
                 # For terminal display
                print(i - len(pattern))

                # Written to the file
                output_file.write(f"{i - len(pattern)}\n")
    
        # For terminal display
        print(f"Number of comparisons: {match+mismatch}"  )
        print(f"Number of matches: {match}")
        print(f"Number of mismatches: {mismatch}")
        
        # Written to the file
        output_file.write(f"Number of comparisons: {match+mismatch}\n")
        output_file.write(f"Number of matches: {match}\n")
        output_file.write(f"Number of mismatches: {mismatch}\n")

#################### MAIN ##################
if __name__ == "__main__":

    # parsing the input
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default='sample_0')
    args = parser.parse_args()
    inputPath =f'samples/{args.input}'

    # reading the input 
    with open(inputPath, 'r') as input:
        inputParsed=input.readlines()
        text=inputParsed[0].strip()
        pattern=inputParsed[1].strip()
    
    # parsing the sample number to attach to the output
    sampleNum=inputPath.split('_')

    # calling the zalgorithm
    zAlgorithm(text, pattern,sampleNum[-1])
