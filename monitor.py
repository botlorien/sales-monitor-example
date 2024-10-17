from typing import List, Tuple

class SalesMonitor:
    _sales:List[tuple]


    def __init__(self):
        self._sales = []

    @property
    def sales(self):
        return self._sales
    
    def __repr__(self):
        return f'SalesMonitor({self.sales})'

    def add_sale(self, sale:tuple):
        template = (int,str,int,float)
        if isinstance(sale, tuple) and len(sale) == len(template) and tuple(type(s) for s in sale) == template:
            self._sales.append(sale)
        else:
            raise ValueError(
                f"""Invalid sale format {tuple(type(s) for s in sale)}. Expected: {template}"""
            )
            

    def total_sales(self):
        return sum(quantity * unit_price for _, _, quantity, unit_price in self.sales)

    def report_products(self, *product_names):
        return (sale for sale in self.sales if sale[1] in product_names)
    
if __name__=='__main__':
    # Criando uma instância da classe SalesMonitor
    monitor = SalesMonitor()

    # Adicionando vendas
    monitor.add_sale((1, 'Laptop', 2, 1500.00))
    monitor.add_sale((2, 'Mouse', 5, 25.50))
    monitor.add_sale((3, 'Keyboard', 3, 99.99))
    monitor.add_sale((4, 'Laptop', 1, 1500.00))

    # Calculando o total de vendas
    print(f'Total de Vendas: {monitor.total_sales()}')

    # Relatório apenas de laptops e mouses
    laptop_mouse_sales = monitor.report_products('Laptop', 'Mouse')
    print(f'Laptops e Mouses vendidos: {list(laptop_mouse_sales)}')

