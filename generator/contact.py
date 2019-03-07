from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 1
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    symbols2 = string.ascii_letters + string.digits
    if prefix == "email" or prefix == "email2" or prefix == "email3":
        return prefix + "".join([random.choice(symbols2) for i in range(random.randrange(maxlen))]) + "@mail.ru"
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", email="", email2="", email3="", homephone="", workphone="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 15), lastname=random_string("lastname", 12),
            nickname=random_string("nickname", 10), email=random_string("email", 10), email2=random_string("email2", 10),
            email3=random_string("email3", 10), homephone=random_string("homephone", 10), workphone=random_string("workphone", 10))
    for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))


