def test_form_view(request):
    if request.method == "POST":
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('save ho gya bhai!')
        else:
            return HttpResponse('noooo its invalid')

    return render(request, 'test.html', {
        'objects': TestModel.objects.all()
    })