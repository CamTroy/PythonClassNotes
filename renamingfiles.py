# Put all the files that need to be renamed in a folder called "Students" in the same directory as this script.
import os
import csv

path = "./Students"

def get_new_name(filename):

    with open(f"{path}/{filename}", 'r') as csvfile:

        csvreader = csv.reader(csvfile)
        elements = next(csvreader)
        new_name = f"{elements[1]}_{elements[0]}_{elements[2]}_{elements[3]}"
        new_name = new_name.replace(" ", "")

    return new_name

for thing in os.scandir(path):

    if thing.is_file():

        if thing.name.endswith(".csv"):

            new_name = f"{get_new_name(thing.name)}.csv"
            os.rename(f"{path}/{thing.name}", f"{path}/{new_name}")