import sys
import json

def MaxKeyDic(my_dic):
	max_value = -999999
	max_key = ""
	for key, value in my_dic.iteritems():
		if value > max_value:
			max_value = value
			max_key = key
	return max_key

def HashCount(fp):
	hash_dic = {}
	for line in fp.readlines():
		if 'entities' in json.loads(line):
			entity = json.loads(line)['entities']
			if 'hashtags' in entity:
				hashtag = entity['hashtags']
				for tag in hashtag:
					if 'text' in tag:
						if tag['text'] in hash_dic.keys():
							hash_dic[tag['text']] += 1
						else:
							hash_dic[tag['text']] = 1

	return hash_dic

def main():
    tweet_file = open(sys.argv[1])
    hash_dic = HashCount(tweet_file)

    for i in range(0,10):
    	print MaxKeyDic(hash_dic), hash_dic[MaxKeyDic(hash_dic)]
    	hash_dic.pop(MaxKeyDic(hash_dic))
    	if len(hash_dic) < 1:
    		break

if __name__ == '__main__':
    main()
