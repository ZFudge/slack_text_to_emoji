import pyperclip
import sys

# letter fill
f = sys.argv[1] if len(sys.argv) > 2 else ":blk:"
# letter spaces
s = ":tinvp:"
# letter border
b = ":tinvp:"

char_map = {
	" ": [b] * 7,
	"a": [
		[b,b,b,b],
		[f,f,f,b],
		[f,s,f,b],
		[f,f,f,b],
		[f,s,f,b],
		[f,s,f,b],
		[b,b,b,b]
	],
	"b": [
		[b,b,b,b],
		[f,f,s,b],
		[f,s,f,b],
		[f,f,s,b],
		[f,s,f,b],
		[f,f,s,b],
		[b,b,b,b]
	],
	"c": [
		[b,b,b,b],
		[s,f,f,b],
		[f,s,s,b],
		[f,s,s,b],
		[f,s,s,b],
		[s,f,f,b],
		[b,b,b,b]
	],
	"d" : [
		[b,b,b,b],
		[f,f,s,b],
		[f,s,f,b],
		[f,s,f,b],
		[f,s,f,b],
		[f,f,s,b],
		[b,b,b,b]
	],
	"e": [
		[b,b,b,b],
		[f,f,f,b],
		[f,s,s,b],
		[f,f,f,b],
		[f,s,s,b],
		[f,f,f,b],
		[b,b,b,b]
	],
	"f" : [
		[b,b,b,b],
		[f,f,f,b],
		[f,s,s,b],
		[f,f,f,b],
		[f,s,s,b],
		[f,s,s,b],
		[b,b,b,b]
	],
	"g": [
		[b,b,b,b,b],
		[s,f,f,f,b],
		[f,s,s,s,b],
		[f,s,f,f,b],
		[f,s,s,f,b],
		[s,f,f,s,b],
		[b,b,b,b,b]
	],
	"h": [
		[b,b,b,b],
		[f,s,f,b],
		[f,s,f,b],
		[f,f,f,b],
		[f,s,f,b],
		[f,s,f,b],
		[b,b,b,b]
	],
	"i" : [
		[b,b,b,b],
		[f,f,f,b],
		[s,f,s,b],
		[s,f,s,b],
		[s,f,s,b],
		[f,f,f,b],
		[b,b,b,b]
	],
	"j": [
		[b,b,b,b,b],
		[s,f,f,f,b],
		[s,s,f,s,b],
		[s,s,f,s,b],
		[f,s,f,s,b],
		[s,f,s,s,b],
		[b,b,b,b,b]
	],
	"k": [
		[b,b,b,b],
		[f,s,f,b],
		[f,s,f,b],
		[f,f,s,b],
		[f,s,f,b],
		[f,s,f,b],
		[b,b,b,b]
	],
	"l": [
		[b,b,b,b],
		[f,s,s,b],
		[f,s,s,b],
		[f,s,s,b],
		[f,s,s,b],
		[f,f,f,b],
		[b,b,b,b]
	],
	"m": [
		[b,b,b,b,b,b],
		[s,f,s,f,s,b],
		[f,s,f,s,f,b],
		[f,s,f,s,f,b],
		[f,s,f,s,f,b],
		[f,s,f,s,f,b],
		[b,b,b,b,b,b]
	],
	"n": [
		[b,b,b,b,b],
		[f,s,s,f,b],
		[f,f,s,f,b],
		[f,s,f,f,b],
		[f,s,s,f,b],
		[f,s,s,f,b],
		[b,b,b,b,b]
	],
	"o": [
		[b,b,b,b],
		[s,f,s,b],
		[f,s,f,b],
		[f,s,f,b],
		[f,s,f,b],
		[s,f,s,b],
		[b,b,b,b]
	],
	"p": [
		[b,b,b,b],
		[f,f,f,b],
		[f,s,f,b],
		[f,f,f,b],
		[f,s,s,b],
		[f,s,s,b],
		[b,b,b,b]
	],
	"q": [
		[b,b,b,b,b],
		[f,f,f,f,b],
		[f,s,s,f,b],
		[f,s,s,f,b],
		[f,s,f,s,b],
		[f,f,s,f,b],
		[b,b,b,b,b]
	],
	"r": [
		[b,b,b,b],
		[f,f,s,b],
		[f,s,f,b],
		[f,f,s,b],
		[f,s,f,b],
		[f,s,f,b],
		[b,b,b,b]
	],
	"s": [
		[b,b,b,b],
		[f,f,f,b],
		[f,s,s,b],
		[f,f,f,b],
		[s,s,f,b],
		[f,f,f,b],
		[b,b,b,b]
	],
	"t": [
		[b,b,b,b],
		[f,f,f,b],
		[s,f,s,b],
		[s,f,s,b],
		[s,f,s,b],
		[s,f,s,b],
		[b,b,b,b]
	],
	"u": [
		[b,b,b,b],
		[f,s,f,b],
		[f,s,f,b],
		[f,s,f,b],
		[f,s,f,b],
		[f,f,f,b],
		[b,b,b,b]
	],
	"v": [
		[b,b,b,b],
		[f,s,f,b],
		[f,s,f,b],
		[f,s,f,b],
		[f,s,f,b],
		[s,f,s,b],
		[b,b,b,b]
	],
	"w": [
		[b,b,b,b,b,b],
		[f,s,f,s,f,b],
		[f,s,f,s,f,b],
		[f,s,f,s,f,b],
		[f,s,f,s,f,b],
		[s,f,s,f,s,b],
		[b,b,b,b,b,b]
	],
	"x": [
		[b,b,b,b],
		[f,s,f,b],
		[f,s,f,b],
		[s,f,s,b],
		[f,s,f,b],
		[f,s,f,b],
		[b,b,b,b]
	],
	"y": [
		[b,b,b,b],
		[f,s,f,b],
		[f,s,f,b],
		[s,f,s,b],
		[s,f,s,b],
		[s,f,s,b],
		[b,b,b,b]
	],
	"z": [
		[b,b,b,b],
		[s,s,s,b],
		[f,f,s,b],
		[f,s,f,b],
		[s,f,f,b],
		[s,s,s,b],
		[b,b,b,b]
	],
	"?": [
		[b,b,b,b],
		[s,f,s,b],
		[f,s,f,b],
		[f,s,f,b],
		[s,s,s,b],
		[s,f,s,b],
		[b,b,b,b]
	],
	"!": [
		[b,b,b,b],
		[s,f,s,b],
		[s,f,s,b],
		[s,f,s,b],
		[s,s,s,b],
		[s,f,s,b],
		[b,b,b,b]
	],
	"3": [
		[b,b,b,b],
		[f,f,f,b],
		[s,s,f,b],
		[s,f,f,b],
		[s,s,f,b],
		[f,f,f,b],
		[b,b,b,b]
	],
	"4": [
		[b,b,b,b],
		[f,s,f,b],
		[f,s,f,b],
		[f,f,f,b],
		[s,s,f,b],
		[s,s,f,b],
		[b,b,b,b]
	]
}

def mank(words):
	# hey now, you're an
	all_string = ''
	word_list = words.split(' ')
	for word in word_list:
		emoji_list = [b] * 7
		for letter in word:
			if letter != '.':
				if letter in char_map:
					for index, map_row in enumerate(char_map[letter]):
						single_row = [ char for char in map_row ]
						single_row = "".join(single_row)
						emoji_list[index] += single_row
				else:
					continue
		word_string = "\n".join(emoji_list)
		all_string += "{}\n".format(word_string)
	pyperclip.copy(all_string)

def main(arr):
	args = " ".join(arr[2:])
	mank(args)

if __name__ == '__main__':
	main(sys.argv)
