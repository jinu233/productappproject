from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from feedbackproject.models import feedback
class BookForm(ModelForm):
    class Meta:
        model =feedback
        fields = ['course', 'feedback']

def book_list(request, template_name='/home/shijas/Desktop/DjangoLuminar/feedback/feedbackproject/templates/feedback_list.html'):
    print("inside book")
    book = feedback.objects.all()
    data = {}
    data['object_list'] = book
    return render(request, template_name, data)

def book_view(request, pk, template_name='/home/shijas/Desktop/DjangoLuminar/feedback/feedbackproject/templates/feedback_detail.html'):
    print("pkkkkkk",pk)
    book= get_object_or_404(feedback, pk=pk)
    return render(request, template_name, {'object':book})

def book_create(request, template_name='/home/shijas/Desktop/DjangoLuminar/feedback/feedbackproject/templates/feedback_form.html'):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('book:book_list')
    return render(request, template_name, {'form':form})

def book_update(request, pk, template_name='/home/shijas/Desktop/DjangoLuminar/feedback/feedbackproject/templates/feedback_form.html'):
    book= get_object_or_404(feedback, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book:book_list')
    return render(request, template_name, {'form':form})

def book_delete(request, pk, template_name='/home/shijas/Desktop/DjangoLuminar/feedback/feedbackproject/templates/feedback_confirm_delete.html'):
    book= get_object_or_404(feedback, pk=pk)
    if request.method=='POST':
        book.delete()
        return redirect('book:book_list')
    return render(request, template_name, {'object':book})


