from experta import *
import os


def limpiar_pantalla():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


class Dieta(Fact):
    """Información sobre la dieta."""
    pass


class SistemaExperto(KnowledgeEngine):
    #------------------Dietas sin problemas medicos / ACTIVIDAD FISIFCA = SI----------------------------------
    @Rule(Dieta(objetivo="perder peso"),
      Dieta(actividad_fisica="si"),
      Dieta(problemas_medicos="no"),
      Dieta(embarazo="no"))
    def dieta_para_perder_peso_activo(self):
        limpiar_pantalla()
        print("Dieta para perder peso (activo):")
        print("\nLunes:")
        print("- Desayuno: Batido de frutas con yogur bajo en grasa.")
        print("- Almuerzo: Ensalada de espinacas, queso feta y nueces.")
        print("- Cena: Pechuga de pollo a la plancha con espárragos al vapor.")
        
        print("\nMartes:")
        print("- Desayuno: Avena cocida con trozos de manzana y canela.")
        print("- Almuerzo: Salmón al horno con brócoli al vapor.")
        print("- Cena: Ensalada de quinoa con vegetales asados.")
        
        print("\nMiércoles:")
        print("- Desayuno: Tortilla de claras de huevo con espinacas y tomates cherry.")
        print("- Almuerzo: Filete de pavo a la plancha con espárragos a la parrilla.")
        print("- Cena: Sopa de verduras con pollo desmenuzado.")
        
        print("\nJueves:")
        print("- Desayuno: Batido de proteínas con espinacas y plátano.")
        print("- Almuerzo: Ensalada de garbanzos, pepino y tomate con vinagreta de limón.")
        print("- Cena: Pescado al horno con espárragos y zanahorias al vapor.")
        
        print("\nViernes:")
        print("- Desayuno: Yogur griego con nueces y arándanos.")
        print("- Almuerzo: Tiras de pollo a la parrilla con ensalada de col.")
        print("- Cena: Berenjenas rellenas de carne magra y verduras.")
        
        print("\nSábado:")
        print("- Desayuno: Tostadas integrales con aguacate y huevo pochado.")
        print("- Almuerzo: Sopa de lentejas con verduras y un poco de queso parmesano.")
        print("- Cena: Brochetas de camarones con vegetales a la parrilla.")
        
        print("\nDomingo:")
        print("- Desayuno: Smoothie de espinacas, piña y jengibre.")
        print("- Almuerzo: Pollo al curry con arroz integral y verduras al vapor.")
        print("- Cena: Salmón a la plancha con espárragos y batata al horno.")



    @Rule(Dieta(objetivo="mantener peso"),
          Dieta(actividad_fisica="si"),
          Dieta(problemas_medicos="no"),
          Dieta(embarazo="no"))
    def dieta_para_mantener_peso_activo(self):
        limpiar_pantalla()
        print("Dieta para mantener peso (activo):")
        print("\nLunes:")
        print("- Desayuno: Tostadas integrales con aguacate y huevo revuelto.")
        print("- Almuerzo: Ensalada de quinoa con vegetales mixtos y aderezo de limón y aceite de oliva.")
        print("- Cena: Filete de salmón al horno con espárragos y batata asada.")

        print("\nMartes:")
        print("- Desayuno: Batido de proteínas con espinacas, plátano y leche de almendras.")
        print("- Almuerzo: Pollo a la parrilla con espárragos al vapor y una ensalada de tomate y pepino.")
        print("- Cena: Tacos de pescado con tortillas de maíz, repollo rallado y salsa de yogur.")

        print("\nMiércoles:")
        print("- Desayuno: Avena cocida con rodajas de manzana, canela y almendras.")
        print("- Almuerzo: Tiras de carne magra salteadas con pimientos y cebolla, servidas con arroz integral.")
        print("- Cena: Sopa de verduras con garbanzos y un trozo de pan integral.")

        print("\nJueves:")
        print("- Desayuno: Yogur griego con granola y frutos rojos.")
        print("- Almuerzo: Ensalada de lentejas con espinacas, tomate y aguacate.")
        print("- Cena: Pechuga de pollo al horno con brócoli al vapor y puré de papas.")

        print("\nViernes:")
        print("- Desayuno: Tostadas de pan integral con crema de cacahuate y plátano en rodajas.")
        print("- Almuerzo: Salmón al horno con espárragos y quinoa cocida.")
        print("- Cena: Ensalada de garbanzos con tomate, pepino, cebolla morada y aderezo de tahini.")

        print("\nSábado:")
        print("- Desayuno: Tortilla de claras de huevo con espinacas y champiñones.")
        print("- Almuerzo: Pollo al curry con arroz basmati y verduras al vapor.")
        print("- Cena: Rollitos de sushi con relleno de salmón, aguacate y pepino.")

        print("\nDomingo:")
        print("- Desayuno: Smoothie de frutas con espinacas y semillas de chía.")
        print("- Almuerzo: Hamburguesas de pavo a la parrilla con ensalada verde y papas asadas.")
        print("- Cena: Pasta integral con salsa de tomate casera y albóndigas de carne magra.")

    @Rule(Dieta(objetivo="perder peso"),
      Dieta(actividad_fisica="no"),
      Dieta(problemas_medicos="no"),
      Dieta(embarazo="no"))
    def dieta_para_sedentario(self):
        limpiar_pantalla()
        print("Dieta para una vida sedentaria [Perder peso]:")
        print("\nLunes:")
        print("- Desayuno: Té verde con tostadas integrales y aguacate.")
        print("- Almuerzo: Ensalada de espinacas, tomate y pechuga de pollo a la plancha.")
        print("- Cena: Sopa de verduras con un trozo de pan integral.")

        print("\nMartes:")
        print("- Desayuno: Yogur natural con granola y frutos rojos.")
        print("- Almuerzo: Salmón al horno con brócoli al vapor.")
        print("- Cena: Ensalada de garbanzos con tomate, pepino y aderezo de limón.")

        print("\nMiércoles:")
        print("- Desayuno: Batido de frutas con espinacas.")
        print("- Almuerzo: Pavo al horno con ensalada verde.")
        print("- Cena: Tortilla de claras con champiñones y espinacas.")

        print("\nJueves:")
        print("- Desayuno: Avena cocida con rodajas de manzana y canela.")
        print("- Almuerzo: Ensalada de quinoa con vegetales asados.")
        print("- Cena: Pechuga de pollo a la plancha con espárragos.")

        print("\nViernes:")
        print("- Desayuno: Tostadas integrales con mantequilla de almendras y plátano en rodajas.")
        print("- Almuerzo: Atún al natural con ensalada de tomate y aguacate.")
        print("- Cena: Berenjenas al horno con queso fresco.")

        print("\nSábado:")
        print("- Desayuno: Smoothie de bayas con espinacas.")
        print("- Almuerzo: Lentejas estofadas con verduras.")
        print("- Cena: Ensalada de salmón ahumado con aguacate y pepino.")

        print("\nDomingo:")
        print("- Desayuno: Té de hierbas con tostadas integrales y mermelada sin azúcar añadido.")
        print("- Almuerzo: Pollo a la parrilla con espárragos al vapor.")
        print("- Cena: Crema de calabaza con un trozo de pan integral.")

    @Rule(Dieta(objetivo="mantener peso"),
          Dieta(actividad_fisica="no"),
          Dieta(problemas_medicos="no"),
          Dieta(embarazo="no"))
    def dieta_para_sedentario_mantenerpeso(self):
        limpiar_pantalla()
        print("Dieta para una vida sedentaria: [mantener peso]")
        print("- Controlar las porciones y evitar alimentos altos en calorías.")
        print("- Priorizar alimentos integrales y frescos.")
        print("- Limitar el consumo de alimentos procesados y azucarados.")  


    @Rule(Dieta(objetivo="ganar peso"),
      Dieta(actividad_fisica="no"),
      Dieta(problemas_medicos="no"),
      Dieta(embarazo="no"))
    def dieta_para_sedentario_ganarpeso(self):
        limpiar_pantalla()
        print("Dieta para una vida sedentaria: [ganar peso]")
        print("- Controlar las porciones y evitar alimentos altos en calorías.")
        print("- Priorizar alimentos integrales y frescos.")
        print("- Limitar el consumo de alimentos procesados y azucarados.")    



    #--------------------Fin dietas sin problemas medicos---------------------------------

    #------------------Dietas con problemas medicos / ACTIVIDAD FISIFCA = SI--------------------------------------
    @Rule(Dieta(objetivo="ganar peso"),
          Dieta(actividad_fisica="si"),
          Dieta(problemas_medicos="si"),
          Dieta(embarazo="no"))
    def dieta_para_ganar_peso(self):
        limpiar_pantalla()
        print("Dieta para ganar peso: [Problemas medicos]")
        print("- Aumentar la ingesta de calorías con alimentos nutritivos.")
        print("- Incluir carbohidratos complejos, proteínas y grasas saludables.")
        print("- Realizar comidas frecuentes y snacks nutritivos.")

    @Rule(Dieta(objetivo="perder peso"),
          Dieta(actividad_fisica="si"),
          Dieta(problemas_medicos="si"),
          Dieta(embarazo="no"))
    def dieta_para_perder_peso(self):
        limpiar_pantalla()
        print("Dieta para perder peso: [Problemas medicos]")
        print("- Aumentar la ingesta de calorías con alimentos nutritivos.")
        print("- Incluir carbohidratos complejos, proteínas y grasas saludables.")
        print("- Realizar comidas frecuentes y snacks nutritivos.")

    @Rule(Dieta(objetivo="mantener peso"),
          Dieta(actividad_fisica="si"),
          Dieta(problemas_medicos="si"),
          Dieta(embarazo="no"))
    def dieta_para_mantener_peso(self):
        limpiar_pantalla()
        print("Dieta para mantener peso: [Problemas medicos]")
        print("- Aumentar la ingesta de calorías con alimentos nutritivos.")
        print("- Incluir carbohidratos complejos, proteínas y grasas saludables.")
        print("- Realizar comidas frecuentes y snacks nutritivos.")

    @Rule(Dieta(objetivo="perder peso"),
          Dieta(actividad_fisica="no"),
          Dieta(problemas_medicos="si"),
          Dieta(embarazo="no"))
    def dieta_para_sedentario_medico(self):
        limpiar_pantalla()
        print("Dieta para una vida sedentaria: [ Perder Peso -Problemas medicos]")
        print("- Controlar las porciones y evitar alimentos altos en calorías.")
        print("- Priorizar alimentos integrales y frescos.")
        print("- Limitar el consumo de alimentos procesados y azucarados.")

    @Rule(Dieta(objetivo="mantener peso"),
          Dieta(actividad_fisica="no"),
          Dieta(problemas_medicos="si"),
          Dieta(embarazo="no"))
    def dieta_para_sedentario_medico_mantenerpeso(self):
        limpiar_pantalla()
        print("Dieta para una vida sedentaria: [ Mantener Peso -Problemas medicos]")
        print("- Controlar las porciones y evitar alimentos altos en calorías.")
        print("- Priorizar alimentos integrales y frescos.")
        print("- Limitar el consumo de alimentos procesados y azucarados.") 

    @Rule(Dieta(objetivo="ganar peso"),
          Dieta(actividad_fisica="no"),
          Dieta(problemas_medicos="si"),
          Dieta(embarazo="no"))
    def dieta_para_sedentario_medico_mantenerpeso(self):
        limpiar_pantalla()
        print("Dieta para una vida sedentaria: [ Ganar Peso -Problemas medicos]")
        print("- Controlar las porciones y evitar alimentos altos en calorías.")
        print("- Priorizar alimentos integrales y frescos.")
        print("- Limitar el consumo de alimentos procesados y azucarados.")       

    #--------------------Fin dietas con problemas medicos---------------------------------
    #------------------Dietas Embarazo ----------------------------------------------------
    @Rule(Dieta(objetivo="salud"),
          Dieta(actividad_fisica="si"),
          Dieta(problemas_medicos="no"),
          Dieta(embarazo="si"))
    def dieta_para_embarazo(self):
        limpiar_pantalla()
        print("Dieta para embarazo ")
        print("- Controlar las porciones y evitar alimentos altos en calorías.")
        print("- Priorizar alimentos integrales y frescos.")
        print("- Limitar el consumo de alimentos procesados y azucarados.")

    @Rule(Dieta(objetivo="salud"),
          Dieta(actividad_fisica="no"),
          Dieta(problemas_medicos="no"),
          Dieta(embarazo="si"))
    def dieta_para_embarazo_sedentaria(self):
        limpiar_pantalla()
        print("Dieta para embarazo [sedentaria]")
        print("- Controlar las porciones y evitar alimentos altos en calorías.")
        print("- Priorizar alimentos integrales y frescos.")
        print("- Limitar el consumo de alimentos procesados y azucarados.")    
    #---------------------PROBLEMAS MEDICOS-----------------------
    @Rule(Dieta(objetivo="salud"),
          Dieta(actividad_fisica="si"),
          Dieta(problemas_medicos="si"),
          Dieta(embarazo="si"))
    def dieta_para_embarazo_medico_fisico(self):
        limpiar_pantalla()
        print("Dieta para embarazo [Problemas medicos - Actividad fisica] ")
        print("- Controlar las porciones y evitar alimentos altos en calorías.")
        print("- Priorizar alimentos integrales y frescos.")
        print("- Limitar el consumo de alimentos procesados y azucarados.")    

    @Rule(Dieta(objetivo="salud"),
          Dieta(actividad_fisica="no"),
          Dieta(problemas_medicos="si"),
          Dieta(embarazo="si"))
    def dieta_para_embarazo_nofisico_medico(self):
        limpiar_pantalla()
        print("Dieta para embarazo [Problemas medicos - sedentaria] ")
        print("- Controlar las porciones y evitar alimentos altos en calorías.")
        print("- Priorizar alimentos integrales y frescos.")
        print("- Limitar el consumo de alimentos procesados y azucarados.")

    #------------------Fin Dietas Embarazo ----------------------------------------------------

    # Define la regla default
