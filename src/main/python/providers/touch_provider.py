'''
Created on 11 May 2014

@author: Don Najd
@description: Provider for Naoqi Touch Events
'''

# List of Events:
# RightBumperPressed, LeftBumperPressed, ChestButtonPressed, FrontTactilTouched
# MiddleTactilTouched, RearTactilTouched, HandRightBackTouched, HandRightLeftTouched

class TouchProvider(object):

    def __init__(self, nao, memory, eventName='FrontTactilTouched'):

        # args
        self.nao = nao 
        self.memory = memory

        # provider properties
        self.running = False
        self.subscribers = []

        # log
        self.nao.log('class=TouchedProvider|method=__init__')   

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)
        self.nao.log('class=TouchedProvider|method=add_subscriber')  

    def setup(self):
        self.memory.subscribeToEvent('FrontTactilTouched', self.event_callback)
        self.nao.log('class=TouchedProvider|method=setup')  

    def tear_down(self):
        self.memory.unsubscribeToEvent('FrontTactilTouched')  
        self.nao.log('class=TouchedProvider|method=teardown')  

    def event_callback(self, dataName, value, message): 

        # control down
        if value==1 and self.running == False:
            
            # status
            self.running = True
            self.nao.log('class=TouchedProvider|method=event_callback|action=call_subscribers')  
            
            # call subscribers
            for s in self.subscribers:
                s.callback(dataName, value, message)

            self.nao.log('class=TouchedProvider|method=event_callback')  
            self.running = False 
