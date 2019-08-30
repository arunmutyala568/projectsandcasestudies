def palindrome(myname):
    
    if myname.lower()==myname[::-1].lower():
        
        print("palindrome")
        
    else:
        
        print("not palindrome")
        
        
palindrome("arun")