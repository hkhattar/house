from .models import PublicHousingAuthorities as ph
from django.shortcuts import render,redirect,reverse
from .models import User , UserManager
from django.contrib import messages
# Create your views her e.
import bcrypt
statedict={
' LABAMA': 'AL',
'ALASKA': 'AK',
'ARIZONA': 'AZ',
'ARKANSAS': 'AR',
'CALIFORNIA': 'CA',
'COLORADO': 'CO',
'CONNECTICUT': 'CT',
'DELAWARE': 'DE',
'FLORIDA': 'FL',
'GEORGIA': 'GA',
'HAWAII': 'HI',
'IDAHO': 'ID',
'ILLINOIS': 'IL',
'INDIANA':'IN',
'IOWA': 'IA',
'KANSAS': 'KS',
'KENTUCKY': 'KY',
'LOUISIANA': 'LA',
'MAINE': 'ME',
'MARYLAND': 'MD',
'MASSACHUSETTS': 'MA',
'MICHIGAN': 'MI',
'MINNESOTA': 'MN',
'MISSISSIPPI': 'MS',
'MISSOURI': 'MO',
'MONTANA': 'MT',
'NEBRASKA': 'NE',
'NEVADA': 'NV',
'NEW HAMPSHIRE': 'NH',
'NEW JERSEY': 'NJ',
'NEW MEXICO': 'NM',
'NEW YORK': 'NY',
'NORTH CAROLINA': 'NC',
'NORTH DAKOTA': 'ND',
'OHIO': 'OH',
'OKLAHOMA': 'OK',
'OREGON': 'OR',
'PENNSYLVANIA': 'PA',
'RHODE ISLAND': 'RI',
'SOUTH CAROLINA': 'SC',
'SOUTH CAROLINA':'SC',
'SOUTH DAKOTA': 'SD',
'TENNESSEE': 'TN',
'TEXAS': 'TX',
'UTAH': 'UT',
'VERMONT': 'VT',
'VIRGINIA': 'VA',
'WASHINGTON': 'WA',
'WEST VIRGINIA': 'WV',
'WISCONSIN': 'WI',
'WYOMING': 'WY',
        }

def index(request):
    query="select id, X from Public_Housing_Authorities where STD_ST = 'WI';"
    allnames=[f.name for f in ph._meta.get_fields()]
    data=ph.objects.raw(query)
    print(data[0].x)
    return render(request,"house/index.html")

def login_reg(request):
    return render(request,"house/login.html")

def registration(request):
    if request.method=="POST":
        first=request.POST['first']
        last=request.POST['last']
        username=request.POST['username']
        email=request.POST['email']
        pin=request.POST['pin']
        confirm=request.POST['confirm']
        errors=User.objects.register_valid(first,last,email,pin,confirm,username)
        if len(errors)>0:
            print(errors)
            for error in errors:
                messages.error(request,error)
            return redirect(reverse('house:login_reg'))
        else:
            hashed=bcrypt.hashpw(pin.encode(),bcrypt.gensalt())
            user=User.objects.create(first_name=first,last_name=last,username=username,email=email,password=hashed)
        return redirect(reverse('house:display'))
 
def login(request):
    if request.method=="POST":
        login_username=request.POST['username_login']
        login_pin=request.POST['pin_login']
        if User.objects.isExist(login_username):
            if User.objects.login_valid(login_username,login_pin):

                return redirect(reverse('house:display'))
            else:
                messages.error(request,"login unsuccessful")
        else:
            messages.error(request,"user not exist")
        return redirect(reverse('house:login_reg'))

def display(request):
    if request.method=="POST":
        state=request.POST['search']
        query='select X, Y, FORMAL_PARTICIPANT_NAME, STD_ADDR, STD_CITY, STD_ZIP5 from Public_Housing_Authorities where STD_ST = {};'.format(state)
	data=ph.objects.raw(query)
	context={'data':data}
    else:
        context={}
    return render(request,'house/success.html',context)

