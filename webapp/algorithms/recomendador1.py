from webapp.models import Adapters, Post
def adapter1(request,data): # item based collaborative filtering
    recomendacoes = []
    links = Post.objects.exclude(href = data.href).values_list("href", flat = True).distinct() #todos os links presentes no banco de dados
    users = Post.objects.filter(href = data.href).exclude(idClick = data.idClick).values_list("idUser", flat = True) #id dos usuarios que acessarm o link clicado
    frequencia = {link:0 for link in links} #iniciliza todos os links exceto o href com 0 de aparições       
    quantidade_recomendacoes = 0 #contador utilizado para não exceder a quantidade de recomendações indo a página destino
    for each_link in links:
        for each_user in users:
            users_links = Post.objects.filter(idUser = each_user).values_list("href",flat = True).distinct() #todos os links acessados por um usuario
            if each_link in users_links and data.href in users_links: #verifica se o usuario acessou o link href e outro link qualquer
                frequencia.update({each_link: frequencia[each_link] + 1}) #se o usuario acessou o href, incrementa-se a ocorrencia do novo link em + 1
    elemts = sorted(iter(frequencia))
    for each_link in elemts : #ordena as recomendacoes conforme as que tiveram mais frequencia
        recomendacoes.append(each_link)
        quantidade_recomendacoes+=1
        if quantidade_recomendacoes>10:
            break
    return recomendacoes

