# net_f00tprint

This repository is intended to save basic scripts written in Python, which can be used in penetration tests, specifically in the footprint phase.

The dns_enumerator script performs an enumeration of dns and their respective IPs. 
    
    Its use is basic:
    
        python3 dns_enumerator.py

The dns_brute_force script performs a series of brute force attempts to find domains, subdomains and their respective IPs. 
    
    To use it, it is necessary to have a file in TXT format with the name "bruteforce.txt", which contains the known subdomains, such as: www, ftp, phpmy etc.

    Once you have your file in hand, now just start the script from the command line:

        python3 dns_brute_force.py