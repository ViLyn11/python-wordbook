words=[]
while True:
    print("1.添加单词")
    print("2.查看单词")
    print("3.退出")
    choice=input("请选择：")
    if choice=="1":
        word=input("输入单词：")
        words.append(word)
        print("已添加------------------------")
    elif choice=="2":
        if len(words)==0:
            print("还没有单词----------------")
        else:
            for w in words:
                print(w)
    elif choice=="3":
        print("再见--------------------------")
        break
    else:
        print("输入无效，请重新选择-----------")