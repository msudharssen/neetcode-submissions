class Twitter:

    def __init__(self):
        self.twitterMap = defaultdict(list)
        self.followersMap = defaultdict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.twitterMap[userId].append([self.count, tweetId])
        self.count-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        allTweets = []
        self.followersMap[userId].add(userId)
        for followee in self.followersMap[userId]:
            if followee in self.twitterMap:
                index = len(self.twitterMap[followee])-1
                count, tweetId = self.twitterMap[followee][index]
                allTweets.append([count, tweetId, followee, index-1])
        
        heapq.heapify(allTweets)

        while allTweets and len(result)<10:
            count, tweetId, followee, index = heapq.heappop(allTweets)
            result.append(tweetId)
            if index >=0:
                count, tweetId = self.twitterMap[followee][index]
                heapq.heappush(allTweets, [count, tweetId, followee, index-1])
        return result



    def follow(self, followerId: int, followeeId: int) -> None:
        self.followersMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followersMap[followerId]:
            self.followersMap[followerId].remove(followeeId)
