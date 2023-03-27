# Import urllib
# Use urllib.request to get the data from the url
# Write a function that takes a url
# Returns a response

import urllib.request as urllib

def main(url):
  print("Checking connectivity ")
  response = urllib.urlopen(url)
  print("Connected to", url, "successfully")
  print("The response code was: ", response.getcode())

print("This is a site connectivity checker program")
input_url = input("Input the url of the site you want to check: ")

# url = https://www.google.com
# url = https://django-blog-38ga.onrender.com/

main(input_url)

