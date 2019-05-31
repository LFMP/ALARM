import json, datetime, os
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from webapp.models import Adapters, Post, RecomendacaoAcessada, RecomendacaoGerada
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from statistics import median

@login_required(login_url='../admin/login/')
def quantidadeRecGeradasPorHora(request):
  dados = {}
  hours = []
  lista = Adapters.objects.filter(ativo=1).values("rid")
  today = datetime.date.today()
  for i in lista:
    for hora in range(25):
      hours.append(RecomendacaoGerada.objects.filter(rid=i["rid"],date__year =str(today.year),date__month =str(today.month), date__day = str(today.day),date__hour=hora).count())
    inf = {i["rid"]:hours}
    hours = []
    dados.update(inf)
  return JsonResponse(dados)

@login_required(login_url='../admin/login/')
def quantidadeRecGeradasPorDia(request):
  dados = {}
  lista = Adapters.objects.filter(ativo=1).values("rid")
  today = datetime.date.today()
  for i in lista:
    inf = {i["rid"]:RecomendacaoGerada.objects.filter(rid=i["rid"],date__istartswith=today).count()}
    dados.update(inf)
  return JsonResponse(dados)

@login_required(login_url='../admin/login/')
def quantidadeRecGeradasPorMes(request):
  lista = Adapters.objects.filter(ativo=1).values("rid")
  today = datetime.date.today()
  month = format(today.month,'02d')
  year = today.year
  dias = []
  dados = {}
  for j in lista:
    for i in range (1,today.day+1):
      dias.append(RecomendacaoGerada.objects.filter(rid=j["rid"],date__year=str(year), date__month = str(month),date__day = format(i, '02d')).count())
    inf = {j["rid"]:dias}
    dias = []
    dados.update(inf)
  return JsonResponse(dados)

@login_required(login_url='../admin/login/')
def quantidadeRecGeradasPorAno(request):
  lista = Adapters.objects.filter(ativo=1).values("rid")
  today = datetime.date.today()
  year = str(today.year)
  dados = {}
  days = {}
  for i in lista:
    eachRec = RecomendacaoGerada.objects.filter(rid=i["rid"])
    for j in eachRec:
      day = str(j.date)
      day = day[:10]
      if day not in days:
        days.update({day: eachRec.filter(date__istartswith=day,date__year =year).count()})
    inf = {i["rid"]:days}
    days = {}
    dados.update(inf)
  return JsonResponse(dados)

@login_required(login_url='../admin/login/')
def quantidadeRecAcessadasPorHora(request):
  dados = {}
  hours = []
  lista = Adapters.objects.filter(ativo=1).values("rid")
  today = datetime.date.today()
  for i in lista:
    for hora in range(25):
      hours.append(RecomendacaoAcessada.objects.filter(rid=i["rid"],date__year =str(today.year),date__month =str(today.month), date__day = str(today.day),date__hour=hora).count())
    inf = {i["rid"]:hours}
    hours = []
    dados.update(inf)

  return JsonResponse(dados)

@login_required(login_url='../admin/login/')
def quantidadeRecAcessadasPorDia(request):
  dados = {}
  lista = Adapters.objects.filter(ativo=1).values("rid")
  today = datetime.date.today()
  for i in lista:
    inf = {i["rid"]:RecomendacaoAcessada.objects.filter(rid=i["rid"],date__istartswith=today).count()}
    dados.update(inf)
  return JsonResponse(dados)

@login_required(login_url='../admin/login/')
def quantidadeRecAcessadasPorMes(request):
  lista = Adapters.objects.filter(ativo=1).values("rid")
  today = datetime.date.today()
  month = format(today.month,'02d')
  year = today.year
  dias = []
  dados = {}
  for j in lista:
    for i in range (1,today.day+1):
      dias.append(RecomendacaoAcessada.objects.filter(rid=j["rid"],date__year=str(year), date__month = str(month),date__day = format(i, '02d')).count())
    inf = {j["rid"]:dias}
    dias = []
    dados.update(inf)
  return JsonResponse(dados)

