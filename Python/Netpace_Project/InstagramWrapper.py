#__author__ = 'chetna vig'
'''
This is an Instagram Wrapper which interacts with Instagram and get required images and videos based on a hashtag. In this, I 
have written several functions like getting recent photos/videos vs popular photos/videos. 
'''
from instagram.client import InstagramAPI
from operator import itemgetter, attrgetter, methodcaller
#__author__ = 'chetna vig'

import inspect
from com.mp.integrationv2.Post import Post
import json

class InstagramWrapper():
	# This id is specific to user who has made an app to use Instagram API.
    client_id= 'xxxxxxx'
    client_secret= 'yyyyyyy'

    def __int__(self):
        return None
	
	#Validating input to the function i.e. whether the trend we are looking for is in desired format or not.
    def searchstring(self, s):
        s=str(s.encode('ascii','replace')).replace('\'','\'\'')
        s = filter(str.isalnum, s)
        if s == '':
            print('empty or invalid string input...  continuing with \"news\"')
            s = 'news'
        return s

	# This function gets images related to a tag and number of images it gets equals the count.
    def getMediaObjectImages(self,tag,count):
        MediaObjectImages = []
        MediaObject = []
        k=0
        m=0
        l=0
        if count == 0:
            return MediaObjectImages
        tag = self.searchstring(tag)
        api = InstagramAPI(client_id=self.client_id, client_secret= self.client_secret)
        recent_media, next_ = api.tag_recent_media(count = 70, tag_name = tag)
        for media in recent_media:
            if media.type == 'image':
                MediaObjectImages.append(Post(str(media.images['standard_resolution']).split('Image: ')[1],
                                              str(media.images['low_resolution']).split('Image: ')[1], str(media.images['thumbnail']).split('Image: ')[1],
                                              media.type, media.like_count, media.comment_count))
                if len(MediaObjectImages) >= count:
                    while k< len(MediaObjectImages):
                        MediaObject.append(json.dumps(MediaObjectImages[k].__dict__))
                        k = k+1
                    return MediaObject
        i=0

        while i<20 and next_:
            recent_media, next_ = api.tag_recent_media(count=70, tag_name=self.searchstring(tag), with_next_url=next_)
            for media in recent_media:
                if media.type == 'image':
                    MediaObjectImages.append(Post(str(media.images['standard_resolution']).split('Image: ')[1],
                                              str(media.images['low_resolution']).split('Image: ')[1], str(media.images['thumbnail']).split('Image: ')[1],
                                              media.type, media.like_count, media.comment_count))
                    if len(MediaObjectImages) >= count:
                        while l< len(MediaObjectImages):
                            MediaObject.append(json.dumps(MediaObjectImages[l].__dict__))
                            l = l+1
                        return MediaObject
            i += 1
   
        while m< len(MediaObjectImages):
            MediaObject.append(json.dumps(MediaObjectImages[k].__dict__))
            m = m+1
        return MediaObject


	# # This function gets videos related to a tag and number of videos it gets equals the count.
    def getMediaObjectVideos(self,tag,count):
        MediaObjectVideos = []
        MediaObject = []
        k = 0
        if count == 0:
            return MediaObjectVideos
        tag = self.searchstring(tag)
        api = InstagramAPI(client_id=self.client_id, client_secret= self.client_secret)
        recent_media, next_ = api.tag_recent_media(count = 70, tag_name = tag)
        for media in recent_media:
            if media.type == 'video':
                MediaObjectVideos.append(Post(str(media.videos['standard_resolution']).split('Video: ')[1],
                                              str(media.videos['low_resolution']).split('Video: ')[1], str(media.videos['low_bandwidth']).split('Video: ')[1],
                                              media.type, media.like_count, media.comment_count))
                if len(MediaObjectVideos) >= count:
                    while k< len(MediaObjectVideos):
                        MediaObject.append(json.dumps(MediaObjectVideos[k].__dict__))
                        k = k+1
                    return MediaObject
        i = 0
        l = 0
        m = 0
        while i<20 and next_:
            recent_media, next_ = api.tag_recent_media(count=70, tag_name=self.searchstring(tag), with_next_url=next_)
            for media in recent_media:
                if media.type == 'video':
                    MediaObjectVideos.append(Post(str(media.videos['standard_resolution']).split('Video: ')[1],
                                              str(media.videos['low_resolution']).split('Video: ')[1], str(media.videos['low_bandwidth']).split('Video: ')[1],
                                              media.type, media.like_count, media.comment_count))
                    if len(MediaObjectVideos) >= count:
                        while l< len(MediaObjectVideos):
                            MediaObject.append(json.dumps(MediaObjectVideos[l].__dict__))
                            l = l+1
                        return MediaObject
            i += 1

        while m< len(MediaObjectVideos):
            MediaObject.append(json.dumps(MediaObjectVideos[m].__dict__))
            m = m+1

        return 	MediaObject
	
	# This function gets most recent images related to a tag and number of images it gets equals the count given. 
    def searchRecentPhotos(self, tag, count):
        photos = []
        if count == 0:
            return photos
        tag = self.searchstring(tag)
        api = InstagramAPI(client_id= self.client_id, client_secret= self.client_secret)
        recent_media, next_ = api.tag_recent_media(count=50, tag_name=tag)
        for media in recent_media:
            if media.type == 'image':
                photos.append(Post(media.images['standard_resolution'], media.type, media.like_count, media.comment_count))
                if len(photos) >= count:
                    return 	photos  
        i=0

        while i<10 and next_:
            recent_media, next_ = api.tag_recent_media(count=50, tag_name=self.searchstring(tag), with_next_url=next_)
            for media in recent_media:
                if media.type == 'image':
                    photos.append(Post(media.images['standard_resolution'], media.type, media.like_count, media.comment_count))
                    if len(photos) >= count:
                        return 	photos  
            i += 1
        return 	photos   

	# This function gets most popular images related to a tag and number of images it gets equals the count given.Popularity of an image is 
	# decided by "weighted_popularity" index which is declared in "Post" class defined separately
    def searchPopularPhotos(self, tag, count):
        photos = []
        if count == 0:
            return photos
        tag = self.searchstring(tag)
        api = InstagramAPI(client_id= '7d428aff533f40e1b3d5f919882576d2', client_secret= 'bfbe419a758141fbaf352c89b579a0a5')
        recent_media, next_ = api.tag_recent_media(count=50, tag_name=tag)
        for media in recent_media:
            if media.type == 'image':
                photos.append(Post(media.images['standard_resolution'], media.type, media.like_count, media.comment_count))
                if len(photos) >= count:
                    popularphotos = sorted(photos, key=methodcaller('weighted_popularity'),reverse=True)
                    return 	popularphotos
        i=0
        if len(photos) >= count:
            popularphotos = sorted(photos, key=methodcaller('weighted_popularity'),reverse=True)
            return 	popularphotos
        else:
            while i<10 and next_:
                recent_media, next_ = api.tag_recent_media(count=50, tag_name=self.searchstring(tag), with_next_url=next_)
                for media in recent_media:
                    if media.type == 'image':
                        photos.append(Post(media.images['standard_resolution'], media.type, media.like_count, media.comment_count))
                        if len(photos) >= count:
                            popularphotos = sorted(photos, key=methodcaller('weighted_popularity'),reverse=True)
                            return 	popularphotos
            i += 1
        popularphotos = sorted(photos, key=methodcaller('weighted_popularity'),reverse=True)
        return 	popularphotos

    def searchRecentVideos(self, tag, count):
        videos = []
        if count == 0:
            return videos
        tag = self.searchstring(tag)
        api = InstagramAPI(client_id= '7d428aff533f40e1b3d5f919882576d2', client_secret= 'bfbe419a758141fbaf352c89b579a0a5')
        recent_media, next_ = api.tag_recent_media(count=50, tag_name=tag)
        for media in recent_media:
            if media.type == 'video':
                videos.append(Post(media.videos['standard_resolution'], media.type, media.like_count, media.comment_count))
                if len(videos) >= count:
                    return videos
        
        i=0
        
        if count < 50:
            return 	videos
        else:
            while i<10 and next_:
                recent_media, next_ = api.tag_recent_media(count=50, tag_name=self.searchstring(tag), with_next_url=next_)
                for media in recent_media:
                    if media.type == 'video':
                        videos.append(Post(media.videos['standard_resolution'], media.type, media.like_count, media.comment_count))
                        if len(videos) >= count:
                            return 	videos
            i += 1
        return 	videos
	
	# This function gets most popular videos related to a tag and number of videos it gets equals the count given.Popularity of a video is 
	# decided by "weighted_popularity" index which is declared in "Post" class defined separately
    def searchPopularVideos(self, tag, count):
        videos = []
        if count == 0:
            return videos
        tag = self.searchstring(tag)
        api = InstagramAPI(client_id= '7d428aff533f40e1b3d5f919882576d2', client_secret= 'bfbe419a758141fbaf352c89b579a0a5')
        recent_media, next_ = api.tag_recent_media(count=50, tag_name=tag)
        for media in recent_media:
            if media.type == 'video':
                videos.append(Post(media.videos['standard_resolution'], media.type, media.like_count, media.comment_count))
                if len(videos) >= count:
                    popularvideos = sorted(videos, key=methodcaller('weighted_popularity'),reverse=True)
                    return popularvideos
        i=0
        if len(videos) >= count:
            popularvideos = sorted(videos, key=methodcaller('weighted_popularity'),reverse=True)
            return 	popularvideos
        else:
            while i<10 and next_:
                recent_media, next_ = api.tag_recent_media(count=50, tag_name=self.searchstring(tag), with_next_url=next_)
                for media in recent_media:
                    if media.type == 'video':
                        videos.append(Post(media.videos['standard_resolution'], media.type, media.like_count, media.comment_count))
                        if len(videos) >= count:
                            popularvideos = sorted(videos, key=methodcaller('weighted_popularity'),reverse=True)
                            return 	popularvideos
            i += 1
        popularvideos= sorted(videos, key=methodcaller('weighted_popularity'),reverse=True)
        return 	popularvideos
	
	# This function basically gets videos but for entire list of trends given to it and not just a hashtag. It returns a list.
    def settrend_listPhotos(self, trends, count):
        trends_list = trends
        photos1 =[]

        for each in trends_list:
            tag = each
            photos = self.searchRecentPhotos(tag, count)
            photos1 = photos1 + photos

        return photos1
	
	# This function basically gets Popular photos but for entire list of trends given to it and not just a hashtag
    def settrend_listPopularPhotos(self, trends, count):
        trends_list = trends
        popularphotos1 =[]

        for each in trends_list:
            tag = each
            popularphotos = self.searchPopularPhotos(tag, count)
            popularphotos1 = popularphotos1 + popularphotos

        return popularphotos1
	
	# This function basically gets videos but for entire list of trends given to it and not just a hashtag. It returns a list.
    def settrend_listVideos(self, trends_list, count):
        videos1 =[]

        for each in trends_list:
            videos = self.searchRecentVideos(each, count)
            videos1 = videos1 + videos

        return videos1
	
	# This function basically gets Popular videos but for entire list of trends given to it and not just a hashtag
    def settrend_listPopularVideos(self, trends_list, count):
        popularvideos1 =[]

        for each in trends_list:
            popularvideos = self.searchPopularVideos(each, count)
            popularvideos1 = popularvideos1 + popularvideos

        return popularvideos1



