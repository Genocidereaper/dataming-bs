# Decision Tree Program - phishing Data

ageInput=int(input("Please enter age in months:  "))
if ageInput>=6:
	age="1"
else:
	age="-1"

# website fowarding
websitefowarding = int(input("Enter website fowarding "))
if websitefowarding>=2 and websitefowarding <4:
	websitefowardingstatus= "suspicious"
elif websitefowarding <= 1:
	websitefowardingstatus = "legitimate"
else: websitefowardingstatus = "phishing"

#pop up window
popupwindow= input("Enter info about pop up window")
if popupwindow != " ":
	popupwindow ="phishing"
else:
	popupwindow="legitimate"

# server form handling
hoursInput=input("server form handling")
if hoursInput == "about blank" or hoursInput==" ":
	hours="Phishing"
elif hoursInput=="different domain":
	hours="Suspicious"
else:
    hours = "legitimate"
	
# length of url
lengthofurl=int(input("enter url length: "))
if (lengthofurl >= 54 and lengthofurl <= 75):
	urlstatus="suspicious"
elif (lengthofurl<54):
	urlstatus="legitimate"
else:
	urlstatus="phishing"
	
# having ip Address
ipAdress = input("enter if it has an ip Address: yes or no only ")
if ipAdress == "yes":
    ipresult = "phishing"
else: ipresult = "legitimate"

# our classification output = fishing level	
# Initialize as unknown in case the tree doesnt cover output
fishing = "unknown"
	
if (websitefowarding>=2 and websitefowarding <4): # first branch
	if (popupwindow != " "):
			if hoursInput == "about blank" or hoursInput==" ":  # applies to all branches
				fishing="phishing"
			else:
				if age == "1":
					if urlstatus == "legitimate":
						fishing="legitimate"
					else:
						fishing="suspious"
				else:
					fishing="phishing"
elif websitefowarding <= 1:
	if  hoursInput=="different domain": #right tree
			if (OccInput >= 54 and OccInput <= 75):	
						fishing="suspicious"
			else:
			    fishing="legitimate"
				
					
	else:
		fishing="phishing"
else: # second branch	
	if (OccInput >= 54 and OccInput <= 75):
		fishing="suspicious" #left branch)
	else:
		if age=="-1":
			fishing="phishing" # left branch
		else:
			if hoursInput=="different domain": #right branch here
				if (websitefowarding>=2 and websitefowarding <4):
					if ipAdress == "yes":
						fishing="phishing"
					else:
						fishing="legitimate"
				else:
					fishing="suspicious"
			else:
				if (hoursInput == "about blank" or hoursInput==" "):	##finish
					if (OccInput >= 54 and OccInput <= 75):
						fishing="suspicious"
					elif (OccInput<54):
						fishing="legitimate"
					else:
						fishing="phishing"
				else:
					fishing="pshishing"
					
				
	
	
	


print("\nExpected website is  "+fishing) 
