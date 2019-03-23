# React Native
Este é um repositório de aprendizado. O material a seguir foi retirado e traduzido da documentação oficial do React-Native, disponível em:
https://facebook.github.io/react-native/docs/tutorial



### Introdução
O react-native é como o react porém, usa os componentes nativos, e componentes web como construtor de blocos. Para entender as estutura básica de um app react-native, você precisa entender alguns conceitos básicos do react, como o JSX, components, **state** e **props**.

#### Hello World
Seguindo as tradições, primeiro vamos criar um app que diga "Hello, world".

```javascript

import React, { Component } from 'react';
import {Text, View, StyleSheet} from 'react-native';

export default class HelloWorldApp extends Component {
  render(){
    return(
      <View style={styles.main_text}>
        <Text>Hello world!</Text>
      </View>
    )
  }
}

const styles = StyleSheet.create({
  main_text: {
    flex: 1,
    justifyContent: "center",
    alignItems: 'center',
  }
});

```

Note as tags <View><Text>, esta é a sintaxe do JSX, que é uma mistura entre XML e JavaScript. Muitos frameworks, injetam código dentro de uma linguagem markup. No react é o contrário. O JSX permite que você escreva seu markup dentro do código. As tags se asemelham
ao HTML, so que ao invés de tags HTML como < div > ou < span > você usa componentes do react, neste caso, <View> e <Text>.

### Componentes
O código acima está definindo o <i>HelloWorldApp</i> como um novo componente. Quando está criano um app React Native, você fará muitos componentes. Tudo que verá na tela, é um tipo de componente que precisa de um método <i>render</i> que retorna JSX para renderizar.
