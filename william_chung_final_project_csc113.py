# william chung
# csc 113 final project
# spring 2019
# 16032029

from tkinter import *
from tkinter import messagebox
import turtle
import operator
import random

# open file, read contents and return
def read_file(file):
	f = open(file, 'r')	# open as read only
	contents = f.read()
	f.close()
	return contents

# get frequencies
def get_freq(contents):
	chars = {}
	for char in contents:
		if char.isalpha():
			chars[char] = chars.get(char, 0) + 1
		elif char.isnumeric():
			chars[char] = chars.get(char, 0) + 1
		elif char == ' ':
			chars['White space']  = chars.get('White space', 0) + 1
		elif char == '\n':
			chars['Newline'] = chars.get('Newline', 0) + 1
		elif char == '\t':
			chars['Tab'] = chars.get('Tab', 0) + 1
		else:
			chars['All Other Symbols'] = chars.get('All Other Sumbols', 0) + 1
	return chars

# calculate probabilities
def calc_probablities():
	contents = read_file('Words.txt') # read file contents
	char_freq = get_freq(contents) # get char freq
	freq_prob = {}
	total = 0
	for n in char_freq.values():
		total = total + n
	#print(total)
	for char, freq in char_freq.items():
		freq_prob[char] = freq / total
	return freq_prob

# restricts entry field to only numerals and backspace to delete
def entry_validation(c):
	if c in '0123456789' or '':
		return True
	return False

############## draw using turtle ###################
def draw_pie_chart():
	turtle.clear() # clears turtle screen for drawing
	turtle.showturtle()

	# check if input is correct
	segments = int(user_input.get())
	if segments < 0 or segments > 54:
		messagebox.showerror('Error', 'input out of range')
	else:
		# begin turtle
		turtle.penup()
		turtle.sety(-200)
		turtle.speed(10)
		turtle.pendown()

		RADIUS = 200
		LABEL = 200 * 1.3
		turtle.colormode(255)

		# sort and get top n probabilities
		freq_prob = calc_probablities()
		sorted_freq_prob = sorted(freq_prob.items(), key = operator.itemgetter(1), reverse = True)
		top_n_probabilities = []
		total = 0
		if segments > len(sorted_freq_prob):
			segments = len(sorted_freq_prob) 
		for i in range(segments):
			top_n_probabilities.append(sorted_freq_prob[i])
			total = total + sorted_freq_prob[i][1]
		if total < 1:
			top_n_probabilities.append(('All other characters', 1 - total))
		
		# draw pie
		for char, prob in top_n_probabilities:
			turtle.fillcolor(random.randrange(0, 256, 5), random.randrange(0, 256, 5), random.randrange(0, 256, 5))
			turtle.begin_fill()
			turtle.circle(RADIUS, prob * 360)
			position = turtle.position()
			turtle.goto(0, 0)
			turtle.end_fill()
			turtle.setposition(position)

		# draw labels
		turtle.penup()
		turtle.sety(-LABEL)
		for char, prob in top_n_probabilities:
			text = char + ': ' + str(round(prob, 4))
			turtle.circle(LABEL, prob * 180) # write at center of arc
			turtle.write(text, align = 'center', font = ('Arial', 8))
			turtle.circle(LABEL, prob * 180)

		turtle.hideturtle()
		
################## GUI #############################
window = Tk()
window.title('Character Frequencies Pie Chart')

# entry field
input_label = Label(window, text = 'Input an integer (0 to 54)').grid(row = 0)
vcmd = (window.register(entry_validation), '%S')
user_input = Entry(window, width = 50, validate = 'key', vcmd = vcmd)
user_input.grid(row = 1)

# submit and exit button
submit_button = Button(window, text = 'Submit', width = 10, command = draw_pie_chart).grid(row = 2, column = 0)
exit_button = Button(window, text = 'Exit', width = 10, command = exit).grid(row = 2, column = 1)

window.mainloop()