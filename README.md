# Overview
This project was created as part of an assignment given in my Information Security class:
"Report the number of web servers in Hanyang University network and explain your method."

The assignment required scanning the Hanyang University network using nmap to identify active web servers. To improve efficiency and automate the process of launching multiple scans over various subnets, I developed this Python script that sends nmap commands via the WSL terminal.

# How it works
The script accepts command-line arguments to specify:
- The output filename (where scan results will be saved).
- The target network in CIDR notation (currently requires /24 subnet).
- Optional range value to scan multiple adjacent subnets.

It iterates through the specified IP ranges, launching nmap scans for ports 80, 443, and 8080 using a SYN scan with service version detection.
The scan results are saved into the specified output file for later analysis.

python main.py --output results.txt --ip xxx.xxx.xxx.0/24 --finishing y
- --output: output filename (adds .txt if no extension)
- --ip: base network address in xxx.xxx.xxx.0/24 format
- --finishing: optional, end of third octet range to scan (defaults to 255)

# Important notes and warnings
Permissions: The script runs nmap with sudo privileges; make sure you understand the security implications
Scope: Only use this script to scan networks you own or have explicit permission to scan. Unauthorized scanning is illegal and unethical !
Performance: Scanning large IP ranges may take a long time (hours or days). Adjust ranges responsibly.

# Responsibility: The author is not responsible for any misuse or damage caused by this tool. The script does not execute arbitrary user input besides controlled nmap commands. Use in a trusted environment only.
