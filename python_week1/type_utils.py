def describe_type(value):
	if(isinstance(value,str)):
		return "String"
	if(isinstance(value,float)):
		return "Float"
	if(isinstance(value,bool)):
		return "Boolean"
	if(isinstance(value,int)):
		return "Integer"
	return "Unknown Type"

def to_number(value):
	if(isinstance(value,float)):
		return value
	if(isinstance(value,bool)):
		return int(value)
	if(isinstance(value,int)):
		return value
	if(isinstance(value,str)):
		try:
			return float(value)
		except:
			return None

def is_truthy(value):
	return bool(value)

def smart_add(a,b):
	if(isinstance(a,str) or isinstance(b,str)):
		return str(a) + str(b)
	return a+b

if __name__ == "__main__":
    print("=== Testing describe_type ===")
    print(describe_type(10))          # Integer
    print(describe_type(3.14))        # Float
    print(describe_type("Hello"))     # String
    print(describe_type(True))        # Boolean
    print(describe_type(None))        # Unknown type

    print("\n=== Testing to_number ===")
    print(to_number(10))              # 10
    print(to_number(5.5))             # 5.5
    print(to_number(True))            # 1
    print(to_number(False))           # 0
    print(to_number("12.75"))          # 12.75
    print(to_number("abc"))            # None

    print("\n=== Testing is_truthy ===")
    print(is_truthy(0))               # False
    print(is_truthy(1))               # True
    print(is_truthy(""))              # False
    print(is_truthy("0"))             # True
    print(is_truthy([]))              # False
    print(is_truthy("AI"))            # True

    print("\n=== Testing smart_add ===")
    print(smart_add(2, 3))             # 5
    print(smart_add(2.5, 3.5))         # 6.0
    print(smart_add("AI", "Lab"))      # AILab
    print(smart_add("Score: ", 10))    # Score: 10
    print(smart_add(True, 5))          # 6
	
