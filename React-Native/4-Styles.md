### 4 Styles

Com o React Native, não precisamos usar uma linguagem especial para definir estilos. Só precisamos aplicar estilo usando JavaScript.
Todos os componentes centrais aceitam a prop **style**. Os nomes dos estilos e valores se assemelham ao CSS usado na web, exceto nomes como **background-color**, neste caso use **backgroundColor**.

A prop **style** pode ser um objeto JavaScript plano. Esta é a forma mais simples que usaremos para exemplificar. Podemos passar uma
lista de estilos, o último estilo da lista tem precedência, então podemos usar isto para herdar estilos. Como um componente cresce em complexidade é melhor usar o **StyleSheet.create** para definir os estilos somente em um local.

####Exemplo:
```javascript
import React, { Component } from 'react';
import { Text, View, StyleSheet } from 'react-native';

export default class MuitosEstilos extends Component {
  render() {
    return (
      <View>
        <Text style={styles.vermelho}>vermelho</Text>
        <Text style={styles.grandeAzul}>grandeAzul</Text>
        <Text style={[styles.grandeAzul, styles.vermelho]}>grandeAzul, e vermelho</Text>
        <Text style={[styles.vermelho, styles.grandeAzul]}>vermelho, e grandeAzul</Text>
      </View>
    );
  }
}
const styles = StyleSheet.create({
  grandeAzul: {
    color: 'blue',
    fontWeight: 'bold',
    fontSize: 30,
  },
  vermelho: {
    color: 'red',
  },
});
```
Note que em "grandeAzul e vermelho" e "vermelho e grandeAzul" a prop style recebe uma lista de estilos. Ambos possuem o estilo color mas, pela precedência da direita para esquerda, o primeiro elemento prevalece. Em "grandeAzul e vermelho", o color: 'red' vem primeiro que o color: 'blue' sendo assim a cor final será vermelho, em vermelho e grandeAzul ocorre o inverso.

Existem outras formas de estilização de texto que abordaremos mais a frente.

O próximo passo é controlar o [tamanho do componente](https://github.com/DiegoMagg/learning-process/blob/master/React-Native/Basico/5-Tamanho.md).
