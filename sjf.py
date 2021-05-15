import json

class SJF:

    totaltime               = 0
    turnaroundtime          = 0
    waitingtime             = 0
    total_waitingtime       = 0
    total_turnaroundtime    = 0

    def __init__(self, preprocessed_data):

        print('')
        print('Shortest Job First: ')
        print('')
        
        self.processes      = preprocessed_data['processes']        # Load data
        self.durationtime   = preprocessed_data['durationtime']
        self.arrivaltime    = preprocessed_data['arrivaltime']
        self.amount         = len(preprocessed_data['processes'])

        self.totaltime      = [0] * self.amount                     # Initialize lists
        self.turnaroundtime = [0] * self.amount
        self.waitingtime    = [0] * self.amount

        with open('sjf.txt', 'a') as f:                             # Save to file
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

    def sort_on_completion(self):

        self.totaltime[0]       = self.arrivaltime[0] + self.durationtime[0]
        self.turnaroundtime[0]  = self.totaltime[0] - self.arrivaltime[0]
        self.waitingtime[0]     = self.turnaroundtime[0] - self.durationtime[0]

        for i in range(1, self.amount):
            temp = self.totaltime[i-1]
            low = self.durationtime[i]
            for j in range(i, self.amount):
                if temp >= self.arrivaltime[j] and low >= self.durationtime[j]:
                    low = self.durationtime[j]
                    self.val = j

            self.totaltime[self.val] = temp + self.durationtime[self.val]
            self.turnaroundtime[self.val] = self.totaltime[self.val] - self.arrivaltime[self.val]
            self.waitingtime[self.val] = self.turnaroundtime[self.val] - self.durationtime[self.val]

            # Swap lists
            self.processes[i], self.processes[self.val] = self.processes[self.val], self.processes[i]
            self.arrivaltime[i], self.arrivaltime[self.val] = self.arrivaltime[self.val], self.arrivaltime[i]
            self.durationtime[i], self.durationtime[self.val] = self.durationtime[self.val], self.durationtime[i]
            self.totaltime[i], self.totaltime[self.val] = self.totaltime[self.val], self.totaltime[i]
            self.turnaroundtime[i], self.turnaroundtime[self.val] = self.turnaroundtime[self.val], self.turnaroundtime[i]
            self.waitingtime[i], self.waitingtime[self.val] = self.waitingtime[self.val], self.waitingtime[i]

    def save_data(self):

        data = {                                        # Serialize data
            'processes': self.processes,
            'durationtime': self.durationtime,
            'arrivaltime': self.arrivaltime,
            'amount': self.amount,
            'waitingtime': self.waitingtime,
            'turnaroundtime': self.turnaroundtime,
        }

        with open('sjf.txt', 'a') as f:                # Save data to file
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

