import json

class FCFS:

    waitingtime             = 0
    turnaroundtime          = 0
    reachingtime            = 0
    total_waitingtime       = 0
    total_turnaroundtime    = 0
    completedtime           = 0
    
    def __init__(self, preprocessed_data):
        
        print('')
        print('First Come First Serve: ')
        print('')
        
        self.processes      = preprocessed_data['processes']         # Load generated data
        self.durationtime   = preprocessed_data['durationtime']
        self.arrivaltime    = preprocessed_data['arrivaltime']
        self.amount         = len(preprocessed_data['processes'])

        self.waitingtime    = [0] * self.amount                    # Initialize lists
        self.turnaroundtime = [0] * self.amount
        self.reachingtime   = [0] * self.amount

        with open('fcfs.txt', 'a') as f:                         # Save initialized data to file
            f.write(json.dumps(preprocessed_data))
            f.write('\n')
            f.close

    def sort_arrival(self):                                         # First sort on arrival time
        for i in range(self.amount):
            for j in range(self.amount-i-1):
                if self.arrivaltime[j] > self.arrivaltime[j+1]:
                    self.processes[j], self.processes[j+1] = self.processes[j+1], self.processes[j]
                    self.arrivaltime[j], self.arrivaltime[j+1] = self.arrivaltime[j+1], self.arrivaltime[j]
                    self.durationtime[j], self.durationtime[j+1] = self.durationtime[j+1], self.durationtime[j]

    def waiting_time(self):                                     # Calculate waiting time

        for i in range(1, self.amount): 
            self.reachingtime[i] = self.reachingtime[i - 1] + self.durationtime[i - 1] # Czas dotarcia + czas trwania
            self.waitingtime[i] = self.reachingtime[i] - self.arrivaltime[i]           # Czas czekania = czas dotarcia - czas nadejscia
            if (self.waitingtime[i] < 0):
                self.waitingtime[i] = 0
  
    def turn_around_time(self):                                 # Calculate turn around time
  
        for i in range(self.amount): 
            self.turnaroundtime[i] = self.durationtime[i] + self.waitingtime[i] 

    def save_data(self):
        
        data = {                                                # Serialize data
            'processes': self.processes,
            'durationtime': self.durationtime,
            'arrivaltime': self.arrivaltime,
            'amount': self.amount,
            'waitingtime': self.waitingtime,
            'turnaroundtime': self.turnaroundtime,
        }

        with open('fcfs.txt', 'a') as f:                        # Save data to file
            f.write(json.dumps(data))
            f.write('\n')
    
    def output_data(self):
        print('Processes', 'Duration time', 'Arrival time', 'Waiting time' , 'Turn around time', 'Completed', sep='\t') 
  
        for i in range(self.amount): 
            self.total_waitingtime = self.total_waitingtime + self.waitingtime[i] 
            self.total_turnaroundtime = self.total_turnaroundtime + self.turnaroundtime[i] 
            completedtime = self.turnaroundtime[i] + self.arrivaltime[i] 
            print(str(self.processes[i]) + '\t\t' + str(self.durationtime[i]) 
                + '\t\t' + str(self.arrivaltime[i]) + '\t\t' + str(self.waitingtime[i]) 
                + '\t\t' + str(self.turnaroundtime[i]) + '\t\t\t' + str(completedtime))  
  
        print('Average waiting time' + '\t\t' + '= ' + str(round(self.total_waitingtime / self.amount, 2)))
        print('Average turn around time' + '\t' + '= '+ str(round(self.total_turnaroundtime / self.amount, 2)))
