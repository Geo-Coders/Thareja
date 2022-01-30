# Write a program that fetches data from a specified url and prints it on screen
import urllib.request
x = urllib.request.urlopen('http://www.google.com/')
print(x.read())