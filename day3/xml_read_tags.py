import xml.etree.ElementTree as et

etree = et.parse('movies.xml')

movie_tags =  etree.getiterator('movie')

for movie_tag in movie_tags:
    print(movie_tag.get('title'))

    for info_tag in movie_tag:
        print('\t', info_tag, ':', info_tag.text)

    print()