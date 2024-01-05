"""Small example streamlit application."""
import streamlit as st
st.title("hello world")

# set the app's title                                                   
st.title("Text Elements")

# header                                                                
st.header("Header in Streamlit")

# subheader                                                             
st.subheader("Subheader in Streamlit")

# markdown                                                              
# display text in bold formatting                                       
st.markdown("**AskPython** is an awesome website!")
# display text in italic formatting                                     
st.markdown("Visit _askpython.com_ to learn from various Python tutoria\
ls.")

# code block                                                            
code = '''                                                              
def add(a, b):                                                          
    print("a+b = ", a+b)                                                
'''
st.code(code, language='python')

# latex                                                                 
st.latex('''                                                            
(a+b)^2 = a^2 + b^2 + 2*a*b                                             
''')

#button                                                                 
if st.button('Click here', help="Click to see the text change"):
    st.write('Hi there!')
else:
    st.write('Goodbye')

# check box                                                             
checked = st.checkbox('Click here')
if checked:
    st.write('Good job!')



"""
def app():
    """Define main application entry point."""
    st.title("Minimal Streamlit Template")
    # And write the rest of the app inside this function!
    st.markdown("Here is where you can insert more text.")
    st.markdown("""Streamlit works more on the basis of 
\"insert things and let Streamlit figure out how to render 
them\".  If you want more flexibility for how to render
the markdown and other elements on your webpage, 
you may want to consider
[Flask](https://flask.palletsprojects.com/).""")

    st.sidebar.markdown("""You can put things in the sidebar:
* Like lists
* Or other things""")

if __name__ == '__main__':
    app()
"""