@login_required(login_url='../admin/login/')
def quantidadeRecAcessadasPorAno(request):
  lista = Adapters.objects.filter(ativo=1).values("rid")
  today = datetime.date.today()
  year = str(today.year)
  dados = {}
  days = {}
  for i in lista:
    eachRec = RecomendacaoAcessada.objects.filter(rid=i["rid"])
    for j in eachRec:
      day = str(j.date)
      day = day[:10]
      if day not in days:
        days.update({day: eachRec.filter(date__istartswith=day,date__year =year).count()})
    inf = {i["rid"]:days}
    days = {}
    dados.update(inf)
  return JsonResponse(dados)

@login_required(login_url='../admin/login/')
def quantidadeRecAderidasPorDia(request):
  dados = {}
  lista = Adapters.objects.filter(ativo=1).values("rid")
  today = datetime.date.today()
  cliquetotal = Post.objects.filter(dateR__istartswith = today).count()
  cliquerestante = 0
  for i in lista:
    inf = {i["rid"]:RecomendacaoAcessada.objects.filter(rid=i["rid"],date__istartswith=today).count()}
    dados.update(inf)
    cliquerestante = cliquerestante + dados[i["rid"]]

  dados.update({"Não-recomendado":cliquetotal - cliquerestante})
  return JsonResponse(dados)


@login_required(login_url='../admin/login/')
def quantidadeRecAderidasPorMes(request):
  lista = Adapters.objects.filter(ativo=1).values("rid")
  today = datetime.date.today()
  month = format(today.month,'02d')
  year = today.year
  dias = []
  dados = {}
  cliquetotal = Post.objects.filter(dateR__year = str(year),dateR__month = str(month)).count()
  cliquerestante = 0
  for j in lista:
      dados.update({j["rid"]:RecomendacaoAcessada.objects.filter(rid=j["rid"],date__year=str(year), date__month = str(month)).count()})
      cliquerestante = cliquerestante + dados[j["rid"]]

  dados.update({"Não-recomendado": cliquetotal - cliquerestante })
  return JsonResponse(dados)

@login_required(login_url='../admin/login/')
def quantidadeRecAderidasPorAno(request):
  lista = Adapters.objects.filter(ativo=1).values("rid")
  today = datetime.date.today()
  year = str(today.year)
  dados = {}
  cliquerestante = 0
  cliquetotal = Post.objects.filter(dateR__year = str(year)).count()
  for i in lista:
    eachRec = RecomendacaoAcessada.objects.filter(rid=i["rid"], date__year = year).count()
    dados.update({i["rid"]:eachRec})
    cliquerestante = cliquerestante + dados[i["rid"]]

  dados.update({"Não-recomendado": cliquetotal - cliquerestante })
  return JsonResponse(dados)


@login_required(login_url='../admin/login/')
def quantidadeRecAderidasPorGeracaoPorDia(request):
  dados = {}
  lista = Adapters.objects.filter(ativo=1).values("rid")
  today = datetime.date.today()
  cliquetotal = RecomendacaoGerada.objects.filter(date__istartswith = today).count()
  cliquerestante = 0
  for i in lista:
    inf = {i["rid"]:RecomendacaoAcessada.objects.filter(rid=i["rid"],date__istartswith=today).count()}
    dados.update(inf)
    cliquerestante = cliquerestante + dados[i["rid"]]

  dados.update({"Não-Clicada":cliquetotal - cliquerestante})
  return JsonResponse(dados)


@login_required(login_url='../admin/login/')
def quantidadeRecAderidasPorGeracaoPorMes(request):
  lista = Adapters.objects.filter(ativo=1).values("rid")
  today = datetime.date.today()
  month = format(today.month,'02d')
  year = today.year
  dias = []
  dados = {}
  cliquetotal = RecomendacaoGerada.objects.filter(date__year = str(year),date__month = str(month)).count()
  cliquerestante = 0
  for j in lista:
      dados.update({j["rid"]:RecomendacaoAcessada.objects.filter(rid=j["rid"],date__year=str(year), date__month = str(month)).count()})
      cliquerestante = cliquerestante + dados[j["rid"]]


  dados.update({"Não-Clicada": cliquetotal - cliquerestante })
  return JsonResponse(dados)

