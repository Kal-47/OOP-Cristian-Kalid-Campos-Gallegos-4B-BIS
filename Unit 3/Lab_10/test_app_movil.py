import pytest

from app_movil import (
    AppMovilError,
    PerfilMovil,
    PerfilPro,
    PuntosInsuficientesError,
    SuscripcionExpiradaError,
)


@pytest.fixture
def perfil():
    return PerfilMovil("kal")


@pytest.fixture
def perfil_pro():
    return PerfilPro("kal_pro", meses_suscripcion=3)


def test_valores_iniciales(perfil):
    assert perfil.username == "kal"
    assert perfil.gemas == 50
    assert perfil.racha_dias == 1
    assert perfil.notificaciones_activas is True


def test_ganar_gemas_suma_al_balance(perfil):
    assert perfil.ganar_gemas(25) == 75
    assert perfil.gemas == 75


def test_gastar_gemas_resta_del_balance(perfil):
    assert perfil.gastar_gemas(20) == 30
    assert perfil.gemas == 30


def test_gastar_todo_el_saldo_deja_cero(perfil):
    assert perfil.gastar_gemas(50) == 0


def test_consistencia_aritmetica_ganar_y_gastar(perfil):
    perfil.ganar_gemas(30)
    perfil.gastar_gemas(30)
    assert perfil.gemas == 50


def test_instancias_aisladas_por_fixture(perfil):
    assert perfil.gemas == 50


def test_gemas_iniciales_negativas_lanzan_valueerror():
    with pytest.raises(ValueError):
        PerfilMovil("kal", gemas=-1)


def test_asignar_gemas_negativas_lanza_valueerror(perfil):
    with pytest.raises(ValueError):
        perfil.gemas = -10


def test_gastar_mas_de_lo_disponible(perfil):
    with pytest.raises(PuntosInsuficientesError):
        perfil.gastar_gemas(51)
    assert perfil.gemas == 50 


@pytest.mark.parametrize("cantidad", [0, -1, -100])
def test_gastar_cantidad_no_positiva(perfil, cantidad):
    with pytest.raises(ValueError):
        perfil.gastar_gemas(cantidad)


def test_pro_con_meses_invalidos():
    with pytest.raises(ValueError):
        PerfilPro("kal", meses_suscripcion=0)


def test_pro_expirado_lanza_error_y_desactiva_es_pro(perfil_pro):
    perfil_pro.meses_suscripcion = 0
    with pytest.raises(SuscripcionExpiradaError):
        perfil_pro.descargar_contenido_offline()
    assert perfil_pro.es_pro is False


def test_mensaje_de_error_de_saldo(perfil):
    with pytest.raises(PuntosInsuficientesError, match="insuficiente"):
        perfil.gastar_gemas(999)


@pytest.mark.parametrize(
    "cantidad, esperado",
    [
        (1, 51),         
        (10, 60),
        (100, 150),
        (10_000, 10_050),  
    ],
)
def test_ganar_gemas_valores_validos(perfil, cantidad, esperado):
    assert perfil.ganar_gemas(cantidad) == esperado


@pytest.mark.parametrize("cantidad", [0, -1, -50, 1.5, "10", None])
def test_ganar_gemas_valores_invalidos(perfil, cantidad):
    with pytest.raises(ValueError):
        perfil.ganar_gemas(cantidad)


def test_perfilpro_hereda_de_perfilmovil(perfil_pro):
    assert isinstance(perfil_pro, PerfilPro)
    assert isinstance(perfil_pro, PerfilMovil)
    assert issubclass(PerfilPro, PerfilMovil)


def test_perfilmovil_no_es_perfilpro(perfil):
    assert not isinstance(perfil, PerfilPro)


def test_excepciones_de_dominio_comparten_base():
    assert issubclass(SuscripcionExpiradaError, AppMovilError)
    assert issubclass(PuntosInsuficientesError, AppMovilError)


def test_perfilpro_hereda_comportamiento_de_gemas(perfil_pro):
    assert perfil_pro.ganar_gemas(10) == 60


def test_ciclo_de_vida_perfilpro(perfil_pro):
    assert perfil_pro.es_pro is True
    assert perfil_pro.meses_suscripcion == 3
    assert "kal_pro" in perfil_pro.descargar_contenido_offline()

    perfil_pro.meses_suscripcion = 0
    with pytest.raises(SuscripcionExpiradaError):
        perfil_pro.descargar_contenido_offline()
    assert perfil_pro.es_pro is False

    with pytest.raises(SuscripcionExpiradaError):
        perfil_pro.descargar_contenido_offline()
