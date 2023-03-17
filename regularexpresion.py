
import re
info =input('Enter the Key : ')

data = {'details':[
    {
        'Name':'auto scaling',
        'max':'234AZ#',
        'min':'UP@5678',
        'server':'Amazon'
    },
     {
        'Name':'auto scaling1',
        'max':'345CZ@',
        'min':'CZ?1256',
        'server':'Amazon1'
    },
      {
        'Name':'auto scaling2',
        'max':'768GT%',
        'min' :'AW@123w',
        'server':'Amazon2'
    },
       {
        'Name':'auto scaling3',
        'max':'asdferty',
        'min':'EV#8769',
        'server':'Amaon3'
    }
]
}
# if info not in data:
#     print('not exist')
for i,j in data.items():
    for k in range(len(j)):
        for e,s in j[k].items():
            if s==info:
                c=j[k]['min']
                d=j[k]['max']
                e=j[k]['server']
                # print('server = ',e)
                #print('min =',c)
                #print('max =',d)
                # a=re.compile(r'[0-9]{3}[A-Z]{2}[^a-zA-Z0-9]')
                # s=a.fullmatch(d)
                s=re.fullmatch('[0-9]{3}[A-Z]{2}[^a-zA-Z0-9]',d)
                if s==None:
                    print('Max num is not matching with the regex')
                else:
                    print('max =',d)
                # m=re.compile(r'[A-Z]{2}[^a-zA-Z0-9][0-9]{4}')   
                # f=m.fullmatch(c) 
                f=re.fullmatch('[A-Z]{2}[^a-zA-Z0-9][0-9]{4}',c)
                if f==None:
                    print('Min num is not matching with the regex')
                else:
                    print('min =',c)
                z=re.fullmatch('[A-Z]{1}[a-z]{5}[0-9]{1}',e)
                if z==None:
                    print('server is not matching with the regex')
                else:
                    print('server =',e)







