word = input("Enter a string: ")
print("Printing only even index chars")

# if the input is pynative, even_num = ['p','y','n','a','t','i','v','e']
even_num = list(word)

for i in even_num[0::2]:  # even_num[starts from 0th index: stops at last index: takes 2 step]
    print(i)
