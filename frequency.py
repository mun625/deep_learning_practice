import sys
import json

def lines(fp):
    print str(len(fp.readlines()))

def FileToWord(fp):
	word_file = open(fp)
	word_dic = {}
	total_count = 0

	for line in word_file:
		tester = json.loads(line)
		if 'text' in tester:
			for word in tester['text'].split():
				word_dic[word] = 0
				total_count += 1
	word_file.close()

	word_file = open(fp)
	for line in word_file:
		tester = json.loads(line)
		if 'text' in tester:
			for word in tester['text'].split():
				word_dic[word] += 1

	for key, value in word_dic.iteritems():
		print key, float(value)/total_count


def main():
	tweet_file = open(sys.argv[1])
	#lines(tweet_file)
	FileToWord(sys.argv[1])

if __name__ == '__main__':
    main()