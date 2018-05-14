'''
Creatonal -> Singleton
'''

class Borg:
    '''Borg class making class attribute global'''
    _shared_state = {} #attribute dictonary
    
    def __init__(self):
        self.__dict__ = self._shared_state #make attribute dict
        
class Singleton(Borg):
    '''
    Share allits attributes amongits various instances
    '''
    def __init__(self,**kwargs):
        Borg.__init__(self)
        self._shared_state.update(kwargs)
        
    def __str__(self):
        return str(self._shared_state)
    
x=Singleton(http='Hyper protocol')
print(x)
y=Singleton(snnp='simple protocol')
print(y)