# Python & AWS Candidate Test

## Basic knowledge questions

- What is \_\_main\_\_.py used for?

```
Solution: 
The __main__.py file is used to indicate that a directory is an executable Python package. When you run a Python package using the command python -m <package_name>, the __main__.py file within the package is executed.

```

- How to prevent python module code from executing when the module is imported?

```
Solution:
 To prevent the code in a Python module from executing when it's imported, you can utilize the global variable __name__. When a module is imported, Python sets the __name__ variable to the module's name. However, when the module is executed directly, Python sets __name__ to "main". 

```

- What's the name of method that represents a class constructor in Python?

```
Solution: 
The method that represents a class constructor in Python is called __init__. The __init__ method is automatically executed whenever an object of a class is created. It's used to initialize the object's attributes.

```

- What options do you have when you need to insert value of a variable into string? Name at least three.

```
Solution: 
Name at least three.
When you need to insert the value of a variable into a string, you have several options in Python:

String concatenation: You can use the + operator to concatenate a string variable with another string.
String formatting: You can use the format() method or f-strings (format strings) to insert the value of a variable into a string.
F-strings (format strings): Starting from Python 3.6, you can use f-strings to insert variable values directly into a string prefixed with f. For example: f"The value of the variable is {variable}".

```

- How can you truly restrict access to a private method of a class in Python?

```
Solution: 
In Python, there isn't a direct way to restrict access to private methods of a class as in some other languages. However, there's a convention in Python to indicate that a method or attribute is private. The convention is to use a single underscore _ as a prefix to the method or attribute name to indicate it's private. This serves as an indication to programmers that the method or attribute should not be accessed directly. However, it's still possible to access and call these methods and attributes directly in Python.

```

- What Python feature would you use to add some functionalities to an existing function without interfering into its code?

```
Solution: 
In Python, you can use decorators to add functionalities to an existing function without directly modifying its code. Decorators are functions that wrap around other functions and allow executing additional code before and/or after the decorated function. This enables extending or modifying the behavior of the function without altering

```

- How is @staticmethod different from @classmethod?

```
Solution: 
The difference between @staticmethod and @classmethod is that @classmethod receives a reference to the class as its first argument, while @staticmethod does not receive a reference to the class. This means that @classmethod can be used to access and modify class variables, while @staticmethod cannot.

```

- What is the advantage of using **with** keyword when reading/writing a file in Python?

```
Solution: 
The advantage of using the with keyword when reading/writing a file in Python is that it ensures the file is automatically closed when the operation is completed, even if an exception occurs during the file processing. This guarantees that the file is properly closed and prevents resource leaks.

```

## Problem solving

**problem-solving.py** script takes advantage of Person class in order to create every person defined in the "people" array and then, for each of them, run introducing method. It also prints total number of created people. Threading is used to create each person in a different thread. Unfortunately, script has some bugs preventing it from working properly. 
- Please debug, fix and explain what issues the script had.  
- Currently, number of created people is printed at the beginning. Please implement some improvements, so that number of people created is printed always at the very end (without using time.sleep).
- You are not allowed to interfere into **introduce** method code.

```
Solution:

problem-solving.py

I added a lock object called "lock" as a class attribute to ensure that access to the people_count variable is synchronized between threads.

I updated the increase_count method to use the lock object and ensure that the count increment is done safely and correctly.

After starting all the threads, I added a for loop to call the join method on each thread. This makes the main program wait for the completion of all threads before proceeding.

Finally, I printed the number of people created after the thread join loop, ensuring that the count is always printed at the end.


```



## Create something whilst learning something new

For this task you will need your personal account in AWS. Please create one if you don't have it yet (do not worry about costs, everything you do here will covered by AWS Free Tier).

- Create a REST API in AWS API Gateway.
- Create 2 HTTP methods in the API: GET & POST.
- Create a DynamoDB Table (keep provisioned WCU & RCU low to stay within Free Tier, 2 will be OK) and name it "users". It should consist only of a parition key (hash key) which is "user_id".
- Create a lambda function and integrate it with the API POST method. In the JSON body of HTTP POST request, user should be able to specify his first name and age. Lambda should take provided body and insert it into your DynamoDB table as a new item. Value for user_id column should be generated as a random GUID and returned to the caller in the response.
- Create second lambda function and integrate it with the API GET method. GET method should take a user_id as path parameter. Lambda should lookup the DynamoDB table (using **query** method!) and either return user or 404 status code if it doesn't exist.

Please create a new GitLab/GitHub repository, upload your lambda code in there and share link to the repo with us.
Repository should also contain a README.md with URLs to your API GET & POST methods and explanation about how to use them (exact paths, example body for POST method).

```
Solution:

I have created a CloudFormation template named Cloudformation.json to deploy the infrastructure, including Lambda functions, DynamoDB, and necessary permissions.

I have organized the code into two separate folders. One folder contains the Lambda function code and a corresponding JSON test file, while the other folder also contains the Lambda function code and a corresponding JSON test file. This structure allows me to keep the code and tests separate and organized more efficiently.

Additionally, I have prepared an API.json file that can be used to deploy the API Gateway using Swagger.

These steps were taken to ensure the proper setup and organization of the project's infrastructure and codebase.

```

## Programming

You will find description of this task in [./programming_task/README.md](./programming_task/README.md) file.

```
Solution:

hanoi_game.py

```



