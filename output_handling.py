import json

class Output_handling:

    total_waitingtime = 0
    total_turnaroundtime = 0

    def __init__(self, preprocessed_data, processed_data):

        self.preprocessed_data = preprocessed_data
        self.preprocessed_processes = preprocessed_data['processes']
        self.preprocessed_processes = preprocessed_data['durationtime']
        self.preprocessed_processes = preprocessed_data['arrivaltime']

        self.processed_data = processed_data
        self.processed_processes = processed_data['processes']
        self.processed_durationtime = processed_data['durationtime']
        self.processed_arrivaltime = processed_data['arrivaltime']
        self.amount = processed_data['amount']
        self.waitingtime = processed_data['waitingtime']
        self.turnaroundtime = processed_data['turnaroundtime']

    def print_output(self):

        print('Processes', 'Duration time', 'Arrival time', 'Waiting time' , 'Turn around time', 'Completed', sep='\t') 
  
        for i in range(self.amount): 
            self.total_waitingtime = self.total_waitingtime + self.waitingtime[i] 
            self.total_turnaroundtime = self.total_turnaroundtime + self.turnaroundtime[i] 
            completedtime = self.turnaroundtime[i] + self.processed_arrivaltime[i] 
            print(str(self.processed_processes[i]) + '\t\t' + str(self.processed_durationtime[i]) 
                + '\t\t' + str(self.processed_arrivaltime[i]) + '\t\t' + str(self.waitingtime[i]) 
                + '\t\t' + str(self.turnaroundtime[i]) + '\t\t\t' + str(completedtime))  
  
        print('Average waiting time' + '\t\t' + '= ' + str(round(self.total_waitingtime / self.amount, 2)))
        print('Average turn around time' + '\t' + '= '+ str(round(self.total_turnaroundtime / self.amount, 2)))

    def save_output(self):

        with open('data.json', 'a', encoding='utf-8') as f:
            json.dump(self.processed_data, f, ensure_ascii=False, indent=4)