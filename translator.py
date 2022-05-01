# coding: utf-8
from lxml import etree

# Global variables
file = "stringtable.xml"

# Core
tree = etree.parse(file)
count_package = 0
count_key = 0

# Count
for package in tree.xpath("/Project/Package"):
    count_package += 1
for key in tree.xpath("/Project/Package/Key"):
    count_key += 1

print("Packages: " + str(count_package))
print("Keys: " + str(count_key))

for package in tree.xpath("/Project/Package"):
    print("Package: " + package.attrib["name"])