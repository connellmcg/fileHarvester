#!/usr/bin/python
import sys, os, argparse

try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 

#Set nice colours
TGREEN =  '\033[32m' # Green Text
ENDC = '\033[m' # reset to the defaults

def banner():
    print("""
           ___ _ _                                      _            
          / __(_) | ___  /\  /\__ _ _ ____   _____  ___| |_ ___ _ __ 
         / _\ | | |/ _ \/ /_/ / _` | '__\ \ / / _ \/ __| __/ _ \ '__|
        / /   | | |  __/ __  / (_| | |   \ V /  __/\__ \ ||  __/ |   
        \/    |_|_|\___\/ /_/ \__,_|_|    \_/ \___||___/\__\___|_|                                                                
        

        Coded By Connell McGinley 2020 - @cmcginley
    """)
 
parser = argparse.ArgumentParser(description=banner())
parser.add_argument('-s','--site', help='Site',required=True)
parser.add_argument('-n','--newfiletypes',help='Clear and defaults and set your own filetypes.', required=False)
parser.add_argument('-a','--addmore',help='Add more to existing filetype list. Example txt,bin,db', required=False)
parser.add_argument('-d','--download',help='Download Results. Use -d y', required=False)
args = parser.parse_args()
 
## show values ##
print ("Site: %s" % args.site )
print ("New Filetypes: %s" % args.newfiletypes )
print ("Add more: %s" % args.addmore )
print ("Download: %s" % args.download )

#Set Variables
print("The site is %s" % args.site)
filetypes = ["pdf", "doc", "docx"]
fileList = []


#-a addnew argument is defined
if args.addmore:
    result = [x.strip() for x in args.addmore.split(',')]
    
    for i in result:
        filetypes.append(i)

#-n newfiletypes argument is defined
filetypes = []
if args.newfiletypes:
    result = [x.strip() for x in args.newfiletypes.split(',')]
    
    for i in result:
        filetypes.append(i)

# to search 
print("Searching for filetypes of: "+ str(filetypes))
try:
    for filetype in filetypes:
        query = "site:" + args.site +  " filetype:" + filetype
        print(TGREEN + "Returning top results for " + filetype + ".", ENDC)
        for j in search(query, tld="com", num=10, stop=10, pause=2): 
            print(j) 
            fileList.append(j)

    if args.download:
        for i in fileList:
            os.system("mkdir "+ args.site)
            os.system("wget " + i + " -P ./" + args.site) 


except KeyboardInterrupt:
    print("Command was cancelled.")

sys.exit()