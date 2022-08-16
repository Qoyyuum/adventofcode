import hashlib

class AdventCoin:
    def __init__(self, key):
        self.key = key

    def mine(self, leading_zeroes):
        num = 1
        while True:
            self.coin = self.key + str(num)
            result = hashlib.md5(self.coin.encode('utf-8')).hexdigest()
            #print(f"{self.coin = } {result = }")
            if result.startswith(leading_zeroes*'0'):
                self.md5hash = result
                self.lowest_number = str(num)
                break
            num += 1

if __name__ == '__main__':
    mykey = 'ckczppom'
    a = AdventCoin(mykey)
    print("For Part One")
    a.mine(5)
    print(a.lowest_number)
    b = AdventCoin(mykey)
    print("For Part Two")
    b.mine(6)
    print(b.lowest_number)
