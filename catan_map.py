import random as rand

class map_rules:
    """stores map rules used for configuring the map e.g number of each resourse, payout scaling ect"""
    def __init__(self) -> None:
        self.size = 4
        self.num_tiles = self.tile_count_recursion(self.size)
        self.num_resources = 6
        self.resources = ("stone", "brick", "wood", "wheat", "livestock", "desert")
        self.resource_num = {   "stone": 3,
                                "brick": 3,
                                "wood": 4,
                                "wheat": 4,
                                "livestock": 4,
                                "desert": 1 } 
        
    
    def tile_count_recursion(self, num):
        if num == 1 :
            return 1
        else:
            return 6*(num - 1) + self.tile_count_recursion(num - 1)

    



class catan_map:
    def __init__(self, rules=map_rules()) -> None:
        self.rules = rules
        self.node_list = []
        self.tile_list = []

        resource_dist = self.rules.resource_num
        resources_list = list(self.rules.resources)
        for tile_id in range(self.rules.num_tiles):
            #rand.sample(,count)
            resourse_id = 3
            temp_tile = tile(tile_id, resourse_id)
            self.tile_list.append(temp_tile)
            #print(temp_tile)
        print(self.tile_list)
            
            


    def show_map(self):
        print("show map called")

class tile:
    """map is made up of tiles, tile object has a material e.g. wood, stone"""
    def __init__(self, id, value) -> None:
        self.id = id
        self.value = value
    def __repr__(self):
        return "[{}, {}]".format(self.id, self.value)



class node:
    """a node is considered to be the corner where 2-3 tiles meet. stores state info such as whats built there """
    def __init__(self) -> None:
        self.id = 0
        self.value = 0

class border:
    """stores info on the edges of the tiles where roads are placed."""
    def __init__(self) -> None:
        self.id = 0
        self.value = 0
