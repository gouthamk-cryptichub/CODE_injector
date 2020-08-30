#Required Python Modules
netfilterqueue
scapy
re
optparse
argpars(for python 3)
sys

#################################################
**NOTE [HTTP sites]
If using this tool on a remote machine in the same network...
1) use ARP_spoofer to become man in the middle > https://github.com/gouthamk-cryptichub/ARP_spoofer
2) Set iptables rules in your machine as follows
    Open Terminal
    >iptables -I FORWARD -j NFQUEUE --queue-num 0
now use the tool

AFTER Experimen
Open Terminal
>iptables --flush
################################################
**NOTE [HTTPS sites]
If using this tool on a remote machine in the same network...
1) use ARP_spoofer to become man in the middle > https://github.com/gouthamk-cryptichub/ARP_spoofer
2) Rn SSLstrip
    >sslstrip
3) Set iptables rules in your machine as follows
    Open new Terminal
    >iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000
    >iptables -I OUTPUT -j NFQUEUE --queue-num 0
    >iptables -I INPUT -j NFQUEUE --queue-num 0
now use the tool inject_https.py

AFTER Experiment
1)stop sslstrip via CTRL + C
2)Open Terminal
>iptables --flush
