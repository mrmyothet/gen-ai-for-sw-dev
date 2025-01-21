### Prompt generating code

> Can you write a python function to add two numbers named 'a' and 'b' and return the result?

> Create a JavaScript function that adds two numbers.

> Write a C# method to add two numbers.

> write a python function using numpy to add two arrays

### Interactive codding

> Write a Javascript function to check if a number is prime.

> Update the function to include error handling for non-integer and non-positive inputs.

> Can you help me create a simple Flask application in Python that includes one API endpoint? This endpoint should handle GET requests at the URL /multiply, which accepts two query parameters a and b and returns the multiplication of these two parameters as a JSON response. Make sure to include error handling if the parameters are not provided or if they are not convertible to integers.

> Help me find errors in this code:

```python
def calculate_average(numbers):

    total_sum = sum(numbers)
    count = len(numbers)
    average = total_sum / count
    return average
```

> Please, write a python function named calculate_area that takes an argument radius. The function should calculate the area of a circle given the radius. Ensure that the function handles non-numeric inputs by raising a ValueError with the message 'Input must be a numeric value.'. Include comments in the code explaining each step.

---

### Iterative Prompting

> write a python function using the requests library to download a file from a URL and save the file to disk without using third-party libraries like wget.

> Create a REST API in flask to return user data

> Now add error handling to the API to handle 404 and 500 status codes

> please, add detailed comments that explain this code. Highlight any complex parts that might require deeper explaination.

---

### Giving the LLM feedback

> Write a python function to calculate the factorial of a number

> Please, modify the function to include a check that ensures the input is a non-negative integer

> create a python function to check if a string is a palaindrome

> Update the code to ensure that the string isn't empty

> write a python function to find all the unique characters in a string

> Please, explain how to use Python's set function to calculate the unique characters in a string

### Assigning the LLM a role

> Write a python function to calculate a factorial.

> As my Python mentor, please write a function to calculate a factorial and explain how it works.

> As a friendly code guide, please explain how loops work in python

#### Assigning multiple roles

> As both a software architect and a security expert, evaluate this python script for a web application and suggest architectural improvements and security enhancements.

```python
def storeuserdata(user_data):
    database = open('user_database.txt', 'a')
    database.write(str(user_data))
    database.close()

storeuserdata({'username':'admin', 'password':'1234'})
```

#### Expert roles for specialized knowledge

> As a contributor to open-source python projects, critique this Python library for data visualization and suggest enhancements to make it comparable to major libraries like Matplotlib or Seaborn

```python
import matplotlib.pyplot as plt

class DataVisualizer:
    def init(self, data):
        self.data = data

    def plot(self, kind='line'):
        if kind == 'line':
            plt.plot(self.data)
        elif kind == 'bar':
            plt.bar(range(len(self.data)), self.data)
        plt.show()

# Example usage
visualizer = DataVisualizer([10, 20, 30, 40, 50])
visualizer.plot('bar')
```

---

> As an NLP expert, suggest improvements to this text summarization feature to enhance its functionality and accuracy.

```python
import nltk

class TextAnalyzer:
    def init(self, text):
        self.text = text

    def summarize(self):
        sentences = nltk.senttokenize(self.text)
        return ''.join(sentences[:2])

# Example usage
analyzer = TextAnalyzer('Here is alot of text to analyze and summarize. It has multiple sentences.')

print(analyzer.summarize())
```

---

> As a software tester, analyze this function for potential edge cases and suggest robust handling strategies.

```python
def calculate_discount(price, discount):
    if discount > 100:
        raise ValueError('Discount cannot exceed 100%')
    return price * (100 - discount) / 100

# Test cases
print(calcuate_discount(100, 105)) # Should raise an exception

```

### Best Practices

- **Be specific:** Provide detail and context about the problem
- **Assign a role:** Assign a role to tailor the output
- **Request an expert opinion:** Assign an expert role and ask the LLM to evaluate the work already done to further refind it
- **Give feedback:** Iteratively prompt the LLM and provide feedback on the output to get closer to expected results
