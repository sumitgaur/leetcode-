import itertools
import uuid
from collections import defaultdict

from sortedcontainers import SortedList


class Post:
    def __init__(self, content, user):
        self.id = str(uuid.uuid4())
        self.content = content
        self.tags = None
        self.user = user

    def display_post(self):
        print("Content {} \n post by {}".format(self.content, self.user.name))


class User:
    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name
        self.posts = []
        self.followed_users = []

    def create_post(self, content: str):
        self.posts.append(Post(content, self))

    def get_latest_posts(self, k):
        return self.posts[-k:]

    def follow_user(self, u):
        self.followed_users.append(u)

    def get_followed_people_post(self, k):
        posts = []
        for user in self.followed_users:
            user_latest = user.get_latest_posts(k)
            if user_latest:
                posts.extend(user_latest)
        return posts


if __name__ == '__main__':
    u1 = User("sumit")
    u2 = User("amit")
    u3 = User("mayank")
    u4 = User("pushp")
    # sumit->[amit,mayank,pushp]
    # amit ->[sumit,mayank]
    #

    u1.follow_user(u2)
    u1.follow_user(u3)
    u1.follow_user(u4)
    u2.follow_user(u1)
    u2.follow_user(u3)
    u3.follow_user(u1)
    u3.follow_user(u4)
    u4.follow_user(u3)

    u1.create_post("Happy weekend people ")
    u1.create_post("Travelling to Delhi soon ")
    u2.create_post("How's weather in Blr ")
    u2.create_post("How's weather in Delhi ")
    u3.create_post("Lets party")

    list(map(Post.display_post, u1.get_latest_posts(3)))
    print()
    list(map(Post.display_post, u2.get_latest_posts(3)))
    print()
    list(map(Post.display_post, u1.get_followed_people_post(3)))
