# Typeracer hack
This is a python script that takes a screenshot and after you select a text, using tesseract it will auto speed write that text when you click (note after selecting it will take 2 seconds(configurable) to detect when you click
# Installation
To use this script, you'll need to clone this repository to your local machine using the following command:

```git clone https://github.com/BainBan/typeracer-hack.git```

### You'll also need to install the following dependencies using either of the following methods:

**Method 1: Install the dependencies using pip:**

```pip install -r requirements.txt```
**and also tesseract from sourceforge https://sourceforge.net/projects/tesseract-ocr-alt/files/**

**Method 2: Install the dependencies manually:**

**Python 3**
**keyboard library (can be installed via pip: pip install keyboard but should already be installed)**
**numpy library (can be installed via pip: pip install numpy) and so on with opencv_python, pynput and pytesseract and also tesseract from sourceforge https://sourceforge.net/projects/tesseract-ocr-alt/files/**
# Usage
Launch the script by running python script.py in your terminal.
The script will take a screenshot and you need to select the text you want to automatically write .
then swap fast to the typeracer window I have given you 2 seconds(configurable) then it will say 'time done' in the console, you need to click so the text starts writing. The default speed is very fast you can change that in line 21 from 0.01 I noticed 0.10 is the minimum so you don't need to do the verification thing. Still very fast. ALSO DON'T FORGET TO PUT THE CORRECT PATHS IN LINE 7, WHERE YOU NEED TO PUT TESSERACT.EXE WHERE YOU INSTALLED IT (IN PROGRAM FILES TESSERACT-OCR TESSERACT.EXE THAT'S THE DEFAULT PATH AND ALSO IN LINE 12 AND 13 IT SHOULD BE THE SAME PATH OF WHERE THE SCREENSHOT WOULD SAVE

https://github.com/BainBan/typeracer-hack/assets/111044589/e5a11b98-5870-4a0d-9374-691f5eaa1c2b



# Configuration
yes. 

# Contributing
Contributions are welcome! If you find a bug or have an idea for a new feature, feel free to submit an issue or a pull request.
This took me like an hour to make so finding bugs I don't think will be hard
