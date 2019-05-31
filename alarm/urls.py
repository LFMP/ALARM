from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
  url(r'^quantidadeRecGeradasPorHora', views.quantidadeRecGeradasPorHora, name='quantidadeRecGeradasPorHora'),
  url(r'^quantidadeRecGeradasPorDia', views.quantidadeRecGeradasPorDia, name='quantidadeRecGeradasPorDia'),
  url(r'^quantidadeRecGeradasPorMes', views.quantidadeRecGeradasPorMes, name='quantidadeRecGeradasPorMes'),
  url(r'^quantidadeRecGeradasPorAno', views.quantidadeRecGeradasPorAno, name='quantidadeRecGeradasPorAno'),
  url(r'^quantidadeRecAcessadasPorHora', views.quantidadeRecAcessadasPorHora, name='quantidadeRecAcessadasPorHora'),
  url(r'^quantidadeRecAcessadasPorDia', views.quantidadeRecAcessadasPorDia, name='quantidadeRecAcessadasPorDia'),
  url(r'^quantidadeRecAcessadasPorMes', views.quantidadeRecAcessadasPorMes, name='quantidadeRecAcessadasPorMes'),
  url(r'^quantidadeRecAcessadasPorAno', views.quantidadeRecAcessadasPorAno, name='quantidadeRecAcessadasPorAno'),
  url(r'^quantidadeRecAderidasPorDia', views.quantidadeRecAderidasPorDia, name='quantidadeRecAderidasPorDia'),
  url(r'^quantidadeRecAderidasPorMes', views.quantidadeRecAderidasPorMes, name='quantidadeRecAderidasPorMes'),
  url(r'^quantidadeRecAderidasPorAno', views.quantidadeRecAderidasPorAno, name='quantidadeRecAderidasPorAno'),
  url(r'^quantidadeRecAderidasPorGeracaoPorDia', views.quantidadeRecAderidasPorGeracaoPorDia, name='quantidadeRecAderidasPorGeracaoPorDia'),
  url(r'^quantidadeRecAderidasPorGeracaoPorMes', views.quantidadeRecAderidasPorGeracaoPorMes, name='quantidadeRecAderidasPorGeracaoPorMes'),
  url(r'^quantidadeRecAderidasPorGeracaoPorAno', views.quantidadeRecAderidasPorGeracaoPorAno, name='quantidadeRecAderidasPorGeracaoPorAno'),
  url(r'^quantidadeRecMinima', views.quantidadeRecMinima, name='quantidadeRecMinima'),
  url(r'^quantidadeRecMaxima', views.quantidadeRecMaxima, name='quantidadeRecMaxima'),
  url(r'^quantidadeRecMedia', views.quantidadeRecMedia, name='quantidadeRecAderidasMedia'),
  url(r'^toggleRecommendator',views.toggleRecommendator,name='toggleRecommendator'),
  url(r'^deleteRecommendator',views.deleteRecommendator,name='deleteRecommendator'),
  url(r'^visulizarRecommendator',views.visulizarRecommendator,name='visulizarRecommendator'),
  url(r'^code',views.code,name='code'),
  url(r'^managercodes',views.managercodes,name='managercodes'),
  url(r'^recomendacaoGerada',views.recomendacaoGerada,name='recomendacaoGerada'),
  url(r'^recomendacaoAcessada',views.recomendacaoAcessada,name='recomendacaoAcessada'),
  url(r'^recomendacaoAderidaPorGeracao',views.recomendacaoAderidaPorGeracao,name='recomendacaoAderidaPorGeracao'),
  url(r'^recomendacaoAderida',views.recomendacaoAderida,name='recomendacaoAderida'),
  url(r'^recomendacaoEficiencia',views.recomendacaoEficiencia,name='recomendacaoEficiencia'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)