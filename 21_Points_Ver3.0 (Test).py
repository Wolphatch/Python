import random
import time
import os

'''Ver2.0 修正了牌A存在1和11两个值的问题，程序会自动判断A的值'''
'''Ver3.0创建了玩家类，以减少冗余代码'''




class  Card(object):

    def __init__(self,color=0):
        self.color=color
    @staticmethod
    def number():
        number={}
        for index, value in enumerate(list(range(1, 14))):
            number[index + 1] = 4
        return number
    @staticmethod
    def value():
        card={}
        for index,value in enumerate(list(range(1,14))):
           if value>=11:
               value=10
           card[index+1]=value
        return card


def random_choose():
    time0 = np.random.normal(20,50,size=1)[0]
    random.seed(time0)
    card_number=random.randint(1,13)
    return card_number

def rule(args):
    for i in args:    #处理A是1还是11的问题
        if i==1:
            small=sum(args)
            big=sum(args)+10
            if small > 21:
                return False
            elif small<=21 and big>21:
                return small
            elif  big<=21:
                group=[small,big]
                return group
    sum_number=sum(args)
    if sum_number>21:
        return False
  
    else:
        return sum_number

class People(object):
    def __init__(self,side):
         self.side=side
    
    def player(self,list):
       random_number=random_choose()  #随机产生一个1-13数字，并返回（表示卡牌）
       random_number=check(random_number)
       print(random_number)
       list.append(value[random_number])  # args表示一个收到卡牌值的和,将收到卡牌对应的值加入args
       result=rule(list)      #，Rule函数会对args求和后返回一个卡牌总的值，如果爆了，就返回False
       if result==False:
           print('Too much,{} lose'.format(self.side))
           return 0.1                              #存在牌A是选择1还是11的判断问题，如果A是1都爆了，A是10肯定爆，所以这里不做改变
    #如果没爆，Rule函数会返回一个当前牌的总数，然后玩家决定是否继续
       else:
          if_continue=input('Continue Press 1,Stop Press 2')
          if int(if_continue)==2:   #要注意开始判断A的值的问题

              if  isinstance(result,__builtins__.list)==True:
                  print(max(result))
                  return max(result)     #玩家选择不继续，返回玩家点数
              else:
                  return result
          else:
              self.player(list) 



def check(a):
    if  number[a]!=0:   #检测卡牌池是否有此牌
        number[a] -= 1  # 次牌型数量减少一个
        return a
    if number[a]==0:
        a= random_choose()
        check(a)



def take_first_2(Player_card_list):   #拿底牌函数
    random_number=random_choose()  #随机产生一个1-13数字，并返回（表示卡牌）
    random_number=check(random_number)
    print(random_number)
    Player_card_list.append(value[random_number])
    return  Player_card_list





#---------------------------------游戏开始------------------------------------

card=Card()
value=card.value()
number=card.number()
print('Start:')
Player_args=[0]
Maker_args=[0]  #玩家和庄家的牌池
a=0
b=0
print('Player Term') #游戏开始



#玩家回合




Player_args=take_first_2(Player_args)



#玩家拿第二张牌（同上）



Player_args=take_first_2(Player_args)




#问是否要牌
if_continue2=input('Continue Press 1,Stop Press 2?')

if int(if_continue2) == 1:
    side='Player'
    player1=People(side)
    a=player1.player(Player_args)
    #print(a)
    if a==0.1:
        os.system('pause')
        os._exit(0)


else:
    a=sum(Player_args)






#庄家回合

    
print('Maker Term')
#庄家拿第一张牌

Maker_args=take_first_2(Maker_args)




#庄家拿第二张牌

Maker_args=take_first_2(Maker_args)


if_continue3=input('Continue Press 1,Stop Press 2?')
if int(if_continue3)==1:
    side='Maker'
    player2=People(side)
    b=player2.player(Maker_args)
    if b==0.1:
        os.system('pause')
        exit()
    else:
        b=sum(Maker_args)
else:
    b=sum(Maker_args)

print('Player:{}'.format(a))
print('Maker:{}'.format(b))
if a>b:
    print('Player Win')
elif a<b:
    print('Maker Win')
else:
    
    print('Tie')

