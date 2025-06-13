'''
IMPORTANT
For this program to run correctly, write the command in your CL in this format : 
python main.py outputFile addressIP finishingRange

The arg addressIp takes only one format : xxx.xxx.xxx.0/24
The arg finishingRange is not mandatory : 
    if not specified, will go over : xxx.xxx.xxx.0/24 to xxx.xxx.255.0/24
    if specified : xxx.xxx.xxx.0/24 to xxx.xxx.finishingRange.0/24

You can retrieve all of the results of the different scans in the file outputFile
 
Be careful of the range you give to the program : the bigger it is, the longer it will take for it to compute ! (May take hours/days...)
'''
import subprocess, time, argparse, ipaddress

def scanning(outputFile, startingRange, finishingRange, ipAddress, STARTING_TIME):
    with open(outputFile, 'w') as file :
        file.write('') #to make sure the cache is completely erased
        ip = '.'.join(ipAddress.split('.')[0:2])

        for bit in range(startingRange, finishingRange + 1):
            dynamicIp = f"{ip}.{bit}.0/24"
            print(f"Scanning {dynamicIp}\t -")
            
            commandIp = f"sudo nmap -p 80,443,8080 -T4 -sS -sV -R {dynamicIp}".split()
            result_scan = subprocess.run(commandIp, capture_output= True, text=True)
            
            result = result_scan.stdout
            print(result,"\n")
            
            file.write(
                f"Scan of {dynamicIp}\n"
                + result
                + '\n\n')
        
        timer = f"\tAll IP scans were done in {(time.time() - STARTING_TIME):.2f} seconds"
        print(timer)
        file.write('\n\n' +timer)

def isValidNumber(entry):
    try : 
        number = int(entry)
        if number < 0 or number > 255 :
            raise ValueError
        return number
    except ValueError:
        raise argparse.ArgumentTypeError("The argument must be an integer in between 0 and 255 included")

def isValidIPNetwork(entry):
    try:
        network = ipaddress.ip_network(entry, strict=True)
        if network.prefixlen != 24:
            raise argparse.ArgumentTypeError("The value after the IP address xxx.xxx.xxx.0 needs to be '/24'")
        return str(network)
    except ValueError:
        raise argparse.ArgumentTypeError("The IP address must be in the following format : xxx.xxx.xxx.0/24 (replace the x by values in between 0 and 255)")

def main():
    STARTING_TIME = time.time()

    parser = argparse.ArgumentParser(description= "Tool to scan active networks")
    parser.add_argument('--output', type=str, required=True, help="Name of the output file")
    parser.add_argument('--ip', type=isValidIPNetwork, required=True, help="Network IP in format xxx.xxx.xxx.0/24")
    parser.add_argument('--finishing', type=isValidNumber, default=255, help="End of third IP octet, range : 0 to 255 included")

    args = parser.parse_args()
    
    startingRange = int(args.ip.split('.')[2])
    if args.finishing < startingRange:
        parser.error(f"Finishing range cannot be smaller than the starting 3rd IP octet : {startingRange}")
    
    if not args.output.lower().endswith('.txt'):
        args.output += '.txt'

    scanning(args.output, startingRange, args.finishing, args.ip, STARTING_TIME)

if __name__ == '__main__' :
    main()

