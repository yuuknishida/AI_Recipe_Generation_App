import { useState, useEffect } from "react";
import { useRouter } from "expo-router";
import {
	StyleSheet,
	Text,
	View,
	TouchableOpacity,
} from "react-native";
import AuthHeader from "../../components/AuthHeader";
import InputField from "../../components/InputField";
export default function Login() {
    const router = useRouter();
    const [email, setEmail] = useState("");
	const [password, setPassword] = useState("");
	
	useEffect(() => {
		fetch("http://localhost:8000/auth/login")
			.then(response => {
				if (response.ok) {
					return response.json()
				}
				throw response;
			})
			.then(data => {
				setEmail(data.email);
				setPassword(data.password);
			});
	}, []);
	
    return (
        <View style={styles.container}>
            <AuthHeader
				title="Welcome Back"
				subtitle="Sign in to your account">
            </AuthHeader>
            
            <InputField
				label="Email"
				placeholder="Email"
				value={email}
				onChangeTex={setEmail}
				keyboardType="email-address"
			></InputField>

			<InputField
                label="Password"
                placeholder="Password"
				value={password}
				onChangeText={setPassword}
            ></InputField>

            <TouchableOpacity style={styles.button}>
				<Text style={styles.buttonText}>Login</Text>
			</TouchableOpacity>
			<View
				style={{
					flexDirection: "row",
					justifyContent: "center",
				}}>
				<Text style={{color: '#fff',}}>Don&apos;t have an account </Text>
				<Text style={{ color: "#1D9E75", fontWeight: "bold" }} onPress={() => router.push("/auth/Register")}>Create account</Text>
            </View>
            <View
                style={{
                    paddingTop: 15,
					flexDirection: "row",
                    justifyContent: "center",
                    alignContent: "flex-start",
                }}>
                <Text style={{color: '#1D9E75'}} onPress={() => router.push("/auth/ForgotPassword")}>Forgot Password</Text>
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