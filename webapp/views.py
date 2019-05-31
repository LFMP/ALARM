import json
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from webapp.models import Adapters, Post, RecomendacaoAcessada,RecomendacaoGerada
from webapp.algorithms import *

def adapterlist(request): #funcao que identifica quais sao os recomendadores ativos
	lista = Adapters.objects.filter(ativo=1).values("rid")
	size = len(lista)
	adapt = []
	for i in lista:
		adapt.append(i["rid"])
	return HttpResponse(json.dumps({'adapters': adapt, 'quantidade' : size}))

@csrf_exempt
def add(request): #broker
	if request.method == 'POST':
		resp = request.body.decode('UTF-8')
		data = json.loads(resp)
		lista = Adapters.objects.filter(ativo=1).values("rid")
		if data["to"] == 1:
			isRecomendation = False
			for i in lista:
				if i["rid"] in (data["id"]).split(" "): #clique de recomendacao
					isRecomendation = True
					adapter = i["rid"]
					break
			post_data = Post(
				data["ip"],
				data["idUser"],
				data["idClick"],
				data["classe"],
				data["texto"],
				data["current"],
				data["href"],
				data["timestamp"],
				data["dateTimestamp"],
				data["dateR"]
			)
			post_data.save() #salva o clique na tabela ClickStream
			if isRecomendation: #salva na tabela recomendações acessadas caso o clique proveio de uma recomendação
				post_data = RecomendacaoAcessada(
				   adapter,
				   data["idClick"],
				   date = data["dateR"]
				)
				post_data.save()
			return HttpResponse(status = 204)
		else: #gerar recomendacao
			dados = Post.objects.get(idClick=data["idClick"])
			for i in lista:
				if i["rid"] == data["iden"]:
					recomendador = i["rid"] + '.' + i["rid"]  #nome do recomendador (ou funcao)
					try:
						recomendador = eval(recomendador) # executa python dentro da execução
					except:
						module = __import__("webapp.algorithms." + i["rid"], fromlist = i["rid"])
						recomendador = getattr(module, i["rid"])
					finally:
						function_output = recomendador(request,dados) #saida deverá ser um vetor de links
						for each_link in function_output:
							post_data = RecomendacaoGerada( #salva as recomendações sugeridas
								i["rid"],
								data["idClick"],
								each_link,
								data["dateR"]
							)
							post_data.save()
						return JsonResponse({i["rid"]:function_output})
			return HttpResponse(status=204)	
	else:
		return HttpResponse(status=204)