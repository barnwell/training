#this should collect file from aivc
#loop through them
#convert them to the testing suit format
#remover - at the begining of line
#ignore the hash tags
import re
import os
import json

# list of files to be sent to Json file
def list_of_files():
	path = '/mnt/c/Users/KVHoy/onedrive/desktop/chatette/aivc-tests/baseline'
	files = os.listdir(path)
	for f in files:
		#print(f)
		return(files)

def load_file(filename):
	loadfile = open("aivc-tests/baseline/"+ filename, "r")
	#gets name of loaded file
	replace_name = os.path.basename(loadfile.name)
	#takes away the extention from name of file
	name_of_file = os.path.splitext(replace_name)[0]

	if loadfile.mode == 'r':
		contents = loadfile.read()
	#remove all unnecessary items
		remove_dashes = re.sub("-","", contents)
		remove_hashes =re.sub("##", "", remove_dashes)
		remove_intent =re.sub("intent", "", remove_hashes)
		remove_colan =re.sub(":", "", remove_intent)
		remove_generic =re.sub("Generic", "", remove_colan)
		remove_critical =re.sub("critical", "", remove_generic)
		remove_line_one=re.sub("<! Generated using Chatette v1.6.2 >", "", remove_critical)
		edited_contents = remove_line_one	
		#print(edited_contents)
		#return(edited_contents)


	data1 = {}
	data1['clf_test_utterances'] = []
	data1['clf_test_utterances'].append({
		name_of_file: edited_contents
	 })
	# data2 = {}
	# data2['testing Suit'] = []
	# data2['testing Suit'].append({
	#     'Name': 'test',
	#     'Description': 'this is just a test',
	#     'Test Dialogue': '',
	#     "format_version": 5,
	#     "clf_test_utterances": data1
	# })
	
	data2 = {}
	data2['testing Suit'] = []
	data2['testing Suit'].append({
	    'Name': 'test',
	    'Description': 'this is just a test',
	    'Test Dialogue': '',
	    "format_version": 5,
	    "clf_test_utterances": data1
	})
	
	#this will write to json file
	with open('data2.json', 'w') as outfile:
	    json.dump(data2, outfile)
	



listoffile = list_of_files()


for i in list_of_files():
    if i.endswith(".txt"):
    	load_file(i)
    

