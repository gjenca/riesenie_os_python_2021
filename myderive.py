#!/usr/bin/env python3
def myderive(symb,var):
    
    if type(symb) is int or type(symb) is float:
    # Cislo
        return 0
    elif type(symb) is str:
    # Premenna alebo konstanta?
        if symb==var:
            return 1
        else:
            return 0
    elif type(symb) is list and len(symb)==3:
    # Binarny operator
        if  symb[0]=='+':
            return ['+',myderive(symb[1],var),myderive(symb[2],var)]
        if  symb[0]=='-':
            return ['-',myderive(symb[1],var),myderive(symb[2],var)]
        if  symb[0]=='*':
            return ['+',
                ['*',myderive(symb[1],var),symb[2]],
                ['*',symb[1],myderive(symb[2],var)]]
        if symb[0]=='/':
            return ['/',
                ['-',
                ['*',myderive(symb[1],var),symb[2]],
                ['*',symb[1],myderive(symb[2],var)]],
                ['*',symb[2],symb[2]]]
        else:
            raise ValueError('Bad expression')
    else:
        raise ValueError('Bad expression')

if __name__=="__main__":
    print(myderive(['+','x',1],'x'))
    print(myderive(['*',['-',10,'x'],'y'],'x'))
    print(myderive(['/',['-',10,'x'],'y'],'x'))
    print(myderive(['/','x','y'],'x'))
    print(myderive(['/','x','y'],'y'))
