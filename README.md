# boilerdownloader

Okay, so this repo is just for my personal purpose.

I had to scrape data from a French website about condensing boilers and convert it into 'Record' to be used in Dymola.

I was so deep into python that I was more excited to implement this in python and also, python is cool :p

So, this script iterates through 100000 to 999999 (changed as per requirements) through the website looking for boilers

It uses Beautiful Soup, mechanize and a few other libraries to parse html to find relevant keywords and downloads the relevant html page

The other script actually parses the downloaded html page and looks for required data into it by searching for tags in html.

It saves the found out data in a particular html for a particular boiler model into .mo file, used in Dymola

It's cool. 

I don't want the script to be TIDY, because I guess that it would be barely useful to others! :p

Just putting my code online!
