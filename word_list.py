class WordList:
    @property
    def all(self):
        f = open('anadict.txt','r')
        anadict = f.read().split('\n')
        f.close()
        return anadict

    @property
    def words(self):
        f = open('../sowpods.txt','r')
        anadict = f.read().split('\n')
        f.close()
        return anadict
