# Python for Cybersecurity

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


### Read HTML

```soup = BeautifulSoup(response.text, "html.parser") ``` Now beautifulSoup can look for link's

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








---
---