@login_required(login_url='../admin/login/')
def quantidadeRecAderidasPorGeracaoPorAno(request):
  lista = Adapters.objects.filter(ativo=1).values("rid")
  today = datetime.date.today()
  year = str(today.year)
  dados = {}
  cliquerestante = 0
  cliquetotal = RecomendacaoGerada.objects.filter(date__year = str(year)).count()
  for i in lista:
    eachRec = RecomendacaoAcessada.objects.filter(rid=i["rid"], date__year = year).count()
    dados.update({i["rid"]:eachRec})
    cliquerestante = cliquerestante + dados[i["rid"]]

  dados.update({"Não-Clicada": cliquetotal - cliquerestante })
  return JsonResponse(dados)



@login_required(login_url='../admin/login/')
def quantidadeRecMinima(request):
  dados = {}
  lista = Adapters.objects.filter(ativo=1).values("rid")
  today = datetime.date.today()
  dias = {}
  eficiencia = []
  for i in lista:
    for dia in range(32):
      quatidadeGerada = RecomendacaoGerada.objects.filter(rid = i["rid"], date__year = str(today.year), date__month = str(today.month), date__day = str(dia)).count()
      quatidadeAcessada = RecomendacaoAcessada.objects.filter(rid = i["rid"], date__year = str(today.year), date__month = str(today.month), date__day = str(dia)).count()
      if quatidadeGerada != 0 and quatidadeAcessada != 0:
        eficiencia.append(quatidadeAcessada/quatidadeGerada * 100)  
    if eficiencia == []:
      dados.update({i["rid"]:0})
    else:
      dados.update({i["rid"]:min(eficiencia)})
    eficiencia = []

  return JsonResponse(dados)


@login_required(login_url='../admin/login/')
def quantidadeRecMedia(request):
  dados = {}
  lista = Adapters.objects.filter(ativo=1).values("rid")
  today = datetime.date.today()
  dias = {}
  eficiencia = []
  for i in lista:
    for dia in range(32):
      quatidadeGerada = RecomendacaoGerada.objects.filter(rid = i["rid"], date__year = str(today.year), date__month = str(today.month), date__day = str(dia)).count()
      quatidadeAcessada = RecomendacaoAcessada.objects.filter(rid = i["rid"], date__year = str(today.year), date__month = str(today.month), date__day = str(dia)).count()
      if quatidadeGerada != 0 and quatidadeAcessada != 0:
        eficiencia.append(quatidadeAcessada/quatidadeGerada * 100)
    if eficiencia == []:
      dados.update({i["rid"]:0})
    else:
      dados.update({i["rid"]:median(eficiencia)})  
    eficiencia = []

  return JsonResponse(dados)

@login_required(login_url='../admin/login/')
def quantidadeRecMaxima(request):
  dados = {}
  lista = Adapters.objects.filter(ativo=1).values("rid")
  today = datetime.date.today()
  dias = {}
  eficiencia = []
  for i in lista:
    for dia in range(32):
      quatidadeGerada = RecomendacaoGerada.objects.filter(rid = i["rid"], date__year = str(today.year), date__month = str(today.month), date__day = str(dia)).count()
      quatidadeAcessada = RecomendacaoAcessada.objects.filter(rid = i["rid"], date__year = str(today.year), date__month = str(today.month), date__day = str(dia)).count()
      if quatidadeGerada != 0 and quatidadeAcessada != 0:
        eficiencia.append(quatidadeAcessada/quatidadeGerada * 100)
    if eficiencia == []:
      dados.update({i["rid"]:0})
    else:
      dados.update({i["rid"]:max(eficiencia)})
    eficiencia = []
  return JsonResponse(dados)

@login_required(login_url='../admin/login/')
def recomenderclick(request):
  return JsonResponse({"caminho":"ok"})

