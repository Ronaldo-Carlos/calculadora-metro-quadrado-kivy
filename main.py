from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class CalculadoraValorM2(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10

        # Labels e entradas para largura, comprimento, custo e frete
        self.largura_input = self.criar_input("Largura do material (m):")
        self.comprimento_input = self.criar_input("Comprimento do material (m):")
        self.custo_input = self.criar_input("Custo do material (R$):")
        self.frete_input = self.criar_input("Valor do frete (R$):")

        # Contêiner horizontal para os botões
        button_layout = BoxLayout(size_hint=(1, 0.2), spacing=10)

        # Botão para calcular o valor do m²
        calcular_button = Button(text="CALCULAR", size_hint=(0.5, 1))
        calcular_button.bind(on_press=self.calcular_valor_m2)
        button_layout.add_widget(calcular_button)

        # Botão para limpar os campos
        limpar_button = Button(text="LIMPAR", size_hint=(0.5, 1), background_color=(1, 0, 0, 1))
        limpar_button.bind(on_press=self.limpar_campos)
        button_layout.add_widget(limpar_button)

        self.add_widget(button_layout)

        # Label para exibir o resultado
        self.resultado_label = Label(text="", size_hint=(1, 0.3))
        self.add_widget(self.resultado_label)

    def criar_input(self, texto):
        layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))
        label = Label(text=texto, size_hint=(0.6, 1), color=(1, 1, 1, 1))
        text_input = TextInput(multiline=False, size_hint=(0.4, 1),
                               background_color=(0.1, 0.1, 0.1, 1), foreground_color=(1, 1, 1, 1))
        layout.add_widget(label)
        layout.add_widget(text_input)
        self.add_widget(layout)
        return text_input

    def calcular_valor_m2(self, instance):
        try:
            # Substitui a vírgula por ponto para conversão correta
            largura = float(self.largura_input.text.replace(',', '.'))
            comprimento = float(self.comprimento_input.text.replace(',', '.'))
            custo = float(self.custo_input.text.replace(',', '.'))
            frete = float(self.frete_input.text.replace(',', '.'))

            # Calcula a área total do rolo em m²
            area_total = largura * comprimento

            # Calcula o custo total incluindo o frete
            custo_total = custo + frete

            # Calcula o valor do m²
            valor_m2 = custo_total / area_total

            # Exibe o resultado
            self.resultado_label.text = f"O valor do m² do material é: R${valor_m2:.2f}"
        except ValueError:
            self.mostrar_erro("Por favor, insira valores numéricos válidos.")

    def limpar_campos(self, instance):
        # Limpa os campos de entrada e o resultado
        self.largura_input.text = ""
        self.comprimento_input.text = ""
        self.custo_input.text = ""
        self.frete_input.text = ""
        self.resultado_label.text = ""

    def mostrar_erro(self, mensagem):
        popup = Popup(title='Erro', content=Label(text=mensagem), size_hint=(0.8, 0.4))
        popup.open()

class CalculadoraApp(App):
    def build(self):
        self.title = "Calculadora de Valor por m²"
        return CalculadoraValorM2()

if __name__ == '__main__':
    CalculadoraApp().run()
