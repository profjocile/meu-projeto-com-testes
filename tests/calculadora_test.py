import unittest

from meu_projeto.calculadora import calcular_desconto


class TestCalculadoraDesconto(unittest.TestCase):
 
    def test_desconto_para_valores_acima_de_cem(self):
        # Cenário: Valor de R$ 150 deve ter 10% de desconto (R$ 15)
        resultado = calcular_desconto(150)
        self.assertEqual(resultado, 15)
 
    def test_sem_desconto_para_valores_baixos(self):
        # Cenário: Valor de R$ 80 não deve ter desconto (R$ 0)
        resultado = calcular_desconto(80)
        self.assertEqual(resultado, 0)

    def test_valor_negativo_deve_retornar_erro(self):
        # Valores negativos devem levantar um erro de valor (ValueError)
        with self.assertRaises(ValueError):
            calcular_desconto(-50)
 
if __name__ == '__main__':
    unittest.main()