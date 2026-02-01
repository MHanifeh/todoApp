import { Tabs } from "expo-router";

export default function TabsLayout() {
  return (
    <Tabs screenOptions={{ headerShown: false }}>
      <Tabs.Screen name="index" options={{ title: "خانه" }} />
      <Tabs.Screen name="analytics" options={{ title: "گزارش‌ها" }} />
      <Tabs.Screen name="settings" options={{ title: "تنظیمات" }} />
    </Tabs>
  );
}
