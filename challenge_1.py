###########################################################################
## Copyright Robert-Gabor Varga
## http://robert-varga.com
##
## 210CT - Programming, Algorithms and Data Structures - Challenge 1
###########################################################################

class Store():
        def create(self):
                #dictionary as it is very efficinet for accessing and modification O(1)
                items = {}
                
                items["name"] = raw_input("Enter Name:")  # O(1)
                items["age"] = input("Enter age:")        # O(1)
                items["uni"] = raw_input("Enter University:")    # O(1)
                records.append(items)    # add items at the end of the list   - O(1)

                print "\nThe following entrie has been added:\n%s - %s - %s\n" % (items["name"], items["age"], items["uni"])  # O(1)

        def retrieve_all(self):
                print "\n"
                print "Name", "\t\t", "Age", "\t\t", "University"
                for item in records:   # O(n)
                        print item["name"], "\t\t", item["age"], "\t\t", item["uni"]  # O(1)
                print "\n"
                
        def sort_retrieve_all(self, sort_key):
                print "\n"
                sorted_elements = sorted(records, key=lambda tup: tup[sort_key])  # Timsrot having O(n * log n)
                print "Name", "\t\t", "Age", "\t\t", "University"
                for item in sorted_elements:  # O(n)
                        print "%s\t\t%i\t\t%s" % (item["name"], item["age"], item["uni"])  # O(1)
                print "\n"
                    
        def retrieve_by_name(self, name):  #printing records even the ones having the same NAME
                found = 0
                print "\n"
                for item in records:   # O(n)
                    if item["name"] == name:    # O(1)
                            if found == 0:    #print below titles only once
                                    print "Name", "\t\t", "Age", "\t\t", "University"
                                    found = 1
                            print "%s\t\t%i\t\t%s" % (item["name"], item["age"], item["uni"])   #skip tasks content  # O(1)
                            
                if (found==0):   
                        print "*Unknown name"
                        print "\n"
                        return
                print "\n"

                
        def remove_by_name(self, name):
                print "\n"
                for item in records:  # O(n)
                    if item["name"] == name:   # O(1)
                            records.pop(records.index(item))  # removes item from list   O(1)

        def add_task(self, name, task, priority):
                print "\n"
                for item in records:    # O(n)
                    if item["name"] == name:   # O(1)
                            item[priority] = task   # O(1)
                            return True
                        
        def highest_priority(self, name):    
                print "\n"
                for item in records:  # O(n)
                    if item["name"] == name and len(item) > 3:  # O(1) and O(n) for len which ferifys if task exists
                        return item["3"]   # O(1)

                return False
                                
        def remove_highest_priority(self, name):    
                print "\n"
                for item in records:
                    if item["name"] == name and len(item) > 3:    # O(1) and O(n)
                        del item["3"]    # O(1)
                        return True
                                
        def save_data(self):
                f = open('output.txt', 'w')
                simplejson.dump(records, f)
                f.close()

        def open_data(self):
                with open("output.txt") as f:
                        temp = simplejson.load(f)
                f.close()

                #delete existing list elements before inserting file contents
                del records[:]
                for items in temp:  
                        records.append(items)

                return True
                
                
                            
def Menu():
        #display menu"
        print "\t\tPeople Database"
        print "-----------------", len(records),"entries", "-----------------"
        print "1 -- Open saved data"
        print "2 -- Add entry"
        if len(records)==0:
                print "0 -- Exit"
        else:
                print "3 -- List entries"
                print "4 -- List sorted entries"
                print "5 -- Search by name"
                print "6 -- Remove by name"
                print "7 -- Add task"
                print "8 -- Highest priority task"
                print "9 -- Remove highest priority task"
                print "0 -- Exit"
                print "---------------------------------------------\n"

        #Get user input
        user = input("Enter option:")
        enter = Store()
        
        if user == 1:
                if ( enter.open_data() ):
                        print "\nData has been imported successfully\n"
                else:
                        print "\nNo data found\n"
        elif user == 2:
                enter.create()
        elif user == 3:
                enter.retrieve_all()
        elif user == 4:
                print "Sort options"
                print "\t1 -- Name"
                print "\t2 -- Age"
                print "\t3 -- University"
                key = input("Sort by:")
                if key > 0 and key < 4:
                        if key == 1: key="name"
                        elif key == 2: key="age"
                        else: key="uni"
                        enter.sort_retrieve_all(key)
                else:
                        print "Unknown prioirty\n"
                
        elif user == 5:
                name = raw_input("Enter name:")
                enter.retrieve_by_name(name)
        elif user == 6:
                name = raw_input("Enter name:")
                enter.remove_by_name(name)
        elif user == 7:
                name = raw_input("Enter name:")
                task = raw_input("Enter task:")
                print "Task priority"
                print "\t1 -- LOW"
                print "\t2 -- MEDIUM"
                print "\t3 -- HIGH"
                priority = raw_input("Priority:")    #if integer error with JSON
                if priority == "1" or priority == "2" or priority == "3":
                        output = enter.add_task(name, task, priority)
                        if output:
                                print "The task has been added\n" 
                        else:
                                print "*No user found\n"
                else:
                        print "Unknown prioirty\n"
        elif user == 8:
                name = raw_input("Enter name:")
                output = enter.highest_priority(name)
                if output:
                        print "The highest priority task is: ", output
                else:
                        print "*No high priority task or user found"
                print "\n"
        elif user == 9:
                name = raw_input("Enter name:")
                output = enter.remove_highest_priority(name)
                if output:
                        print "The task has been removed" 
                else:
                        print "*No high priority task or user found"
                print "\n"
        elif user == 0:
                decision = raw_input("\nWould you like to save your data y/n ? ")
                if decision == 'y':
                        print "Data successfully saved. Program has exited."                
                        enter.save_data()
                else:
                        print "No data has been saved. Pogram has exited."
                return False
        else:
                print "*Unknown command\n"

        return True


if __name__ == "__main__":
        import json as simplejson
        #list as it is very effective for appending and removing O(1)
        records = []

        while Menu():
                continue
        
