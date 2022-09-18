import numpy as np
import os
import time
import random

NUM_ACTIVITIES_IN_SPIN = 5
# List of activities
activities_database =[
                'Walking for 10 minutes', 
                'Listen to a song',
                'Read 5 papers of a book',
                'Sightseeing for 10 minutes',
                'Eat a new flavor ice cream',
                'Go out for one day',
                'Make friend with a stranger',
                'Sing a song and upload on mood',
            ]


class RandomSpin:
    def __init__(self, activities):
        self.activities = activities
        # Chia đều tỉ lệ activities
        self.rates = [1 / len(activities)] * len(activities)

    def getActivities(self):
        return np.random.choice(self.activities, p=self.rates)

    def changeRates(self, ex_activity):
        index = self.activities.index(ex_activity)
        self.rates[index] = self.rates[index] / NUM_ACTIVITIES_IN_SPIN
        add_rates = [self.rates[index] * (NUM_ACTIVITIES_IN_SPIN - 1) / (len(self.activities) - 1)] * len(self.activities)
        add_rates[index] = 0
        self.rates = [x + y for x,y in zip(self.rates, add_rates)]


def main():
    # Neu nhu file ex_activity khong co gi tuc la nguoi dung chua choi, tao 1 vong quay

    activities = random.sample(activities_database, NUM_ACTIVITIES_IN_SPIN)
    spin = RandomSpin(activities)
    print(spin.getActivities())

    

    
    

if __name__=="__main__":
    main()