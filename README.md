# Hacker News Client  <img align="right" width="75" height="75" src="./img/hackernews-logo.png">

Hacker News Client is a simple Python client to interact with the official Hacker News Firebase API.

The client comes with a request-cache for each API call so entire data dumps can be handled without making subsequent calls. This will save you valuable time when data wrangling.

## Install :computer:
<br>

```
pip install hacker-news-client
```

## Getting Started :rocket:
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
The program above will print out a list of dictionaries where each dictionary is the metadata values for an individual story:  
```
{'author': 'tristanho',
 'comments': 156,
 'id': 34006202,
 'score': 318,
 'text': 'Hey HN, cofounder of Readwise here. We&#x27;ve been working on this '
          'cross-platform reader app for about 2 years, excited to finally '
          'share it in public beta.<p>Probably the most notable thing that '
          'makes Reader unique is that it supports almost any content type you '
          'could want to save&#x2F;read&#x2F;highlight:<p>* web pages<p>* '
          'emails&#x2F;newsletters<p>* PDFs<p>* ePubs<p>* twitter threads<p>* '
          'youtube videos (with transcripts)<p>* RSS feeds<p>With all of your '
          'knowledge content in one place, we built powerful reading and '
          'highlighting, as well as a bunch of novel triage&#x2F;organization '
          'features, so you can actually consume &amp; stay on top of that '
          'content!<p>There are also a lot of advanced features too, such as '
          'text-to-speech, GPT3 questions&#x2F;summaries, super powerful '
          'highlighting (that includes markup and images), complex '
          'filtering&#x2F;search (with our own query language), sleek mobile '
          'triage UI, keyboard shortcuts for reading&#x2F;everything, '
          'integrations with note-taking apps, a browser extension for both '
          'saving pages and highlighting them, and much more.<p>If '
          'anyone&#x27;s interested in more product details, as well as our '
          'business model, etc, we wrote a detailed launch post: <a '
          'href="https:&#x2F;&#x2F;blog.readwise.io&#x2F;the-next-chapter-of-reader-public-beta&#x2F;" '
          'rel="nofollow">https:&#x2F;&#x2F;blog.readwise.io&#x2F;the-next-chapter-of-reader-public-b...</a><p>Predicting '
          'a common question: Reader is part of the Readwise subscription '
          'pricing right now in beta -- there&#x27;s a 30 day free trial and '
          'then it&#x27;s paid at ~$8usd&#x2F;month. We also promise to not '
          'raise this price for existing subscribers.<p>Reader is also fairly '
          'technically interesting -- our iOS, Android and webapp all work '
          'fully offline and sync your reading data&#x2F;progress with '
          'eachother. Our search on web is built with wasm sqlite. We have a '
          'fairly intense pipeline for cleaning web articles (removing '
          'ads&#x2F;styling). We share lot of modules around '
          'syncing&#x2F;highlighting across all platforms, etc...<p>Happy to '
          'answer any questions :)',
  'time': 1671140643,
  'title': 'Show HN: Readwise Reader, an all-in-one reading app',
  'url': 'https://readwise.io/read'}
  ```
