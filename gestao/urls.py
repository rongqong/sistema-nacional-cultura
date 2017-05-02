from django.conf.urls import url
from django.contrib.admin.views.decorators import staff_member_required

from . import views

urlpatterns = [
    # Acompanhar andamento dos processos de adesão
    url(r'^$', staff_member_required(
        views.AcompanharAdesao.as_view(),
        login_url='adesao:login'), name='acompanhar_adesao'),
    url(r'^alterar/situacao/(?P<id>[\w]+)$',
        staff_member_required(views.alterar_situacao, login_url='adesao:login'),
        name='alterar_situacao'),
    url(r'^alterar/cadastrador/municipio/',
        staff_member_required(views.AlterarCadastrador.as_view()), name='alterar_cadastrador'),
    url(r'^alterar/cadastrador/estado/',
        staff_member_required(views.AlterarCadastradorEstado.as_view()), name='alterar_cadastrador_estado'),
    # Acompanhar e aditivar prazos dos municípios
    url(r'^acompanhar/prazo/',
        staff_member_required(views.AcompanharPrazo.as_view()), name='acompanhar_prazo'),
    url(r'^aditivar/prazo/(?P<id>[\w]+)$',
        staff_member_required(views.aditivar_prazo, login_url='adesao:login'), name='aditivar_prazo'),

    # Acompanhar criação do sistema de cultura
    url(r'^acompanhar/sistema$', staff_member_required(
        views.AcompanharSistema.as_view(),
        login_url='adesao:login'), name='acompanhar_sistema'),
    # Acompanhar criação do órgão gestor
    url(r'^acompanhar/orgao$', staff_member_required(
        views.AcompanharOrgao.as_view(),
        login_url='adesao:login'), name='acompanhar_orgao'),
    # Acompanhar criação do conselho cultural
    url(r'^acompanhar/conselho$', staff_member_required(
        views.AcompanharConselho.as_view(),
        login_url='adesao:login'), name='acompanhar_conselho'),
    # Acompanhar criação do fundo de cultura
    url(r'^acompanhar/fundo$', staff_member_required(
        views.AcompanharFundo.as_view(),
        login_url='adesao:login'), name='acompanhar_fundo'),
    # Acompanhar elaboração do plano de cultura
    url(r'^acompanhar/plano$', staff_member_required(
        views.AcompanharPlano.as_view(),
        login_url='adesao:login'), name='acompanhar_plano'),

    # Diligência no anexo
    url(r'^diligencia/(?P<etapa>[\w]+)/(?P<st>[\w]+)/(?P<id>[\w]+)$',
        staff_member_required(
            views.diligencia_documental,
            login_url='adesao:login'), name='diligencia_documental'),
    # Conclusão da etapa
    url(r'^concluir/(?P<etapa>[\w]+)/(?P<st>[\w]+)/(?P<id>[\w]+)$',
        staff_member_required(
            views.concluir_etapa,
            login_url='adesao:login'), name='concluir_etapa'),

    # Detalhar usuário
    url(r'^detalhar/municipio/(?P<pk>[0-9]+)$',
        views.DetalharUsuario.as_view(),
        name='detalhar'),
    url(r'^usuarios/',
        staff_member_required(
            views.ListarUsuarios.as_view(),
            login_url='adesao:login'), name='usuarios'),
    url(r'^alterar/usuario/(?P<pk>[\d]+)$',
        staff_member_required(
            views.AlterarUsuario.as_view(),
            login_url='adesao:login'), name='alterar_usuario'),

    # UF e Município aninhados
    url(r'^chain/municipio$', staff_member_required(views.MunicipioChain.as_view()), name='municipio_chain'),

    # Inserir de documentos de entes federados
    url(r'^inserir-documentos/ente-federado$',
        staff_member_required(views.ListarDocumentosEnteFederado.as_view()), name='inserir_entefederado'),
    url(r'^inserir-documentos/ente-federado/alterar/(?P<pk>[0-9]+)$',
        staff_member_required(views.AlterarDocumentosEnteFederado.as_view()), name='alterar_entefederado'),

    # Inserção de documentos da criação do sistema de cultura
    url(r'^inserir-documentos/sistema$', staff_member_required(
        views.InserirSistema.as_view(),
        login_url='adesao:login'), name='inserir_sistema'),
    # Inserção de documentos da criação do órgão gestor
    url(r'^inserir-documentos/orgao$', staff_member_required(
        views.InserirOrgao.as_view(),
        login_url='adesao:login'), name='inserir_orgao'),
    # Inserção de documentos da criação do conselho cultural
    url(r'^inserir-documentos/conselho$', staff_member_required(
        views.InserirConselho.as_view(),
        login_url='adesao:login'), name='inserir_conselho'),
    # Inserção de documentos da criação do fundo de cultura
    url(r'^inserir-documentos/fundo$', staff_member_required(
        views.InserirFundo.as_view(),
        login_url='adesao:login'), name='inserir_fundo'),
    # Inserção de documentos da elaboração do plano de cultura
    url(r'^inserir-documentos/plano$', staff_member_required(
        views.InserirPlano.as_view(),
        login_url='adesao:login'), name='inserir_plano'),

    # Tela de alteração de upload do plano de trabalho
    url(r'^inserir-documentos/sistema/alterar/(?P<pk>[0-9]+)$',
        staff_member_required(views.AlterarSistema.as_view()), name='alterar_sistema'),
    url(r'^inserir-documentos/fundo/alterar/(?P<pk>[0-9]+)$',
        staff_member_required(views.AlterarFundo.as_view()), name='alterar_fundo'),
    url(r'^inserir-documentos/plano/alterar/(?P<pk>[0-9]+)$',
        staff_member_required(views.AlterarPlano.as_view()), name='alterar_plano'),
    url(r'^inserir-documentos/orgao/alterar/(?P<pk>[0-9]+)$',
        staff_member_required(views.AlterarOrgao.as_view()), name='alterar_orgao'),
    url(r'^inserir-documentos/conselho/alterar/(?P<pk>[0-9]+)$',
        staff_member_required(views.AlterarConselho.as_view()), name='alterar_conselho'),

    # Prorrogar o prazo do plano de trabalho
    url(r'^prorrogacao/$', views.Prorrogacao.as_view(), name='prorrogacao'),
    url(r'^prorrogacao/fundo/(?P<pk>[0-9]+)$', views.ProrrogacaoFundo.as_view(), name='prorrogacao_fundo'),
    url(r'^prorrogacao/conselho/(?P<pk>[0-9]+)$', views.ProrrogacaoConselho.as_view(), name='prorrogacao_conselho'),
    url(r'^prorrogacao/sistema/(?P<pk>[0-9]+)$', views.ProrrogacaoSistema.as_view(), name='prorrogacao_sistema'),
    url(r'^prorrogacao/orgao/(?P<pk>[0-9]+)$', views.ProrrogacaoOrgao.as_view(), name='prorrogacao_orgao'),
    url(r'^prorrogacao/plano/(?P<pk>[0-9]+)$', views.ProrrogacaoPlano.as_view(), name='prorrogacao_plano'),

    # ajax mudança de cadastrador
    url(r'^ajax_cadastrador_cpf$', staff_member_required(views.ajax_cadastrador_cpf), name='ajax_cadastrador_cpf'),

    url(r'^rotina-limpeza-arquivos$', staff_member_required(
        views.rotina_limpeza_arquivos_inexistentes), name='rotina_limpeza_arquivos'),
    ]
