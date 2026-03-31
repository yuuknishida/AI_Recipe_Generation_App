import { Text, StyleSheet, Image, View } from 'react-native';
import icon from "@/assets/dishcraft_icon.png";

export default function AuthHeader({ title, subtitle }) {
    return (
        <>
            <View style={{
                shadowColor: "#1D9E75",
                shadowRadius: 35,
                shadowOpacity: 0.5,
                shadowOffset: { width: 0, height: 0 },
            }}>
                <Image source={icon} style={styles.image}></Image>
            </View>
            
            <Text style={styles.title}>{title}</Text>
            <Text style={styles.subtitle}>{subtitle}</Text>
        </>
    )
};

const styles = StyleSheet.create({
    title: {
        fontSize: 28,
		fontWeight: "bold",
		textAlign: "center",
        marginBottom: 10,
        color: '#fff',
    },
    subtitle: {
        textAlign: "center",
        marginBottom: 30,
        color: '#fff'
    },
    image: {
        width: 100,
		height: 100,
		marginBottom: 20,
        alignSelf: "center",
        color: '#fff',
    },
})