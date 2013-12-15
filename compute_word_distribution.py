__author__ = 'ericshape'

import re
import string
import urllib
from PIL import Image, ImageDraw
import glob
import math
import collections

import Node_Object

searchWordsList = collections.defaultdict(set)

for uid in range(1,27):

    #load files in subdirectory
    folderLoacation = "/Users/ericshape/project/2012_TagCloud_user_study/user_data/" + str(uid) + "/"
    len_folderLocation = len(folderLoacation)
    #mouse move file
    fileType_move = "*Move_Log.dat"
    moveFileList = glob.glob(folderLoacation+fileType_move)
    #search list file
    fileType_search = "*Search_Log.dat"
    searchFileList = glob.glob(folderLoacation+fileType_search)

    im = Image.new('RGBA', (1024, 768), (255, 255, 255, 0))
    draw = ImageDraw.Draw(im)

    x_postion = 0
    y_postion = 0



    for file_entity in moveFileList:
        i = 0
        moveDistance = 0
        search_word = ""
        hoverWords = 0

        for line in open(file_entity, 'r').readlines():
            line_split = line.strip().split('\t')

            if len(line_split) > 3:
                cur_x = int(line_split[3])
                cur_y = int(line_split[4])
                cur_word = line_split[2]

                if i == 0:
                    x_postion = cur_x
                    y_postion = cur_y
                    search_word = cur_word

                draw.line((x_postion, y_postion, cur_x, cur_y), fill=128)

                moveDistance += math.hypot(cur_x - x_postion, cur_y - y_postion)

                x_postion = cur_x
                y_postion = cur_y

                if search_word != cur_word and i != 0:
                    #output words
                    #print search_word
                    hoverWords += 1

            search_word = cur_word

            i += 1

        #number_search_hit
        numberSearchHit = 0
        for line in open(file_entity[:-18]+"Search_Log.dat", 'r').readlines():
            line_split = line.strip().split('\t')
            if line_split != [""]:
                numberSearchHit += 1
                searchWordsList[file_entity[len_folderLocation:-18]].add(line_split[2])

        rate = 0

        if hoverWords!= 0:
            rate = numberSearchHit/(hoverWords*1.0)

        print uid, file_entity[len_folderLocation:-18], hoverWords, numberSearchHit, rate, int(moveDistance)

for searchWordsEntity in searchWordsList:
    print searchWordsEntity, ", ", searchWordsList[searchWordsEntity]

# im.show()