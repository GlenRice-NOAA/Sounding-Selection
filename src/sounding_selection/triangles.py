class Triangle(object):
    """ A Triangle is encoded as the triple of the indexes of its vertices in the Vertex array. """
    def __init__(self, v1, v2, v3):
        self.__v_ids = [v1, v2, v3]
        self.__visit = False

    def get_TV(self, pos):
        try:
            return self.__v_ids[pos]
        except IndexError as e:
            raise e

    def set_TV(self, pos, new_id):
        try:
            self.__v_ids[pos] = new_id
        except IndexError as e:
            raise e

    def get_vertices_num(self):
        return 3

    def __str__(self):
        return "%s %s %s" % (self.__v_ids[0], self.__v_ids[1], self.__v_ids[2])
