from random import randint, randrange, seed
import json

class Generator:

    data = 0

    def __init__(self, data):
        
        self.type = data['type']
        self.length = data['length']
        self.range = data['range']
        self.specified = data['specified']
        self.runfromfile = data['runfromfile']

        if self.runfromfile == 1:
            self.read_from_file()
        else:
            if self.type == 'scheduling':
                self.scheduling()
            elif self.type == 'replacement':
                self.replacement()

    def scheduling(self):
        
        processes = []
        durationtime = []
        arrivaltime = []

        seed(100) # Turn off later

        for n in range(1, self.length+1):
            processes.append(n)
            durationtime.append(randint(1, self.range))
            arrivaltime.append(randint(0, self.range))

        self.data = {
            'processes': processes,
            'durationtime': durationtime,
            'arrivaltime': arrivaltime
        }

    def replacement(self):

        seed(100) # Turn off later

        processes = []
        if self.specified == 0:
            capacity = randint(1, self.range)
        else: 
            capacity = self.specified

        for n in range(self.length):
            processes.append(randrange(self.range))

        self.data = {
            'processes': processes,
            'capacity': capacity
        }

    def return_numbers(self):
        return self.data

    def read_from_file(self):
        if self.type == 'scheduling':
            with open('schedulingdata.txt', 'r') as f:
                inp = json.load(f)
                self.data = {
                    'processes': inp['processes'],
                    'durationtime': inp['durationtime'],
                    'arrivaltime': inp['arrivaltime']
                }
                return self.data
                
        elif self.type == 'replacement':
            with open('replacementdata.txt', 'r') as f:
                inp = json.load(f)
                self.data = {
                    'processes': inp['processes'],
                    'capacity': inp['capacity']
                }
                return self.data