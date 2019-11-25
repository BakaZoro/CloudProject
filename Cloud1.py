
import socket                
import subprocess
def rem_punc(file):    
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    
    my_str = file.read()
    no_punct = ""
    for char in my_str:
        if char not in punctuations:
            no_punct = no_punct + char
    return no_punct
def readfile(text):
    unique_words = []
    total_words = []
    for i in text.split('\n'):
        for j in i.split(' '):
            total_words.append(j)
            if j not in unique_words:
                unique_words.append(j)
    return (unique_words, total_words)
def wordcount(unique_words,total_words):
    words_freq = {}
    for i in unique_words:
        if i not in " ":
            words_freq[str(i)] = int(total_words.count(i))
    return words_freq

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

def add_string(_str_):
    j = 0
    for i in _str_:
        j = j + int(i)
    return str(j)

s = socket.socket()          
print ("Socket successfully created")
port = int(input("enter port: "))
s.bind(('', port))         
print ("socket binded to %s" %(port) )
s.listen(5)      
print ("socket is listening" )           

c, addr = s.accept()      
print ("Got connection from", addr) 

while True: 
    
    data=c.recv(1024)
    command = data.decode()
    if int(command) == 1:
        file = open("texttoberun","r")
        uw, tw = readfile(rem_punc(file))
        dics = wordcount(uw, tw)
        rangee = 10
        for key, value in sorted(dics.items(), key=lambda item: item[1], reverse=True):
            
            a = subprocess.check_output("top -bn 1 | awk '{print $9}' | tail -n +8 | awk '{s+=$1} END {print s}'", shell=True)
            pp = str(a).split("'")[1]
            print(str(pp).split("\\")[0])
        
            if(float(str(pp).split("\\")[0]) > 100):
                print("Stopping process")
                break

            
            if key.lower() not in stop_words:
                if rangee >=0:
                    rangee-=1
                    print("%s: %s" % (key, value))
               
c.close()


# In[ ]:








