class Dictionary(object):
    def __init__(self):
        self.random = self.makeRandomList()
        self.pattern = self.makePatternDictionary()

    def makeRandomList(self):
        rfile = open("dics/random.txt", "r", encoding="utf-8")
        r_lines = rfile.readlines()
        rfile.close()

        randomList = []
        for line in r_lines:
            str = line.rstrip("\n")
            if str != "":
                randomList.append(str)
        return randomList

    def makePatternDictionary(self):
        pfile = open("dics/pattern.txt", "r", encoding="utf-8")
        p_lines = pfile.readlines()
        pfile.close()

        new_lines = []
        for line in p_lines:
            str = line.rstrip("\n")
            if str != "":
                new_lines.append(str)

        patternDictionary = {}
        for line in new_lines:
            ptn, prs = line.split("\t")
            patternDictionary.setdefault("pattern", []).append(ptn)
            patternDictionary.setdefault("phrases", []).append(prs)
        return patternDictionary
