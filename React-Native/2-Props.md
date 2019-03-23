### 2 Props

A maioria dos componentes podem ser personalizados no momento que são criados, com diferentes parâmetros. Esses parâmetros de criação são chamados de **props**.
Um exemplo de componente básico do React Native é o <Image>. Quando você cria uma imagem, você pode usar um objeto chamado **source** para controlar qual imagem será exibida.


```javascript
import React, { Component } from 'react';
import { Image, StyleSheets } from 'react-native';

export default class Bananas extends Component {
  render() {
    let pic = {
      uri: 'https://upload.wikimedia.org/wikipedia/commons/d/de/Bananavarieties.jpg'
    };
    return (
      <Image source={pic} style={style.image}/>
    );
  }
}

const style = StyleSheet.create({
  image: {
      flex: 1,
  }
});
```
Note que as chaves em **{pic}** estão adicionando a variável **pic** ao **JSX**. Você pode adicionar qualquer expressão JavaScript dentro de chaves no **JSX**.
Seus próprios componentes podem receber **props**. Isto permite que um componente possa ser reutilizável em outras partes do seu app, com diferentes propriedades. Refira ao **this.props** no método render.

Exemplo:

```javascript
import React, { Component } from 'react';
import { Text, View, StyleSheet } from 'react-native';

class Ola extends Component {
  render() {
    return (
      <View style={{alignItems: 'center'}}>
        <Text>Olá {this.props.nome}!</Text>
      </View>
    );
  }
}
export default class variosOlas extends Component {
  render() {
    return (
      <View style={style.greetings}>
        <Ola nome='Aline' />
        <Ola nome='Pablo' />
        <Ola nome='Diego' />
      </View>
    );
  }
}
const style = StyleSheet.create({
  greetings: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  }
});
```

Usando *nome* como prop, nos permite customizar o componente **Ola**. Neste caso, reautilizamos o componente para cada olá. Este exemplo usa o componente 'Ola' no JSX como se fosse um componente já existente. Isso que faz o React ser tão legal, se em algum momento desejar ter mais elementos de UI para trabalhar, é só criar.

Note que nos exemplos exitem customizações de estilo (prop **style** da tag <View>) muito similar ao css. Outra forma de definir o estilo é definindo a **prop** dentro da tag, ex: <View style={{flex: 1, justifyContent: 'center'}}></View> O <View> é util como container para outros componentes, controlando e estilo e layout.

Com **props**, e os componentes básicos <Text>, <Image> e <View> é possível criar uma variedade de telas. Para saber como fazer seu aplicativo mudar ao longo do tempo, vamos aprender [states](https://github.com/DiegoMagg/learning-process/tree/master/React-Native/states).
