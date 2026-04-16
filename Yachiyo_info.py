import time
import string

yachiyo = {'name': 'yachiyo','age':'8000','friend':['iroha','Fushi']}


def get_info(info):
    return yachiyo.get(info)
def change_info(what_info):
    yachiyo.update(what_info)