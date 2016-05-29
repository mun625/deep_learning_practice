import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def SentenceToScore(str, score_dic):
	words = str.split()
	score = 0
	for word in words:
		if word in score_dic.keys():
			score += score_dic[word]
	return score

def scoredic(fp):
	score_file = open(fp)	# open the score file
	score_dic = {}			# initialize an empty dictionary
	for line in score_file:
		term, score = line.split("\t")	# the file is tab-deliminated.
		score_dic[term] = int(score)	# Convert the score to an integer.
	return score_dic

def makescore(fp, score_dic):
	analyzing_file = open(fp)
	tester = ''
	scores = []
	for line in analyzing_file:
		tester = json.loads(line)
		if 'text' in tester:
			score = SentenceToScore(tester['text'], score_dic)
			scores.append(score)
			print score
		else:
			scores.append(0)
			print 0
	return scores


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)

    score_dic = scoredic(sys.argv[1])			# make AFINN-111.txt to dictionary
    scores = makescore(sys.argv[2], score_dic)	# derive the sentiment score of each tweet

    f = open("problem_2_submission.txt","w")	# write score to problem_2_submission.txt
    for score in scores:
    	f.write("%s\n" % str(score))
    f.close()


if __name__ == '__main__':
    main()
