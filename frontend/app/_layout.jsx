import { Stack } from "expo-router";

export default function RootLayout() {
  return (
    <Stack screenOptions={{ headerShown: false }}>
      <Stack.Screen name="index" options={{ title: 'Welcome' }}></Stack.Screen>
      <Stack.Screen name="auth" options={{ title: 'Auth' }}></Stack.Screen>
    </Stack>
  )
}
