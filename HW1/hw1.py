import sys
import os

# 每層樹最上面和最下面有幾個*
def CeilingandFloor (i):   
    ceiling = 1
    floor = 5
    
    # n指第幾層
    n = 1 
    # m指第n層有多少子層(sublayer)
    m = n+2
    # 每層落差
    d = 3
    
    while(n!=i):
        ceiling = floor + 2*d
        floor = ceiling + m*2
          
        # 因為奇數層和雙數層在換層時的落差會受影響
        if n%2 ==0:
            d = d+1
        else:
            d = d
        
        n += 1
        m = n+2
            
        
    return ceiling, floor

 # 基底中央數
def find_middle(n):
    """(10 pts) Find the Middle Line of the Tree
    
    In this part, you have to find the middle line of the tree and return the distance from the middle line to 
    left end.
    For example, if the input number is 2, you have to find the middle line of a level two tree and return the
    distance to left end that is 10.

            /*\
           /***\
          /*****\
       /***********\
      /*************\
     /***************\
    /********|********\
    1234567891
             0
    
    Similarly, if the input number is 3, you have to return 17.

                   /*\
                  /***\
                 /*****\
              /***********\
             /*************\
            /***************\
           /*****************\
        /***********************\
       /*************************\
      /************|||************\
     /*************|||*************\
    /**************|||**************\
    12345678911111111
             01234567
    """
    layer = CeilingandFloor(n)
    return int((layer[1]+3)/2)
    pass

def content(i, j, n, m):
    
    # 樹幹區左右延伸計數
    if n%2 ==0:
        trunk = (n-2)/2
    else:  
        trunk = (n-1)/2
        
    # 層中心往左右延伸計數 
    sublayer = CeilingandFloor(m)
    count = (sublayer[0]-1)/2 + i - (((m+1)*(m+2)/2)-3)
    
    # 樹幹區
    if n >= 5 and i == int(((n+2)*(n+3)/2)-3)-trunk and j == (find_middle(n))+trunk-1:
        return '@'
    elif i >= int(((n+2)*(n+3)/2)-3)-trunk*2 and (find_middle(n))-trunk <=j and (find_middle(n))+trunk >= j:
        return '|'
        
    #樹葉區
    elif (find_middle(n))-count <=j and (find_middle(n))+count >= j:
        return'*'
    elif (find_middle(n))-count-1 == j:
        return '/'
    elif (find_middle(n))+count+1 == j:
        return '\\'
    else:
        return ' '

# 組裝good，填空good
def print_level_n_tree(n):
     """(50 pts) Print Out Level N Tree
    
    In this part, you have to print the level n tree which n is a integer.
    You can use 'hw1_example.py' to take a look what a level n tree looks like.
    For example, if the input number is 2, you have to print out a level two tree, and it will looks like:
 
            /*\
           /***\
          /*****\
       /***********\
      /*************\
     /***************\
    /********|********\
    
    If the input number is 5, your tree will looks like:

                                      /*\
                                     /***\
                                    /*****\
                                 /***********\
                                /*************\
                               /***************\
                              /*****************\
                           /***********************\
                          /*************************\
                         /***************************\
                        /*****************************\
                       /*******************************\
                   /***************************************\
                  /*****************************************\
                 /*******************************************\
                /*********************************************\
               /***********************************************\
              /*************************************************\
          /*********************************************************\
         /***********************************************************\
        /****************************|||||****************************\
       /*****************************|||||*****************************\
      /******************************|||@|******************************\
     /*******************************|||||*******************************\
    /********************************|||||********************************\

    Image that n is a big number. You tree must be huge.
    !!! Notice that your result must the same as what 'hw1_example.py' print out. !!!


    """
    m = 1
    
    # 圖高
    for i in range(int(((n+2)*(n+3)/2)-3)+1):
        # 預備字串
        string = ''
        # 圖寬
        for j in range(find_middle(n)*2+1):
            string += content(i, j, n, m)
        #輸出一行
        print(string)
        # 計算現在到第幾層
        if i >= ((m+2)*(m+3)/2)-3:
            m += 1
    pass


def print_level_two_tree():
    """(10 pts) Print Out Level Two Tree

    You have to print out a level two tree in this part.
    If you don't have what a level two tree look like, you can use 'hw1_example.py' to generate a level two tree.
    It will look like this:
    
            /*\
           /***\
          /*****\
       /***********\
      /*************\
     /***************\
    /********|********\

    """
    return print_level_n_tree(2)
    pass

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# 列出a的可能
def fora(p, g, A):   
    for i in range(p):
        if g**(i)%p==A:
            amin = i
            break
    return amin

# 列出b的可能
def forb(p, g, B):
    bmin = 0
    for i in range(p):
        if g**(i)%p==B:
            bmin = i
            break
    return bmin

# 找出K
def forK(p, g, a, b):
    K = g**(a*b)%p
    return K

# 組裝讚讚
def Diffie_Hellman_cracker(PublicPrime, PublicNum, PrivateA, PrivateB):
    """(30 pts) Diffie Hellman cracker
    In this part, you need to implement a function which can enter four numbers as 
    parameters and find out the private key a ,b and common number K then return those numbers.
    
    """
    a = fora(PublicPrime, PublicNum, PrivateA)
    b = forb(PublicPrime, PublicNum, PrivateB)
    K = forK(PublicPrime, PublicNum, a, b)
    print(a, b, K)
    
    pass
