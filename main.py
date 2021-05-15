from fcfs import FCFS
from sjf import SJF
from lfu import Lfu
from lru import Lru
from output_handling import Output_handling
from generator import Generator

choices = {
    'type': 'replacement',   # generate data for page raplacement or cpu scheduling. Option between 'scheduling' and 'replacement'
    'length': 30,          # length of lists
    'range': 50,            # range that numbers can be generated in
    'specified' : 3,        # for page replacement algorithms, it's capacity
    'runfromfile': 1        # 1 is for prepared data
}

gen = Generator(choices)    # runs generator
preprocessed_data = gen.return_numbers()

print(preprocessed_data)    # display generated data

def firstcomefirstserve(preprocessed_data):
    alg = FCFS(preprocessed_data)
    alg.sort_arrival()
    alg.waiting_time()
    alg.turn_around_time()
    alg.save_data()
    alg.output_data()

def shortestjobfirst(preprocessed_data):
    alg = SJF(preprocessed_data)
    alg.sort_arrival()
    alg.sort_on_completion()
    alg.save_data()
    alg.output_data()

def leastfrequentlyused(preprocessed_data):
    alg = Lfu(preprocessed_data)
    alg.page_replacement()
    alg.save_data()

def leastrecentlyused(preprocessed_data):
    alg = Lru(preprocessed_data)
    alg.page_replacement()
    alg.save_data()

# firstcomefirstserve(preprocessed_data)

# shortestjobfirst(preprocessed_data)

leastrecentlyused(preprocessed_data)

# leastfrequentlyused(preprocessed_data)
