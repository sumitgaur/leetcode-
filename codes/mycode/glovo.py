'''
## Problem Description

Design a data structure to store and retrieve tweets.
The system it's a simplified Twitter system where users can:
- Post tweets
- Follow/unfollow other users
- Retrieve the 10 most recent tweet IDs in the user's news feed

The news feed should include tweets posted by the user and by users they follow, sorted from most recent to least recent.

## Constraints

- Tweet IDs and User IDs are positive integers.
- A user can follow themselves, but it doesn't affect the news feed.
- Posting following/unfollowing can happen multiple times.
- Each call to postTweet function will be made with a unique tweetId.

You need to implement the following behaviors:
- postTweet(int userId, int tweetId):
    - Compose a new tweet with tweetId by user userId.
- List<Integer> getNewsFeed(int userId):
    - Retrieve the 10 most recent tweet IDs in the user's news feed. Tweets must be ordered from most recent to least recent.
- void follow(int followerId, int followeeId):
    - The user followerId starts following the user followeeId.
- void unfollow(int followerId, int followeeId):
    - The user followerId stops following the user followeeId.

'''
import heapq
from collections import defaultdict


# follow_map
# follower -> set(followees)
# userA-> {userB,userC}
#
# tweets per user  / reverse chronological order
# userid->{[time,tweetid]}
# 1-> (5,101),(2,95)
# O(FlogF) -> F is followees

# Users - U
# Tweets T

class Twitter:
    # space complexity O(U) + O(T)
    def __init__(self):

        self.time = 0
        self.tweets = defaultdict(list)
        self.follow_map = defaultdict(set)

    def postTweet(self, userId, tweetId):
        # Time complexity O(1)
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def follow(self, followerId, followeeId):
        # Time complexity O(1)
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        # Time complexity O(1)
        if followeeId in self.follow_map[followerId] and followerId != followeeId:
            self.follow_map[followerId].remove(followeeId)

    def getNewsFeed(self, userId):
        # Time complexity O(FlgnF)
        heap = []
        res = []
        self.follow_map[userId].add(userId)  # ad myself
        for followee in self.follow_map[userId]:  # get followees
            if followee in self.tweets:
                time, tweetId = self.tweets[followee][-1]
                idx = len(self.tweets[followee]) - 1
                heapq.heappush(heap, (-time, tweetId, followee, idx))
        while heap and len(res) < 10:
            time, tweetId, followee, idx = heapq.heappop(heap)
            res.append(tweetId)
            if idx > 0:
                idx -= 1
                time, tweetId = self.tweets[followee][idx]
                heapq.heappush(heap, (-time, tweetId, followee, idx))

        return res


if __name__ == '__main__':
    # happy path and <10 tweet
    # twitter = Twitter()
    # twitter.postTweet(1, 5)  # User 1 posts a tweet with id 5
    # assert twitter.getNewsFeed(1) == [5]  # returns [5]
    # twitter.follow(1, 2)  # User 1 follows User 2
    # twitter.postTweet(2, 6)  # User 2 posts a tweet with id 6
    # assert twitter.getNewsFeed(1) == [6, 5]  # returns [6,5]
    #
    # twitter.unfollow(1, 2)  # User 1 unfollows User 2
    # assert twitter.getNewsFeed(1) == [5]  # returns [5]

    # Test 2
    twitter = Twitter()
    twitter.postTweet(1, 5)  # User 1 posts 10 tweets
    twitter.postTweet(1, 10)  # User 1 posts 10 tweets
    print(twitter.getNewsFeed(1))  # ==   # returns [10,5]

    twitter.follow(1, 2)  # User 1 follows User 2
    twitter.postTweet(2, 6)  # User 2 posts a tweet with id 6
    print(twitter.getNewsFeed(1))  # == [6, 5]  # returns [6,10,5]

    twitter.unfollow(1, 2)  # User 1 unfollows User 2
    print(twitter.getNewsFeed(1))  # == [5]  # returns [10,5]
