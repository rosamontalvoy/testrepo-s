Writing Your First Python Code

("Hello, Python!")

print('Hello, Python!')


import sys
print(sys.version)


print('Hello, Python! This line prints a string')
print('Hi')

# Print string as error message

frint("Hello, Python!")


# Try to see built-in error message

print("Hello, Python!)

# Print string and error to see the running order

print("This will be printed")
frint("This will cause an error")
print("This will NOT be printed")


("Hello, world!")
print("Hello, world!")

print("Hello, world") # Print the traditional hello world

# Integer

11


# Float

2.14


# In[ ]:


# String

"Hello, Python 101!"

# Type of 12

type(12)

# Type of 2.14

type(2.14)

type("Hello, Python 101!")

type(12.0)

# Print the type of -1

type(-1)

# Print the type of 4

type(4)


# In[ ]:


# Print the type of 0

type(0)

# Print the type of 1.0

type(1.0) # Notice that 1 is an int, and 1.0 is a float


# In[ ]:


# Print the type of 0.5

type(0.5)


# In[ ]:


# Print the type of 0.56

type(0.56)


# In[ ]:


# System settings about float type

sys.float_info


# <h3 id="convert">Converting from one object type to a different object type</h3>
# 

# <p>You can change the type of the object in Python; this is called typecasting. For example, you can convert an <i>integer</i> into a <i>float</i> (e.g. 2 to 2.0).</p>
# <p>Let's try it:</p>
# 

# In[18]:


# Verify that this is an integer

type(2)


# <h4>Converting integers to floats</h4>
# <p>Let's cast integer 2 to float:</p>
# 

# In[19]:


# Convert 2 to a float

float(2)


# In[20]:


# Convert integer 2 to a float and check its type

type(float(2))


# <p>When we convert an integer into a float, we don't really change the value (i.e., the significand) of the number. However, if we cast a float into an integer, we could potentially lose some information. For example, if we cast the float 1.1 to integer we will get 1 and lose the decimal information (i.e., 0.1):</p>
# 

# In[21]:


# Casting 1.1 to integer will result in loss of information

int(1.1)


# <h4>Converting from strings to integers or floats</h4>
# 

# <p>Sometimes, we can have a string that contains a number within it. If this is the case, we can cast that string that represents a number into an integer using <code>int()</code>:</p>
# 

# In[22]:


# Convert a string into an integer

int('1')


# <p>But if you try to do so with a string that is not a perfect match for a number, you'll get an error. Try the following:</p>
# 

# In[23]:


# Convert a string into an integer with error

int('1 or 2 people')


# <p>You can also convert strings containing floating point numbers into <i>float</i> objects:</p>
# 

# In[24]:


# Convert the string "1.2" into a float

float('1.2')


# <hr/>
# <div class="alert alert-success alertsuccess" style="margin-top: 20px">
#     [Tip:] Note that strings can be represented with single quotes (<code>'1.2'</code>) or double quotes (<code>"1.2"</code>), but you can't mix both (e.g., <code>"1.2'</code>).
# </div>
# <hr/>
# 

# <h4>Converting numbers to strings</h4>
# 

# <p>If we can convert strings to numbers, it is only natural to assume that we can convert numbers to strings, right?</p>
# 

# In[25]:


# Convert an integer to a string

str(1)


# <p>And there is no reason why we shouldn't be able to make floats into strings as well:</p> 
# 

# In[26]:


# Convert a float to a string

str(1.2)


# <h3 id="bool">Boolean data type</h3>
# 

# <p><i>Boolean</i> is another important type in Python. An object of type <i>Boolean</i> can take on one of two values: <code>True</code> or <code>False</code>:</p>
# 

# In[27]:


# Value true

True


# <p>Notice that the value <code>True</code> has an uppercase "T". The same is true for <code>False</code> (i.e. you must use the uppercase "F").</p>
# 

# In[28]:


# Value false

False


# <p>When you ask Python to display the type of a boolean object it will show <code>bool</code> which stands for <i>boolean</i>:</p> 
# 

# In[29]:


# Type of True

type(True)


# In[30]:


# Type of False

type(False)


# <p>We can cast boolean objects to other data types. If we cast a boolean with a value of <code>True</code> to an integer or float we will get a one. If we cast a boolean with a value of <code>False</code> to an integer or float we will get a zero. Similarly, if we cast a 1 to a Boolean, you get a <code>True</code>. And if we cast a 0 to a Boolean we will get a <code>False</code>. Let's give it a try:</p> 
# 

# In[31]:


# Convert True to int

int(True)


# In[32]:


# Convert 1 to boolean

bool(1)


# In[33]:


# Convert 0 to boolean

bool(0)


# In[34]:


# Convert True to float

float(True)


# <h3 id="exer_type">Exercise: Types</h3>
# 

# <p>What is the data type of the result of: <code>6 / 2</code>?</p>
# 

# In[35]:


# Write your code below. Don't forget to press Shift+Enter to execute the cell
type(6/2)


# <details><summary>Click here for the solution</summary>
# 
# ```python
# type(6/2) # float
# 
# ```
# 
# </details>
# 

# <p>What is the type of the result of: <code>6 // 2</code>? (Note the double slash <code>//</code>.)</p>
# 

# In[36]:


# Write your code below. Don't forget to press Shift+Enter to execute the cell
type(6//2)


# <details><summary>Click here for the solution</summary>
# 
# ```python
# type(6//2) # int, as the double slashes stand for integer division 
# 
# ```
# 
# </details>
# 

# <hr>
# 

# <h2 id="expressions">Expression and Variables</h2>
# 

# <h3 id="exp">Expressions</h3>
# 

# <p>Expressions in Python can include operations among compatible types (e.g., integers and floats). For example, basic arithmetic operations like adding multiple numbers:</p>
# 

# In[37]:


# Addition operation expression

43 + 60 + 16 + 41


# <p>We can perform subtraction operations using the minus operator. In this case the result is a negative number:</p>
# 

# In[38]:


# Subtraction operation expression

50 - 60


# <p>We can do multiplication using an asterisk:</p>
# 

# In[39]:


# Multiplication operation expression

5 * 5


# <p>We can also perform division with the forward slash:
# 

# In[40]:


# Division operation expression

25 / 5


# In[41]:


# Division operation expression

25 / 6


# <p>As seen in the quiz above, we can use the double slash for integer division, where the result is rounded down to the nearest integer:
# 

# In[42]:


# Integer division operation expression

25 // 5


# In[43]:


# Integer division operation expression

25 // 6


# <h3 id="exer_exp">Exercise: Expression</h3>
# 

# <p>Let's write an expression that calculates how many hours there are in 160 minutes:
# 

# In[ ]:


# Write your code below. Don't forget to press Shift+Enter to execute the cell


# <details><summary>Click here for the solution</summary>
# 
# ```python
# 160/60 
# 
# # Or 
# 
# 160//60
# 
# ```
# 
# </details>
# 

# <p>Python follows well accepted mathematical conventions when evaluating mathematical expressions. In the following example, Python adds 30 to the result of the multiplication (i.e., 120).
# 

# In[44]:


# Mathematical expression

30 + 2 * 60


# <p>And just like mathematics, expressions enclosed in parentheses have priority. So the following multiplies 32 by 60.
# 

# In[45]:


# Mathematical expression

(30 + 2) * 60


# <h3 id="var">Variables</h3>
# 

# <p>Just like with most programming languages, we can store values in <i>variables</i>, so we can use them later on. For example:</p>
# 

# In[47]:


# Store value into variable

x = 43 + 60 + 16 + 41


# <p>To see the value of <code>x</code> in a Notebook, we can simply place it on the last line of a cell:</p>
# 

# In[48]:


# Print out the value in variable

x


# <p>We can also perform operations on <code>x</code> and save the result to a new variable:</p>
# 

# In[49]:


# Use another variable to store the result of the operation between variable and value

y = x / 60
y


# <p>If we save a value to an existing variable, the new value will overwrite the previous value:</p>
# 

# In[50]:


# Overwrite variable with new value

x = x / 60
x


# <p>It's a good practice to use meaningful variable names, so you and others can read the code and understand it more easily:</p>
# 

# In[51]:


# Name the variables meaningfully

total_min = 43 + 42 + 57 # Total length of albums in minutes
total_min


# In[52]:


# Name the variables meaningfully

total_hours = total_min / 60 # Total length of albums in hours 
total_hours


# <p>In the cells above we added the length of three albums in minutes and stored it in <code>total_min</code>. We then divided it by 60 to calculate total length <code>total_hours</code> in hours. You can also do it all at once in a single expression, as long as you use parenthesis to add the albums length before you divide, as shown below.</p>
# 

# In[53]:


# Complicate expression

total_hours = (43 + 42 + 57) / 60  # Total hours in a single expression
total_hours


# <p>If you'd rather have total hours as an integer, you can of course replace the floating point division with integer division (i.e., <code>//</code>).</p>
# 

# <h3 id="exer_exp_var">Exercise: Expression and Variables in Python</h3>
# 

# <p>What is the value of <code>x</code> where <code>x = 3 + 2 * 2</code></p>
# 

# In[54]:


# Write your code below. Don't forget to press Shift+Enter to execute the cell
x = 3 + 2 * 2
x


# <details><summary>Click here for the solution</summary>
# 
# ```python
# 7
# 
# ```
# 
# </details>
# 

# <p>What is the value of <code>y</code> where <code>y = (3 + 2) * 2</code>?</p>
# 

# In[55]:


# Write your code below. Don't forget to press Shift+Enter to execute the cell
y = (3 + 2) * 2
y


# <details><summary>Click here for the solution</summary>
# 
# ```python
# 10
# 
# ```
# 
# </details>
# 

# <p>What is the value of <code>z</code> where <code>z = x + y</code>?</p>
# 

# In[57]:


# Write your code below. Don't forget to press Shift+Enter to execute the cell
z = x + y 
z 


# <details><summary>Click here for the solution</summary>
# 
# ```python
# 17
# 
# ```
# 
# </details>
# 

# <hr>
# <h2>The last exercise!</h2>
# <p>Congratulations, you have completed your first lesson and hands-on lab in Python. However, there is one more thing you need to do. The Data Science community encourages sharing work. The best way to share and showcase your work is to share it on GitHub. By sharing your notebook on GitHub you are not only building your reputation with fellow data scientists, but you can also show it off when applying for a job. Even though this was your first piece of work, it is never too early to start building good habits. So, please read and follow <a href="https://cognitiveclass.ai/blog/data-scientists-stand-out-by-sharing-your-notebooks/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2021-01-01" target="_blank">this article</a> to learn how to share your work.
# <hr>
# 

# ## Author
# 
# <a href="https://www.linkedin.com/in/joseph-s-50398b136/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2021-01-01" target="_blank">Joseph Santarcangelo</a>
# 
# ## Other contributors
# 
# <a href="https://www.linkedin.com/in/jiahui-mavis-zhou-a4537814a?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2021-01-01">Mavis Zhou</a>
# 
# ## Change Log
# 
# | Date (YYYY-MM-DD) | Version | Changed By | Change Description                 |
# | ----------------- | ------- | ---------- | ---------------------------------- |
# | 2020-08-26        | 2.0     | Lavanya    | Moved lab to course repo in GitLab |
# |                   |         |            |                                    |
# |                   |         |            |                                    |
# 
# ## <h3 align="center"> © IBM Corporation 2020. All rights reserved. <h3/>
# 
