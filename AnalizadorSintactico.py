from prettytable import PrettyTable

class AnalizadorSintactico:

    def __init__(self,tokens : list) -> None:
        self.errores = []
        self.tokens = tokens

    def agregarError(self,esperado,obtenido):
        self.errores.append(
            '''ERROR SINTÁCTICO: se obtuvo {} se esperaba {}'''.format(obtenido,esperado)
        )

    def sacarToken(self):
        ''' Saca el primer token y lo quita de la lista'''
        try:
            return self.tokens.pop(0)
        except:
            return None

    def observarToken(self):
        ''' Saca el primer token y lo mete de nuevo en de la lista'''
        try:
            return self.tokens[0]
        except:
            return None

    
    def analizar(self):
        self.S()

    def S(self):
        self.INICIO()

    def INICIO(self):
        temp = self.observarToken()
        if temp is None:
            self.agregarError('reservada_CrearBD | reservada_ElmiminarBD | reservada_CrearColeccion | reservada_EliminarColeccion | InsertarUnico | reservada_ActualizarUnico | reservada_EliminarUnico | reservada_BuscarTodo | reservada_BuscarUnico','EOF') 

        if temp.tipo == 'reservada_CrearBD':
            self.CREARBD()
        if temp.tipo == 'reservada_EliminarBD':
            self.ELIMINARBD()
        if temp.tipo == 'reservada_CrearColeccion':
            self.CREARCOLECCION()               
        if temp.tipo == 'reservada_EliminarColeccion':
            self.ELIMINARCOLECCION()
        if temp.tipo == 'reservada_InsertarUnico':
            self.INSERTARUNICO()
        if temp.tipo == 'reservada_ActualizarUnico':
            self.ACTUALIZARUNICO()
        if temp.tipo == 'reservada_EliminarUnico':
            self.ELIMINARUNICO()
        if temp.tipo == 'reservada_BuscarTodo':
            self.BUSCARTODO()
        if temp.tipo == 'reservada_BuscarUnico':
            self.BUSCARUNICO()
        else:
            self.agregarError('reservada_CrearBD | reservada_ElmiminarBD | reservada_CrearColeccion | reservada_EliminarColeccion | InsertarUnico | reservada_ActualizarUnico | reservada_EliminarUnico | reservada_BuscarTodo | reservada_BuscarUnico',temp.tipo) 

    def CREARBD(self):
        token = self.sacarToken()
        if token.tipo == 'reservada_CrearBD':
            token = self.sacarToken()
            if token is None:
                self.agregarError('identificador','EOF')
                return
            elif token.tipo ==  'identificador':
                token = self.sacarToken()

                if token is None:
                    self.agregarError('signoIgual','EOF')
                    return
                elif token.tipo == 'signoIgual':
                    token = self.sacarToken()

                    if token is None:
                        self.agregarError('identificador','EOF')
                        return
                    elif token.tipo == 'identificador':
                        token = self.sacarToken()

                        if token is None:
                            self.agregarError('reservada_CrearBD','EOF')
                            return
                        elif token.tipo == 'reservada_CrearBD':
                            token = self.sacarToken()

                            if token is None:
                                self.agregarError('parentesisIzquierdo','EOF')
                            elif token.tipo == 'parentesisIzquierdo':
                                token = self.sacarToken()

                                if token is None:
                                    self.agregarError('parentesisDerecho','EOF')
                                    return    
                                elif token.tipo == 'parentesisDerecho':
                                    token = self.sacarToken()

                                    if token is None:
                                        self.agregarError('puntoYComa','EOF')
                                        return
                                    elif token.tipo == 'puntoYComa':
                                        token = self.sacarToken()
                                    else:
                                        self.agregarError('puntoYComa',token.tipo)
                                        print('Error falta punto y coma')    

                                else:
                                    self.agregarError('parentesisDerecho',token.tipo)
                                    print('Error falta parentesis Derecho')
                            else:
                                self.agregarError('parentesisIzquierdo',token.tipo)
                                print('Error falta parentesis Izquierdo')
                        else:
                            self.agregarError('reservada_CrearBD',token.tipo)
                            print('Error falta reservada CrearBD')
                    else:
                        self.agregarError('identificador',token.tipo)
                        print('Error falta identificador')
                else:
                    self.agregarError('signoIgual',token.tipo)
                    print('Error falta signo igual')
            else:
                self.agregarError('identificador',token.tipo)
                print('Error falta identificador')
        else:
            self.agregarError('reservada_CrearBD','EOF')
            print('Error')
            

    def ELIMINARBD(self):
        temp = self.sacarToken()
        if temp is None:
            self.agregarError('reservada_EliminarBD','EOF') 
        if temp.tipo == 'reservada_EliminarBD':
            temp = self.sacarToken()
            if temp is None:
                self.agregarError('identificador','EOF') 
            if temp.tipo == 'identificador':
                temp = self.sacarToken()
                if temp is None:
                    self.agregarError('simbolo_punto_coma','EOF') 
                if temp.tipo == 'simbolo_punto_coma':
                    self.INICIO()
                else:
                    self.agregarError('simbolo_punto_coma',temp.tipo) 
            else:
                self.agregarError('identificador',temp.tipo) 
        else:
            self.agregarError('reservada_EliminarBD',temp.tipo)        

    def imprimirErrores(self):
        '''Imprime una tabla con los errores'''
        '''x = PrettyTable()
        x.field_names = ["Descripcion"]
        for error_ in self.errores:
            x.add_row([error_])
        print(x)           '''