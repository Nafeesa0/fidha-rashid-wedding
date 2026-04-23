from django.shortcuts import render, redirect

def envelope(request):
    if request.method == 'POST':
        name = request.POST.get('guest_name', '').strip()
        if name:
            request.session['guest_name'] = name
            return redirect('main_invite')
        return render(request, 'invitation/envelope.html', {'error': 'Please enter your name.'})
    return render(request, 'invitation/envelope.html')

def main_invite(request):
    guest_name = request.session.get('guest_name', '')
    return render(request, 'invitation/main_invite.html', {'guest_name': guest_name})

def rsvp_yes(request):
    guest_name = request.session.get('guest_name', 'Dear Guest')
    return render(request, 'invitation/rsvp_yes.html', {'guest_name': guest_name})

def rsvp_no(request):
    guest_name = request.session.get('guest_name', 'Dear Guest')
    return render(request, 'invitation/rsvp_no.html', {'guest_name': guest_name})