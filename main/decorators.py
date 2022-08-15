def detector(callback):
	def wrap(request):
		if 'Mobile' in request.META['HTTP_USER_AGENT']:
			request.session['mobile'] = True
		else:
			request.session['mobile'] = False
		return callback(request)

	return wrap