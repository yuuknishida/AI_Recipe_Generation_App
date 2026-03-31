import {
	StyleSheet,
	Text,
	TextInput,
} from "react-native";

export default function InputField({ label, placeholder, value, onChangeText, keyboardType = "default" }) {
    return (
        <>
            <Text style={styles.label}>{label}</Text>
            <TextInput
                placeholder={placeholder}
                style={styles.input}
                placeholderTextColor="#888"
                value={value}
                onChangeText={onChangeText}
                autoCapitalize="none"
                autoCorrect={false}
                keyboardType={keyboardType}
            >
            </TextInput>
        </>
    )
}

const styles = StyleSheet.create({
    input: {
		height: 50,
		borderColor: "#ccc",
		borderWidth: 1,
		borderRadius: 8,
		paddingHorizontal: 15,
		marginBottom: 15,
		backgroundColor: "#fff",
		fontSize: 16,
        color: '#fff',
    },
    label: {
        color: '#fff',
    }
});