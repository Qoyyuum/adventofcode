import hashlib

class AdventCoin:
    def __init__(self, key):
        self.key = key

    def mine(self):
        #for num in count():
        num = 1
        while True:
            self.coin = self.key + str(num)
            result = hashlib.md5(self.coin.encode('utf-8')).hexdigest()
            #print(f"{self.coin = } {result = }")
            if result.startswith('00000'):
                break
            num += 1
        self.md5hash = result
        self.lowest_number = str(num)
        return self.md5hash

if __name__ == '__main__':
    mykey = 'ckczppom'
    a = AdventCoin(mykey)
    a.mine()
    print(a.lowest_number)
