from django.shortcuts import render
from make_payment.models import Transaction
# Create your views here.
def history(request):
    if request.method == "get":
        check=request.session['user_username']
        history = Transaction.objects.filter(sender_username=check).order_by('-date')
        data={'history':history}
        return render(request,'transaction_history/base.html',data)
    else:
        return render(request,'transaction_history/base.html')
        