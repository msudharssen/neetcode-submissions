class Twitter:

    def __init__(self):
        self.postingTweets = defaultdict(list)
        self.followers = defaultdict(set)
        self.count = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.postingTweets[userId].append([self.count, tweetId])
        self.count-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        allTweets = []
        self.followers[userId].add(userId)
        for value in self.followers[userId]:
            if value in self.postingTweets:
                index = len(self.postingTweets[value])-1
                count, tweetId = self.postingTweets[value][index]
                allTweets.append([count, tweetId, value, index-1])

        heapq.heapify(allTweets)
        result = []
        while allTweets and len(result)<10:
            count, tweetId, value, index = heapq.heappop(allTweets)
            result.append(tweetId)
            if index >= 0:
                count, tweetId = self.postingTweets[value][index]
                heapq.heappush(allTweets, [count, tweetId, value, index-1])
        return result


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
