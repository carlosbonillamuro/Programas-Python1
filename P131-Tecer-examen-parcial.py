import os
class Jugador:
    def __init__(self,nombre,añonac,sexo,becado,costo):
        
        self.nombre=nombre
        self.añonac=añonac
        self.sexo=sexo
        self.becado=becado
        self.costo=costo
        if becado=='Becado':
            self.total=0
        else:
            self.total=costo
        self.total   
    def __str__(self):
        return f'Nombre: {self.nombre:<25} AñoNac: {self.añonac:>3} Sexo: {self.sexo:>5}    Becado :{self.becado:>10}    Total :{self.total:>5}'

class Categoria:
    def __init__(self,cat,rango,costo):
        self.cat=cat
        self.rango=rango
        self.costo=costo
        self.categorias= list()
    
    def agregarJugador(self,jugador):
        self.categorias.append(jugador)
             
    def __str__(self):
        return f'Nombre: {self.cat:<20} Rango: {self.rango:<12} Costo: {self.costo:<20}'        
class Academia:
    def __init__(self,nombre,propietario,domicilio):
        self.nombre=nombre
        self.propietario=propietario
        self.domicilio=domicilio
        self.categorias =list()
    def agregarCategoria(self,categoria):
        self.categorias.append(categoria)
   
    def __str__(self):
        return f'Tienda -> [ Nombre:{self.nombre} Domicilio:{self.domicilio}, Propietario: {self.propietario} ]'

def main():  
    os.system('Cls')
    
# Crear Academia
    miacademia = Academia(nombre='Academia Santos Laguna',propietario='Francisco Nava',domicilio='Aguanaval 123, Hidráulica')
# Agregar Categorias a la Academia
    miacademia.agregarCategoria( Categoria(cat='Junior A',rango='2006/2007/2008',costo=1250) )
    miacademia.agregarCategoria( Categoria(cat='Junior B',rango='2009/2010/2011',costo=850) )
    miacademia.agregarCategoria( Categoria(cat='Pony A',rango='2012/2013/2014',costo=700) )

# Agregar costo a los jugadores

    miacademia.categorias[0].agregarJugador( Jugador(nombre='Alexander Lopez',añonac=2006,sexo ='Hombre',becado='Sin Beca',costo=1250) );
    miacademia.categorias[0].agregarJugador( Jugador(nombre='Uriel Puga',añonac=2007,sexo ='Hombre',becado='Becado',costo=1250) );
    miacademia.categorias[0].agregarJugador( Jugador(nombre='Alejandra Escalona',añonac=2008,sexo ='Mujer',becado='Sin Beca',costo=1250) );
    miacademia.categorias[1].agregarJugador( Jugador(nombre='Armando Santana',añonac=2009,sexo ='Hombre',becado='Sin Beca',costo=850) );
    miacademia.categorias[1].agregarJugador( Jugador(nombre='Daniel Mijares',añonac=2010,sexo ='Hombre',becado='Sin Beca',costo=850) );
    miacademia.categorias[1].agregarJugador( Jugador(nombre='Antonio Hernandez',añonac=2011,sexo ='Mujer',becado='Becado',costo=850) );
    miacademia.categorias[2].agregarJugador( Jugador(nombre='Andrea Solis',añonac=2012,sexo ='Mujer',becado='Becado',costo=700) );
    miacademia.categorias[2].agregarJugador( Jugador(nombre='Marissa Hernandez',añonac=2013,sexo ='Mujer',becado='Becado',costo=700) );
    miacademia.categorias[2].agregarJugador( Jugador(nombre='Diana Soto',añonac=2014,sexo ='Mujer',becado='Sin Beca',costo=700) );
# Reporte
    print(f'\nREPORTE DEL CLUB DEPORTIVO: \n\nNombre: {miacademia.nombre}\nPropietario: {miacademia.propietario}\nDomicilio: {miacademia.domicilio}\n')
    print(f'Total de categorias : {len(miacademia.categorias)}')
    
    hombre=0
    mujer=0
    for categoria in miacademia.categorias:
    
        for jugador in categoria.categorias:
            if jugador.sexo == 'Hombre':
               hombre=hombre+1
            elif jugador.sexo=='Mujer':
                mujer=mujer+1   
    print('Total de Hombres:  ',hombre)
    print('Total de Mujeres:  ',mujer)
    
    print('\n>> Datos generales de las Categorias\n')
    for categoria in miacademia.categorias:
        print(f'{categoria}')
    print('\n>> Jugadores por Categoria:')
    totalfin=0
    for categoria in miacademia.categorias:
        print(f'\n> {categoria.cat}  -  {categoria.rango}  -  3\n')
        total=0
        for jugador in categoria.categorias:
            print(f' {jugador}')
            total=total+jugador.total
        totalfin=totalfin+total    
        print(f'\n- Subtotal : {total:,.2f}')    
    print(f'\n->Total : {totalfin:,.2f}')

# Programa principal
if __name__ == '__main__':
    main()