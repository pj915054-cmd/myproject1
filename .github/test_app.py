from app import add,subtract

def test_add():
  assert add(30+10) == 40

def test_subtract():
  assert subtract(30-10) == 20
  
