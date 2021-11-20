import esm

class AC(object):
    """ AC自动机最长匹配 """
    def __init__(self, words):
                
        self.ac = esm.Index()
        for k in words:
            self.ac.enter(k, k)
        self.ac.fix()

    def query(self, text):
        """ 最大长度匹配 """
        res = []
        matched = self.ac.query(text)
        matched.sort(key=lambda x: len(x[1]), reverse=True)

        ex_pos = []
        for pos, x in matched:
            bad = False
            for p in ex_pos:
                if not (pos[1] <= p[0] or pos[0] >= p[1]):
                    bad = True
                    break
            if bad:
                continue
            res.append((pos[-1], x))
            ex_pos.append(pos)

        res.sort(key=lambda x: x[0])
        res = [x[1] for x in res]
        return res
