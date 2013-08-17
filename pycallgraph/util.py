from __future__ import division


class Util(object):

    @staticmethod
    def human_readable_bibyte(num):
        for x in ['B', 'KiB', 'MiB', 'GiB']:
            if num < 1024 and num > -1024:
                return '{:3.1f}{}'.format(num, x)
            num /= 1024
        return '{:3.1f}{}'.format(num, 'TB')
