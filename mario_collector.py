#Mario Collector
#ERROR lines (coins), WARNING lines (bananas), and total lines

#Variables
coins = 0
bananas = 0
total_lines = 0

#File
with open("mario.kart", "r") as file: 

  #Loop
    for line in file: 
        total_lines += 1
  
        if "ERROR" in line:
            coins += 1
    
        if "WARNING" in line: 
             bananas += 1

#Print Results
print("Total lines:", total_lines)
print("Coins collected:", coins)
print("Bananas collected:", bananas)
    

