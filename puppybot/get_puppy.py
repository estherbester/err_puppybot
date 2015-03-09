# Class that uses Flickr to fetch photos of dogs

from random import randint
from random import choice

import plugins.puppybot.flickr as flickr

from plugins.puppybot.secret_settings import (API_KEY,
                                             API_SECRET)

from plugins.puppybot.throttler import Throttler

from plugins.puppybot.plugin_config import (AVAILABLE_COMMANDS,
                                            PHOTOS_PER_PAGE,
                                            MAX_API_CALLS)


flickr.API_KEY = API_KEY
flickr.API_SECRET = API_SECRET


class PuppyFetch(object):
    """
    TODO: 

    * make fewer API calls
    * Rename since we don't just get puppies
    """
    reply_string = "{prefix}: {msg}"

    throttler = Throttler('flickr', MAX_API_CALLS)

    def __init__(self, puppy_type):
        self.puppy_type = puppy_type
        groups = self.get_dict_for('flickr_group_id')
        self.group = flickr.Group(groups[puppy_type])

    @staticmethod
    def get_dict_for(property_name):
        # return a dict keyed on puppytype for hte attribute we want to retrieve
        # from the PuppyCommand named tuple
        return dict(
            [(pc.puppy_type, getattr(pc, property_name)) for pc in AVAILABLE_COMMANDS])
    
    @staticmethod
    def get_command_list():
        return dict([(pc.command, pc.puppy_type) for pc in  AVAILABLE_COMMANDS])

    @classmethod
    @throttler.track
    def get(cls, puppy_type):
        message = "Sorry, can't get an image =("
        try:
            command = cls(puppy_type)
            replies = cls.get_dict_for('reply_prefix')
            prefix = replies[puppy_type]
            #print "fetching url"
            result = command._get_flickr_photo()
            photo_url = cls.get_photo_url(result)
            message = command.reply_string.format(prefix=prefix, msg=photo_url)
        except flickr.FlickrError as error:
            message = "Error in PuppyFetch: %s" % error
        # TODO: log a message
        except (NameError, KeyError) as error: 
            print error
            pass
        #else:
            # TODO: this should not be a blocking call.
            #if TWEET_RESULT:
            #    from .twitterbot import tweet_result, TweetBotError
            #    try:
            #        tweet_result(puppy_type, result)
            #    except TweetBotError as error:
            #        print "Tweetbot error: %s" % error
        return message

    def _get_flickr_photo(self):
        """ 
        a flickr Photo object looks like this::

            photo.id, 
            owner=owner, 
            title=title, 
            ispublic=ispublic,
            isfriend=isfriend, 
            isfamily=isfamily, 
            secret=secret, 
            server=server

        :returns: flickr.photo object 
        """
        photo = None
        counter = 1
        while photo is None and counter < 3:
            try:
                random_page = self._select_random_page()
                photo = self._select_random_photo(random_page)
            except (AttributeError, flickr.FlickrError) as e:
                #print "Error: %s" % e
                counter += 1

        # This could be better
        if photo is None:
            # Since we failed at randomizing just get one from the first
            # page of results
            #print "Randomized fetching failed. Getting one from the front page"
            photo = self._select_random_photo(1, 100)
        return photo

    def _select_random_page(self, per_page=PHOTOS_PER_PAGE):
        """ Pick a page, any page. """
        number_of_pages = self.group.poolcount / per_page
        return randint(1, number_of_pages)

    def _select_random_photo(self, page_number, per_page=PHOTOS_PER_PAGE):
        # Trying to randomize the fetch a bit, limited by the number of photos
        # in the group
        photos = self.group.getPhotos(per_page=per_page,
                                      page=page_number)
        return choice(photos)

    @staticmethod
    def get_photo_url(photo):
        """ 
        we default to medium as it works well most times; getLarge and 
        getSmall work too. 
        """
        url = photo.getMedium()
        if url:
            return url
        raise flickr.FlickrError, "No URL found"


if __name__ == '__main__':
    import sys
    try:
        group = sys.argv[1]
        print PuppyFetch.get_dict_for('command')
        command = PuppyFetch.get(group)

        print command
    except IndexError:
        print "Please specify a group"
