def main(): 

 try: 
  miles_needed = int(input('Enter the number of miles driven: ')) 

  miles_to_kilometers(miles_needed)

 except: 
  print("An error occurred, please try again by entering only a whole number") 
  print() 
  
def miles_to_kilometers(miles): 
    kilometers = miles * 1.609
    print('You have driven a total of', miles, 'miles', 'which is also', kilometers, 'kilometers.')

main() 
