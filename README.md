# Hacker News Client  <img align="right" width="75" height="75" src="./img/hackernews-logo.png">

Hacker News Client is a simple Python client to interact with the official Hacker News Firebase API.

The client comes with a request-cache for each API call so entire data dumps can be handled without making subsequent calls. This will save you valuable time when data wrangling.

## `Install`
<br>

```
pip install hacker-news-client
```

## `Getting Started`
<br>

The base object for interacting with the api is `HackerNewsClient`:

```py
from hnclient import HackerNewsClient

client = HackerNewsClient()
```
<br>
#### `Get the data dump`

To fetch data about a specific section of Hacker News, pass in the section to the `getstories` method. The default story is `Top`, for the Top stories on Hacker News, but you can choose other sections such as: `Best`, `Ask`, `Show`. 

In addition, you can also alter the sorting order of the stories' score with the `descending` argument.

```py
from hnclient import HackerNewsClient

client = HackerNewsClient()

data = client.get_stories(story="top", descending=False)

print(data)
```


