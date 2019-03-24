## 5 Tamanho dos Componentes

#### Altura e Largura
A altura e largura de um componente determina seu tamanho em tela.

#### Dimensões Fixas
A maneira mais simples de determinar a dimensão de um componente é adicionar uma largura (**width**) e uma altura (**height**) fixos. Todas as dimensões no React Native são sem unidade e representam pixels independentes da densidade.


#### Exemplo:

```javascript
import React, { Component } from 'react';
import { View, StyleSheet } from 'react-native';

export default class DimensoesFixasBasicas extends Component {
  render() {
    return (
      <View>
        <View style={style.azulclaro}/>
        <View style={style.azulceleste}/>
        <View style={style.azulmetalico}/>
      </View>
    );
  }
}
const style = StyleSheet.create({
  azulclaro: {
    width: 50,
    height: 50,
    backgroundColor: 'powderblue'
  },
  azulceleste: {
    width: 100,
    height: 100,
    backgroundColor: 'skyblue'
  },
  azulmetalico:{
    width: 150,
    height: 150,
    backgroundColor: 'steelblue'
  },

});
```
Usando dimensões fixas, os componentes serão renderizados no tamanho definido, idependente da resolução da tela.

### Dimensões Flex
Use o **flex** no style de um componente para que ele expanda e adeque dinamicamente ao espaço disponível em tela. Normalmente usamos **flex: 1**. O espaço pode ser compartilhado mais de um elemento compartilham o mesmo pai. Quanto maior o **flex**, maior a proporção de espaço que um componente terá em relação aos seus irmãos.


*Um componente só poderá expandir e preencher o espaço disponível se seu pai possui dimensões maiores que 0. Se um pai não possui uma largura e altura fixas ou flex, o pai terá dimensões 0 e os filhos **flex** não serão visíveis.*

```javascript
import React, { Component } from 'react';
import { View, StyleSheet } from 'react-native';

export default class DimensoesFixasBasicas extends Component {
  render() {
    return (
      <View style={style.pai}>
        <View style={style.azulclaro}/>
        <View style={style.azulceleste}/>
        <View style={style.azulmetalico}/>
      </View>
    );
  }
}
const style = StyleSheet.create({
  pai: {
    flex: 1
  },
  azulclaro: {
    flex: 1,
    backgroundColor: 'powderblue'
  },
  azulceleste: {
    flex: 1,
    backgroundColor: 'skyblue'
  },
  azulmetalico:{
    flex: 1,
    backgroundColor: 'steelblue'
  },

});
```
Remova o `flex: 1` do pai. Perceba que seus filhos não possuem dimensões então não podem expandir.
E se substituir `flex: 1` por `height: 300`?

Depois de controlar o tamanho de um componente, o próximo passo é aprender como [colocá-lo na tela.](https://github.com/DiegoMagg/learning-process/blob/master/React-Native/Basico/6-FlexBoxLayout.md).
