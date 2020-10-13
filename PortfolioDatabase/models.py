from django.db import models#import

# Create your models here.
class Hobby(models.Model):#class hobby
    def __str__(self):#string method
        x = (self.Hobby_name)  # passing in the name
        y = (self.Hobby_desc)  # passing in the description
        z = (x + y)  # putting the strings together
        return z#returned string
    Hobby_name = models.CharField(max_length=200)#declaring hobby name
    Hobby_desc = models.CharField(max_length=200)#declaring description name
    Hobby_image = models.CharField(max_length=500,default="https://fjwp.s3.amazonaws.com/blog/wp-content/uploads/2020/02/29113959/hobby-money-1024x512.png")



class  portfolio(models.Model):#class portfolio
    def __str__(self):#string method
        x = (self.portfolio_name)#passing in the name
        y = (self.portfolio_desc)#passing in the description
        z = (x + y)#putting the strings together
        return z#returning string
    portfolio_name = models.CharField(max_length=200)#declaring portfolio name
    portfolio_desc = models.CharField(max_length=200)#declaring portfolio  description
    portfolio_image = models.CharField(max_length=500,default="https://www.usnews.com/dims4/USNEWS/07be4c0/2147483647/thumbnail/640x420/quality/85/?url=http%3A%2F%2Fmedia.beam.usnews.com%2F46%2F19%2F5c6c54fb4c6f812dc85c20fc656a%2F141106-portfolio-stock.jpg")





class  contact(models.Model):#class portfolio
    def __str__(self):#string method
        w = (self.contact_name)#passing in the name
        x = (self.contact_email)#passing in the description
        y = (self.contact_message)  # paitssing in the description
        z = (w + x + y)#putting the strings together
        return z#returning string
    contact_name = models.CharField(max_length=200)#declaring portfolio name
    contact_email = models.CharField(max_length=200)#declaring portfolio  description
    contact_message = models.CharField(max_length=200)  # declaring portfolio  description








