from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm, CallForm

def handle_forms(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST, prefix='contact')
        call_form = CallForm(request.POST, prefix='call')

        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Форма обратной связи успешно отправлена!')
        elif call_form.is_valid():
            call_form.save()
            messages.success(request, 'Форма заказа звонка успешно отправлена!')
        else:
            if not contact_form.is_valid():
                messages.error(request, 'Произошла ошибка при отправке формы обратной связи. Пожалуйста, попробуйте снова.')
            if not call_form.is_valid():
                messages.error(request, 'Произошла ошибка при отправке формы заказа звонка. Пожалуйста, попробуйте снова.')
        return redirect(request.META.get('HTTP_REFERER', 'contact:contact_and_call'))

    return redirect('contact:contact_and_call')
