#编译一个game(图书馆)
import random  as ram
#a=ram.randint(1,3)
#print(a)
allpages=[]
pages1={}
pages2={}
def make_tuo(lei,max,min):
    #lei为类型，max为最大值，min为最小值
    tuo={'lei':lei,'min':min,'max':max}
    return tuo
def make_page1(tuo):
    

    
def make_page2(name,tzs,guang,alldx=None):
    #alldx为书页效果
    #tzs=骰子数
    page={'name': name, 'tzs': tzs, 'guang': guang, 'alldx': alldx}
def suiji(tuo):
    return ram.randint(tuo['min'], tuo['max'])
class g_player:
    def __init__(self,hp,gp,guang):
        #guang为行动点数
        #gp为混乱值
        self.hp=hp
        self.gp=gp
        self.guan=guang
        
        
    def bookpage(pages1,chouqu=3):
        #chouqu为抽取的书页数量
        #pages1为书页列表
        page1=pages1
        for i in range(chouqu):
            a=ram.randint(0,len(page1)-1)
            print(page1[a])
tuo1=make_tuo('gong',20,10)
page=
        
        
        
        
    
s=g_player(100,90,4)

print(s.__init__)
