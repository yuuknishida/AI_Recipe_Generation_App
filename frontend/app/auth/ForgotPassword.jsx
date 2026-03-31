import { useRouter } from "expo-router";
import { useState } from "react";
import { StyleSheet, Text, TouchableOpacity, View } from "react-native";
import AuthHeader from "../../components/AuthHeader";
import InputField from "../../components/InputField";
export default function ForgotPassword() {
  const [email, setEmail] = useState("");
  const router = useRouter();
  return (
    <View style={styles.container}>
        <AuthHeader
            title="Forgot Password"
            subtitle="Enter email used to create account"
        />
        <InputField
            label="Enter Email"
            placeholder="example@gmail.com"
            value={email}
            onChangeText={setEmail}
            keyboardType="email-address"
        ></InputField>
        <Text
            style={{ textAlign: "center", marginBottom: 20, color: '#fff'}}
            onPress={() => router.push("/Auth/Login")}
        >
        Back to Sign in
          </Text>
          
        <TouchableOpacity style={styles.button}>
            <Text style={styles.buttonText}>Send</Text>
        </TouchableOpacity>
        <Text style={{ textAlign: "center", marginTop: 20, marginBottom: 20, color: '#fff' }}>Or</Text>
          
        <Text style={{textAlign: 'center', color: '#fff '}}>Don&apos;t have an account</Text>  
        <TouchableOpacity style={styles.button} onPress={() => router.push("/Auth/Register")}>
            <Text style={styles.buttonText}>Sign Up</Text>
        </TouchableOpacity>  
    </View>
  );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: "flex-start",
        backgroundColor: "#1C1714",
        padding: 50,
        paddingTop: 80,
    },
    button: {
        backgroundColor: "#1D9E75",
        paddingVertical: 15,
        borderRadius: 8,
    },
    buttonText: {
        color: "#fff",
        fontSize: 18,
        textAlign: "center",
    },
});
