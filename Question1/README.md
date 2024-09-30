# Z- Algorithm 

Z- Algorithm is a Exact pattern matching algorithm with time complexity of O(n) n=length of pattern + length of text.

## Steps to run

1. install argparse, if not present.
```
pip install argparse
```
2. clone or download the repository. To clone open the command line and run the below command.
```
git clone https://github.com/preethi1516/CompBioAssignment1.git
```

3. Move to the cloned/downloaded directory.
```
cd /pathWhereItWasCloned/zAlgo
```

4. Run the python file to get the result both in standard output as-well into a "sol_{Input Number}" result file. Pass the input file as arguments, below code has 2 example, default input is "sample_0".
```
# Default runs with sample_0
python3 exactPatternMatching.py 

# to test sample_1
python3 exactPatternMatching.py --input sample_1

# to test sample_2
python3 exactPatternMatching.py --input sample_2
```

>[!NOTE]
>Given that the input file has format "sample_{Any Number}", the code will automatically save it to a file named "sol_{Input Number}" [x can be any value, it will be parsed in the code].

>[!TIP]
>If you want to give any other input apart from the ones present in the samples folder, please add your test file into the samples folder in the format "sample_{Any Number}", for the code to work. 

