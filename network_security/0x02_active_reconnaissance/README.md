# Active Reconnaissance

---
## 1. Are there any opened ports?
Exercise 0: 0-ports.txt

I use `nmap` to scan 1000 ports at ip:10.42.64.157

### nmap --top-ports 1000 10.42.64.157

- Starting Nmap 7.98 ( https://nmap.org ) at 2026-06-25 18:55 +0200
- Nmap scan report for 10.42.64.157
- Host is up (0.020s latency).
- Not shown: 999 closed tcp ports (reset)
- PORT   STATE SERVICE
- 80/tcp open  http

---
## 1. Inspect the runner
Exercise 1: 1-webserver.txt

### command: sudo bash -c 'echo "10.42.64.157  active.hbtn" >> /etc/hosts'
It creates a local DNS mapping, so when the system tries to resolve active.hbtn, it will point to the target IP

`Wappalyzer`: We had trouble accessing the website.

I use `curl -I http://active.hbtn` to obtain results
- HTTP/1.1 200 OK
- Server: nginx/1.18.0
- Date: Thu, 25 Jun 2026 17:19:52 GMT
- Content-Type: text/html; charset=utf-8
- Content-Length: 4154
- Connection: keep-alive
- Vary: Cookie

---

## 2. Nothing defeat Manual inspection 
Exercise 3: 100-flag.txt

Flag in the comment :  Dont forget to delete this comment please
         Holberton Sec Lab - 26160aebb9c9dc8ed585078091886d66 

---

## 3. Trypanophobia
Exercise 4: 2-injectable.txt

The /product endpoint always returns HTTP 200 OK, even for non-existent pages or high ID values (up to 1000), meaning the server does not properly validate the existence of resources and always serves a valid response.

---
## 4. SQLmap is an army \o/
Exercise 5: 3-database.txt, 4-tables.txt

 sqlmap -u "http://active.hbtn/product/1" --dbs --batch

---


