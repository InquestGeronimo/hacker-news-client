from settings import post_ids_url, get_post_data # this line used for testing only
from request import RequestClient
import pprint as pp # this line used for testing only


class HackerNewsHandler:

    def get_post_data(self, uids):  
    
        post_data = []
        for uid in uids:
            data = RequestClient(get_post_data(uid))()

            try:
                post_data.append(
                    {
                        "id":        uid,
                        "title":     data["title"],
                        "text":      data["text"][:135] + "...",
                        "comments":  data["descendants"],
                        "score":     data["score"],
                        "time":      data["time"],
                        "hacker":    data["by"]
                    }
                )

            except KeyError:
                continue
        # pp.pprint(post_data) # this line used for testing only
        # sorts dictionary by 'score' in descending order
        return sorted(post_data, key=lambda d: d["score"], reverse=True)

posts = RequestClient(post_ids_url)
HN = HackerNewsHandler()
post_ids = HN.get_post_data(posts())
