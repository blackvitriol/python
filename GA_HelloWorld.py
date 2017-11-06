#!/usr/bin/python

import random
import string
from time import sleep
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write('%s' % c)
        sys.stdout.flush()
        sleep(0.25)

delay_print("--== A7MD0V PRESENTS ==--\n")
delay_print("GASPE: Genetic Algorithm String Production Engine...\n")

print("Hello user...")
sleep(0.5)
print("Please wait, loading program...")
sleep(2)
print("Welcome to GASPE ...")
sleep(1)
print("From the geneset of all the characters, we will try to produce your string...")
sleep(1)
target = raw_input("Please enter a string...\n")
# target = "Hello, World! Hey Ahmad :)"

def calc_fitness(source, target):
    fitval = 0
    for i in range(0, len(source)):
        fitval += (ord(target[i]) - ord(source[i])) ** 2
    return(fitval)

def mutate(parent1, parent2):
    child_dna = parent1['dna'][:]

    # Mix both DNAs
    start = random.randint(0, len(parent2['dna']) - 1)
    stop = random.randint(0, len(parent2['dna']) - 1)
    if start > stop:
        stop, start = start, stop
    child_dna[start:stop] = parent2['dna'][start:stop]

    # Mutate one position
    charpos = random.randint(0, len(child_dna) - 1)
    child_dna[charpos] = chr(ord(child_dna[charpos]) + random.randint(-1,1))
    child_fitness = calc_fitness(child_dna, target)
    return({'dna': child_dna, 'fitness': child_fitness})

def random_parent(genepool):
    wRndNr = random.random() * random.random() * (GENSIZE - 1)
    wRndNr = int(wRndNr)
    return(genepool[wRndNr])

def dump_genepool(generation, genepool):
    for candidate in genepool:
        print "%6i %6i %15s" % (
            generation,
            candidate['fitness'],
            ''.join(candidate['dna'])
        )
        sleep(0.000001)


GENSIZE = 20
genepool = []
for i in range(0, GENSIZE):
    dna = [random.choice(string.printable[:-5]) for j in range(0, len(target))]
    fitness = calc_fitness(dna, target)
    candidate = {'dna': dna, 'fitness': fitness }
    genepool.append(candidate)

generation = 0
while True:
    generation += 1
    genepool.sort(key=lambda candidate: candidate['fitness'])
    dump_genepool(generation, genepool)

    if genepool[0]['fitness'] == 0:
        # Target reached
        break

    parent1 = random_parent(genepool)
    parent2 = random_parent(genepool)

    child = mutate(parent1, parent2)
    if child['fitness'] < genepool[-1]['fitness']:
        genepool[-1] = child