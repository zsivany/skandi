#
#Scandinavaian Lottery - counts of "4-long" combinations
#__author__ = "Tamas Papp"
#__version__ = "1.0.0"
import collections

#function for comparing two lists - looking for the same elements (using inbuilt set function, too)
def listcomp (list1, list2):
    if  len(list(set(list1).intersection(list2))) == 4:
        return list(set(list1).intersection(list2))
    else:
        False


# Import the numbers from file into a list (technically in list of lists format)
list_of_lists = []
with open("skandi.txt") as f:
    for line in f:
        # in alternative, if you need to use the file content as numbers
        inner_list = [int(elt.strip()) for elt in line.split(',')]
        list_of_lists.append(inner_list)

f.close()

#test reason
##print list_of_lists

# Making the pairs for the comparing function
list_of_pairs = [[list_of_lists[p1], list_of_lists[p2]] for p1 in range(len(list_of_lists)) for p2 in range(p1+1,len(list_of_lists))]

#test reason
##print len(list_of_pairs)


# Making the comparisona and storing the matches in the result array
result = []

for i in range(len(list_of_pairs)):
    ##print "The result of ", list_of_pairs[i][0], list_of_pairs[i][1], " is: "
    if listcomp(list_of_pairs[i][0],list_of_pairs[i][1] ):
        result.append(listcomp(list_of_pairs[i][0],list_of_pairs[i][1] ))

#test reason    
##print len(result)
##print result

# Sorting the elements for get right counts number
# Without sorting not ensured the correct values
result_sorted = []
for i in result:
    result_sorted.append(sorted(i))

#test reason    
##print result_sorted

#Counting the same elements. Using collections module.
counts = [(a, v) for a,v in collections.Counter(map(tuple,result_sorted)).iteritems()]

#Writing the result into a file
with open ("result.txt", "w") as result_file:

    for i in counts:
        result_file.writelines("%s\n" % str(i))

result_file.close()



