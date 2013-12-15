__author__ = 'ericshape'

import Hashtag_Object

# Node_Object define
class Node_Object(object):
    name = ""

    def __init__(self, name):
        self.name = name
        self.hashtag_list = {}

    def update_hashtag(self, hashtag_name):

        #if the first time to add hashtag to this node
        if not (hashtag_name in self.hashtag_list.keys()):
            self.hashtag_list[hashtag_name] =  Hashtag_Object.Hashtag_Object(hashtag_name)

        hashtag_object = self.hashtag_list[hashtag_name]
        hashtag_object.update()

def make_object(name):
    node_object = Node_Object(name)
    node_object.update_hashtag('abc')
    node_object.update_hashtag('abc')
    return node_object

