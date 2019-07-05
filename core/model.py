from core.db import vocab
import re
from core.utils import detokenize, current_time, tokenize, get_date_from_string, get_time_diff, display_format

def insert(word : str, speech: str,meaning : str, usage = '', example = ''):

	# check if the word  already exits in the database

	old_doc = vocab.find_one({'word':detokenize(word)},{'_id':0})

	if old_doc:
		display_format(old_doc)
		print('\n')
		key = input(f'If you want to update this word: {detokenize(word)}  in database type \'y\' or \'yes\' and hit Enter :')
		if key.lower() == 'y' or key.lower() == 'yes':
			adhoc_doc = {'speech':tokenize(speech),'meaning': detokenize(meaning), 'example':detokenize(example),
		'usage':detokenize(usage)}
			vocab.update_one({'word':detokenize(word)},adhoc_doc)
		return 

	doc = {'word':detokenize(word), 'speech':tokenize(speech),'meaning': detokenize(meaning), 'example':detokenize(example),
		'usage':detokenize(usage), 'date':current_time()}

	vocab.insert_one(doc)


def display(timestamp):
	last_time = get_date_from_string(current_time()) - get_time_diff(timestamp)
	for docs in vocab.find({},{'_id':0}).limit(100):
		if get_date_from_string(docs['date']) > last_time:
			yield docs


# get random record from mongodb using aggregation
# new features in mongodb  , Really Fascinating and so useful
def get_random_record(num):
	'''
	@num: number of random records you want to get
	'''
	for docs in vocab.aggregate([{ '$sample': { 'size': num } }]):
		yield docs
