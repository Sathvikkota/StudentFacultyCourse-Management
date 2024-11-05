from django.shortcuts import redirect

def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if "auname" not in request.session:
            return redirect('home')  # Redirect to the login page if not logged in
        return view_func(request, *args, **kwargs)
    return wrapper
