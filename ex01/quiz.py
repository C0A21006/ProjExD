import random
import datetime
mondai = ["サザエの旦那の名前は？","カツオの妹の名前は？","タラオはカツオから見てどんな関係？"]
kotae = [["マスオ","ますお"],["ワカメ","わかめ"],["甥","おい","甥っ子","おいっこ"]]
def main():
    start = datetime.datetime.now()
    n = random.randint(0,2)
    shutudai(n)
    ans = input("答えは：")
    kaito(n,ans)
    end = datetime.datetime.now()
    print(f"所要時間：{(end - start).seconds}秒")

def shutudai(n):
    print("問題：")
    print(mondai[n])

def kaito(n,ans):
    for i in range(len(kotae[n])):
        if ans == kotae[n][i]:
            print("正解")
            break
        else:
            print("不正解")
    
if __name__ == "__main__":
    main()


    