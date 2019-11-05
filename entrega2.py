import itertools

from simpleai.search import (CspProblem, backtrack, min_conflicts,
                             MOST_CONSTRAINED_VARIABLE,
                             LEAST_CONSTRAINING_VALUE,
                             HIGHEST_DEGREE_VARIABLE)



def csp_conferencia():

    variables = ('TallerDjangoGirls', 'TallerIntroducciónaPython', 'KeynoteDiversidad', 'KeynoteCoreDeveloperPython', 
                'APIsDjango', 'Diseñodesistemas', 'UnitTestingPython', 'EditoresCódigoPython', 'MúsicaconPython', 
                'BuenVendedor', 'PythonAnálisisImágenes', 'PythonSatélites', 'LibPyPI', 'Pandas')
    
    aulasyhorarios = [['Aula Magna', 10], ['Aula Magna', 11], ['Aula Magna', 14], ['Aula Magna', 15], ['Aula Magna', 16], ['Aula Magna', 17],
                    ['Aula 42', 10], ['Aula 42', 11], ['Aula 42', 14], ['Aula 42', 15], ['Aula 42', 16], ['Aula 42', 17],
                    ['Laboratorio', 10], ['Laboratorio', 11], ['Laboratorio', 14], ['Laboratorio', 15], ['Laboratorio', 16], ['Laboratorio', 17]]

    domains = {taller: aulasyhorarios[:] for taller in variables}
    restricciones = []
    #Aula magna: capacidad para 200 personas, en la planta baja, y posee proyector y sistema de audio.
    #Aula 42: capacidad para 100 personas, en la planta alta, posee proyector pero no equipo de audio.
    #Laboratorio: capacidad para 50 personas, en la planta baja, no proyector ni equipo de audio, pero dispone de computadoras para los asistentes.

    #Deben cumplirse las siguientes restricciones:
    #Taller de Django Girls: requiere de computadoras, y se espera una asistencia de 40 personas.
    domains['TallerDjangoGirls'].remove(['Aula Magna', 10])
    domains['TallerDjangoGirls'].remove(['Aula Magna', 11])
    domains['TallerDjangoGirls'].remove(['Aula Magna', 14])
    domains['TallerDjangoGirls'].remove(['Aula Magna', 15])
    domains['TallerDjangoGirls'].remove(['Aula Magna', 16])
    domains['TallerDjangoGirls'].remove(['Aula Magna', 17])
    domains['TallerDjangoGirls'].remove(['Aula 42', 10])
    domains['TallerDjangoGirls'].remove(['Aula 42', 11])
    domains['TallerDjangoGirls'].remove(['Aula 42', 14])
    domains['TallerDjangoGirls'].remove(['Aula 42', 15])
    domains['TallerDjangoGirls'].remove(['Aula 42', 16])
    domains['TallerDjangoGirls'].remove(['Aula 42', 17])


    #Taller de introducción a Python: también requiere de computadoras, 
    #y debería darse por la mañana, para que los asistentes más novatos puedan aprovechar el resto de la conferencia.
    domains['TallerIntroducciónaPython'].remove(['Aula Magna', 10])
    domains['TallerIntroducciónaPython'].remove(['Aula Magna', 11])
    domains['TallerIntroducciónaPython'].remove(['Aula Magna', 14])
    domains['TallerIntroducciónaPython'].remove(['Aula Magna', 15])
    domains['TallerIntroducciónaPython'].remove(['Aula Magna', 16])
    domains['TallerIntroducciónaPython'].remove(['Aula Magna', 17])
    domains['TallerIntroducciónaPython'].remove(['Aula 42', 10])
    domains['TallerIntroducciónaPython'].remove(['Aula 42', 11])
    domains['TallerIntroducciónaPython'].remove(['Aula 42', 14])
    domains['TallerIntroducciónaPython'].remove(['Aula 42', 15])
    domains['TallerIntroducciónaPython'].remove(['Aula 42', 16])
    domains['TallerIntroducciónaPython'].remove(['Aula 42', 17])
    domains['TallerIntroducciónaPython'].remove(['Laboratorio', 14])
    domains['TallerIntroducciónaPython'].remove(['Laboratorio', 15])
    domains['TallerIntroducciónaPython'].remove(['Laboratorio', 16])
    domains['TallerIntroducciónaPython'].remove(['Laboratorio', 17])


    ##Cómo hacer APIs rest en Django: charla normal sin requerimientos de tamaño de sala ni horarios, pero requiere de proyector.
    domains['APIsDjango'].remove(['Laboratorio', 10])
    domains['APIsDjango'].remove(['Laboratorio', 11])
    domains['APIsDjango'].remove(['Laboratorio', 14])
    domains['APIsDjango'].remove(['Laboratorio', 15])
    domains['APIsDjango'].remove(['Laboratorio', 16])
    domains['APIsDjango'].remove(['Laboratorio', 17])

    ##Diseño de sistemas accesibles: charla normal, y el orador no puede subir por escaleras por una dificultad de salud,
    ##por lo que no puede ser en la planta alta.
    domains['Diseñodesistemas'].remove(['Aula 42', 10])
    domains['Diseñodesistemas'].remove(['Aula 42', 11])
    domains['Diseñodesistemas'].remove(['Aula 42', 14])
    domains['Diseñodesistemas'].remove(['Aula 42', 15])
    domains['Diseñodesistemas'].remove(['Aula 42', 16])
    domains['Diseñodesistemas'].remove(['Aula 42', 17])

    ##Cómo hacer unit testing en Python: charla normal, requiere proyector.
    domains['UnitTestingPython'].remove(['Laboratorio', 10])
    domains['UnitTestingPython'].remove(['Laboratorio', 11])
    domains['UnitTestingPython'].remove(['Laboratorio', 14])
    domains['UnitTestingPython'].remove(['Laboratorio', 15])
    domains['UnitTestingPython'].remove(['Laboratorio', 16])
    domains['UnitTestingPython'].remove(['Laboratorio', 17])

    ##Editores de código para Python: charla normal, requiere proyector y sistema de audio,
    ##ya que el disertante no puede esforzar demasiado su voz.
    domains['EditoresCódigoPython'].remove(['Aula 42', 10])
    domains['EditoresCódigoPython'].remove(['Aula 42', 11])
    domains['EditoresCódigoPython'].remove(['Aula 42', 14])
    domains['EditoresCódigoPython'].remove(['Aula 42', 15])
    domains['EditoresCódigoPython'].remove(['Aula 42', 16])
    domains['EditoresCódigoPython'].remove(['Aula 42', 17])
    domains['EditoresCódigoPython'].remove(['Laboratorio', 10])
    domains['EditoresCódigoPython'].remove(['Laboratorio', 11])
    domains['EditoresCódigoPython'].remove(['Laboratorio', 14])
    domains['EditoresCódigoPython'].remove(['Laboratorio', 15])
    domains['EditoresCódigoPython'].remove(['Laboratorio', 16])
    domains['EditoresCódigoPython'].remove(['Laboratorio', 17])

    ##Cómo hacer música con Python: charla normal, requiere proyector,
    ##pero el orador es alguien famoso por lo que se espera bastante asistencia, más de 60 personas.
    domains['MúsicaconPython'].remove(['Laboratorio', 10])
    domains['MúsicaconPython'].remove(['Laboratorio', 11])
    domains['MúsicaconPython'].remove(['Laboratorio', 14])
    domains['MúsicaconPython'].remove(['Laboratorio', 15])
    domains['MúsicaconPython'].remove(['Laboratorio', 16])
    domains['MúsicaconPython'].remove(['Laboratorio', 17])

    ##Cómo ser un buen vendedor de software, negocios, contabilidad y mucho más:
    ##charla que no se espera que tenga mucha asistencia, por lo que no debería ocupar el aula magna.
    ##Además debe ser por la mañana, porque su orador solo vendrá en esos horarios para esta charla y luego se irá.
    domains['BuenVendedor'].remove(['Aula Magna', 10])
    domains['BuenVendedor'].remove(['Aula Magna', 11])
    domains['BuenVendedor'].remove(['Aula Magna', 14])
    domains['BuenVendedor'].remove(['Aula Magna', 15])
    domains['BuenVendedor'].remove(['Aula Magna', 16])
    domains['BuenVendedor'].remove(['Aula Magna', 17])
    domains['BuenVendedor'].remove(['Aula 42', 14])
    domains['BuenVendedor'].remove(['Aula 42', 15])
    domains['BuenVendedor'].remove(['Aula 42', 16])
    domains['BuenVendedor'].remove(['Aula 42', 17])
    domains['BuenVendedor'].remove(['Laboratorio', 14])
    domains['BuenVendedor'].remove(['Laboratorio', 15])
    domains['BuenVendedor'].remove(['Laboratorio', 16])
    domains['BuenVendedor'].remove(['Laboratorio', 17])

    ##Python para análisis de imágenes: charla normal pero con una demo interactiva que
    ##requiere que el público esté bien visible, por lo que no puede darse en el laboratorio.
    domains['PythonAnálisisImágenes'].remove(['Laboratorio', 10])
    domains['PythonAnálisisImágenes'].remove(['Laboratorio', 11])
    domains['PythonAnálisisImágenes'].remove(['Laboratorio', 14])
    domains['PythonAnálisisImágenes'].remove(['Laboratorio', 15])
    domains['PythonAnálisisImágenes'].remove(['Laboratorio', 16])
    domains['PythonAnálisisImágenes'].remove(['Laboratorio', 17])

    ##Python para satélites espaciales: charla normal que requiere proyector, y darse por la tarde,
    ##porque su orador no funciona bien de mañana.
    domains['PythonSatélites'].remove(['Aula Magna', 10])
    domains['PythonSatélites'].remove(['Aula Magna', 11])
    domains['PythonSatélites'].remove(['Aula 42', 10])
    domains['PythonSatélites'].remove(['Aula 42', 11])
    domains['PythonSatélites'].remove(['Laboratorio', 10])
    domains['PythonSatélites'].remove(['Laboratorio', 11])
    domains['PythonSatélites'].remove(['Laboratorio', 14])
    domains['PythonSatélites'].remove(['Laboratorio', 15])
    domains['PythonSatélites'].remove(['Laboratorio', 16])
    domains['PythonSatélites'].remove(['Laboratorio', 17])

    ##Cómo publicar tu lib en PyPI: charla normal que requiere proyector.
    domains['LibPyPI'].remove(['Laboratorio', 10])
    domains['LibPyPI'].remove(['Laboratorio', 11])
    domains['LibPyPI'].remove(['Laboratorio', 14])
    domains['LibPyPI'].remove(['Laboratorio', 15])
    domains['LibPyPI'].remove(['Laboratorio', 16])
    domains['LibPyPI'].remove(['Laboratorio', 17])

    ##Introducción a Pandas para procesamiento de datos: charla normal con proyector,
    ##que por requerimientos de conexión a internet solo puede darse en la planta alta (la planta baja no posee conexión).
    domains['Pandas'].remove(['Aula Magna', 10])
    domains['Pandas'].remove(['Aula Magna', 11])
    domains['Pandas'].remove(['Aula Magna', 14])
    domains['Pandas'].remove(['Aula Magna', 15])
    domains['Pandas'].remove(['Aula Magna', 16])
    domains['Pandas'].remove(['Aula Magna', 17])
    domains['Pandas'].remove(['Laboratorio', 10])
    domains['Pandas'].remove(['Laboratorio', 11])
    domains['Pandas'].remove(['Laboratorio', 14])
    domains['Pandas'].remove(['Laboratorio', 15])
    domains['Pandas'].remove(['Laboratorio', 16])
    domains['Pandas'].remove(['Laboratorio', 17])

    ##    #Keynote sobre diversidad: al ser keynote se espera que la mayor parte de la conferencia asista, 
