import random

class EmailGen ():

    def __init__(self):
        self.countries = ('afghanistan', 'argentina', 'australia', 'bangladesh', 'belgium', 'brazil', 'canada', 'china', 'denmark', 'egypt', 'france', 'gambia', 'germany', 'ghana', 'guinea', 'india', 'israel', 'kenya', 'malaysia', 'namibia', 'netherland', 'nigeria', 'southafrica', 'spain', 'tanzania', 'uganda', 'uk', 'usa', 'zambia', 'zimbabwe')
        self.domains = ('gmail.com', 'yahoo.com', 'hotmail.com', 'aol.com')
        self.formats = ('fs', 'fsn', 'f_s', 'f_s_n', 'f.s', 'f.s.n')
        self.numFormats = (1,2,3)

        """
        print,("\n--------------------------------------------------------------------")

        print('EMAILGEN CAN ONLY GENERATE FROM THESE COUNTRIES')
        print(countries)
        print('')

        print("--------------------------------------------------------------------\n")

        """

        self.country_input = ""
        self.domain_input = ""
        self.number_of_emails = 0
        self.typeOfEmail = ""
        self.file_name = "tempemaillist"
        self.start = True
        self.emailList = ''

        """

        print("--------------------------------------------------------------")

        print('%d email IDs to generate' % (number_of_emails))

        """
    def validateInputs(self):
        if self.country_input is not "" and self.domain_input is not "" and self.typeOfEmail is not "" and self.number_of_emails is not "":
            #print('Emails to be generated from all countries available')
            self.start = True

        if self.typeOfEmail is not "y" and self.typeOfEmail is not "n":
            self.typeOfEmail =="n"

        if self.number_of_emails > 10000:
            self.number_of_emails = 10000

        """
        if self.file_name is not "":
            self.start = True
        """
        return self.start
        


        #print('Emails to be saved to "%s.txt"' % (file_name))

    def generateEmail(self, typeOfEmail):
        i = 0
        #print("TypeOfEmail = ", typeOfEmail)
        #print("EmailType = ", emailType)
        while i<self.number_of_emails and self.start is True:
            #print(i)

            if self.country_input == "all":
                country = random.choice(self.countries)
            elif self.country_input in self.countries:
                country = self.country_input
            
            if self.domain_input == "all":
                domain = random.choice(self.domains)
            elif self.domain_input in self.domains:
                domain = self.domain_input
            elif (self.domain_input is not "all") and (self.domain_input not in self.domains):
                domain = self.domain_input

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

            email = ''
            if self.typeOfEmail is "y":
                selected_format = random.choice(self.formats)
                if selected_format is "fs":
                    email = firstname+lastname+'@'+domain+',\n'
                    #print(email)
                elif selected_format is "fsn":
                    numLen = random.choice(self.numFormats)
                    num = ""
                    for y in range(1, numLen+1):
                        num = num+str(random.randrange(1, 9))
                    email = firstname+lastname+num+'@'+domain+',\n'
                    #print(email)
                elif selected_format is "f_s":
                    email = firstname+'_'+lastname+'@'+domain+',\n'
                    #print(email)
                elif selected_format is "f_s_n":
                    numLen = random.choice(self.numFormats)
                    num = ""
                    for y in range(1, numLen):
                        num = num+str(random.randrange(1, 9))
                    email = firstname+'_'+lastname+'_'+num+'@'+domain+',\n'
                    #print(email)
                elif selected_format is "f.s":
                    email = firstname+'.'+lastname+'@'+domain+',\n'
                elif selected_format is "f.s.n":
                    numLen = random.choice(self.numFormats)
                    num = ""
                    for y in range(1, numLen):
                        num = num+str(random.randrange(1, 9))
                    email = firstname+'.'+lastname+'.'+num+'@'+domain+',\n'
                    #print(email)
            elif self.typeOfEmail is "n":
                email = firstname+lastname+'@'+domain+',\n'
                #print(email)

            self.emailList = self.emailList + email

            #foo = open(self.file_name+'.txt', 'a+')
            #foo.write(email)
            #foo.close()
            #print('%d => %s' % (i, email))
            i += 1
            
        return self.emailList

    #print('%d email IDs generated' % (number_of_emails))

    #print("------------------------------------------------------------")