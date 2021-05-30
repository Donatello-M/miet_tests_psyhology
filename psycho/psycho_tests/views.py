from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer


def index(request):
	if request.method == 'POST':
		data = []
		cb = request.POST.get("cb")
		data.append(request.POST.get("first_name"))
		data.append(request.POST.get("middle_name"))
		data.append(request.POST.get("last_name"))
		data.append(request.POST.get("w_group"))
		if cb:
			return poll(request, {'cb': True, 'data': data})
	return render(request, 'index.html') 


def poll(request, lst):
	cb = lst['cb']

	if cb:
		qs = Question.objects.all()
		q_block = ('<div class="result-wrapper">'
					'<div class="result-item">'
					'<div class="result-block">')
		cnt = 1
		for q in qs:
			q_block += (f'<h4 class="result-highlight">Вопрос {cnt}</h4>'
						f'<p class="result-text">{q.ask}</p>')
			for i in range(len(q.key_type)):
				q_block +=  ('<label class="marks_text">'
                	f'<input type="checkbox" name="mark_choice'
                	f' value="{cnt}{i}"</label>')
			cnt += 1
		q_block += ('</div>'
					'<p class="result-answer">Ответ</p>'
					'</div></div>')
		return render(request, 'result.html', {'q_block': q_block})
	return redirect('index')

def verdict(request):
    return render(request, 'result.html')
