from django.shortcuts import render
def Profile(request):
    return render(request,'Profile.html')

def Education(request):
    return render(request,'Education.html')

def Attention(request):
    return render(request,'Attention.html')

def Career(request):
    return render(request, 'Career.html')

def Product(request):
    return render(request,'Product.html')

def RoleModel(request):
    return render(request,'RoleModel.html')

def ShowData(request):
    name = 'CHATWIMON WANGSABAY'
    id = '65342310180-5'
    age = 21
    birthday = 'January 6, 2002'
    weight = '50'
    height = '155'
    flavors = 'Spicy Taste'
    colors = 'Red, Black, Purple'
    weather = 'Cold'
    motto = 'Turn the pain into power.'
    products = [
        ['W269251004TH','/static/images/showdata01.jpeg','Alienware Aurora R13','177,990'],
        ['W569211003TH', '/static/images/showdata02.png', 'Alienware x15', '143,490'],
        ['W269251003TH', '/static/images/showdata03.jpeg', 'Alienware Aurora R13', '137,990'],
        ['W569212800ATHW10', '/static/images/showdata04.png', 'Alienware m15 Ryzen™ Edition R5', '94,490'],
        ['W569212300THW10', '/static/images/showdata05.png', 'Alienware m15 R6', '93,790'],
        ['AW3420DW', '/static/images/showdata06.jpg', 'Alienware 34 Curved Gaming Monitor', '46,790'],
        ['AW2521HF', '/static/images/showdata07.jpg', 'Alienware 25 Gaming Monitor', '15,990'],
        ['580-AIZV', '/static/images/showdata08.png', 'Alienware RGB Mechanical Gaming Keyboard US English – AW410K', '5,190'],
        ['520-AAQF', '/static/images/showdata09.png', 'Alienware 510H 7.1 Gaming Headset AW510H', '3,300'],
        ['570-ABCS', '/static/images/showdata10.png', 'Alienware 610M Wired/Wireless Gaming Mouse AW610M', '2,910']
    ]
    context = {'name':name, 'id':id, 'age':age, 'birthday':birthday, 'weight':weight,
               'height':height, 'flavors':flavors, 'colors':colors, 'weather':weather, 'motto':motto,
               'products':products}
    return render(request,'showData.html',context)