##    #por lo que se requiere un aula de al menos 150 personas, proyector y sistema de audio. 
##    #Debería ser dada por la tarde, para maximizar asistencia. Y no se deben dar otras charlas en el mismo horario que esta.

    domains['KeynoteDiversidad'].remove(['Aula Magna', 10])
    domains['KeynoteDiversidad'].remove(['Aula Magna', 11])
    domains['KeynoteDiversidad'].remove(['Aula 42', 10])
    domains['KeynoteDiversidad'].remove(['Aula 42', 11])
    domains['KeynoteDiversidad'].remove(['Aula 42', 14])
    domains['KeynoteDiversidad'].remove(['Aula 42', 15])
    domains['KeynoteDiversidad'].remove(['Aula 42', 16])
    domains['KeynoteDiversidad'].remove(['Aula 42', 17])
    domains['KeynoteDiversidad'].remove(['Laboratorio', 10])
    domains['KeynoteDiversidad'].remove(['Laboratorio', 11])
    domains['KeynoteDiversidad'].remove(['Laboratorio', 14])
    domains['KeynoteDiversidad'].remove(['Laboratorio', 15])
    domains['KeynoteDiversidad'].remove(['Laboratorio', 16])
    domains['KeynoteDiversidad'].remove(['Laboratorio', 17])
    domains['KeynoteCoreDeveloperPython'].remove(['Aula Magna', 10])
    domains['KeynoteCoreDeveloperPython'].remove(['Aula Magna', 11])
    domains['KeynoteCoreDeveloperPython'].remove(['Aula 42', 10])
    domains['KeynoteCoreDeveloperPython'].remove(['Aula 42', 11])
    domains['KeynoteCoreDeveloperPython'].remove(['Aula 42', 14])
    domains['KeynoteCoreDeveloperPython'].remove(['Aula 42', 15])
    domains['KeynoteCoreDeveloperPython'].remove(['Aula 42', 16])
    domains['KeynoteCoreDeveloperPython'].remove(['Aula 42', 17])
    domains['KeynoteCoreDeveloperPython'].remove(['Laboratorio', 10])
    domains['KeynoteCoreDeveloperPython'].remove(['Laboratorio', 11])
    domains['KeynoteCoreDeveloperPython'].remove(['Laboratorio', 14])
    domains['KeynoteCoreDeveloperPython'].remove(['Laboratorio', 15])
    domains['KeynoteCoreDeveloperPython'].remove(['Laboratorio', 16])
    domains['KeynoteCoreDeveloperPython'].remove(['Laboratorio', 17])


    def Restriccion_Keys(variables, values):
        v1, v2 = values
        return v1[1] != v2[1]

    def AulaYHorarios_Distintos_Para_Todos(variables, values):
        v1, v2 = values
        return v1 != v2

    
    for var in variables:
        if var != 'KeynoteDiversidad':
            restricciones.append((('KeynoteDiversidad', var), Restriccion_Keys))
        if var != 'KeynoteCoreDeveloperPython':
            restricciones.append((('KeynoteCoreDeveloperPython', var), Restriccion_Keys))

    for var1, var2 in itertools.combinations(variables, 2):
        restricciones.append(((var1, var2), AulaYHorarios_Distintos_Para_Todos))
        
    
    
    ##Keynote sobre cómo ser core developer de Python: al igual que la keynote anterior,
    ##debería ser por la tarde y en un aula con capacidad de al menos 150 personas, proyector y sistema de audio.
    ##Y no se deben dar otras charlas en el mismo horario que esta.
    
    
    #problem = CspProblem(variables, domains, restricciones)
    #result = backtrack(problem, variable_heuristic=MOST_CONSTRAINED_VARIABLE, value_heuristic=LEAST_CONSTRAINING_VALUE, inference=True)
    #result = min_conflicts(problem, iterations_limit=100)
    #Para pruebas sin "resolver" poner "result" en return
    return CspProblem(variables, domains, restricciones)

def resolver(metodo_busqueda, iteraciones):
    problema = csp_conferencia()

    if metodo_busqueda == "backtrack":
        resultado = backtrack(problema)
        #resultado = backtrack(problema, variable_heuristic=MOST_CONSTRAINED_VARIABLE, value_heuristic=LEAST_CONSTRAINING_VALUE)
        
    elif metodo_busqueda == "min_conflicts":    
        resultado = min_conflicts(problema, iterations_limit=iteraciones)

    return resultado

##if __name__ == '__main__':    
##    result = csp_conferencia()
##    print(result)
