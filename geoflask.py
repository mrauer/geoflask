from osmread import parse_file


def process_osm_file():
    for entity in parse_file('./data/switzerland-latest.osm.pbf'):
        if(len(entity.tags) > 0 and 'addr:city' in entity.tags
           and 'addr:street' in entity.tags):

            print ' '.join([entity.tags['addr:street'],
                            entity.tags['addr:city']])

            print entity.lon
            print entity.lat
