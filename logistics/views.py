from django.shortcuts import render,redirect
from .models import *
from .forms import PersonalInfoForm, AddressForm, QuoteForm

from django.contrib import messages
# Create your views here.

def index1(request):
    try:
        if request.method == "POST":
            firstName = request.POST.get("firstName")
            lastName = request.POST.get("lastName") 
            business = request.POST.get("business")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            address1 = request.POST.get("address1")
            address2 = request.POST.get("address2")
            city = request.POST.get("city")
            state = request.POST.get("state")
            postalCode = request.POST.get('postalCode')
            date = request.POST.get('date')
            time = request.POST.get('time')
            if firstName and lastName and business and email and phone and address1 and address2 and city and state and postalCode and date and time:
                getQuote = GetQuote.objects.create(firstName=firstName,lastName=lastName,business=business,email=email,phone=phone,address1=address1,address2=address2,city=city,state=state,postalCode=postalCode,date=date,time=time)
                messages.success(request,'you\'ve successfully requested a quote')
            else:
                messages.success(request,'an error occured requesting a quote')
            return redirect('home')
    except Exception as e:
        print(e)
        messages.error(request,'subscription not successfull' )
    return render(request,'index.html')


def index(request):
    
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            # Process the data
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            business = form.cleaned_data['business']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address1 = form.cleaned_data['address1']
            address2 = form.cleaned_data['address2']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            postalCode = form.cleaned_data['postalCode']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']

            if firstName and lastName and business and email and phone and address1 and address2 and city and state and postalCode and date and time:
                getQuote = GetQuote.objects.create(firstName=firstName,lastName=lastName,business=business,email=email,phone=phone,address1=address1,address2=address2,city=city,state=state,postalCode=postalCode,date=date,time=time)
                messages.success(request,'you\'ve successfully requested a quote')
                print('success=========================')

            else:
                messages.success(request,'an error occured requesting a quote')
                form.add_error(None,'Invalid reCAPTCHA')
                print('errorr===================')
            # Save the data to the database or process it as needed
            
            return redirect('home')  # Redirect to a success page or render a success message
    else:

        form = QuoteForm()
            
    
    return render(request, 'index.html', {'form': form})



