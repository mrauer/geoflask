import geoflask

osm_file_path = './data/switzerland-latest.osm.pbf'

entities = geoflask.process_osm_file(osm_file_path)

print geoflask.write_to_file(entities)
