from django.shortcuts import render
from django.contrib import messages
from properties.controllers.contact_requests import ContactRequests
from properties.forms.form_contact import ContactForm
from properties.controllers.properties import Properties

def index(request, page = 1):

    response = Properties().getProperties(page)
    properties = response.json()
    
    pagination = properties['pagination']
    content = properties['content']

    next_page = pagination['next_page']
    public_id = []
    title = []
    property_type = []
    location = []
    title_image_thumb = []

    for i in content:
        public_id.append(i['public_id'])
        title.append(i['title'])
        property_type.append(i['property_type'])
        location.append(i['location'])
        title_image_thumb.append(i['title_image_full'])

    properties = zip(public_id, title, property_type, location, title_image_thumb)

    context = {
        'properties': properties,
        'next_page': next_page,
        'page': page + 1
    }

    return render(request, 'index.html', context)
    

def property(request, id):
    form = processContactRequest(request, id)

    response = Properties().getProperty(id)

    property = response.json()

    if len(property['property_images']) > 0:
        property_image = property['property_images'][0]['url']
    else:
        property_image = ''

    public_id = property['public_id']
    title = property['title']
    description = property['description']
    property_type = property['property_type']
    location = property['location']['name']

    propertyDict = {
        'public_id': public_id,
        'title': title,
        'description': description,
        'property_type': property_type,
        'location': location,
        'property_image': property_image
    } 

    context = {
        'property': propertyDict,
        'form': form
    }

    return render(request, 'property.html', context)

def processContactRequest(request, id):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            response = ContactRequests().postContactRequest(
                {
                    'name': name,
                    'phone': phone,
                    'email': email,
                    'message': message,
                    'property_id': id,
                    'source': 'iraisaguirre.com'
                }
            )

            print(response.json())

            if response.status_code == 200:
                messages.success(request, 'Tu mensaje se ha enviado')
                print(response.json()['status'])
                form = ContactForm()
            else:
                messages.error(request, 'Tu mensaje falló al enviarse')
                print(response.json()['error'])
        else:
            print('Algunos datos no son válidos')
    else:
        form = ContactForm()

    return form
