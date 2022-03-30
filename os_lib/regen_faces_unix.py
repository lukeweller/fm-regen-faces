#!/usr/bin/env python3
# Luke Weller [https://github.com/lukeweller]
# Mar 8 2022
# -------------------------------------------
import random
import os.path
import os
import shutil
import sys
import pandas as pd

# Helper function for skiprows parameter in pandas.read_csv()
# Returns True for all lines numbers to read & returns False for all line numbers to skip
def skip_rows(x):
	if x < 9 or x % 2 == 0:
		return False
	else:
		return True

def load_rtf(rtf_filename):
	
	if not os.path.exists(rtf_filename):
		print('error: unable to open input file \'{}\''.format(rtf_filename))
		sys.exit(1)
		
	try:
		df = pd.read_csv(rtf_filename, sep = '|', skiprows=lambda x: skip_rows(x), skipinitialspace=True)
	
	except:
		print('error: failed to load input file \'{}\' into the df'.format(rtf_filename))
		sys.exit(1)

	return df

def preprocessing(df):

	# In its current state, read_csv() includes two extra, unnamed columns
	# before and after all of the real columns (i.e., at index 0 & -1)
	df = df.iloc[:, 1:-1]

	# Removes whitespace from column headers
	df = df.rename(columns=lambda x: x.strip())

	# Removes whitespace from body (all values)
	df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

	# Give names to columns for hidden attributes
	df.rename(columns={'Unnamed: 5': 'Hair Length', 'Unnamed: 6': 'Hair Color', 'Unnamed: 7': 'Skin Tone'}, inplace=True)

	hair_length_map = {0: 'Bald', 1: 'Not Bald'}
	hair_color_map = {1: 'Blonde', 2: 'Light Brown', 3: 'Dark Brown', 4: 'Red', 5: 'Black', 6: 'Gray'}
	# TODO: find value for skin tone 8, 9
	skin_tone_map = {0: 'White', 1: 'Hispanic-Lighter', 2: 'Arabic', 3: 'Black', 4: 'South Asian', 5: 'Southeast Asian', 6: 'Pacific Islander', 7: 'Hispanic-Darker', 8: '?', 9: 'Biracial', 10: 'East Asian'}

	df['Hair Length'] = df['Hair Length'].apply(lambda x: hair_length_map[x])
	df['Hair Color'] = df['Hair Color'].apply(lambda x: hair_color_map[x])
	df['Skin Tone'] = df['Skin Tone'].apply(lambda x: skin_tone_map[x])

	return df

def create_regens(df):

	for index, row in df.iterrows(): 

		print("• {:<20} | {:<16} | {:<10} | {:<8} | {:<10} | ".format(row['Name'], row['Skin Tone'], row['Hair Color'], row['Hair Length'], row['UID']), end='')

		# Check if player exists in real life
		# TODO: Verify that this UID value is correct
		if row['UID'] <= 1915400000:
			print('Real Player')
			continue

		# Check if face has already exists
		filename = 'faces/in-use/{}.png'.format(str(row['UID']))

		if os.path.exists(filename):
			print('Existing Regen')
			continue

		# Randomly selected a new regen face with matching features
		matching_folder = 'faces/{}/{}/{}'.format(row['Skin Tone'], row['Hair Color'], row['Hair Length'])

		try:
			canidates = os.listdir(matching_folder)

		except FileNotFoundError:
			print('\nerror: unable to find canidates folder for features: {}'.format([row['Skin Tone'], row['Hair Color'], row['Hair Length']]))
			sys.exit(1)

		selected_face = random.choice(canidates)

		try:
			shutil.copy2('{}/{}'.format(matching_folder, selected_face), 'faces/in-use/{}.png'.format(row['UID']))

		except:
			print('\nerror: failed to copy selected face to \'faces/in-use/\'')
			sys.exit(1)


		new_config_entry = '\t\t<record from=\'{}\' to=\'graphics/pictures/person/{}/portrait\'/>\n'.format(row['UID'], row['UID'])
		
		try:
			config = ''
			
			with open('faces/in-use/config.xml', 'r') as config_file:
				config = config_file.readlines()
				config.insert(-3, new_config_entry)

			with open('faces/in-use/config.xml', 'w') as config_file:
				config = ''.join(config)
				config_file.write(config)

		except:
			print('\nerror: failed to copy selected face to \'/faces/in-use/\'')
			sys.exit(1)

		print('Added Regen')
