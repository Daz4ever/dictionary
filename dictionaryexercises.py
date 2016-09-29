from sys import argv

script, filename = argv

readfile = open(filename, "r")






paragraph = readfile.read()
paragraph = paragraph.lower()

paragraph = paragraph.replace('.', '').replace('(', '').replace(')', '').replace("\n", "").replace(",","").replace("!","")
text = paragraph.split()
print text




counts ={}

for word in text:
    counter = counts.get(word, 0)
    counts[word] = counter + 1


for word, count in counts.items():
    print "%d %s's" % (count, word)


# #exercise 1
# phonebook_dict = {
#   'Alice': '703-493-1834',
#   'Bob': '857-384-1234',
#   'Elizabeth': '484-584-2923'
#   }
#
#
# print phonebook_dict["Elizabeth"]
#
#
# phonebook_dict["Kareem"] = '968-345-2345'
#
# print phonebook_dict["Kareem"]
#
# del phonebook_dict["Alice"]
#
# print phonebook_dict.get("Alice, none")
#
# phonebook_dict["Bob"] = '968-345-2345'
#
# print phonebook_dict["Bob"]
#
# print phonebook_dict
#
#
# #exercise 2
#
# ramit = {
#   'name': 'Ramit',
#   'email': 'ramit@gmail.com',
#   'interests': ['movies', 'tennis'],
#   'friends': [
#     {
#       'name': 'Jasmine',
#       'email': 'jasmine@yahoo.com',
#       'interests': ['photography', 'tennis']
#     },
#     {
#       'name': 'Jan',
#       'email': 'jan@hotmail.com',
#       'interests': ['movies', 'tv']
#     }
#   ]
# }
#
# print ramit["email"]
#
# print ramit["interests"][0]
#
# print ramit["friends"][0]["email"]
#
# print ramit["friends"][1]["interests"][1]
#
#
