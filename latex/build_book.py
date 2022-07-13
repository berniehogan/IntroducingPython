import glob
import os
from pathlib import Path 
from os import sep as ossep

def ignore_colab(text):

    return text
    
def convert_notebooks(pattern="*",output_dir="."):
    
    for file in glob.glob(pattern):
        os.system(f'jupyter nbconvert --to latex {file} --no-prompt --output-dir {output_dir} ')
    
    return


def main(nbconvert=True,texclean=True,makelatex=True,jobname="book"): 
    
    if nbconvert: 
        print("NBCONVERT - Started.")
        convert_notebooks("../chapters/Ch.*.ipynb","tex/")
        convert_notebooks("../exercises/Ch.*.ipynb","tex/")
        
        print("NBCONVERT - Done.")

    if texclean:
    
        for file in glob.glob("tex/Ch.*.tex"):
            blob = open(file).read()
            
            blob_split = blob.split("maketitle",1)
            if len(blob_split) > 1:
                blob = blob_split[1].split("% Add a bibliography")[0]
        
            with open(file,'w') as fileout: 
                fileout.write(blob)
        
        print("Tex files cleaned")

        
    if makelatex: 
        os.chdir("tex/")
        os.system(f'xelatex -jobname {jobname} book.tex')
        os.system(f'biber -jobname {jobname} book.tex')
        os.system(f'xelatex -jobname {jobname} book.tex')
        os.system(f'xelatex -jobname {jobname} book.tex')

if __name__ == "__main__":
    main(nbconvert=True,
         texclean=True,
         makelatex=True,
         jobname = "IntroducingPython")
 