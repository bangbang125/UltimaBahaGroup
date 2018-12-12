import  math

print("参加する人数を入力、7〜11まで")
membernum = input()
if int(membernum) > 11 :
    print("2チームでやった方がいい")

teamnum = 0
list = []
print("誰が参加しますか？　(名前入力したらEnterを忘れずに)")
"""print("団メンバーコード")"""\
"""print("1.ヨニキ　2.にっしー  3.あら　4.あてなん　5.ぴす　6.板　7.小人 8.コケバナナ 9.だっちゅ 10.せろりぃ 11.lex3 12.あとおじ　13.れんでぃ")"""
i = 0
while int(membernum) > i :
    selectmember = input()
    list.append(selectmember)
    i+=1
j = 0
k = 0
buttle = list
"""print(buttle)"""
while int(membernum) > j:
    print("{0}{1}{2}{3}{4}{5}".format(buttle[j],
                                           buttle[j+1 if j+1 < int(membernum)  else j-(int(membernum)-1)],
                                           buttle[j+2 if j+2 < int(membernum)  else j-(int(membernum)-2)],
                                           buttle[j+3 if j+3 < int(membernum)  else j-(int(membernum)-3)],
                                           buttle[j+4 if j+4 < int(membernum)  else j-(int(membernum)-4)],
                                           buttle[j+5 if j+5 < int(membernum)  else j-(int(membernum)-5)])
    )

    j+=1
    k+=1










