import random

countries = ('afghanistan', 'argentina', 'australia', 'bangladesh', 'belgium', 'brazil', 'canada', 'china', 'denmark', 'egypt', 'france', 'gambia', 'germany', 'ghana', 'guinea', 'india', 'israel', 'kenya', 'malaysia', 'namibia', 'netherland', 'nigeria', 'southafrica', 'spain', 'tanzania', 'uganda', 'uk', 'usa', 'zambia', 'zimbabwe')
domains = ('gmail.com', 'yahoo.com', 'hotmail.com', 'aol.com')
formats = ('fs', 'fsn', 'f_s', 'f_s_n', 'f.s', 'f.s.n')
numFormats = (1,2,3)
print,("\n--------------------------------------------------------------------")

print('EMAILGEN CAN ONLY GENERATE FROM THESE COUNTRIES')
print(countries)
print('')

print("--------------------------------------------------------------------\n")

country_input = input('Which country should the email IDs be generated from (type "all" if you want email IDs from all available countries): ').lower()
domain_input = input('Email domain (E.g "gmail.com")\nYou can input your own custom domain (E.g "example.com")\n or type "all" to generate from the most popular domain: ').lower()
number_of_emails = int(input("How many emails to generate: "))
typeOfEmail = input('Should the emails include special characters\n(It is recommended that you do not inlcude special characters because it reduces the chance that the email exists)\nType "y" is yes or "n" if no: ').lower()
file_name = input('filename to save emails to: ').lower()
start = False

print("--------------------------------------------------------------")

print('%d email IDs to generate' % (number_of_emails))

if country_input == "all":
    print('Emails to be generated from all countries available')
    start = True
else:
    print('Emails to be generated from %s' % (country_input))
    start = True

if domain_input == "all":
    print('Email domains to generate = ', domains)
    start = True
else:
    print('Email domains to generate = ', domain_input)
    start = True

if typeOfEmail == "y":
    print("Emails will include special characters")
    start = True
elif typeOfEmail == "n":
    print("Emails will inlcude only names and surnames")
    start = True
elif typeOfEmail is not "y" and typeOfEmail is not "n":
    typeOfEmail = "n"
    start = True

if number_of_emails > 10000:
    number_of_emails = 10000

if file_name is not "":
    start = True


print('Emails to be saved to "%s.txt"' % (file_name))

def generateEmail(emailType = typeOfEmail):
    i = 0
    #print("TypeOfEmail = ", typeOfEmail)
    #print("EmailType = ", emailType)
    while i<number_of_emails and start is True:
        #print(i)

        if country_input == "all":
            country = random.choice(countries)
        elif country_input in countries:
            country = country_input
        
        if domain_input == "all":
            domain = random.choice(domains)
        elif domain_input in domains:
            domain = domain_input
        elif (domain_input is not "all") and (domain_input not in domains):
            domain = domain_input

        fn_file, ln_file = 'db/'+country+'-firstnames.txt', 'db/'+country+'-surnames.txt'
        fn_file_handler, ln_file_handler = open(fn_file, 'r'), open(ln_file, 'r')
        firstnames = fn_file_handler.readlines()
        surnames = ln_file_handler.readlines()
        fn_file_handler.close()
        ln_file_handler.close()
        rand_fn, rand_ln = list(random.choice(firstnames)), list(random.choice(surnames))

        while '\n' in rand_fn:
            rand_fn.remove('\n')
        while '\r' in rand_fn:
            rand_fn.remove('\r')
        while '\r\n' in rand_fn:
            rand_fn.remove('\r\n')

        while '\n' in rand_ln:
            rand_ln.remove('\n')
        while '\r' in rand_ln:
            rand_ln.remove('\r')
        while '\r\n' in rand_ln:
            rand_ln.remove('\r\n')

        firstname = ""
        lastname = ""

        for y in range(len(rand_fn)):
            firstname = firstname+rand_fn[y]
        for y in range(len(rand_ln)):
            lastname =lastname+rand_ln[y]

        firstname.encode('utf-8', errors='ignore').decode('utf-8')
        lastname.encode('utf-8', errors='ignore').decode('utf-8')

        email = ""
        if emailType == "y":
            selected_format = random.choice(formats)
            if selected_format is "fs":
                email = firstname+lastname+'@'+domain+',\n'
                print(email)
            elif selected_format is "fsn":
                numLen = random.choice(numFormats)
                num = ""
                for y in range(1, numLen+1):
                    num = num+str(random.randrange(1, 9))
                email = firstname+lastname+num+'@'+domain+',\n'
                print(email)
            elif selected_format is "f_s":
                email = firstname+'_'+lastname+'@'+domain+',\n'
                print(email)
            elif selected_format is "f_s_n":
                numLen = random.choice(numFormats)
                num = ""
                for y in range(1, numLen):
                    num = num+str(random.randrange(1, 9))
                email = firstname+'_'+lastname+'_'+num+'@'+domain+',\n'
                print(email)
            elif selected_format is "f.s":
                email = firstname+'.'+lastname+'@'+domain+',\n'
            elif selected_format is "f.s.n":
                numLen = random.choice(numFormats)
                num = ""
                for y in range(1, numLen):
                    num = num+str(random.randrange(1, 9))
                email = firstname+'.'+lastname+'.'+num+'@'+domain+',\n'
                print(email)
        elif emailType == "n":
            email = firstname+lastname+'@'+domain+',\n'
            print(email)
        print(email)
        foo = open(file_name+'.txt', 'a+')
        foo.write(email)
        foo.close()
        #print('%d => %s' % (i, email))
        i += 1

generateEmail()

print('%d email IDs generated' % (number_of_emails))

print("------------------------------------------------------------")