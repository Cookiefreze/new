import time
import string

yachiyo = {'name': 'yachiyo','age':'8000','friend':['iroha','Fushi']}


def get_info(info):
    #read which info you want
    return yachiyo.get(info)
def change_info(what_info):
    #chenge or add info to the dict
    yachiyo.update(what_info)