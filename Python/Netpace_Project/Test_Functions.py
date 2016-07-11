#__author__ = 'chetna vig'
#This file contains all the test function for different functions

from TwitterInstagram import TrendingMedia
from InstagramWrapper import InstagramWrapper
from TwitterWrapper import TwitterWrapper
from TwitterHashtagSearchSorted import TwitterHashtagSearchSorted
from VineWrapper import vineWrapper
from operator import itemgetter, attrgetter, methodcaller

def test_TwitterInstagram():
    regions = ['23424848', '23424977']                 
    trends = TwitterInstagram().get_TwitterTrends(regions)
    photos,sortedphotos,videos,sortedvideos = TwitterInstagram().get_InstaMedia(trends)
    print photos,sortedphotos,videos,sortedvideos


def test_TwitterWrapper():
    regions = ['23424977', '23424848']
    trends, trends_names = TwitterWrapper().displayTrend_func(regions)
    print trends
    print trends_names

def test_InstagramWrapper():
    trends = ['Tom Cruise', 'Car', 'Festival']
    photos = InstagramWrapper().settrend_listPhotos(trends)
    print photos

def test_TwitterHashtagSearchSorted():

    #Testing for getting tweets and sorted tweets for each hashtag
    tag_list = []
    tw =[]
    tws = []
    count  = 20
    with open("abc.txt", 'r') as f:
        tag_list = f.readlines()
    for each in tag_list:
        TwitterList = TwitterHashtagSearchSorted().getTwitterFeed(each, count)    # second argument tells the count of tweets that we want to fetch for each hashtag
        tw.append(TwitterList)
        TwitterListPopular = TwitterHashtagSearchSorted().getTwitterFeedPopular(each,count)
        tws.append(TwitterListPopular)
    
    mergedtags = TwitterHashtagSearchSorted().get_Related_Tags(tw[0])
    print mergedtags
    mergedtagspopular = TwitterHashtagSearchSorted().get_Related_Tags(tws[0])
    print mergedtagspopular

def test_vineWrapper():
    tag = 'Car'
    vines = vineWrapper().vineSearch(tag) #get the return value from Vine
    svines = vineWrapper().vineSearchPopular(tag)
    print vines
    print svines






