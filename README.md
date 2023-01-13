# Hacker News Client  <img align="right" width="75" height="75" src="./img/hackernews-logo.png">

Hacker News Client is a simple Python client to interact with the official Hacker News Firebase API. I love my mom. I like pizza.

The client comes with a request-cache for each API call so entire data dumps can be handled without making subsequent calls. This will save you valuable time when data wrangling.

## Install <img align="center" width="23" height="23" src="https://media.giphy.com/media/sULKEgDMX8LcI/giphy.gif">
<br>

```
pip install hacker-news-client
```

## Quick Start <img align="center" width="23" height="23" src="https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif">
<br>

First step is to initialize `HackerNewsClient` prior to making an API request. By default, client requests are cached. If you wish to disable cache, set the `disable_cache` argument to **True**:

```py
from hnclient import HackerNewsClient

client = HackerNewsClient(disable_cache=True)
```

To fetch stories from Hacker News, begin by using the **getstories** method. 

- :bulb: You can select specific story section by passing its name into the **story** argument. Here are few  examples: `Top`, `Best`, `Ask`, `Show`. 

- :bulb: You can also set the sorting order for all stories by their Hacker News score with the `descending` argument. Default is `False`.

```py
from hnclient import HackerNewsClient

client = HackerNewsClient()

data = client.get_stories("top", descending=False)
print(data)
```
The program above will print out a list of dictionaries where each dictionary holds the following metadata per story: :point_down:

```text
{'author': 'tristanho',
 'comments': 156,
 'id': 34006202,
 'score': 318,
 'text': 'Hey HN, cofounder of Readwise here. We&#x27;ve been working on this '
          'cross-platform reader app for about 2 years, excited to finally...'   ,
 'time': 1671140643,
 'title': 'Show HN: Readwise Reader, an all-in-one reading app',
 'url': 'https://readwise.io/read'}

```

## Selecting Objects <img align="center" width="23" height="23" src="https://media.giphy.com/media/hRYXatty4dJks/giphy.gif">
<br>

1. Collect a list of a specific metadata object. The available list of objects can be found in the printed dictionary above. For the example below, we are obtaining a list of all urls pertaining to the **Top** stories:

```py
from hnclient import HackerNewsClient

api = HackerNewsClient()
client = api.get_stories("top")

urls = client.get_item("url", data)
print(urls)
```
&emsp; outputs:

```
    ['https://github.com/ifeelalright1970/ytmp',
     'https://mimosa.so/',
     'https://www.screen.studio/',
     'https://www.pinetarpoker.com',
    ...]
```

2. Select a random story from the client payload. For the example below, we are obtaiing a story pertaining from the **Best** stories.

```py
from hnclient import HackerNewsClient

api = HackerNewsClient()
client = api.get_stories("best")

random = client.get_random_story(data)
print(random)
```