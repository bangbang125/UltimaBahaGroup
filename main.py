import  math

print("参加する人数を入力、7〜11まで")
membernum = input()
if int(membernum) > 11 :
    print("2チームでやった方がいい")

teamnum = 0
list = []

while teamnum < int(membernum) :
    print("誰が参加しますか？ {0} 人中 {1} 人選択済み ".format(membernum,teamnum))
    print("団メンバーコード")
    print("1.ヨニキ　2.にっしー  3.あら　4.あてなん　5.ぴす　6.板　7.小人 8.コケバナナ 9.だっちゅ 10.せろりぃ 11.lex3 12.あとおじ　13.れんでぃ")
    i = 0
    while int(membernum) > i :
        selectmember = input()
        list.append(int(selectmember))
        i+=1
    i = 0
    buttle = []
    while int(membernum) > i :
        buttle = list









