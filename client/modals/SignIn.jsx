import { NavigationRouteContext } from "@react-navigation/native";
import React, { useState } from "react";
import { Alert, Modal, StyleSheet, Text, Pressable, View } from "react-native";
import { NavigationEvents } from "react-navigation";

function SignInModal({
  isSignInVisible,
  setSignInVisibility,
  type,
  navigation,
}) {
  const signInOnPress = () => {
    if (type === "Captain") {
      navigation.navigate("Room", { type: "Captain" });
      setSignInVisibility(!isSignInVisible);
    } else {
      navigation.navigate("JoinGame", { type: "Player" });
      setSignInVisibility(!isSignInVisible);
    }
  };
  return (
    <Modal animationType="slide" transparent={true} visible={isSignInVisible}>
      <View style={styles.centeredView}>
        <View style={styles.modalView}>
          <Text style={styles.modalText}>
            Sign-in with your MetaMask account to add funds to your game 🦊
          </Text>
          <Pressable
            style={[styles.button, styles.buttonClose]}
            // Need to be able to sign in with metamask when the button is clicked
            onPress={signInOnPress}
          >
            <Text style={styles.textStyle}>SIGN IN</Text>
          </Pressable>
        </View>
      </View>
    </Modal>
  );
}
const styles = StyleSheet.create({
  centeredView: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    marginTop: 22,
  },
  modalView: {
    margin: 20,
    backgroundColor: "white",
    borderRadius: 20,
    padding: 55,
    alignItems: "center",
    shadowColor: "#000",
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
    backgroundColor: "#182724",
  },
  textStyle: {
    color: "white",
    fontWeight: "bold",
    textAlign: "center",
  },
  modalText: {
    marginBottom: 15,
    textAlign: "center",
  },
});

export default SignInModal;
