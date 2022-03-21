import React, { useState } from 'react';
import {
  Alert,
  Modal,
  StyleSheet,
  Text,
  Pressable,
  View,
  TextInput,
} from 'react-native';

function EnterCryptoModal() {
  const [modalVisible, setModalVisible] = useState(true);
  const [amount, setAmount] = useState();
  const handlePress = () => {
    setModalVisible(!modalVisible);
    Alert.alert(`Amount has been set to ${amount}ETH`);
  };
  return (
    <Modal
      animationType='slide'
      transparent={true}
      visible={modalVisible}
      onRequestClose={() => {
        //TODO metamask sign in logic goes here
        Alert.alert('Modal has been closed.');
        setModalVisible(!modalVisible);
      }}
    >
      <View style={styles.centeredView}>
        <View style={styles.modalView}>
          <Text style={styles.modalText}>
            Captain sets the pot amount for all players. Players will be sent an
            alert to agree or diagree with the buy-in amount.
          </Text>
          <TextInput
            value={amount}
            onChangeText={(text) => setAmount(text)}
            style={styles.input}
            placeholder='Enter amount'
            placeholderTextColor={'white'}
          ></TextInput>
          <Pressable
            style={[styles.button, styles.buttonClose]}
            // Need to be able to sign in with metamask when the button is clicked
            onPress={handlePress}
          >
            <Text style={styles.textStyle}>SET PRICE</Text>
          </Pressable>
        </View>
      </View>
    </Modal>
  );
}
const styles = StyleSheet.create({
  centeredView: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    marginTop: 22,
  },
  modalView: {
    margin: 20,
    backgroundColor: 'white',
    borderRadius: 20,
    padding: 55,
    alignItems: 'center',
    shadowColor: '#000',
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: 0.25,
    shadowRadius: 4,
    elevation: 5,
  },
  button: {
    marginTop: 20,
    borderRadius: 10,
    padding: 10,
    paddingHorizontal: 50,
    elevation: 2,
    backgroundColor: '#57f3d3',
  },
  textStyle: {
    color: 'white',
    fontWeight: 'bold',
    textAlign: 'center',
  },
  modalText: {
    marginBottom: 15,
    textAlign: 'center',
  },
  input: {
    backgroundColor: 'black',
    width: 250,
    height: 50,
    borderRadius: 10,
    textAlign: 'center',
    color: 'white',
  },
});

export default EnterCryptoModal;
