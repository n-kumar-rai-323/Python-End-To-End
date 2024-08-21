# Write a program to print Nepal Netional Song ? 

print("""सयौं थूंगा फूलका हामी, एउटै माला नेपाली
सार्वभौम भई फैलिएका, मेची-महाकाली।
प्रकृतिका कोटी-कोटी सम्पदाको आँचल
वीरहरूका रगतले, स्वतन्त्र र अटल
ज्ञानभूमि, शान्तिभूमि तराई, पहाड, हिमाल
अखण्ड यो प्यारो हाम्रो मातृभूमि नेपाल।
बहुल जाति, भाषा, धर्म, संस्कृती छन् विशाल
अग्रगामी राष्ट्र हाम्रो, जय जय नेपाल।""")

# Install exteral module and use it to  perform an operation of your interest. 
import pyttsx3
engine = pyttsx3.init()
engine.say("I love Coding ")
engine.runAndWait()


# wirte a python program to print contents of a  directory using the os module. Search online for the function which does that 
import os 


# Specify the directory path
directory_path = "/Users"

# List all files and directories in the specified path
contents = os.listdir(directory_path)

# Print the contents
for item in contents:
    print(item)