from django.shortcuts import render
from django.shortcuts import redirect

from Leave.models import leaveModel
from Schoolapp.models import tbl_login
from Schoolapp.views import Home


# Create your views here.


def leave(request):
    if 'email' in request.session:
        email=request.session['email']
        data=leaveModel.objects.filter(email=email)
        context = {
            'data': data
        }
        return render(request, 'Leave/leave_view.html', context)
    else:
        return redirect(Home)

def leaveApply(request):
    if 'email' in request.session:
        email=request.session['email']
        user=tbl_login.objects.get(email=email)
        if request.method == 'POST':
            # print('1')
            name = request.POST['name']
            leaveDate = request.POST['date']
            leaveDiv = request.POST['session']
            leaveReason = request.POST['reason']
            # leaveRecords = request.POST['proof']
            # print(leaveDate)
            if leaveDiv=='FD':
                leaveDiv='AN, FN'
            leaveStatus = False
            email = request.user
            leaveModel.objects.create(name=name,email=user, leaveDate=leaveDate, leaveDiv=leaveDiv, leaveReason=leaveReason, leaveStatus=leaveStatus).save()
            return redirect('leave')
        return render(request, 'Leave/leave.html')
    else:
        return redirect(Home)
