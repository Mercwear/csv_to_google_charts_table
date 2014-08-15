# Import the newere version of the print fuction so the sep argument will work when formatting my strings
from __future__ import print_function
import csv
import sys

# File that will be generated I want this to be a command line argument soon
out_file = open('Google Chart Table.txt', 'w')

# Name and location of the CSV file I want this to be a command line argument soon
in_file  = open('in.csv', "rb")

# Import the csv file
reader = csv.reader(in_file)

# Assign the column titles to the col_head variable. Note that the reader will now start on the first line of data rather than the column titles
col_titles = reader.next()


# Store the first part of the google charts code in a multi line string
google_chart_code = """
<script type="text/javascript" src="https://www.google.com/jsapi"></script>

    <script type="text/javascript">

    

google.load('visualization', '1', {packages:['table']});

      google.setOnLoadCallback(drawTable);

      function drawTable() {

        var data = new google.visualization.DataTable();
"""

# Store the second part of the google charts code in a multi line string
google_chart_code_bottom = """
]);



        var table = new google.visualization.Table(document.getElementById('table_div'));

        table.draw(data, {showRowNumber: true});

      }

    </script>

      <div id='table_div'></div>
"""

# Write first part of google code to file
out_file.write(google_chart_code)

#Write the colum titles to the output file in string format * I need to write a test to determine if they should be int or str * for the time being they are all being handled as strings
for word in col_titles:
	print("data.addColumn('string', '",word, "');",sep='',file=out_file)

# Write Google chart code to close out rows
print("data.addRows([",file=out_file)

# Cycle through each row of the CSV starting at row 2 and format the data to work with google charts a loop would be better to use here..
for row in reader:
	print(
		"[",
		"'",
		row[0],
		"'",
		",",
		"'",
		row[1],
		"'",
		",",
		"'",
		row[2],
		"'",
		",",
		"'",
		row[3],
		"'",
		",",
		"'",
		row[4],
		"'",
		",",
		"'",
		row[5],
		"'",
		",",
		"'",
		row[6],
		"'",
		",",
		"'",
		row[7],
		"'",
		",",
		"]",
		",",
		sep='',
		file=out_file
		)

# Write the last bit of Google chart code to the output file
out_file.write(google_chart_code_bottom)

# Close the csv file
in_file.close()

# Close the output file
out_file.close()


# Format that google charts expects for table output
#  ['A', 'A', 1, 'A', 'A', 'A', 'A', 'A'],