import sys
import numpy as np

class Data():
    def __init__(self):
        self.headings = ["Yaw", "Pitch", "Roll"]
        self.data = {}

    def fill_dict(self, sys_len):
        i = 0
        for args in range(1,sys_len):
            temp = np.float64(sys.argv[args])
            self.data[self.headings[i]] = temp
            i += 1

        return self.data


if __name__ == '__main__':
    myObj = Data()
    sys_len = len(sys.argv)
    myDict = myObj.fill_dict(sys_len)
    print(myDict)