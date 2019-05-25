from tkinter import *
import turtle
import operator

# open file, read contents and return
def read_file(filename):
	f = open(filename, 'r')	# open as read only
	contents = f.read()
	f.close()
	return contents


# get frequencies of top n in percents
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
			chars['Newline'] = chars.get(char, 0) + 1
		elif char == '\t':
			chars['Tab'] = chars.get(char, 0) + 1
		else:
			chars['Other Symbols'] = chars.get(char, 0) + 1
	return chars


# calculate probabilities of each character
def calc_probablities(char_freq):
	contents = read_file('Words.txt')
	char_freq = get_freq(contents)
	freq_prob = {}
	total = sum(char_freq.values())
	for char, freq in char_freq.items():
		freq_prob[char] = freq / total
	return freq_prob

freq_prob = calc_probablities(get_freq(read_file('Words.txt')))

# sort freq
sorted_freq_prob = sorted(freq_prob.items(), key = operator.itemgetter(1), reverse = True)
print(sorted_freq_prob)

# draw using turtle

################## GUI #############################
window = Tk()
window.title('Character Frequencies Pie Chart')

#create canvas for drawing 
main_canvas = Canvas(window, width = 300, height = 50)

# entry field
input_label = Label(window, text = 'Input an integer (1 to 54)').grid(row = 0)
user_input = Entry(window, width = 50).grid(row = 1)

# submit and exit button
submit_button = Button(window, text = 'Submit', width = 10).grid(row = 1, column = 1)
exit_button = Button(window, text = 'Exit', width = 10, command = window.destroy).grid(row = 2, column = 1)


window.mainloop()
