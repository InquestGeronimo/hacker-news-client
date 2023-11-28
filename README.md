# Hacker News Client  <img align="right" width="75" height="75" src="./img/hackernews-logo.png">

The Hacker News Client is a Python-based tool designed to seamlessly engage with the official Hacker News Firebase API. This client incorporates a built-in request-cache mechanism for each API call, allowing for the efficient handling of complete data dumps without the need for redundant subsequent calls. This feature significantly optimizes your data wrangling processes, saving you time and resources.

## Install <img align="center" width="23" height="25" src="https://media.giphy.com/media/sULKEgDMX8LcI/giphy.gif">
<br>

```
pip install hnclient
```

## Quick Start <img align="center" width="23" height="25" src="https://media.giphy.com/media/PeaNPlyOVPNMHjqTm7/giphy.gif">
<br>

First step is to initialize `HackerNewsClient` prior to making an API request. By default, client requests are cached. To disable cache, set the `disable_cache` argument to **True**:

```py
from hnclient import HackerNewsClient

client = HackerNewsClient()
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

## Data Wrangling <img align="center" width="23" height="25" src="https://media.giphy.com/media/fmkYSBlJt3XjNF6p9c/giphy.gif">
<br>

Collect a list of a specific metadata object. The available list of objects can be found in the printed dictionary above. For the example below, we are obtaining a list of all URLS pertaining to the **Top** stories:

```py
from hnclient import HackerNewsClient

client = HackerNewsClient()
data = client.get_stories("top")

urls = client.get_item("url", data)
print(urls)
```
&emsp; output:

```
    ['https://github.com/ifeelalright1970/ytmp',
     'https://mimosa.so/',
     'https://www.screen.studio/',
     'https://www.pinetarpoker.com',
    ...]
```

Select a random story from the client payload. For the example below, we are obtaining a story pertaining from the **Best** stories.

```py
from hnclient import HackerNewsClient

client = HackerNewsClient()
data = client.get_stories("best")

random = client.get_random_story(data)
print(random)
```
