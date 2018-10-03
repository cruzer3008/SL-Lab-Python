student_list = {
	##'name': ['A','B','C','D','E'],
	##'USNs': ['1MS16IS001','1MS16IS002','1MS16IS003','1MS16IS004','1MS16IS005'],
	##'course': ['SL','DBMS','SL','CN','OS']
	##1:['A','1MS16IS001','SL'],
	##2:['B','1MS16IS002','DBMS'],
	##3:['C','1MS16IS003','OS'],
	##4:['D','1MS16IS004','CN'],
	##5:['E','1MS16IS005','SL']

	'1MS16IS120' : ['A','SL'],
	'1MS16IS121' : ['B','NLP'],
	'1MS16IS122' : ['C','DBMS'],
	'1MS16IS123' : ['D','CN'],
	'1MS16IS124' : ['E','OS']	
	
}


print "Number of Students: ",len(student_list)
##print "\nThe list of students is: \n",student_list.get('name')
##student_list[6]= ['F','1MS16IS006','DIP']
##student_list[6]= ['G','1MS16IS007','NLP']

##student_list.get('name').append('F')
##student_list.get('name').append('G')
##print "\nThe list of students after adding new names is:\n ",student_list.get('name')


print '\n<----List of List--->\n'
list_of_lists = [['John','Johnson','Jonathan'],['Apple','Orange','Pear'],['Red','Green','Blue']]
print list_of_lists
print "\nThe second student is ",list_of_lists[0][1]