@login_required(login_url='../admin/login/')
@csrf_exempt
def code(request):
  if request.method == 'POST':
    data = json.loads(request.body.decode('UTF-8'))
    fileName = data["nome"]
    codigo = data["valor"]
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = dir_path.replace('alarm','webapp/algorithms/'+ fileName + '.py')
    try:
      exec('from random import randint\n'+codigo+'\n'+'count = Post.objects.count()\n'+'random_object = Post.objects.all()[randint(0, count - 1)]\n'+fileName+'(request,random_object)')
    except Exception as ex:
      return HttpResponse(json.dumps({"type":type(ex).__name__ , "args" : str(ex.args)}),status=404)
    else:  
      if not os.path.exists(dir_path):
        file = open(dir_path, "w+")
        file.write(codigo)
        novoRecomendador = Adapters(fileName,1)
        novoRecomendador.save()
        return HttpResponse(status=204)  
    return HttpResponse(json.dumps({"type":"Arquivo já existente com este nome" , "args" : "Mude-o!"}),status=404)
  else:
    return render(request,"admin/code-editor/code-editor.html")

@login_required(login_url='../admin/login/')
@csrf_exempt
def toggleRecommendator(request):
  if(request.method == 'POST'):
    data = json.loads(request.body.decode('UTF-8'))
    name = data["nome"]
    value = data["value"]
    element = Adapters.objects.get(rid=name)
    element.ativo = value
    element.save()
    return HttpResponse(status=204)
  else:
    lista = Adapters.objects.values()
    adap = {}
    for i in lista:
      adap.update({i["rid"]:[str(i["ativo"])]})
    return JsonResponse(adap)

@login_required(login_url='../admin/login/')
@csrf_exempt
def deleteRecommendator(request):
  if (request.method == 'POST'):
    data = json.loads(request.body.decode('UTF-8'))
    fileName = data["name"]  # contem o nome do recomendador a ser excluido
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = dir_path.replace('alarm','webapp/algorithms/'+ fileName + '.py')
    if os.path.exists(dir_path):
      os.remove(dir_path)
      Adapters.objects.get(rid = fileName).delete()
      return HttpResponse(status=204)
    try:
      Adapters.objects.get(rid = fileName).delete()   
    except:   
      return HttpResponse(status=404)

  return HttpResponse(status=200)

@login_required(login_url='../admin/login/')
@csrf_exempt
def visulizarRecommendator(request):
  if (request.method == 'POST'):
    data = json.loads(request.body.decode('UTF-8'))
    fileName = data["name"]  # contem o nome do recomendador a ser visualizado
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = dir_path.replace('alarm','webapp/algorithms/'+ fileName + '.py')
    if os.path.exists(dir_path):
      file = open(dir_path, "r")
      conteudo = {"conteudo":file.read(), "nome":fileName}
      return JsonResponse(conteudo)
    return HttpResponse(status=404)

  return HttpResponse(status=200)


@login_required(login_url='../admin/login/')
def managercodes(request):
  return render(request,"admin/toggle/toggleRecomender.html")

@login_required(login_url='../admin/login/')
def recomendacaoGerada(request):
  return render(request,"admin/graficos/recomendacaogerada/recomendacaogerada.html")

@login_required(login_url='../admin/login/')
def recomendacaoAcessada(request):
  return render(request,"admin/graficos/recomendacaoacessada/recomendacaoacessada.html")

@login_required(login_url='../admin/login/')
def recomendacaoAderida(request):
  return render(request,"admin/graficos/recomendacaoaderida/recomendacaoaderida.html")

@login_required(login_url='../admin/login/')
def recomendacaoAderidaPorGeracao(request):
  return render(request,"admin/graficos/recomendacaoaderidaporgeracao/recomendacaoaderidaporgeracao.html")

@login_required(login_url='../admin/login/')
def recomendacaoEficiencia(request):
  return render(request,"admin/graficos/recomendacaoeficiencia/recomendacaoeficiencia.html")
