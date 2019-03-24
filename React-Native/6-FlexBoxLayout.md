## 6 Layout com Flexbox

Um componente pode especificar o layout de seus filhos usando o algoritmo flexbox. O Flexbox foi projetado para fornecer um layout consistente em diferentes tamanhos de tela.

Normalmente, usando uma combinação de `flexDirection`, `alignItems` e `justifyContent` é o bastante para chegar ao layout pretendido.

Adicionando `flexDirection` ao estilo do componente determina o eixo primário do layout. Os filhos serão organizados horizontalmente (`row`) ou verticalmente (`column`)? O padrão é `column`.

```javascript
import React, { Component } from 'react';
import { AppRegistry, View, StyleSheet } from 'react-native';

export default class FlexDirecoesBasicas extends Component {
  render() {
    return (
      <View style={styles.pai}>
        <View style={styles.azulclaro} />
        <View style={styles.azulceleste} />
        <View style={styles.azulmetalico} />
      </View>
    );
  }
};

const styles = StyleSheet.create({
  pai: {
    flex: 1,
    flexDirection: 'row'
  },
  azulclaro: {
    width: 50,
    height: 50,
    backgroundColor: 'powderblue'
  },
  azulceleste: {
    width: 50,
    height: 50,
    backgroundColor: 'skyblue'
  },
  azulmetalico:{
    width: 50,
    height: 50,
    backgroundColor: 'steelblue'
  },
});



// skip this line if using Create React Native App
AppRegistry.registerComponent('Aprendendo', () => FlexDirecoesBasicas);
```
Experimente mudar o `flexDirection: ` para `column`.


### Justify Content
Adicionando `justifyContent` ao estilo do componente, determina a distribuição ao longo do primeiro eixo. Os elementos
filhos podem ser distribuídos no início, ao centro, ao fim ou mesmo espaçados? As opções disponíveis são: `flex-start`, `center`,`flex-end`, `space-around`, `space-between` and `space-evenly`.

```javascript
import React, { Component } from 'react';
import { AppRegistry, View, StyleSheet } from 'react-native';

export default class FlexDirecoesBasicas extends Component {
  render() {
    return (
      <View style={styles.pai}>
        <View style={styles.azulclaro} />
        <View style={styles.azulceleste} />
        <View style={styles.azulmetalico} />
      </View>
    );
  }
};

const styles = StyleSheet.create({
  pai: {
    flex: 1,
    flexDirection: 'column',
    justifyContent: 'space-between',
  },
  azulclaro: {
    width: 50,
    height: 50,
    backgroundColor: 'powderblue'
  },
  azulceleste: {
    width: 50,
    height: 50,
    backgroundColor: 'skyblue'
  },
  azulmetalico:{
    width: 50,
    height: 50,
    backgroundColor: 'steelblue'
  },
});
```
