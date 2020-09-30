#this should collect file from aivc
#loop through them
#convert them to the testing suit format
#remover - at the begining of line
#ignore the hash tags
import re
import os
import json


#load the text file from aivc-test/baseline	
loadfile = open("aivc-tests/baseline/clf_risk_start.txt", "r")
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
	remove_line_one=re.sub("<! Generated using Chatette v1.6.2 >", name_of_file, remove_critical)
	edited_contents = remove_line_one	
	#print(edited_contents)
#write to json
data1 = {}
data1['clf_test_utterances'] = []

data1['clf_test_utterances'].append({
	name_of_file: edited_contents
 })
data2= {}
data2['testing Suit'] = []

data2['testing Suit'].append({
    'Name': 'test',
    'Description': 'this is just a test',
    'Test Dialogue': '',
    "format_version": 5,
    "clf_test_utterances": data1

})

#print(data2)
with open('data2.json', 'w') as outfile:
    json.dump(data, outfile)	


#replace the content unwanted contents of text file
#repeat for all txt files

#convert to json
