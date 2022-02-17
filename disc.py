def main():
    
	#this part gets an input from the user
    word = input("Enter the word,prase or number you want to multiply.")
	
	#this part takes "word" the users input. multiplies it by 2000 and names it wordX
    wordX = word * 2000
    
	#this part stops the output from exceeding 2000    
    print(wordX[:2000])
    
main()