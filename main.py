import subprocess
import time

# IMPORTANT
#use this program in wsl for the command to work properly
#you can retrieve all of the results of the different scans in the file OUTPUT_FILE

OUTPUT_FILE = "scan_results.txt"
STARTING_RANGE, FINAL_RANGE = 0, 5  #a small range of ip addresses like you advised

STARTING_TIME = time.time()

with open(OUTPUT_FILE, 'w') as file :
    file.write('') #to make sure the cache is completely erased
    
    for bit in range(STARTING_RANGE, FINAL_RANGE):
        ip = f"166.104.{bit}.0/24"
        print(f"Scanning {ip}\n")
        
        command_ip = f"sudo nmap -p 80,443,8080 -T4 -sS -sV -R {ip}".split()
        result_scan = subprocess.run(command_ip, capture_output= True, text=True)
        
        result = result_scan.stdout
        print(result,"\n")
        
        file.write(
            f"Scan of {ip}\n"
            + result
            + '\n\n')
    
    timer = f"All IP scans were done in {(time.time() - STARTING_TIME):.2f} seconds"
    print(timer)
    file.write('\n\n' +timer)
    


