import sys
import os
import rapidjson as json


def parse_instances(instances):
    for instance in instances:
        print(instance)
        instance_output = {
            'type': instance.get('objectId').get('name'),
            'id': instance.get('name'),
            'x': instance.get('x'),
            'y': instance.get('y'),
            'xscale': instance.get('scaleX'),
            'yscale': instance.get('scaleY'),
        }
        

def parse_room_file(file):
    output = {}
    with open(file, 'r') as f:
        room = json.loads(f.read(), parse_mode=json.PM_TRAILING_COMMAS)
    for layer in room.get('layers'):
        output_layer = {
            'name': layer.get('name'),
            'type': layer.get('resourceType')
        }
        if (output_layer['type'] == 'GMRInstanceLayer'):
            output_layer['instances'] = parse_instances(layer.get('instances')) 
        elif (output_layer['type'] == 'GMRBackgroundLayer'):
            output_layer['background'] = layer.get('spriteId')
        print(output_layer)


def main(path_to_project):
    room_dir = "{}/rooms".format(path_to_project)
    rooms = os.listdir(room_dir)
    for room in rooms:
        print("Parsing room::{}".format(room))
        parse_room_file("{0}/{1}/{1}.yy".format(room_dir, room))


if __name__ == "__main__":
    main(sys.argv[1])
