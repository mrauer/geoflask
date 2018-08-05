import json
import os

from osmread import parse_file


def process_osm_file(osm_file_path, limit):
    """Process OSM file, converting to a list of dict.

    Keyword arguments:
    osm_file_path          --  str path of the OSM file
    limit                  --  number of records to store

    Returns:
    entities_list          --  list of dict
    """
    entities_list = list()
    osm_file = parse_file(osm_file_path)
    for i, entity in enumerate(osm_file):
        print '|'.join([str(i), str(len(entities_list))])
        try:
            if len(entity.tags) > 0 and entity.lat and entity.lon:
                loc = ','.join([str(entity.lat), str(entity.lon)])

                entities = dict()

                response = list()
                indexable = set()

                if 'name' in entity.tags:
                    response.append(entity.tags['name'])

                if 'addr:housenumber' in entity.tags:
                    response.append(entity.tags['addr:housenumber'])

                if 'addr:street' in entity.tags:
                    response.append(entity.tags['addr:street'])

                if 'addr:city' in entity.tags:
                    response.append(entity.tags['addr:city'])

                if 'postal_code' in entity.tags:
                    response.append(entity.tags['postal_code'])

                if len(response) == 0:
                    continue
                response = ','.join(response)
                for key, value in entity.tags.iteritems():
                    indexable.add(value)
                indexable = ' '.join(indexable)

                entities['id'] = len(entities_list) + 1
                entities['fields'] = {}
                entities['fields']['response'] = response
                entities['fields']['indexable'] = indexable
                entities['fields']['location_field'] = loc
                entities['type'] = 'add'

                print entities
                entities_list.append(entities)
        except Exception, e:
            print e
            pass
        if len(entities_list) == limit:
            break
    print len(entities_list)
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
