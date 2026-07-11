# Python for Cybersecurity

# 0 - dns resolver

The purpose of this program is to obtain the IP address by providing the domain name.

```import socket```
Imports the socket module, which provides access to the network functions of the operating system.

Among them is ```gethostbyname()```, used to query DNS servers.

try
```
try:
    return socket.gethostbyname(domain_name)

socket.gethostbyname(domain_name)
```

This function:

Queries DNS.
Looks up the IPv4 address associated with the domain.
Returns a string containing the IP.

### On ERROR

```
except socket.gaierror:
    return None
```

### Exception nd variable e

The variable `e` contains the error description.

For example:

```return str(e)```

It might return something like:

```"[Errno 101] Network is unreachable"```


---
---

# 5 - Crawler

visited = set()

```set()```
set() do not alow duplicated content. Its like a list to save data.

```visited.add(url)```
If the same URL appears again, it is not added again.
This is perfect for a crawler because it avoids visiting the same page several times.

---

```from bs4 import BeautifulSoup```

BeautifulSoup reads HTML and allows you to search for elements.

soup.find_all("a")
```html
it find all <a href="...">
```

### Main function

Hardcoded for depth

``` python
def crawl_website(start_url, max_depth=2):
```

### Finding domain

```domain = urlparse(start_url).netloc```

if ```start_url = "https://example.com/blog/index.html"```

then ```urlparse(start_url)``` domain = example.com

```
scheme = https
netloc = example.com
path = /blog/index.html
```

From now crawler only visits pages from the same domain ```example.com```

### Recursive

```def crawl(url, depth):``` Inside have another function who called herself

First condition ```if depth > max_depth or url in visited:
    return``` check depth or already visited pages

Call HTTP, if response 404, 500 or timeout -> ```except RequestException:  -> return ```

```response = requests.get(url, timeout=5)```

### Read HTML

```soup = BeautifulSoup(response.text, "html.parser") ``` Now beautifulSoup can look for link's

Looking for links

```
for link in soup.find_all("a", href=True):
```

Iterates through all tags

```
<a href="...">

Example>

<a href="/about">
<a href="/contact">
<a href="https://google.com">
```

## Transform in absolut URL

```
absolute_url = urljoin(url, link["href"])
```

Se estiveres em ```https://example.com/blog```

and  HTML have ```<a href="/about">``` then absolute_url stays ```https://example.com/about```

### Analisar a URL

```parsed = urlparse(absolute_url)```

Parse URL in parts.

Only HTTP, Ignore links like " mailto:, tel:, ftp:

```phyton
if parsed.scheme not in ("http", "https"):
    continue
```

### Same domain

if domain was ```Example.com``` and find a link like ```https://google.com``` it is ignored, then curl never goes out from site

```
if parsed.netloc != domain:
    continue
```

### Removing URL fragments

A URL can look like this:

```https://example.com/page#section1```

The #section1 part is called a URL fragment (or anchor). It points to a specific section within the same page and is not sent to the server when the page is requested.

```clean_url = parsed._replace(fragment="").geturl()```

This removes the fragment, turning:

```https://example.com/page#section1```

into:

```https://example.com/page```

This helps avoid visiting or processing the same page multiple times when the only difference is the fragment identifier.


### Starting the crawler

At the end of the function:

```crawl(start_url, 0)```

This starts the crawler from the initial URL with a depth of 0. The crawler then begins visiting pages and recursively follows links until it reaches the maximum depth.

---
---
