#Taking input 

Input_lst = input('Enter words with spaces: ').split(' ')


#Defining a count program
count = {}
def count_words(a_list) :
    for word in a_list :
        if word in count:
            count[word] += 1
        
        else:
            count[word] = 1

    return count

# Calling the Function
x = count_words(Input_lst)

print('Occurence of the words are as follows: ')
for word in x:
    print(f'{word} : {x[word]}')
