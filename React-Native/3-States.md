### 3 States

Existem dois tipos de dados que controlam um componente: **props** e **state**. **props** são definidos pelo pai e são fixados durante o tempo de vida de um componente. Em mudanças de dados, usaremos o **state**.

De modo geral, devemos iniciar um **state** no construtor, e então chamar um **setState** quando quiser muda-lo.

Como exemplo, vamos utilizar um texto que pisque todo o tempo. O texto em si é definido assim que componente é criado, assim o texto em si é um prop.


```javascript
import React, { Component } from 'react';
import {Text, View, StyleSheet } from 'react-native';

class Pisca extends Component {
  constructor(props) {
    super(props);
    this.state = { mostraTexto: true };

    setInterval(() => (
      this.setState(previousState => (
        { mostraTexto: !previousState.mostraTexto }
      ))
    ), 2000);
  }

  render() {
    if (!this.state.mostraTexto) {
      return null;
    }

    return (
      <Text>{this.props.text}</Text>
    );
  }
}

export default class PiscaApp extends Component {
  render() {
    return (
      <View style={style.estilo}>
        <Pisca text='Eu gosto de piscar' />
        <Pisca text='Sim, piscar é legal' />
        <Pisca text='Por que tiraram isso do HTML?' />
        <Pisca text='Me olha, me olha!' />
      </View>
    );
  }
}

const style = StyleSheet.create({
  estilo: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  }
});
```
Eu uma aplicação real, provavelmente o intervalo não será por tempo, e sim em situações como um novo dado no servidor, ou uma entrada de usuário. Você poderá usar um container de estado como o Redux ou Mobx para controlar seu fluxo de dados. Neste caso use o Redux ou Mobx para modificar seus estado além de chamar o **setState** diretamente.

Quando o setState é chamado, o PiscaApp terá seu componente re-renderizado. Neste ponto você deve estar cansado de ver tanto preto no branco. Hora de deixar as coisas mais bonitas. Vamos aprender sobre [estilos](https://github.com/DiegoMagg/learning-process/tree/master/React-Native/estilos).
