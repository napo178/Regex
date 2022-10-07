## Application page for regex playground

import re
import streamlit as st

st.title('Regex Playground')


st.sidebar.title("How it works")
st.sidebar.info(
        """
1. Paste the text document in the first box. 


2. Try Creating a regular expression pattern to fit the word or string that you want to find. For example the twitter handle of Ron Miller - "@[a-z_]+"
3. Press Enter - the text **becomes bold** if your pattern is correct.
""")

sentence = st.text_input('Input your text here:') 
 
pattern = st.text_input('Enter pattern to find here')

patt = ""
find = []

try:
    re.compile(pattern)
except:
    st.text("Wrong Pattern")
else:
    patt = re.compile(pattern)


if patt:
    find = re.findall(patt, sentence)
    
text = sentence   
x = re.finditer(patt, text)
counter = 0
listext = list(text)
for i in x:
    listext.insert(i.span()[0]+counter,"<b>")
    listext.insert(i.span()[1]+1+counter,"</b>")
    counter +=2

listext ="".join(listext)


if len(pattern) == 0:
    st.text("Waiting For Pattern")
    st.markdown(sentence, unsafe_allow_html=True)
elif not find: 
    st.text("Pattern Not Found")
    st.markdown(sentence, unsafe_allow_html=True)    
else:
    message = "Pattern Found at " + str(len(find)) + " location(s)"
    st.text(message)
    st.markdown(listext, unsafe_allow_html=True)
    



    

