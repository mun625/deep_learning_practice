import sys
import json

def lines(fp):
    print str(len(fp.readlines()))

def StateAbbreviation(str):
	states = {
        'Alaska':'AK',
        'Alabama':'AL',
        'Arkansas':'AR',
        'American Samoa':'AS',
        'Arizona':'AZ',
        'California':'CA',
        'Colorado':'CO',
        'Connecticut':'CT',
        'District of Columbia':'DC',
        'Delaware':'DE',
        'Florida':'FL',
        'Georgia':'GA',
        'Guam':'GU',
        'Hawaii':'HI',
        'Iowa':'IA',
        'Idaho':'ID',
        'Illinois':'IL',
        'Indiana':'IN',
        'Kansas':'KS',
        'Kentucky':'KY',
        'Louisiana':'LA',
        'Massachusetts':'MA',
        'Maryland':'MD',
        'Maine':'ME',
        'Michigan':'MI',
        'Minnesota':'MN',
        'Missouri':'MO',
        'Northern Mariana Islands':'MP',
        'Mississippi':'MS',
        'Montana':'MT',
        'National':'NA',
        'North Carolina':'NC',
        'North Dakota':'ND',
        'Nebraska':'NE',
        'New Hampshire':'NH',
        'New Jersey':'NJ',
        'New Mexico':'NM',
        'Nevada':'NV',
        'New York':'NY',
        'Ohio':'OH',
        'Oklahoma':'OK',
        'Oregon':'OR',
        'Pennsylvania':'PA',
        'Puerto Rico':'PR',
        'Rhode Island':'RI',
        'South Carolina':'SC',
        'South Dakota':'SD',
        'Tennessee':'TN',
        'Texas':'TX',
        'Utah':'UT',
        'Virginia':'VA',
        'Virgin Islands':'VI',
        'Vermont':'VT',
        'Washington':'WA',
        'Wisconsin':'WI',
        'West Virginia':'WV',
        'Wyoming':'WY'
	}
	if str in states:
		return states[str]
	else:
		return 'USA'

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
			#print score
		else:
			scores.append(0)
			#print 0
	return scores



def GetPlaces(fp):
	#print json.loads(fp.readlines()[0])['delete']
	places = []
	for line in fp.readlines():
		if 'place' in json.loads(line):
			places.append(json.loads(line)['place'])
		else:
			places.append(None)
	return places

def MaxKeyDic(my_dic):
	max_value = -999999
	max_key = ""
	for key, value in my_dic.iteritems():
		if value > max_value:
			max_value = value
			max_key = key
	return max_key

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	#lines(sent_file)
	#lines(tweet_file)

	score_dic = scoredic(sys.argv[1])			# make AFINN-111.txt to dictionary
	scores = makescore(sys.argv[2], score_dic)	# derive the sentiment score of each tweet
	places = GetPlaces(tweet_file)

	states_list = {}
	counter = 0
	for place in places:
		if place is not None:
			if 'country' in place:
				if place['country'].encode('utf8') == "United States":
					if 'full_name' in place:
						first, second = place['full_name'].split(', ')
						states = second
						if states == 'USA':
							states = StateAbbreviation(first)

						if states in states_list.keys():
							states_list[states] += scores[counter]
						else:
							states_list[states] = scores[counter]
		counter+=1

	print MaxKeyDic(states_list)

if __name__ == '__main__':
    main()