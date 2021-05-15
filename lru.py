import json

class Lru:

    currentpages = []
    pagefaults = 0

    def __init__(self, preprocessed_data):

        self.capacity   = preprocessed_data['capacity']     # Load data
        self.processes  = preprocessed_data['processes']

        with open('lru.txt', 'a') as f:                     # Save loaded values to file
            f.write(json.dumps(preprocessed_data))
            f.write('\n')
            f.close

    def page_replacement(self):

        for page in self.processes:
            if page not in self.currentpages:
                if len(self.currentpages) == self.capacity:
                    self.currentpages.remove(self.currentpages[0])
                    self.currentpages.append(page)

                else:
                    self.currentpages.append(page)      # Add page

                self.pagefaults += 1

            else:

                self.currentpages.remove(page)          # Replace pages
                self.currentpages.append(page)

            self.save_data()
            print(self.currentpages)
        
        print('Pagefaults = ', self.pagefaults)

    def save_data(self):                                # Save data to file
        with open('lru.txt', 'a') as f:
            f.write(json.dumps(self.currentpages))
            f.write('\n')
