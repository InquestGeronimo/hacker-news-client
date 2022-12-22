# Hacker News Client  <img align="right" width="75" height="75" src="./img/hackernews-logo.png">

Hacker News Client is a simple Python client to interact with the official Hacker News Firebase API.

The client comes with a request-cache for each API call so entire data dumps can be handled without making subsequent calls. This will save you valuable time when data wrangling.

## `Install`

```
pip install hacker-news-client
```

## `Getting Started`

The base object for interacting with the api is `HackerNewsClient`:

```python
from hnclient import HackerNewsClient

client = HackerNewsClient()
```


