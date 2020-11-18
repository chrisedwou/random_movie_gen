import sys
import pandas
import random

def gen(com):
	if (com == 'sci'):
		movies = pandas.read_csv('sci_fi_movies.csv',sep=',')
		to_print = movies.values.tolist()
		print(random.choice(to_print)[0])

	elif (com == 'act'):
		movies = pandas.read_csv('action_movies.csv',sep=',')
		to_print = movies.values.tolist()
		print(random.choice(to_print)[0])

	elif (com == 'hor'):
		movies = pandas.read_csv('horror_movies.csv',sep=',')
		to_print = movies.values.tolist()
		print(random.choice(to_print)[0])

	elif (com == 'all'):
		movies = pandas.read_csv('all_movies.csv',sep=',')
		to_print = movies.values.tolist()
		print(random.choice(to_print)[0])

	else:
		print("Command Not Reconized, please select either sci, act, hor, or all")

if __name__ == '__main__':
	globals()[sys.argv[1]](sys.argv[2])