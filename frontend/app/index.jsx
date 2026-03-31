// Home Screen
import DishCraft_Icon from "@/assets/dishcraft_icon.png";
import { useRouter } from "expo-router";
import { Image, StyleSheet, Text, TouchableOpacity, View } from "react-native";


export default function WelcomeScreen() {
  const router = useRouter();
  return (
    <View style={styles.container}>
      <View style={styles.topSection}>
        <View style={styles.logoContainer}>
          <Image
            style={styles.icon}
            source={DishCraft_Icon}
            resizeMode="contain"w
          ></Image>

          <View style={styles.monogram}>
            <View style={{ position: 'relative' }}>

              <Text style={styles.D}>D</Text>
              <Text style={styles.C}>C</Text>
            </View>
          </View>
        </View>
      </View>
      <View style={{
        flexDirection: 'row',
        paddingLeft: 20,
        paddingTop: 60,
        paddingBottom: 30,
      }}>
        <Text style={{
          fontFamily: 'Georgia',
          fontSize: 68,
          fontWeight: 300,
          alignSelf: "center",
          color: '#fff',
          letterSpacing: -2,
        }}>Dish</Text>
        <Text style={{
          fontStyle: 'italic',
          fontFamily: 'Georgia',
          color: '#1D9E75',
          alignSelf: 'center',
          fontWeight: 600,
          fontSize: 68,
          shadowColor: "#1D9E75",
          shadowRadius: 25,
          shadowOpacity: 0.9,
          borderRadius: 18,
          shadowOffset: { width: 0, height: 0 },
        }}>Craft</Text>
      </View>
      
      <Text style={styles.text}>
        Your personal recipe manager -- cook with confidence
      </Text>

      <View
        style={{
          gap: 15,
          justifyContent: "center",
          paddingTop: 50,
          paddingHorizontal: 50,
        }}
      >
        <TouchableOpacity
          style={styles.button}
          onPress={() => router.push("/auth/Register")}
        >
          <Text
            style={{
              fontSize: 14,
              alignSelf: "center",
              color: "#E1F5EE",
            }}
          >
            Get Started
          </Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={{
            backgroundColor: "#E1F5EE",
            paddingVertical: 15,
            borderRadius: 8,
            borderWidth: 1,
          }}
          onPress={() => router.push("/auth/Login")}
        >
          <Text
            style={{
              fontSize: 14,
              alignSelf: "center",
            }}
          >
            Sign In
          </Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#1C1714",
  },
  topSection: {
    flexDirection: 'row',
  },
  logoContainer: {
    position: "relative",
    marginTop: 20,
    marginLeft: 20,
    overflow: "visible",
    shadowColor: "#1D9E75",
    shadowRadius: 35,
    shadowOpacity: 0.5,
    shadowOffset: { width: 0, height: 0 },
  },
  text: {
    fontSize: 14,
    alignSelf: "center",
    color: '#FFFEFB',
  },
  button: {
    backgroundColor: "#1D9E75",
    paddingVertical: 15,
    borderRadius: 8,

    shadowColor: "#1D9E75",
    shadowRadius: 20,
    shadowOpacity: 0.5,
    shadowOffset: { width: 0, height: 0 },
  },
  icon: {
    width: 100,
    height: 100,
    marginBottom: 20,
    marginTop: 100,
    marginLeft: 20,
    
  },
  monogram: {
    position: 'absolute',
    top: 100,
    left: 250,
    overflow: 'visible',
    width: 180,
    height: 150,
  },
  D: {
    fontFamily: 'Georgia',
    color: '#fff',
    fontSize: 90,
    fontWeight: 300,
    opacity: 0.25,

    shadowColor: "#ffffff",
    shadowOffset: { width: 0, height: 0 },
    shadowOpacity: 1.0,
    shadowRadius: 25,
  },
  C: {
    position: "absolute",
    top: 10,
    left: 15,
    fontFamily: "Georgia",
    fontSize: 110,
    color: "#1D9E75",
    fontStyle: 'italic',
    fontWeight: 600,
    opacity: 0.3,

    shadowColor: "#1D9E75",
    shadowOffset: { width: 0, height: 0 },
    shadowOpacity: 0.9,
    shadowRadius: 30,
  },
});