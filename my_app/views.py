from django.shortcuts import render, redirect

from .models import Profile


# Create your views here.
def home_view(request):
    profile_list = Profile.objects.all()
    return render(request, 'index.html', {'profile_list': profile_list})


def profile_view(request, _id):
    fetch_profile = Profile.objects.get(id=_id)
    user_profile = request.user.profile

    followers = fetch_profile.followed_by.count() - 1  # omitting self
    following = fetch_profile.following.count() - 1  # omitting self

    if request.method == 'POST':
        action = request.POST.get('follow_unfollow')
        if action == 'follow':
            user_profile.following.add(fetch_profile)
        else:
            user_profile.following.remove(fetch_profile)
        return redirect('my_app:profile_view', fetch_profile.id)
        # return redirect(request, 'my_app:profile_view', _id=fetch_profile.id)

    context = {'fetch_profile': fetch_profile, 'user_profile': user_profile, 'followers': followers,
               'following': following}
    return render(request, 'profile.html', context)
