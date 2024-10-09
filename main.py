from catan_map import catan_map, map_rules

def main():
    print("Hello world!")
    world_map = catan_map()
    world_map.show_map()
    rules = map_rules()
    #print(rules.resources[0])
    #print(rules.resource_num["stone"])
ff

if __name__ == "__main__":
    main()