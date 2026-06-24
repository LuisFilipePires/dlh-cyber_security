## Network Protocols: Auditing and Securing

- 'sudo'
  runs the command with administrator (root) privileges
- 'iptables'
  Linux firewall tool used to manage network traffic rules
- '-L'
  lists all current firewall rules
- '--line-numbers'
  adds line numbers to each rule (useful to delete or modify specific rules)
- '-v'
  verbose mode → shows detailed information (packets, bytes, interfaces)
- '-n'
  numeric output → shows IP addresses and ports without resolving names (faster and clearer)

'''
### exercice 2-harden.sh

- `find /`  
  searches the entire system starting from the root directory `/`

- `-xdev`  
  does not cross other filesystems or mounted partitions

- `-type d`  
  searches only directories

- `-perm 0002`  
  finds files with write permission for others

- `-print`  
  prints the results

- `-exec`  
  executes a command on the found results

- `chmod o-w`  
  removes write permission for others (`o`)

- `{}`  
  represents the currently found item

- `+`  
  executes commands in batch (more efficient)
