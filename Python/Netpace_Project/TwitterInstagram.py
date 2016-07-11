#_author_ = 'chetna vig'
from instagram.client import InstagramAPI
from operator import itemgetter, attrgetter, methodcaller
import twitter
import oauth2 as oauth
import json
from TwitterWrapper import TwitterWrapper
from InstagramWrapper import InstagramWrapper
import time
import httplib2
import simplejson
import six
from ast import literal_eval
from VineWrapper import vineWrapper

class TrendingMedia:
    # This function gets all the latest twitter trends from Twitter for all the regions specified in "regions" list
	def get_TwitterTrends(self,regions):
		WR = TwitterWrapper()
		trends, trends_names = WR.getTrendsFromRegions(regions)   # trends has all the desired data related to a hashtag. trends_name is just a list of Hashtags which will then be passed onto Instagram to fetch images
		return trends_names

	# This function gets images and videos from Instagram based on trends given and also perform algorithms to get popular images and videos out of them
	def get_InstaMedia(self, trends_names):
		IW = InstagramWrapper()
		photos = IW.settrend_listPhotos(trends_names)
		popularphotos = IW.settrend_listPopularPhotos(trends_names)
		videos = IW.settrend_listVideos(trends_names)
		popularvideos = IW.settrend_listPopularVideos(trends_names)
		return photos,popularphotos,videos,popularvideos

	#This function gets videos from both Instagram and Vine based on trends/keywords/hashtags
	def get_videos(self, trends_names):
		videos1 = InstagramWrapper().settrend_listVideos(trends_names)
		videos2 = vineWrapper().settrend_vineSearch(trends_names)
		mergedlist = videos1 + videos2
		return mergedlist

