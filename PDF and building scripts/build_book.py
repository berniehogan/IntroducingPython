# check within each subdirectory for the single ipynb file. 

# Use nbconvert to convert to .tex 
# strip out the preambles 
# add a single preamble to a main text file 
# run the build script on the file. 

import glob
import os
from pathlib import Path 
from os import sep as ossep

# Because it seems that multi-character emoji finding in Python is still 
# not good enough. So this list gets edited by hand and should be equal to
# or a superset of the total emojis in the book. 

# The emojis have to be sorted so that find and replacing a single character
# doesn't mess up the multicharacter ones. Luckily we don't have to contend with
# multicharacter skin tones, but at that point we simple must build a multi-emoji
# parser. 



def convert_notebooks(pattern="*",output_dir="."):
    
    for file in glob.glob(pattern):
        os.system(f'jupyter nbconvert --to latex {file} --no-prompt --output-dir {output_dir} ')
    
    return


def main(nbconvert=True,texclean=True,makelatex=True,jobname="book"): 
    
    if nbconvert: 
        print("NBCONVERT - Started.")
        convert_notebooks("./chapters/Ch.*.ipynb","./tex/chapters/")
        print("NBCONVERT - Done.")

    if texclean:
    
        for file in glob.glob("./tex/chapters/Ch.*.tex"):
            blob = open(file).read()
            
            blob_split = blob.split("maketitle",1)
            if len(blob_split) > 1:
                blob = blob_split[1].split("% Add a bibliography")[0]
        
            with open(file,'w') as fileout: 
                fileout.write(blob)
        
        print("Tex files cleaned")

        
    if makelatex: 
        os.chdir("tex/chapters/")
        os.system(f'xelatex -jobname {jobname} book.tex')
        os.system(f'biber -jobname {jobname} book.tex')
        os.system(f'xelatex -jobname {jobname} book.tex')
        os.system(f'xelatex -jobname {jobname} book.tex')

if __name__ == "__main__":
#     1/0
    main(nbconvert=False,texclean=True,jobname = "IntroducingPython")
 