import json

class Lfu:

    currentpages    = []
    frequency       = {}
    data            = {}

    pagefaults = 0 

    def __init__(self, preprocessed_data):

        self.capacity   = preprocessed_data['capacity']     # Load input
        self.processes  = preprocessed_data['processes']

        for item in self.processes:                         # Initialize freqiencies
            if item in self.frequency: 
                self.frequency[item] = 0
            else: 
                self.frequency[item] = 0

        with open('lfu.txt', 'a') as f:                     # Save input to file
            f.write(json.dumps(preprocessed_data))
            f.write('\n')
            f.close

    def page_replacement(self):

        for page in self.processes:                                 # For every page
            if page not in self.currentpages:                       # Jezeli nie jest w liście
                if len(self.currentpages) == self.capacity:         # Jezeli lista jest mniejsza niz wielkosc

                    lowestfrequency = 9999
                    lowestfrequencykey = 0
                    for items in self.currentpages:                 # Sprawdzenie ktora czestotliwosc jest najmniejsza
                        for key, value in self.frequency.items():
                            if items == key:
                                if value < lowestfrequency:
                                    lowestfrequency = value
                                    lowestfrequencykey = key

                    self.frequency[lowestfrequencykey] = 0          # Zamienienie stron
                    self.frequency[page] += 1

                    self.currentpages.remove(lowestfrequencykey)
                    self.currentpages.append(page)
                else:
                    self.currentpages.append(page)                  # Dodanie ston
                    self.frequency[page] += 1
            
                self.pagefaults += 1

            else:
                self.frequency[page] += 1                           # Zamienienie stron
                self.currentpages.remove(page)
                self.currentpages.append(page)

            self.save_data()
            print(self.currentpages)
            for key, value in self.frequency.items():   # Print frequencys
                print('%d: %d' %(key, value))

        print('Pagefaults = ', self.pagefaults)

    def save_data(self):                                # Save output to file
        with open('lfu.txt', 'a') as f:
            f.write(json.dumps(self.currentpages))
            f.write('\n')
