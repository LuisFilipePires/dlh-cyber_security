# Active Reconnaissance

---
## Are there any opened ports?
Exercise 0: 0-ports.txt
---

I use `nmap` to scan 1000 ports at ip:10.42.64.157

### nmap --top-ports 1000 10.42.64.157

- Starting Nmap 7.98 ( https://nmap.org ) at 2026-06-25 18:55 +0200
- Nmap scan report for 10.42.64.157
- Host is up (0.020s latency).
- Not shown: 999 closed tcp ports (reset)
- PORT   STATE SERVICE
- 80/tcp open  http
