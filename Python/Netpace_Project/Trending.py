#__author__ = 'chetna vig'
from InstagramWrapper import InstagramWrapper
from TwitterWrapper import TwitterWrapper
from VineWrapper import vineWrapper
from operator import itemgetter, attrgetter, methodcaller
from com.mp.integrationv2.Post import Post
import json


class Trending():
    '''
	This function will return the list of trending stories/keywords in specific regions.
	@Input: List of regions

	@Return: Object of Trend
	'''
    def getTrendingKeywords(self,regions):
        tag, notag = TwitterWrapper().getTrends(regions)

        return  tag,notag

	'''
	This function will return the object of Images for a specfic keyword
	@Input: String keyword/hashtag
	@Return: Return the Object of Results
	'''
    def getImagesForKey(self, keyword, count):
        Allphotos = InstagramWrapper().getMediaObjectImages(keyword,count)

        return Allphotos  # This is a list of Media object directly from Instagram  with no sorting. It has type, link, comments_count, like_count and weight.

	'''
	This function will return the object of Videos for a specfic keyword
	@Input: String keyword/hashtag
	@Return: Return the Object of Results
	'''
    def getVideosForKey(self, keyword,count):
        Allvideos = InstagramWrapper().getMediaObjectVideos(keyword,count)
        return  Allvideos

	'''
	This function will return the object of Popular Images for a specfic keyword
	@Input: String keyword/hashtag
	@Return: Return the Object of Results
	'''
    def getPopularImagesForKey(self, keyword, count):
        
        photos = InstagramWrapper().searchPopularPhotos(keyword,count)
        list = []
        for photo in photos:
           list.append(str( photo.getLink()))
          
        return  list
	'''
	This function will return the object of Popular Images for a specfic keyword
	@Input: String keyword/hashtag
	@Return: Return the Object of Results
	'''
    def getRecentImagesForKey(self, keyword, count):
        
        photos = InstagramWrapper().searchRecentPhotos(keyword,count)
        list = []
        for photo in photos:
           list.append(str( photo.getLink()))
           
        return  list

	'''
	This function will return the object of List of Latest Video for a specfic keyword
	@Input: String keyword/hashtag
	@Return: Return the Object of Results
	'''
    def getRecentVideosForKey(self, keyword,count):
        
        videos = InstagramWrapper().searchRecentVideos(keyword,count)
        
        list = []
        for video in videos:
           list.append(str( video.getLink()))
           
        return  list


    '''
    This function will return the object of List of Popular Video for a specfic keyword
    @Input: String keyword/hashtag
    @Return: Return the Object of Results
    '''
    def getPopularVideosForKey(self, keyword,count):
       
        videos = InstagramWrapper().searchPopularVideos(keyword,count)
          
        list = []
        for video in videos:
           list.append(str( video.getLink()))
           
        return  list

    '''
    This function will return a string in json format which contains sorted Posts based on number of likes and comments of a particular Instagram Post for a specific keyword
    @Input: Json String containing all the attributes (like key, id, likeCount, commentsCount etc.) of Instagram posts i.e. Images/Videos
    @Return: Return a string in json format which is sorted based on popularityIndex
    '''
    def SortByPopularityIndex(self, s):
        #This function will sort the images fetched from database on the basis of popularity index which is a number (likes + 5*comments)
        Media = []
        for media in s:
             Media.append(Post(media['key'], media['id'],  media['standardResolution'], media['lowResolution'],media['thumbnail'],  media['jobid'],  media['likeCount'],  media['commentsCount']))

        popularMedia = sorted(Media, key= methodcaller('weighted_popularity') ,reverse=True)
        dd = []
        for each in popularMedia:
            dd.append({"key" :each.key, "id" : each.id, "standardResolution": each.link_standard, "lowResolution": each.link_low, "thumbnail": each.link_thumbnail, "jobid" : each.jobid, "likeCount": each.likes, "commentsCount":each.comments, "popularityIndex": each.weight})
        popularMediajson = json.dumps(dd)
        return popularMediajson

