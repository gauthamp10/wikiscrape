#-----------------------------------------------------------------Wikipedia Information Scrape Tool---------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#
from colorama import Fore, Back, Style                         #give back & foreground color
import pandas as pd
import wikipedia as wk
import csv
import sys
import os
def main():                                                     #main definition
 
 def print_lines():                                             #printing dotted lines
  print(Style.BRIGHT+Fore.GREEN+"-"*168)
  print(Style.RESET_ALL)

 def box_msg(msg):                                              #for printing text in a box
  print(Style.BRIGHT+Back.GREEN+Fore.WHITE)
  row = len(msg)
  h = ''.join(['+'] + ['-' *row] + ['+'])
  result= h + '\n'"|"+msg+"|"'\n' + h
  print(result)

 def screen_clear():                                            #clearing terminal screen
  if os.name == 'nt':
   os.system('cls')
  else:
   os.system('clear')

 def intro():
  print(Fore.CYAN+Style.BRIGHT+"\t\t\t\t\t------------------------------Wikipedia Information Scrape Tool------------------------------")
  box_msg(''' Created by Gautham Prakash   @: gauthamp10@gmail.com''')

 def exit(code):
  print(Style.BRIGHT+'\nQuitting....')
  print(Style.BRIGHT+'\nBye bye.....')
  print_lines()
  sys.exit(code)


 def save_file(filename,content):                                 #for writing the ouput file. 
  with open('%s'%filename,'w') as f:
   for row in content:
    f.write(str(row))  

 def wiki_resolve_page(SEARCHTERM):                               #searching the term in wikipedia and resolving it's page source.
  data = wk.page(SEARCHTERM).html().encode("UTF-8")
  return data

 def get_infobox(wiki_page):                                      #for fetching class element named 'infobox' into python dataframe.     
   data = pd.read_html(wiki_page,attrs={'class':['infobox']})
   return data

 def get_small_summary():                                         #for fetching single sentence summary.
  print_lines()  
  try:                                                            #Exception handling for DisambiguationError
   print(Style.BRIGHT+wk.summary(SEARCHTERM,sentences=1))
  except wikipedia.exceptions.DisambiguationError as e:  
   print(e.options)
  print_lines()

 def save_summary():                                              #for saving the whole summary.
  summary=wk.summary(SEARCHTERM)
  print(Style.BRIGHT+summary)
  print_lines()
  save_file((SEARCHTERM+".txt"),summary.encode("utf-8"))
  print(Style.BRIGHT+"Saved summary as %s.txt\n"%SEARCHTERM)

 def save_infobox(info_box,SEARCHTERM):                           #for saving the infobox dataframe.
  save_file((SEARCHTERM+".csv"),info_box)
  print(Style.BRIGHT+"Saved Information table as %s.csv\n"%SEARCHTERM)
  ch=raw_input(Style.BRIGHT+"Do you want to scrape again...(y/n)")
  if ch=='y':
   main()
  else:
   exit(0)

 info_box=[]
 screen_clear()
 intro()
 SEARCHTERM = raw_input(Back.RED+Fore.WHITE+"\nEnter the search term: ")
 print(Style.RESET_ALL)
 wiki_page =wiki_resolve_page(SEARCHTERM) 
 if wiki_page:
  get_small_summary()
 else:
  print_lines()
  print("\nPAGE NOT FOUND: Try Another Search Term")
  print_lines()
  main()
 try:                                                            #Exception handling if the infobox table was not found.                            
  info_box=get_infobox(wiki_page)
  print(Back.BLUE+Fore.WHITE+Style.BRIGHT+"\n****************************") 
  print(Style.BRIGHT+"Information Table Found.....")
  print(Style.BRIGHT+"****************************\n")
  print(Style.RESET_ALL) 
  print_lines()
  print(info_box)
  print_lines()
  c=raw_input(Style.BRIGHT+"Want to save table information?...(y/n)\n")
  if c=='y':
   save_infobox(info_box,SEARCHTERM)
  else:
   cho=raw_input(Style.BRIGHT+"Do you want to scrape again?...(y/n)\n")
   if cho=='y':
    main()
   else:
    exit(0)
 except ValueError:
  answer=raw_input(Style.BRIGHT+"\nNo Table data found!...Do you want to save the whole summary itstead?..(y/n)\n")
  if answer=="y":
   print_lines()
   save_summary()
  else:
   ch=raw_input(Style.BRIGHT+"Do you want to scrape again...(y/n)\n")
   if ch=='y':
    main()
   else:
    exit(0)

if __name__ == '__main__':                                       #Calling main(), the actual entry point for the scraper
    main()  
    exit(0)                                            
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#
