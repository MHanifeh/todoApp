import { View, Text } from "@/lib/deps";
import { theme } from "@/design/theme";

export default function NewTaskScreen() {
  return (
    <View style={{ flex: 1, backgroundColor: theme.colors.bg, padding: theme.spacing.md }}>
      <Text style={{ fontFamily: theme.typography.fontFamily.bold, fontSize: theme.typography.size.xl, color: theme.colors.text }}>
        افزودن وظیفه
      </Text>
      <Text style={{ marginTop: theme.spacing.sm, color: theme.colors.textMuted }}>
        فرم ایجاد وظیفه اینجا ساخته می‌شود.
      </Text>
    </View>
  );
}
