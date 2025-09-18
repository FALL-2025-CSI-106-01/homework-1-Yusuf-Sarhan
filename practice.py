for i in range(3,11):
    print(i)

def print_abcs():
    for letter in ["a","b","c"]:
        print(letter)

print_abcs()

var1 = "hello"

def my_function(var1):
  var1 = 'goodbye'
  return var1

my_function(var1)
print(var1)


var1 = "hello"

def my_function(var):
  global var1
  var1 = 'goodbye' 

var1 = my_function(var1)
print(var1)