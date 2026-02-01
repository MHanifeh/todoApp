import { View, Text, Pressable } from "@/lib/deps";
import { theme } from "@/design/theme";

export default function HomeScreen() {
  return (
    <View style={{ flex: 1, backgroundColor: theme.colors.bg, padding: theme.spacing.md }}>
      <Text style={{ fontFamily: theme.typography.fontFamily.bold, fontSize: theme.typography.size.xl, color: theme.colors.text }}>
        سلام 👋
      </Text>

      <Text style={{ marginTop: theme.spacing.sm, color: theme.colors.textMuted }}>
        لیست کارها اینجا نمایش داده می‌شود.
      </Text>

      <Pressable
        style={{
          marginTop: theme.spacing.lg,
          paddingVertical: theme.spacing.sm,
          borderRadius: theme.radius.lg,
          backgroundColor: theme.colors.primary,
          alignItems: "center",
        }}
        onPress={() => {}}
      >
        <Text style={{ fontFamily: theme.typography.fontFamily.medium, color: theme.colors.text }}>
          + افزودن وظیفه
        </Text>
      </Pressable>
    </View>
  );
}
