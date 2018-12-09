import xml.etree.ElementTree as et

etree = et.parse('movies.xml')

root_tag = etree.getroot()

# pp(dir(root_tag))
# exit(1)
# pp(root_tag.getchildren())
# root_tag.findall('.') -> xpath way
# roo_tag.findall("./movie[@title='Trigun']")
# root_tag.iterfind('title')
for movie_tag in (root_tag[0], root_tag[-1]):
    print(movie_tag.get('title'))

    for info_tag in movie_tag:
        print('\t', info_tag, ':', info_tag.text)

    print()
