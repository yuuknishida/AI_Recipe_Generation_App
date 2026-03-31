import { Stack } from "expo-router";

export default function AuthLayout() {
    return (
        <Stack screenOptions={{ headerShown: false }}>
            <Stack.Screen name="Register"></Stack.Screen>
            <Stack.Screen name="Login"></Stack.Screen>
        </Stack>
    )
}