#It will tell the name of country and the service 
#of specific number
def phonecountry():
    import phonenumbers
    number=input("enter your number with country code:")
    from phonenumbers import geocoder #geocoder is a built in function in phonenumbers
#used to tell country of number
    ch_number=phonenumbers.parse(number) #c for country,H for history
#variable ch_number is created to show country name
    print(geocoder.description_for_number(ch_number,"en")) # here 
#first parameter will be our variable and second the language
#the following part is used to find service provider
    from phonenumbers import carrier
    service=phonenumbers.parse(number)
    print(carrier.name_for_number(service,"any language"))
    choice=input("do you want to check more phone numbers(yes/no)")
    if choice=="yes":
      phonecountry()
    else:
       print("Thanks alot")
phonecountry()
    