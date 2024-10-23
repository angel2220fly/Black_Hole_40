s=2
while s!=65535:

		# Content for point number 2
    with open("1.txt", "r") as file:
              R = file.read()
    s=int(R)
    s+=1
    content = str(s)
    with open("1.txt", "w") as file:
	    file.write(content)	
    
    with open("Black_Hole_40.py") as hello:
    	exec(hello.read())