def test_function():
    def inner_function():
        a = "Я в области видимости функции test_function"
        print(a)
    inner_function()
test_function()
"""
Вызов фунции inner_function() вне функции test_function() вызовет ошибку,
так как она относится к области видимости внутри функции test_function().
"""