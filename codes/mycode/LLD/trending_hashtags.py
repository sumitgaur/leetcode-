from collections import Counter


class TopKHashTags:
    def __init__(self):
        self.posts = Counter()

    def post(self, hashtag, t):
        self.posts[hashtag] += 1

    def get_top_k(self, k):
        self.posts.most_common(k)

