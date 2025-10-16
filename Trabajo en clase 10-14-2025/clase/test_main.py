from main import restar

def test_restar():  #el archivo de test siempre debe de empezar con test_ al igual que la funcion
    assert restar(10,5) == 5
    assert restar(5.5,2.5) == 3.0
    assert restar(0,0) == 0
    assert restar(-5,-19) == -14
