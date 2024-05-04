from experta import *


class Dieta(Fact):
    """Información sobre la dieta."""
    pass


class SistemaExperto(KnowledgeEngine):
    @Rule(Dieta(objetivo="perder peso"),
          Dieta(actividad_fisica="si"),
          ~Dieta(problemas_medicos="si"))
    def dieta_para_perder_peso(self):
        print("Dieta para perder peso:")
        print("- Consumir más vegetales y proteínas magras.")
        print("- Limitar la ingesta de carbohidratos y grasas.")
        print("- Beber mucha agua y evitar bebidas azucaradas.")

    @Rule(Dieta(objetivo="mantener peso"),
          Dieta(actividad_fisica="no"),
          ~Dieta(problemas_medicos="si"))
    def dieta_para_mantener_peso_sedentario(self):
        print("Dieta para mantener peso (sedentario):")
        print("- Equilibrar la ingesta de carbohidratos, proteínas y grasas.")
        print("- Consumir porciones moderadas y evitar excesos.")
        print("- Incluir variedad de alimentos en la dieta.")

    @Rule(Dieta(objetivo="mantener peso"),
          Dieta(actividad_fisica="si"),
          ~Dieta(problemas_medicos="si"))      
    def dieta_para_mantener_peso_activo(self):
        print("Dieta para mantener peso (activo):")
        print("- Equilibrar la ingesta de carbohidratos, proteínas y grasas.")
        print("- Consumir porciones moderadas y evitar excesos.")
        print("- Incluir variedad de alimentos en la dieta.")

    @Rule(Dieta(objetivo="ganar peso"),
          Dieta(actividad_fisica="si"),
          ~Dieta(problemas_medicos="si"))
    def dieta_para_ganar_peso(self):
        print("Dieta para ganar peso:")
        print("- Aumentar la ingesta de calorías con alimentos nutritivos.")
        print("- Incluir carbohidratos complejos, proteínas y grasas saludables.")
        print("- Realizar comidas frecuentes y snacks nutritivos.")

    @Rule(Dieta(objetivo=OR("perder peso", "mantener peso", "ganar peso")),
          Dieta(actividad_fisica="no"),
          ~Dieta(problemas_medicos="si"))
    def dieta_para_sedentario(self):
        print("Dieta para una vida sedentaria:")
        print("- Controlar las porciones y evitar alimentos altos en calorías.")
        print("- Priorizar alimentos integrales y frescos.")
        print("- Limitar el consumo de alimentos procesados y azucarados.")

    @Rule()
    def default(self):
        print("Lo siento, no hay dietas disponibles para tus respuestas.")


if __name__ == "__main__":
    engine = SistemaExperto()
    engine.reset()
    engine.declare(Dieta(objetivo=input("1. ¿Cuál es tu objetivo del plan alimenticio? (Perder peso / Mantener peso / Ganar peso): ").lower(),
                        actividad_fisica=input("2. ¿Realizas alguna actividad física? (Sí / No): ").lower(),
                        problemas_medicos=input("3. ¿Sufres de algún problema médico? (Sí / No): ").lower(),
                        calorias=input("4. ¿Cuál es tu estimación de metabolismo y requisitos calóricos? (Bajo / Moderado / Alto): ").lower(),
                        restricciones=input("5. ¿Tienes preferencias alimenticias o restricciones específicas? (Vegetariano / Vegano / Sin restricciones): ").lower()))
    engine.run()
