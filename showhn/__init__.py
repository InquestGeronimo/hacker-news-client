from .extraction import HackerNewsHandler
from .request import RequestClient
from .settings import post_ids_url
from rich.console import Console
console = Console()


uids = RequestClient(post_ids_url)
HN = HackerNewsHandler()
with console.status("fetching data...", speed=3):
    post_ids = HN.get_post_data(uids())