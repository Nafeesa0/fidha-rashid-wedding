from django.shortcuts import render, redirect

def envelope(request):
    if request.method == 'POST':
        name = request.POST.get('guest_name', '').strip()
        if name:
            request.session['guest_name'] = name
            request.session.modified = True
            return redirect('main_invite')
        return render(request, 'invitation/envelope.html', {'error': 'Please enter your name.'})
    # If someone visits /invite/ directly without name, clear session
    return render(request, 'invitation/envelope.html')

def main_invite(request):
    # If no session, redirect to envelope
    if not request.session.get('guest_name'):
        return redirect('envelope')
    return render(request, 'invitation/main_invite.html', {
        'guest_name': request.session.get('guest_name', '')
    })

def rsvp_yes(request):
    if not request.session.get('guest_name'):
        return redirect('envelope')
    return render(request, 'invitation/rsvp_yes.html', {
        'guest_name': request.session.get('guest_name', 'Dear Guest')
    })

def rsvp_no(request):
    if not request.session.get('guest_name'):
        return redirect('envelope')
    return render(request, 'invitation/rsvp_no.html', {
        'guest_name': request.session.get('guest_name', 'Dear Guest')
    })