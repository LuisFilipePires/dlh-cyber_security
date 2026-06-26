## Cybersecurity Luxembourg Academy
 
 This repository contains my progress on the projects from the Cybersecurity Luxembourg Academy.

All projects are committed by modules as I progress through the program.

Each project includes a detailed description of the studies, concepts learned, and the project itself.

## Target Environment
- To connect to the target environment, I first establish the VPN connection using the .ovpn file with:
- `sudo openvpn /path/to/file.ovpn`
- After that, I launch the target machine in the sandbox/platform and start testing.
- If the target hostname does not resolve, I add it manually to /etc/hosts by mapping the target IP to the hostname. `echo "10.10.11.25 target.local" | sudo tee -a /etc/hosts` (tee to resolve a problem of authorization with linux) or `sudo nano /etc/hosts`
