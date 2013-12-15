__author__ = 'ericshape'
import sys

# Hashtag_Object define
class Hashtag_Object(object):
    #hashtag name
    name = ""


    def __init__(self, name):
        self.name = name
        self.number = 0

    def update(self):
        # update number
        self.number += 1

