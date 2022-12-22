# Hacker News Client  <img align="right" width="75" height="75" src="./img/hackernews-logo.png">

Hacker News Client is a simple Python client to interact with the official Hacker News Firebase API.

The client comes with a request-cache for each API call so entire data dumps can be handled without making subsequent calls. This will save you valuable time when data wrangling.

## Install <img align="center" width="23" height="23" src="https://media.giphy.com/media/sULKEgDMX8LcI/giphy.gif">
<br>

```
pip install hacker-news-client
```

## Quick Start <img align="center" width="23" height="23" src="https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif">
<br>

First step is to initialize `HackerNewsClient`:

```py
from hnclient import HackerNewsClient

client = HackerNewsClient()
```

To fetch data about a specific section of Hacker News, pass in the section using the **getstories** method. 

- :bulb: For selecting a specific section from HN, pass their name into the **story** argument: `Top`, `Best`, `Ask`, `Show`. 

- :bulb: You can also alter the sorting order all the storries by their Hacker News score with the `descending` argument.

```py
from hnclient import HackerNewsClient

client = HackerNewsClient()

data = client.get_stories(story="top", descending=False)
print(data)
```
The program above will print out a list of dictionaries where each dictionary holds the following metadata keys per story: :point_down:

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

```py
from hnclient import HackerNewsClient

api = HackerNewsClient(disable_cache=False)

data = api.get_stories(story="top", descending=False)
```

Select a specific object from the :

```py
random = api.get_random_story(data)
```


Select a random object from the client:

```py
random = api.get_random_story(data)
```