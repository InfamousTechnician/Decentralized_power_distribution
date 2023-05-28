import hashlib
from random import randint as rdi

''' SIMULATION CONFIGURATION '''
max_consumer_power = 14
heaters = [1, 2, 3, 5, 8, 12] # power consumption in kilo Watts
generated_power = 40000 # total power generated in kilo Watts
households = 10000 # number of simulated households#heaters = [1, 2, 3, 5, 7, 8] # power consumption in kilo Watts
#generated_power = 3500 # total power generated in kilo Watts
#households = 1000 # number of simulated households
expected_network_frequency = 50

simulation_loops = 150

''' SIMULATION SETUP '''
consumptions = [heaters[rdi(0, len(heaters)-1)] for _ in range(households)] # consumers with diverse heaters
integration_offset = 1000
integration_regulators = 900 # the control value inside the integration regulator in the smart switches
available = [True for _ in range(households)]
timer = 0

def total_power_consumption(): # sum up all households' consumptions
    power = 0
    for consumer in range(households):
        if available[consumer]:
            power += consumptions[consumer]
    return power

def network_frequency(total_power_consumption): # simulate a network frequency inversely proportional to overloading
    return expected_network_frequency*(1+(generated_power-total_power_consumption)/generated_power)

def update_regulators():
    global integration_regulators
    #for regulators in range(households):
    integration_regulators -= (expected_network_frequency - network_frequency(total_power_consumption())) / expected_network_frequency * regulation_speed

def update_availability(): # randomly switch consumers on and off to maintain a balanced load on the system
    for house in range(households):        
        pseudo_random = 0
        for chance in range(max_consumer_power-consumptions[house]): # bigger the consumption the LOWER the chance to switch it off
            s = str(house)+str(chance)+str(timer)
            next_hash = hashlib.sha256(s.encode('utf-8'))
            next_hash = int.from_bytes(next_hash.digest(), byteorder='big', signed=False)
            next_hash %= integration_offset
            if next_hash > pseudo_random:
                pseudo_random = next_hash
        
        if pseudo_random > integration_regulators:
            available[house] = False
        else:
            available[house] = True     

''' CALIBRATION '''
speeds = [20*(i+1) for i in range(8)]
variations = []
for regulation_speed in speeds: # this must be adjusted well to amount for the smallest network frequency variations
    print('regulation speed:', regulation_speed)
    variation = 0
    for s in range(simulation_loops):
        update_availability(network_frequency(total_power_consumption()))
        update_regulators()
        timer += 1
        if s > 50: # roughly excluding initial condition
            variation += (expected_network_frequency - network_frequency(total_power_consumption()))**2
    variations.append(variation**0.5 / (households-50))
    print(variations[-1])
print(variations)

''' SIMULATION ''
regulation_speed = 30

for _ in range(simulation_loops):
    update_availability(network_frequency(total_power_consumption()))
    update_regulators()
    timer += 1
    print(total_power_consumption(), ':total power | frequency:', network_frequency(total_power_consumption()))
'''
