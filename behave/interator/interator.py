


def interator(num):

    msglist = ["a","b","c","d"]

    for index in range(num):
        yield msglist[index%len(msglist)]


if __name__ == "__main__":
    for data in interator(10):
        print data
