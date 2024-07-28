# Project Overview
This project is a Python-based tool that converts the text content of a PDF file into spoken words. It reads a PDF file, extracts text from each page, and uses a text-to-speech engine to vocalize the text. This can be particularly useful for those who prefer listening to reading or for accessibility purposes.

## Features
- PDF Reading: Reads and extracts text from all pages of a given PDF file.
- Text-to-Speech Conversion: Converts the extracted text into speech using the pyttsx3 library.
- Page Announcements: Announces the end of each page during the speech output.
## Technology Stack
- Programming Language: Python
- Libraries:
  - pyttsx3 for text-to-speech conversion
  - PyPDF2 for reading and extracting text from PDF files
## Setup Instructions
### Prerequisites
- Python 3.8+
- Required Python libraries: pyttsx3, PyPDF2
## Installation
1. Clone the repository:
```bash
https://github.com/Ahmad1015/PDF-Text-to-Speech-using-Python.git
cd PDF-Text-to-Speech-using-Python
```
Install the required Python packages:
```bash
pip install pyttsx3 PyPDF2
```
## Usage
Ensure you have a PDF file named sample.pdf in the root directory of the project.
Run the main script:
```bash
python main.py
```
## Functionality
- The script will open and read the sample.pdf file.
- It extracts text from each page of the PDF.
- Using the pyttsx3 library, it converts the text to speech and announces the end of each page.
## Project Structure
- main.py: The main script that runs the program.
- sample.pdf: The PDF file to be read (ensure this file is present in the root directory).
