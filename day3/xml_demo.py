import xml.etree.ElementTree as et

etree = et.parse('movies.xml')

print(etree)

root_tag = etree.getroot()

print(root_tag)

print(root_tag.tag)

print(root_tag.attrib)
print(root_tag.get('shelf'))
