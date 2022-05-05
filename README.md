# MailCode

This is a programming language formatted like a letter or email. Each statement must start with a greeting and end with a closing such as:

Dear MailCode,  
(code block)  
Thanks,  
Drew  

The recipient and sender can be whatever you would like, but I find it amusing to address the letter to the language itself. These names can also be used as the name of the file, function, or anything to identify the code block, and the name of whoever created the code as a means of documentation. Each line of code within the code block is formatted like a regular English sentence with a period at the end. Whitespace is ignored so you can just type sentences like normal or you can put each sentence on its own line (which I find to be much cleaner).  

Loops are denoted by a colon with each line of code to be looped starting with a `~`:

Hello MailCode,  
Do this 10 times:  
~(line)  
~(line)  
...  
Sincerely,  
Drew

The language is currently able to:
* Create and store integer variables
* Print strings and the value of variables
* Loop a block of code a fixed number of times
* Perform basic math opperations on a variable and change its value

To run the code on a command line simply run mailCode.py with a .txt program as a paramater:  
`python mailCode.py code.txt`

3 sample programs have been provided.
