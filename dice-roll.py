from random import randrange
from os import system, name
from time import sleep


randomNum = None
guess = None
randshow = None

def Num9():
    print('-----------------')
    print('|@ @| |@ @| |@ @|\n|@ @| |@ @| |@ @|')
    print('_____ _____ _____')
    print('|@ @| |@ @| |@ @|\n|@ @| |@ @| |@ @|')
    print('_____ _____ _____')
    print('|@ @| |@ @| |@ @|\n|@ @| |@ @| |@ @|')
    print('-----------------')
    
    
def Num8():
    print('-----------------')
    print('|@ @| |@ @| |@ @|\n|@ @| |@ @| |@ @|')
    print('_____ _____ _____')
    print('|@ @| |@ @| |@ @|\n|@ @| |@ @| |@ @|')
    print('_____ _____')
    print('|@ @| |@ @| \n|@ @| |@ @| ')
    print('-----------------')

   
def Num7():
    print('-----------------')
    print('|@ @| |@ @| |@ @|\n|@ @| |@ @| |@ @|')
    print('_____ _____ _____')
    print('|@ @| |@ @| |@ @|\n|@ @| |@ @| |@ @|')
    print('_____ ')
    print('|@ @| \n|@ @| ')
    print('-----------------')
    
    
    
def Num6():
    print('-----------------')
    print('|@ @| |@ @| |@ @|\n|@ @| |@ @| |@ @|')
    print('_____ _____ _____')
    print('|@ @| |@ @| |@ @|\n|@ @| |@ @| |@ @|\n\n')
    print('-----------------')
    
    
    
def Num5():
    print('-----------------')
    print('|@ @| |@ @| |@ @|\n|@ @| |@ @| |@ @|')
    print('_____ _____ ')
    print('|@ @| |@ @| \n|@ @| |@ @|\n\n')
    print('-----------------')
    
    
    
def Num4():
    print('-----------------')
    print('|@ @| |@ @| |@ @|\n|@ @| |@ @| |@ @|')
    print('_____')
    print('|@ @|\n|@ @|\n\n')
    print('-----------------')
    
    
def Num3():
    print('-----------------')
    print('|@ @| |@ @| |@ @|\n|@ @| |@ @| |@ @|\n\n\n\n\n')
    print('-----------------')
    
    
    
def Num2():
    print('-----------------')
    print('|@ @| |@ @|\n|@ @| |@ @|\n\n\n\n')
    print('-----------------')
    
    
     
def Num1():
    print('-----------------')
    print('|@ @|\n|@ @|\n\n\n\n')
    print('-----------------')
    

def randfunction(randshow):
    if randshow == 1:
        Num1()
    elif randshow == 2:
        Num2()
    elif randshow == 3:
        Num3()
    elif randshow == 4:
        Num4()
    elif randshow == 5:
        Num5()
    elif randshow == 6:
        Num6()
    elif randshow == 7:
        Num7()
    elif randshow == 8:
        Num8()
    elif randshow == 9:
        Num9()
        
        
        

def random():
    global randomNum
    randomNum = randrange(1,9)
    status = 0
    while status < 22:
        randshow = randrange(1,9)
        randfunction(randshow)
        sleep(0.25)
        system('cls' if name == 'nt' else 'clear')
        status += 1
    randfunction(randomNum)
    


def inputs():
    global guess 
    guess = int(input('please enter your guess: '))


def isTrue():
    global guess,randomNum
    if guess == randomNum:
        print('what the fuck!!\n you are genius!!')
    else:
        print(f"the random Nember was: {randomNum}")
        
        
def reset():
    NO = input('Do you fancy continue? (NO->> exit): ').upper()
    if NO == 'NO':
        exit()
        status = False
    else:
        system('cls' if name == 'nt' else 'clear')
        main()
        


                
def main():
    status = True
    while status:
        inputs()
        random()
        isTrue()
        reset()
main()

        
        
        