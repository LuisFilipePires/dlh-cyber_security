# Passive Reconnaissance "holbertonschool.com"

#### `search: hostname:holbertonschool.com` To obtain a basic information
---

### Cloud Providers

- Amazon Web Services (AWS)
  - ASN: AS16509
  - Region: eu-west-3 (Paris, France)
  - Service: EC2

- Scaleway
  - ASN: AS12876
  - ISP: SCALEWAY S.A.S.
  - Location: Paris, France

---

## subdomains
- guinee.holbertonschool.com
- apply.holbertonschool.com
- yriry2.holbertonschool.com
- read.holbertonschool.com

---
#### The same subdomain resolves to multiple IP addresses, indicating a distributed cloud architecture and load balancing strategy.
---

|subdomain|ip|
|---|---|
|guinee.holbertonschool.com|51.15.213.103|
|apply.holbertonschool.com|15.236.2.28|
|yriry2.holbertonschool.com|52.47.143.83|
|read.holbertonschool.com|35.181.141.244|

---

## IP Addresses Observed

### AWS Infrastructure

- 15.236.2.28
- 15.188.95.246
- 35.180.145.93
- 35.181.10.155
- 35.181.141.244
- 52.47.143.83

---

### Scaleway Infrastructure

- 51.15.213.103

---


## Technologies Identified

### Web Servers

- nginx/1.20.0
- nginx/1.28.3 (Ubuntu)

### SSL/TLS

- Let's Encrypt certificates
- Amazon RSA certificates
- TLS 1.2
- TLS 1.3

---

## Security Headers Observed

- X-Frame-Options
- X-XSS-Protection
- X-Content-Type-Options
- X-Download-Options

---

## Observations

- The infrastructure is distributed across multiple cloud providers (AWS and Scaleway).
- Multiple IP addresses are associated with the same subdomains, indicating load balancing or historical DNS resolution.
- Security headers are implemented, showing basic web hardening practices.
- nginx is the primary web server across services.

---

## Conclusion

The domain `holbertonschool.com` is hosted in a distributed, multi-cloud architecture leveraging AWS and Scaleway. The presence of multiple IPs per subdomain suggests load balancing and scalable infrastructure design. Basic security headers and TLS encryption are properly implemented, indicating standard security practices.
