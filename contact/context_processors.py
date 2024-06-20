from .forms import ContactForm, CallForm

def forms_processor(request):
    return {
        'contact_form': ContactForm(prefix='contact'),
        'call_form': CallForm(prefix='call')
    }
