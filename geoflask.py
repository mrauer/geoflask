import json
import os

from osmread import parse_file


def process_osm_file(osm_file_path):
    """Process OSM file, converting to a list of dict.

    Keyword arguments:
    osm_file_path          --  str path of the OSM file

    Returns:
    entities_list          --  list of dict
    """
    entities_list = list()
    osm_file = parse_file(osm_file_path)
    for entity in osm_file:
        if(len(entity.tags) > 0 and 'addr:city' in entity.tags
           and 'addr:street' in entity.tags):
            entities = dict()
            loc = ','.join([str(entity.lat), str(entity.lon)])
            text = ' '.join([entity.tags['addr:street'],
                             entity.tags['addr:city']])

            entities['id'] = len(entities_list) + 1
            entities['fields'] = {}
            entities['fields']['text'] = text
            entities['fields']['location_field'] = loc

            print entities
            entities_list.append(entities)
        if len(entities_list) == 50000:
            break
    return entities_list


def write_to_file(entities):
    """Write to a JSON file"""
    file = 'data.json'
    f = open(file, 'w')
    f.write(json.dumps(entities))
    f.close()
    return sizeof_fmt(os.path.getsize(file))


def sizeof_fmt(num, suffix='B'):
    """Convert size of directory in readable units."""
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)
