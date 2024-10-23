class Calculadora:
    # Método que simula sobrecarga usando *args e **kwargs
    def soma(self, *args, **kwargs):
        # Se nenhum argumento foi passado
        if len(args) == 0 and len(kwargs) == 0:
            return "Nada a somar"

        # Somar os valores passados em args
        total_args = sum(args)

        # Somar os valores passados em kwargs
        total_kwargs = sum(kwargs.values())

        return total_args + total_kwargs

# Exemplo de uso
calc = Calculadora()

print(calc.soma(a=10, c=5))