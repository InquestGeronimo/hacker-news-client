from src.extraction import HackerNewsHandler
from src.request import RequestClient
from src.settings import post_ids_url
from rich.console import Console
console = Console()


uids = RequestClient(post_ids_url)
HN = HackerNewsHandler()
with console.status("fetching data...", speed=3):
    post_ids = HN.get_post_data(uids())