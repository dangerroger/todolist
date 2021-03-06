from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Item, List

# Create your views here.
def home_page(request):
    #return render(request, 'home.html')
    if request.method == 'POST':
        #new_item_text = request.POST['item_text']
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/the-only-list-in-the-world')
    return render(request,'home.html')
        #return redirect('/')




    #items = Item.objects.all()

    #else:
        #new_item_text = ''

        #return HttpResponse(request.POST['item_text'])
        #item = Item()
        #item.text = request.POST.get('item_text', '')
        #item.save()

     #return render(request,'home.html') #, {'items' : items })

    #, {
            #'new_item_text': new_item_text
            #}
def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    #items = Item.objects.filter(list=list_)
    #items = Item.objects.all()
    #return render(request, 'list.html', {'items': items})
    return render(request, 'list.html', {'list': list_})



def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    #return redirect ('/lists/the-only-list-in-the-world/')
    return redirect (f'/lists/{list_.id}/')

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')
