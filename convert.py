import csv
from datetime import datetime

direct_keys = ['registration_name', 'max_reservations', 'registration_description']
date_keys = {
	'registration_start_datetime':['registration_start_date_full', 'registration_start_time'],
	'registration_end_datetime':['registration_end_date_full', 'registration_end_time']
}
value_keys = {
	'signup_start_days_before':60,
	'signup_start_days_before':0
}
date_mapping = {
	'2017-04-26':'2017-09-20',
	'2017-04-27':'2017-09-21',
	'2017-04-28':'2017-09-22',
	'2017-04-29':'2017-09-23',
	'2017-04-30':'2017-09-24',
}
input_key_mapping = {}
with open('data_to_convert.csv') as csvfile:
	reader = csv.DictReader(csvfile)

	with open('headers.csv', 'rb') as header_file:

		header_dict = csv.DictReader(header_file)
		# print(header_dict.fieldnames)

		with open('output_data.csv', 'w') as outputfile:
			writer = csv.DictWriter(outputfile, fieldnames=header_dict.fieldnames)
			writer.writeheader()

			for row in reader:
				registration_name = row['registration_name']
				max_reservations = row['max_reservations']
				registration_description = row['registration_description']


				registration_start_date_full = date_mapping[row['registration_start_datetime'].split(' ')[0]]
				registration_start_time = datetime.strptime(row['registration_start_datetime'].split(' ')[1],'%H:%M:%S').strftime('%I:%M %p')
				registration_end_date_full = date_mapping[row['registration_end_datetime'].split(' ')[0]]
				registration_end_time = datetime.strptime(row['registration_end_datetime'].split(' ')[1],'%H:%M:%S').strftime('%I:%M %p')

				signup_start_days_before = 60
				signup_end_days_before = 0

				writer.writerow({'registration_name': registration_name, 'max_reservations': max_reservations, 
					'registration_description':registration_description, 'registration_start_date_full':registration_start_date_full,
					'registration_start_time':registration_start_time, 'registration_end_date_full':registration_end_date_full, 
					'registration_end_time':registration_end_time,'signup_start_days_before':signup_start_days_before, 
					'signup_end_days_before':signup_end_days_before})