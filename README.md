# pdfWidener

pdfWidener is a simple program used to double the width of pages in a PDF. 
Professors often like to fill the presentation-slides full of text and figures, so for people using tablets to take notes on the slides it's helpful to have some space next to the slides.
This simple script doubles the width of the pdf-pages.

## Setup

You need to be in an environment with ```PyPDF2```
```bash
pip install PyPDF2
```

## Usage
Place all files you want to widen in the same folder as ```main.py```, and then run
```bash
python main.py
```
It will create copies of the files with the filename "..._wide.pdf".

### Executable
The python script can be created into an executable using [PyInstaller](https://pip.pypa.io/en/stable/). This way, the program can be run by just "double-clicking" the executable, instead of running the script everytime.
