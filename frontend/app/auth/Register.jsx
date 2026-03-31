import { TouchableOpacity, View, Text, StyleSheet } from 'react-native';
import { useState } from "react";
import { useRouter } from 'expo-router';
import AuthHeader from '../../components/AuthHeader';
import InputField from '../../components/InputField';

export default function Register() {
    const router = useRouter();
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");
    return (
        <View style={styles.container}>
            <AuthHeader title='Register Here' subtitle='Start your cooking journey today'></AuthHeader>

            <InputField
                label="Email"
                placeholder="Email"
                value={email}
                onChangeText={setEmail}
                keyboardType='email-address'
            />
            <InputField
                label="Password"
                placeholder="Password"
                value={password}
                onChangeText={setPassword}
            ></InputField>
            <InputField
                label="Confirm Password"
                placeholder="Password"
                value={confirmPassword}
                onChangeText={setConfirmPassword}
            ></InputField>
            <TouchableOpacity style={styles.button}>
                <Text style={styles.buttonText}>Register</Text>
            </TouchableOpacity>
            <View style={{
                flex: 1,
                justifyContent: 'center',
                flexDirection: 'row',
            }}>
                <Text>Already have an account </Text>
                <Text style={{color: "#1D9E75", fontWeight: "bold"}} onPress={() => router.push("/auth/Login")}>Sign in</Text>
            </View>
            
        </View>
    )
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
        shadowColor: "#1D9E75",
        shadowRadius: 35,
        shadowOpacity: 0.5,
        shadowOffset: { width: 0, height: 0 },
    },
    buttonText: {
        color: "#fff",
        fontSize: 18,
        textAlign: "center",
    },
})