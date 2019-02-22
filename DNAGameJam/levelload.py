from xml.dom import minidom
def go():
    mydoc = minidom.parse('test.tmx')

    platform = mydoc.getElementsByTagName('object')
    
    print("test: ")
    print(platform[1].attributes['id'].value);
    print("test ended")
