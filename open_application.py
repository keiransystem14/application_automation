import webbrowser
import subprocess

#Webpage URL to access
url = 'https://www.google.com'

#File path to open documents

file_path = "/home/internetbrowser/Documents/Domain 1 - Answers.docx"

#Tell the program to open the URL link on the browser

webbrowser.open(url)

#Tell the program to open the document. 

subprocess.call(["open", doc_path])


