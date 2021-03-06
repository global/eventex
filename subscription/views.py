from forms import SubscriptionForm
from django.shortcuts import render_to_response
from django.template import RequestContext 
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from models import Subscription

def success(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    context = RequestContext(request, {'subscription': subscription})
    return render_to_response('subscription/success.html', context_instance=context)

def subscribe(request):
    if request.method == 'POST':
        return _create(request)
    else:
        return _new(request)

def _new(request):
    form = SubscriptionForm()
    context = RequestContext(request, {'form': form})
    return render_to_response('subscription/new.html', context_instance=context)

def _create(request):
    form = SubscriptionForm(request.POST)
    
    if not form.is_valid():
        context = RequestContext(request, {'form': form})
        return render_to_response('subscription/new.html', context)

    subscription = form.save()
    send_mail(
        subject = u'Subscription to EventeX',
        message = u'Thanks for your participation',
        from_email = 'contato@eventex.com', 
        recipient_list = [subscription.email]
    )

    return HttpResponseRedirect(
        reverse('subscription:success', args=[subscription.pk]))
