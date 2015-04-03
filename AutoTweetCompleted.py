#Import required libraries

import twitter
import datetime
import urllib2

#Locates the users browser history of the current session - in this case it is locating Chromes current session

file = open("/Users/tdower/Library/Application Support/Google/Chrome/Default/Current Session")
data = file.read()

#Finds the most recent website that has been browsed. I have used 'webStart' and 'webEnd' as it is finding the url of websites 

webStart = str(data).rfind("http")
webEnd = str(data).find(chr(0), webStart)
url = data[webStart:webEnd]

#Prints the most recent website

response = urllib2.urlopen(url)
website = response.read()
print(website)

#This is finding the 'title' of the webpage

findPageTitle = website.find("<title>")
findPageEnd = website.find("</title>")

#Once it has found the title of the most recent webpage in then prints this out in terminal when the code is ran

title = website [findPageTitle:findPageEnd]
title = title.replace("<title>", "")
print(title)


#These are the keys for the Twitter API (I have used Jess' Twitter Keys)

api = twitter.Api(consumer_key="Q64bTmPxvwMdc316c1ltdISBa",consumer_secret="OSpBG5wllJVovXWBDkx0s7s0p40o4sBDyifZYulCD84XLspe1f",access_token_key="256981328-2btHERPIxsoEQqOunm531ZdM8qI0l3g3JZJxloFM",access_token_secret="MofFdtukeCmrXBxYWYEM8SfqGTNsyn8IwoC02ArfWxzrr")


timestamp = datetime.datetime.utcnow()


#This is the message that is posted to Twitter - The message that would appear is "I've recently looked at" followed by the title of the webpage and then the time that it was posted 
response = api.PostUpdate("I've recently looked at " +  title + str(timestamp))

print("Status updated to: " + response.text)
