'''branch = {'message':'',
    'options':{'': ,
                '': }}'''
import time

branch0 = {'message':'You are in a dark room. What do you do?',
   'options':{'look around': 1,
              'search around': 2}}
branch1 = {'message':'You are still in a dark room',
          'options':{'look around': 1,
                     'search around': 2}}
branch2 = {'message':'You find a light switch and a Door',
    'options':{'turn on switch': 3,
                'open door': 4}}
branch3 = {'message':'The switch doesn\'t work',
    'options':{'open door': 4,
                'look around': 1}}
branch4 = {'message':'The door is locked',
    'options':{'turn on switch': 3,
                'look around': 1}}

tree = [branch0, branch1, branch2, branch3, branch4]

def getBranch(branch, action):
    if action.lower()not in tree[branch]['options'].keys():
        print ()
        print ('action not valid')
        return branch
    
    else:
        newBranch = tree[branch]['options'][action.lower()]
    print()
    print(tree[newBranch]['message'])
    print ()
    for op in tree[newBranch]['options'].keys():
        print('\t' + op)
    print ()
    return newBranch
    