@Rule(AS.f1 << Dieta(objetivo=MATCH.o),
      AS.f2 << Dieta(actividad_fisica=MATCH.af),
      AS.f3 << Dieta(problemas_medicos=MATCH.pm),
      AS.f4 << Dieta(embarazo=MATCH.e))
def default(self, f1, f2, f3, f4, o, af, pm, e):
    if (o, af, pm, e) not in [(p, "si", "no", "no"), (p, "no", "no", "no")]:
        print("Lo siento, no hay dietas disponibles para tus respuestas.")



if __name__ == "__main__":
    engine = SistemaExperto()
    engine.reset()
    is_correct = False
    while not is_correct:
        objetivo = input("1. ¿Cuál es tu objetivo del plan alimenticio? (perder peso / mantener peso / ganar peso / salud): ").lower()
        actividad_fisica = input("2. ¿Realizas alguna actividad física? (Si / No): ").lower()
        problemas_medicos = input("3. ¿Sufres de algún problema médico? (Si / No): ").lower()
        embarazo = input("4. ¿Te encuentras en etapa de gestación? (si / No): ").lower()

        if objetivo in ["perder peso", "mantener peso", "ganar peso", "salud"]:
            if actividad_fisica in ["si", "no"]:
                if problemas_medicos in ["si", "no"]:
                    if embarazo in ["si", "no"]:
                        is_correct = True
                    else:
                        print("Respuesta incorrecta para la pregunta 4.")
                else:
                    print("Respuesta incorrecta para la pregunta 3.")
            else:
                print("Respuesta incorrecta para la pregunta 2.")
        else:
            print("Respuesta incorrecta para la pregunta 1.")

        if not is_correct:
            print("Por favor, ingresa respuestas válidas.\n")
            input()
            limpiar_pantalla()

    engine.declare(Dieta(objetivo=objetivo, actividad_fisica=actividad_fisica, problemas_medicos=problemas_medicos, embarazo=embarazo))
    print("[---------------------------------------------------------------------------------------------------------]")
    engine.run()
