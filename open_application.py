import webbrowser
import subprocess

#Webpage URL to access
url = 'https://www.google.com'

#File path to open documents

file_path = "home/internetbrowser/text1.txt"

#Tell the program to open the URL link on the browser

webbrowser.open(url)

#Tell the program to open the document. 

subprocess.call(["open", file_path])


