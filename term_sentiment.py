import sys
import json
import io

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

def FilterZeroScoreSentence(fp, score_dic):
	sentence_file = open(fp)
	sentence_dic = {}
	for line in sentence_file:
		tester = json.loads(line)
		if 'text' in tester:
			if SentenceToScore(tester['text'], score_dic) != 0:
				sentence_dic[tester['text']] = SentenceToScore(tester['text'], score_dic)
	return sentence_dic

def DeriveScoreFromSentence(sentence_dic):
	word_dic = {}
	count_dic = {}
	for key, value in sentence_dic.iteritems():
		for word in key.split():
			if word in word_dic.keys():
				word_dic[word] += value
				count_dic[word] += 1
			else:
				word_dic[word] = value
				count_dic[word] = 1

	for key, value in word_dic.iteritems():
		word_dic[key] = float(word_dic[key]) / count_dic[key]
	
	return word_dic

def scoredic(fp):
	score_file = open(fp)	# open the score file
	score_dic = {}			# initialize an empty dictionary
	for line in score_file:
		term, score = line.split("\t")	# the file is tab-deliminated.
		score_dic[term] = int(score)	# Convert the score to an integer.
	return score_dic

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    lines(sent_file)
    lines(tweet_file)

    score_dic = scoredic(sys.argv[1])	# make AFINN-111.txt to dictionary
    filterd_sentence = FilterZeroScoreSentence(sys.argv[2], score_dic)
    new_score_dic = DeriveScoreFromSentence(filterd_sentence)

    f = open("problem_3_submission.txt","w")	# write score to problem_3_submission.txt
    for key, value in new_score_dic.iteritems():
    	#f.write("%s %s\n" % (str(key), str(value)))
    	f.write("%s\n" % str(key))
    f.close()

if __name__ == '__main__':
    main()
