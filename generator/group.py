from model.group import Group
import random
import string
import jsonpickle
import os.path
import getopt # https://docs.python.org/3/library/getopt.html
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

# default values
n = 5
f = "data/groups.json"

# parameters values from script configuration (Lection 6.4. )
for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10 # + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = \
    [
        Group(name="11111", header="1111111", footer="1111111"),
        Group(name="", header="", footer="")
    ]+[
        Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
        for i in range(n)
    ]
#+[Group(name=name, header=header, footer=footer)
#  for name in ["", random_string("name", 10)]
#for header in ["", random_string("header", 20)]
#for footer in ["", random_string("footer", 20)]
#  ]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

# закоментировано после смены библиотеки для обработки json с json на jsonpickle
# with open(file, "w") as out:
#    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
