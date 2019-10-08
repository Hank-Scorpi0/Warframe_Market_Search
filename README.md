# Warframe_Market_Search
Allows users to look up multiple items on the warframe market all at once, in an effort to make the creation of sell orders more effcient. 

# Libraries Used
requests, urllib, string, json, tkinter

# How to use
If you already have a version of Python 3 on your machine you can simply download the file and double click on it intializing the UI. From there you can search search multiple items at once as a comma seperated list. 

Ex. Rhino Prime Set, Frost Prime Chasis, Gram Prime Blade

No limitations have been encountered in terms of the number of comma seperated items a user can have

# Notes about search
When searching for a list of items the user does not need to worry about any issues arsing with case sensitivity. For example, Frost Prime Chassis, FROST PRIME CHASSIS, frost prime chasis would all yield the same result. 

That being said the user needs to have the exact name of the part that they are looking for. For exmaple, Searching Valkyr Prime would result in "Part not found". The user must enter the name verbatim as it would be referred to on the site. In the previous example that would be "Valkyr Prime Set"

# Modification of the script
Currently the applicatoin returns the Average Prime for the item you are searching for. If the user wants a different value for the part they must go to line 27 and Replace 'avg_price' with 'min_price' or 'max_price' etc. 

There are more options interms of the data points available to the user, if you would like to see what other data points you can look up use the JSON library to read the JSON response for a particular search to see what you have availble to you. 
