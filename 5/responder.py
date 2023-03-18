import random


class Responder(object):
    def __init__(self, name):
        self.name = name

    def response(self, input):
        return ""


class RepeatResponder(Responder):
    def response(self, input):
        return "{}、ヨシ！！".format(input)


class RandomResponder(Responder):
    def __init__(self, name):
        super().__init__(name)
        self.responses = []
        rfile = open("dics/random.txt", "r", encoding="utf-8")
        r_lines = rfile.readlines()
        rfile.close()
        for line in r_lines:
            str = line.rstrip("\n")
            if str != "":
                self.responses.append(str)

    def response(self, input):
        return random.choice(self.responses)