def subscription(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subscribe = Subscribe(email=email)
        print(f'email ============ {email}')
        if email:
            messages.success(request,'you\'ve successfully subscribed to our news letter')
            subscribe.save()
        else:
            messages.error(request,'subscription not successfull' )
        return redirect(request.path)
    return render(request,'index.html')


def contactUs(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact_us = ContactUs(name=name,email=email,subject=subject,message=message)
        #print(f'email ============ {email}')
        if not all([name,email,subject,message]):
            messages.error(request,'form submission not successful' )
        else:
            messages.success(request,'your message has been sent successfully!!!')
            contact_us.save()
        return redirect(request.path)
    return render(request,'contact.html')


def index1(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        business = request.POST.get('business')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        postal_code = request.POST.get('postalCode')
        date = request.POST.get('date')
        time = request.POST.get('time')
        
        # Validate personal information
        if not all([first_name, last_name, business, email, phone]):
            print(first_name, last_name, business, email, phone)
            print("error in personal")
            return render(request, 'index.html', {
                'error': 'Please fill in all required fields in the personal information section.',
                'form_section': 'personal_info',
            })

        # Validate address information
        if not all([address1, address2, city, state, postal_code, date, time]):
            print(address1, address2, city, state, postal_code, date, time)
            print("error in address")
            return render(request, 'index.html', {
                'error': 'Please fill in all required fields in the address section.',
                'form_section': 'address',
            })
        print(address1, address2, city, state, postal_code, date, time)

        try:
            print(first_name, last_name, business, email, phone,address1, address2, city, state, postal_code, date, time)
            GetQuote.objects.create(
                firstName=first_name,
                lastname=last_name,
                business=business,
                email=email,
                phone=phone,
                address1=address1,
                address2=address2,
                city=city,
                state=state,
                postalCode=postal_code,
                date=date,
                time=time,
            )
            return render(request, 'index.html', {
                'success': 'Thank you! We will get back to you soon.'
            })
        except Exception as e:
            return render(request, 'index.html', {
                'error': f'An error occurred: {str(e)}',
            })

    return redirect('home')



def about(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            # Process the data
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            business = form.cleaned_data['business']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address1 = form.cleaned_data['address1']
            address2 = form.cleaned_data['address2']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            postalCode = form.cleaned_data['postalCode']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']

            if firstName and lastName and business and email and phone and address1 and address2 and city and state and postalCode and date and time:
                getQuote = GetQuote.objects.create(firstName=firstName,lastName=lastName,business=business,email=email,phone=phone,address1=address1,address2=address2,city=city,state=state,postalCode=postalCode,date=date,time=time)
                messages.success(request,'you\'ve successfully requested a quote')
                print('success=========================')

            else:
                messages.success(request,'an error occured requesting a quote')
                form.add_error(None,'Invalid reCAPTCHA')
                print('errorr===================')
            # Save the data to the database or process it as needed
            
            return redirect('about')  # Redirect to a success page or render a success message
    else:

        form = QuoteForm()
            
    
    return render(request, 'about.html', {'form': form})

def contact(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            # Process the data
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            business = form.cleaned_data['business']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address1 = form.cleaned_data['address1']
            address2 = form.cleaned_data['address2']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            postalCode = form.cleaned_data['postalCode']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']

            if firstName and lastName and business and email and phone and address1 and address2 and city and state and postalCode and date and time:
                getQuote = GetQuote.objects.create(firstName=firstName,lastName=lastName,business=business,email=email,phone=phone,address1=address1,address2=address2,city=city,state=state,postalCode=postalCode,date=date,time=time)
                messages.success(request,'you\'ve successfully requested a quote')
                print('success=========================')

            else:
                messages.success(request,'an error occured requesting a quote')
                form.add_error(None,'Invalid reCAPTCHA')
                print('errorr===================')
            # Save the data to the database or process it as needed
            
            return redirect('contact')  # Redirect to a success page or render a success message
    else:

        form = QuoteForm()
            
    
    return render(request, 'contact.html', {'form': form})

def security(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            # Process the data
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            business = form.cleaned_data['business']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address1 = form.cleaned_data['address1']
            address2 = form.cleaned_data['address2']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            postalCode = form.cleaned_data['postalCode']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']

            if firstName and lastName and business and email and phone and address1 and address2 and city and state and postalCode and date and time:
                getQuote = GetQuote.objects.create(firstName=firstName,lastName=lastName,business=business,email=email,phone=phone,address1=address1,address2=address2,city=city,state=state,postalCode=postalCode,date=date,time=time)
                messages.success(request,'you\'ve successfully requested a quote')
                print('success=========================')

            else:
                messages.success(request,'an error occured requesting a quote')
                form.add_error(None,'Invalid reCAPTCHA')
                print('errorr===================')
            # Save the data to the database or process it as needed
            
            return redirect('security')  # Redirect to a success page or render a success message
    else:

        form = QuoteForm()
            
    
    return render(request, 'security.html', {'form': form})

def service(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            # Process the data
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            business = form.cleaned_data['business']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address1 = form.cleaned_data['address1']
            address2 = form.cleaned_data['address2']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            postalCode = form.cleaned_data['postalCode']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']

            if firstName and lastName and business and email and phone and address1 and address2 and city and state and postalCode and date and time:
                getQuote = GetQuote.objects.create(firstName=firstName,lastName=lastName,business=business,email=email,phone=phone,address1=address1,address2=address2,city=city,state=state,postalCode=postalCode,date=date,time=time)
                messages.success(request,'you\'ve successfully requested a quote')
                print('success=========================')

            else:
                messages.success(request,'an error occured requesting a quote')
                form.add_error(None,'Invalid reCAPTCHA')
                print('errorr===================')
            # Save the data to the database or process it as needed
            
            return redirect('service')  # Redirect to a success page or render a success message
    else:

        form = QuoteForm()
            
    
    return render(request, 'service.html', {'form': form})

def transport(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            # Process the data
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            business = form.cleaned_data['business']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address1 = form.cleaned_data['address1']
            address2 = form.cleaned_data['address2']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            postalCode = form.cleaned_data['postalCode']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']

            if firstName and lastName and business and email and phone and address1 and address2 and city and state and postalCode and date and time:
                getQuote = GetQuote.objects.create(firstName=firstName,lastName=lastName,business=business,email=email,phone=phone,address1=address1,address2=address2,city=city,state=state,postalCode=postalCode,date=date,time=time)
                messages.success(request,'you\'ve successfully requested a quote')
                print('success=========================')

            else:
                messages.success(request,'an error occured requesting a quote')
                form.add_error(None,'Invalid reCAPTCHA')
                print('errorr===================')
            # Save the data to the database or process it as needed
            
            return redirect('transport')  # Redirect to a success page or render a success message
    else:

        form = QuoteForm()
            
    
    return render(request, 'transport.html', {'form': form})

def waste(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            # Process the data
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            business = form.cleaned_data['business']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address1 = form.cleaned_data['address1']
            address2 = form.cleaned_data['address2']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            postalCode = form.cleaned_data['postalCode']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']

            if firstName and lastName and business and email and phone and address1 and address2 and city and state and postalCode and date and time:
                getQuote = GetQuote.objects.create(firstName=firstName,lastName=lastName,business=business,email=email,phone=phone,address1=address1,address2=address2,city=city,state=state,postalCode=postalCode,date=date,time=time)
                messages.success(request,'you\'ve successfully requested a quote')
                print('success=========================')

            else:
                messages.success(request,'an error occured requesting a quote')
                form.add_error(None,'Invalid reCAPTCHA')
                print('errorr===================')
            # Save the data to the database or process it as needed
            
            return redirect('waste')  # Redirect to a success page or render a success message
    else:

        form = QuoteForm()
            
    
    return render(request, 'waste.html', {'form': form})