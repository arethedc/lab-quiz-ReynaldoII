import time
file = open("network_issue.txt", "a") 
print("Reynaldo II Dela Cruz")
print("Student ID: 191-0988")
print(f"Date and time: {time.ctime()}")

text = input("Networking issue: ")
file.write("Reynaldo II Dela Cruz\n")
file.write("Student ID: 191-0988\n")
file.write(f"Date and time: {time.ctime()}\n")
file.write(f"Issue: {text}\n")
file.write("-" * 30 + "\n")
file.close()
