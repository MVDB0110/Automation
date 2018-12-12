import xml.etree.ElementTree

tree = xml.etree.ElementTree.parse('netwerk.xml')
root = tree.getroot()

for client in root[1]:
    string = client.tag
    for element in client:
        string += " " + element.text
    print(string)